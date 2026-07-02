#!/usr/bin/env python3
"""Create a structured PILOT-0001 experiment response YAML file."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
RESPONSES_DIR = ROOT / "pilots" / "PILOT-0001" / "experiment" / "responses"
MANIFEST_PATH = ROOT / "pilots" / "PILOT-0001" / "RUN-MANIFEST.yaml"
RESPONSE_ID_RE = re.compile(r"^RESPONSE-PILOT-0001-(\d{4})$")

ANSWER_FIELDS = [
    "q1_changed_in_hero",
    "q2_return_voluntary_or_obligated",
    "q3_pressure_debt_or_manipulation",
    "q4_meaning_of_expansion_metaphor",
]

SCORE_FIELDS = [
    "voluntary_safety",
    "recovery_as_resource",
    "non_coercive_return",
    "boundary_awareness",
    "metaphorical_expansion",
]

FAILURE_FIELDS = [
    "woman_owes_safety",
    "man_owes_return",
    "relationship_as_transaction",
    "resource_sharing_as_payment",
    "expansion_as_domination",
    "safety_as_manipulation",
]


def load_json(path: str) -> dict[str, Any]:
    if path == "-":
        raw = sys.stdin.read()
    else:
        raw = Path(path).read_text(encoding="utf-8")
    data = json.loads(raw)
    if not isinstance(data, dict):
        raise ValueError("input JSON must be an object")
    return data


def load_yaml(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a YAML object")
    return data


def next_response_number() -> int:
    RESPONSES_DIR.mkdir(parents=True, exist_ok=True)
    numbers: list[int] = []
    for path in RESPONSES_DIR.glob("RESPONSE-PILOT-0001-*.yaml"):
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            continue
        match = RESPONSE_ID_RE.match(str(data.get("id", "")))
        if match:
            numbers.append(int(match.group(1)))
    return max(numbers, default=0) + 1


def real_response_file_count() -> int:
    if not RESPONSES_DIR.exists():
        return 0
    return len(
        [
            path
            for path in RESPONSES_DIR.glob("RESPONSE-PILOT-0001-*.yaml")
            if path.is_file() and not path.name.endswith(".example.yaml")
        ]
    )


def require_text(data: dict[str, Any], field: str) -> str:
    value = data.get(field)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"missing required text field: {field}")
    return value.strip()


def build_answers(data: dict[str, Any]) -> dict[str, str]:
    answers = data.get("answers")
    if not isinstance(answers, dict):
        raise ValueError("answers must be an object")
    result: dict[str, str] = {}
    for field in ANSWER_FIELDS:
        value = answers.get(field)
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"answers.{field} must be non-empty text")
        result[field] = value.strip()
    return result


def build_scores(data: dict[str, Any]) -> dict[str, int]:
    scores = data.get("meaning_signal_scores")
    if not isinstance(scores, dict):
        raise ValueError("meaning_signal_scores must be an object")
    result: dict[str, int] = {}
    for field in SCORE_FIELDS:
        value = scores.get(field)
        if not isinstance(value, int) or not 0 <= value <= 5:
            raise ValueError(f"meaning_signal_scores.{field} must be an integer from 0 to 5")
        result[field] = value
    return result


def build_failure_signals(data: dict[str, Any]) -> dict[str, Any]:
    failure_signals = data.get("failure_signals", {})
    if failure_signals is None:
        failure_signals = {}
    if not isinstance(failure_signals, dict):
        raise ValueError("failure_signals must be an object when provided")

    result: dict[str, Any] = {}
    for field in FAILURE_FIELDS:
        value = failure_signals.get(field, False)
        if not isinstance(value, bool):
            raise ValueError(f"failure_signals.{field} must be true or false")
        result[field] = value

    notes = failure_signals.get("notes")
    result["notes"] = notes.strip() if isinstance(notes, str) and notes.strip() else None
    return result


def build_response(data: dict[str, Any], response_number: int) -> dict[str, Any]:
    if data.get("personal_data_removed") is not True:
        raise ValueError("personal_data_removed must be true before writing a response")
    if data.get("simulated_response") is True:
        raise ValueError("simulated responses must not be written as real response files")

    raw_quotes = data.get("raw_quotes", [])
    if raw_quotes is None:
        raw_quotes = []
    if not isinstance(raw_quotes, list) or not all(isinstance(item, str) for item in raw_quotes):
        raise ValueError("raw_quotes must be a list of strings")

    response_id = f"RESPONSE-PILOT-0001-{response_number:04d}"
    return {
        "id": response_id,
        "type": "experiment_response",
        "status": "collected",
        "pilot_id": "PILOT-0001",
        "experiment_id": "EXP-PILOT-0001",
        "source_script_path": "pilots/PILOT-0001/output/script-draft.md",
        "response_date": data.get("response_date") or date.today().isoformat(),
        "respondent_id": require_text(data, "respondent_id"),
        "respondent_context": data.get("respondent_context"),
        "personal_data_removed": True,
        "answers": build_answers(data),
        "meaning_signal_scores": build_scores(data),
        "failure_signals": build_failure_signals(data),
        "raw_quotes": raw_quotes,
        "moderator_notes": data.get("moderator_notes"),
        "evidence_boundary": {
            "real_response_required": True,
            "simulated_response": False,
            "creates_learning": False,
            "creates_law_candidate": False,
            "creates_logos_law": False,
            "law_promotion_allowed": False,
        },
    }


def dump_yaml(data: dict[str, Any]) -> str:
    return yaml.safe_dump(data, allow_unicode=True, sort_keys=False, width=100)


def update_manifest_count(real_response_count: int) -> None:
    manifest = load_yaml(MANIFEST_PATH)
    boundary = manifest.setdefault("current_boundary", {})
    if not isinstance(boundary, dict):
        raise ValueError("RUN-MANIFEST current_boundary must be an object")
    boundary["real_response_count"] = real_response_count
    MANIFEST_PATH.write_text(dump_yaml(manifest), encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", "-i", required=True, help="JSON input file, or '-' for stdin")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="print the YAML that would be written without creating files",
    )
    args = parser.parse_args(argv)

    try:
        data = load_json(args.input)
        response_number = next_response_number()
        response = build_response(data, response_number)
        response_yaml = dump_yaml(response)

        if args.dry_run:
            print(response_yaml, end="")
            return 0

        target = RESPONSES_DIR / f"{response['id']}.yaml"
        if target.exists():
            raise ValueError(f"refusing to overwrite existing response: {target}")
        target.write_text(response_yaml, encoding="utf-8")
        real_response_count = real_response_file_count()
        update_manifest_count(real_response_count)
        print(f"created {target.relative_to(ROOT).as_posix()}")
        print(
            f"updated {MANIFEST_PATH.relative_to(ROOT).as_posix()} "
            f"real_response_count={real_response_count}"
        )
        return 0
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
