#!/usr/bin/env python3
"""Report WF-0002 readiness without mutating repository or n8n state."""

from __future__ import annotations

import argparse
import copy
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from logos_engine.wf_0001_issue import (  # noqa: E402
    PROMOTION_REVIEW_ATTESTATION,
    validate_wf_0001_promotion_readiness,
)
from logos_engine.wf_0002_belief_movement import (  # noqa: E402
    validate_wf_0002_belief_movement_input,
)


REQUIRED_ARTIFACTS = [
    "automation/workflows/belief-shift-generator.md",
    "automation/n8n/wf-0002/BELIEF-MOVEMENT-INPUT-CONTRACT.md",
    "automation/n8n/wf-0002/BELIEF-MOVEMENT-INPUT-PREVIEW-GATE.md",
    "automation/n8n/wf-0002/writeback/belief-movement-input-contract-2026-07-02.md",
    "automation/n8n/wf-0002/writeback/belief-movement-input-preview-gate-test-2026-07-02.md",
    "automation/n8n/wf-0002/writeback/belief-movement-status-readiness-2026-07-02.md",
    "schemas/wf-0002-belief-movement-input.schema.yaml",
    "testing/fixtures/wf-0002-belief-movement-input.json.example",
    "testing/fixtures/wf-0001-issue-reviewed-stable.md",
    "scripts/validate_wf_0002_belief_movement_input.py",
    "scripts/wf_0002_status.py",
]

SOURCE_FIXTURE_TITLE = "HT-0100: Intake must preserve raw observations before interpretation"


def load_json(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return data


def check(callable_obj: Any, *args: Any, **kwargs: Any) -> tuple[bool, str | None]:
    try:
        callable_obj(*args, **kwargs)
    except Exception as exc:  # noqa: BLE001
        return False, str(exc)
    return True, None


def placeholder_rejection_enforced(data: dict[str, Any]) -> tuple[bool, str | None]:
    mutated = copy.deepcopy(data)
    mutated["source_human_truth_id"] = "HT-0000"
    accepted, error = check(validate_wf_0002_belief_movement_input, mutated)
    if accepted:
        return False, "HT-0000 placeholder was unexpectedly accepted"
    return "source_human_truth_id" in (error or ""), error


def build_status(root: Path) -> dict[str, Any]:
    missing_artifacts = [
        path for path in REQUIRED_ARTIFACTS if not (root / path).exists()
    ]

    input_fixture_path = root / "testing" / "fixtures" / "wf-0002-belief-movement-input.json.example"
    source_fixture_path = root / "testing" / "fixtures" / "wf-0001-issue-reviewed-stable.md"

    input_data = load_json(input_fixture_path)
    input_fixture_valid, input_fixture_error = check(
        validate_wf_0002_belief_movement_input,
        input_data,
    )

    placeholder_rejected, placeholder_rejection_error = placeholder_rejection_enforced(
        input_data
    )

    source_body = source_fixture_path.read_text(encoding="utf-8")
    source_fixture_promotion_ready, source_fixture_error = check(
        validate_wf_0001_promotion_readiness,
        source_body,
        title=SOURCE_FIXTURE_TITLE,
        review_attestation=PROMOTION_REVIEW_ATTESTATION,
    )

    fixture_has_source_issue_reference = any(
        key in input_data for key in ("source_issue_number", "source_issue_url")
    )
    fixture_traceability_is_local = not fixture_has_source_issue_reference

    validation_passed = (
        not missing_artifacts
        and input_fixture_valid
        and placeholder_rejected
        and source_fixture_promotion_ready
        and fixture_traceability_is_local
    )

    if missing_artifacts:
        next_action = "restore_missing_wf_0002_artifacts"
    elif not input_fixture_valid or not placeholder_rejected:
        next_action = "fix_wf_0002_input_contract"
    elif not source_fixture_promotion_ready or not fixture_traceability_is_local:
        next_action = "fix_wf_0002_source_traceability"
    else:
        next_action = "build_wf_0002_generation_preflight_gate_after_reviewed_source_selection"

    return {
        "workflow_id": "WF-0002",
        "preview_gate": {
            "name": "LOGOS WF-0002 Belief Movement Input Preview Gate",
            "n8n_id": "Rue7sAU14UMv1hTr",
            "expected_active": False,
        },
        "source": {
            "human_truth_id": input_data.get("source_human_truth_id"),
            "review_fixture": "testing/fixtures/wf-0001-issue-reviewed-stable.md",
            "review_fixture_promotion_ready": source_fixture_promotion_ready,
            "review_fixture_error": source_fixture_error,
            "uses_live_issue_reference": fixture_has_source_issue_reference,
            "traceability": "local_review_fixture",
        },
        "input_fixture_valid": input_fixture_valid,
        "input_fixture_error": input_fixture_error,
        "placeholder_rejection_enforced": placeholder_rejected,
        "placeholder_rejection_error": placeholder_rejection_error,
        "missing_required_artifacts": missing_artifacts,
        "writeback_performed": False,
        "belief_shift_issue_created": False,
        "yaml_object_created": False,
        "meaning_atom_created": False,
        "generation_gate_created": False,
        "validation_passed": validation_passed,
        "next_action": next_action,
    }


def render_text(status: dict[str, Any]) -> str:
    source = status["source"]
    lines = [
        f"workflow_id: {status['workflow_id']}",
        f"source_human_truth_id: {source['human_truth_id']}",
        f"input_fixture_valid: {str(status['input_fixture_valid']).lower()}",
        f"placeholder_rejection_enforced: {str(status['placeholder_rejection_enforced']).lower()}",
        f"source_review_fixture_promotion_ready: {str(source['review_fixture_promotion_ready']).lower()}",
        f"uses_live_issue_reference: {str(source['uses_live_issue_reference']).lower()}",
        f"writeback_performed: {str(status['writeback_performed']).lower()}",
        f"belief_shift_issue_created: {str(status['belief_shift_issue_created']).lower()}",
        f"yaml_object_created: {str(status['yaml_object_created']).lower()}",
        f"generation_gate_created: {str(status['generation_gate_created']).lower()}",
        f"validation_passed: {str(status['validation_passed']).lower()}",
        f"next_action: {status['next_action']}",
    ]
    if status["input_fixture_error"]:
        lines.append(f"input_fixture_error: {status['input_fixture_error']}")
    if status["placeholder_rejection_error"]:
        lines.append(f"placeholder_rejection_error: {status['placeholder_rejection_error']}")
    if source["review_fixture_error"]:
        lines.append(f"source_review_fixture_error: {source['review_fixture_error']}")
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
