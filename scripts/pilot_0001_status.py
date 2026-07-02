#!/usr/bin/env python3
"""Report PILOT-0001 readiness without mutating repository state."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from logos_engine.validate import (  # noqa: E402
    PILOT_0001_MIN_RESPONSES_FOR_LEARNING,
    iter_pilot_0001_response_files,
    validate_repository,
)


MANIFEST_PATH = ROOT / "pilots" / "PILOT-0001" / "RUN-MANIFEST.yaml"
REQUIRED_ARTIFACTS = [
    "pilots/PILOT-0001/input/raw-meaning.yaml",
    "pilots/PILOT-0001/output/meaning-edges.yaml",
    "pilots/PILOT-0001/output/human-truth.yaml",
    "pilots/PILOT-0001/output/human-contradiction.yaml",
    "pilots/PILOT-0001/output/belief-shift.yaml",
    "pilots/PILOT-0001/output/meaning-atoms.yaml",
    "pilots/PILOT-0001/output/story-pattern.yaml",
    "pilots/PILOT-0001/output/script-draft.md",
    "pilots/PILOT-0001/review/script-draft-review.md",
    "pilots/PILOT-0001/output/experiment-plan.yaml",
    "pilots/PILOT-0001/experiment/TEST-PROTOCOL.md",
    "pilots/PILOT-0001/experiment/RESPONDENT-PACKET.md",
    "pilots/PILOT-0001/experiment/COLLECTOR-GUIDE.md",
    "pilots/PILOT-0001/experiment/response-template.yaml",
]


def load_yaml(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a YAML object")
    return data


def build_status(root: Path) -> dict[str, Any]:
    manifest_path = root / "pilots" / "PILOT-0001" / "RUN-MANIFEST.yaml"
    manifest = load_yaml(manifest_path)
    response_files = iter_pilot_0001_response_files(root)
    validation_issues = validate_repository(root)

    boundary = manifest.get("current_boundary", {})
    if not isinstance(boundary, dict):
        boundary = {}

    response_count = len(response_files)
    min_responses = PILOT_0001_MIN_RESPONSES_FOR_LEARNING
    missing_artifacts = [
        path for path in REQUIRED_ARTIFACTS if not (root / path).exists()
    ]
    learning_allowed = (
        response_count >= min_responses
        and not validation_issues
        and not bool(missing_artifacts)
    )

    if learning_allowed:
        next_action = "draft_learning_candidate_from_real_responses"
    elif missing_artifacts:
        next_action = "restore_missing_required_artifacts"
    elif validation_issues:
        next_action = "fix_validation_issues"
    else:
        next_action = "collect_real_responses"

    return {
        "pilot_id": "PILOT-0001",
        "completed_through_stage": manifest.get("completed_through_stage"),
        "prepared_through_stage": manifest.get("prepared_through_stage"),
        "response_count": response_count,
        "manifest_response_count": boundary.get("real_response_count"),
        "min_responses_for_learning": min_responses,
        "learning_allowed": learning_allowed,
        "validation_passed": not validation_issues,
        "validation_issue_count": len(validation_issues),
        "missing_required_artifacts": missing_artifacts,
        "learning_created": boundary.get("learning_created"),
        "law_candidate_created": boundary.get("law_candidate_created"),
        "logos_law_created": boundary.get("logos_law_created"),
        "next_action": next_action,
        "response_files": [
            path.relative_to(root).as_posix() for path in response_files
        ],
    }


def render_text(status: dict[str, Any]) -> str:
    lines = [
        f"pilot_id: {status['pilot_id']}",
        f"completed_through_stage: {status['completed_through_stage']}",
        f"prepared_through_stage: {status['prepared_through_stage']}",
        f"response_count: {status['response_count']}",
        f"min_responses_for_learning: {status['min_responses_for_learning']}",
        f"learning_allowed: {str(status['learning_allowed']).lower()}",
        f"validation_passed: {str(status['validation_passed']).lower()}",
        f"next_action: {status['next_action']}",
    ]
    if status["missing_required_artifacts"]:
        lines.append("missing_required_artifacts:")
        lines.extend(f"  - {path}" for path in status["missing_required_artifacts"])
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="print JSON instead of text")
    args = parser.parse_args(argv)

    try:
        status = build_status(ROOT)
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(status, ensure_ascii=False, indent=2))
    else:
        print(render_text(status))
    return 0


if __name__ == "__main__":
    sys.exit(main())
