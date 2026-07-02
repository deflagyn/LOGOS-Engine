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
    validate_wf_0002_belief_shift_issue_body,
    validate_wf_0002_belief_movement_input,
)


REQUIRED_ARTIFACTS = [
    "automation/workflows/belief-shift-generator.md",
    "automation/n8n/wf-0002/BELIEF-MOVEMENT-INPUT-CONTRACT.md",
    "automation/n8n/wf-0002/BELIEF-MOVEMENT-INPUT-PREVIEW-GATE.md",
    "automation/n8n/wf-0002/BELIEF-MOVEMENT-GENERATION-PREFLIGHT-CONTRACT.md",
    "automation/n8n/wf-0002/BELIEF-MOVEMENT-GENERATION-PREFLIGHT-GATE.md",
    "automation/n8n/wf-0002/BELIEF-MOVEMENT-ISSUE-CREATION-GATE.md",
    "automation/n8n/wf-0002/writeback/belief-movement-input-contract-2026-07-02.md",
    "automation/n8n/wf-0002/writeback/belief-movement-input-preview-gate-test-2026-07-02.md",
    "automation/n8n/wf-0002/writeback/belief-movement-status-readiness-2026-07-02.md",
    "automation/n8n/wf-0002/writeback/belief-movement-generation-preflight-contract-2026-07-02.md",
    "automation/n8n/wf-0002/writeback/belief-movement-generation-preflight-gate-test-2026-07-02.md",
    "automation/n8n/wf-0002/writeback/belief-movement-issue-creation-gate-test-2026-07-02.md",
    "schemas/wf-0002-belief-movement-input.schema.yaml",
    "testing/fixtures/wf-0002-belief-movement-input.json.example",
    "testing/fixtures/wf-0002-belief-shift-issue.md",
    "testing/fixtures/wf-0002-issue-30.md",
    "testing/fixtures/wf-0001-issue-reviewed-stable.md",
    "scripts/validate_wf_0002_belief_movement_input.py",
    "scripts/validate_wf_0002_belief_shift_issue.py",
    "scripts/wf_0002_status.py",
]

SOURCE_FIXTURE_TITLE = "HT-0100: Intake must preserve raw observations before interpretation"
BELIEF_SHIFT_ISSUE_TITLE = "BS-0000: Preserve before interpreting"
CREATED_ISSUE_TITLE = "BS-0000: Preserve before interpreting"


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
    issue_fixture_path = root / "testing" / "fixtures" / "wf-0002-belief-shift-issue.md"
    created_issue_fixture_path = root / "testing" / "fixtures" / "wf-0002-issue-30.md"
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

    issue_body = issue_fixture_path.read_text(encoding="utf-8")
    issue_fixture_review_ready, issue_fixture_error = check(
        validate_wf_0002_belief_shift_issue_body,
        issue_body,
        title=BELIEF_SHIFT_ISSUE_TITLE,
    )

    created_issue_body = created_issue_fixture_path.read_text(encoding="utf-8")
    created_issue_review_ready, created_issue_error = check(
        validate_wf_0002_belief_shift_issue_body,
        created_issue_body,
        title=CREATED_ISSUE_TITLE,
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
        and issue_fixture_review_ready
        and created_issue_review_ready
        and fixture_traceability_is_local
    )

    if missing_artifacts:
        next_action = "restore_missing_wf_0002_artifacts"
    elif not input_fixture_valid or not placeholder_rejected:
        next_action = "fix_wf_0002_input_contract"
    elif (
        not source_fixture_promotion_ready
        or not issue_fixture_review_ready
        or not created_issue_review_ready
        or not fixture_traceability_is_local
    ):
        next_action = "fix_wf_0002_source_traceability"
    else:
        next_action = "review_issue_30_before_yaml_promotion_gate"

    return {
        "workflow_id": "WF-0002",
        "preview_gate": {
            "name": "LOGOS WF-0002 Belief Movement Input Preview Gate",
            "n8n_id": "Rue7sAU14UMv1hTr",
            "expected_active": False,
        },
        "generation_preflight_gate": {
            "name": "LOGOS WF-0002 Belief Movement Generation Preflight Gate",
            "n8n_id": "uBrha0GALDy3HfSC",
            "expected_active": False,
        },
        "issue_creation_gate": {
            "name": "LOGOS WF-0002 Belief Movement Issue Creation Gate",
            "n8n_id": "wjiTK4Ov1nY1EndY",
            "expected_active": False,
        },
        "created_issue": {
            "number": 30,
            "url": "https://github.com/deflagyn/LOGOS-Engine/issues/30",
            "title": CREATED_ISSUE_TITLE,
            "review_ready": created_issue_review_ready,
            "review_error": created_issue_error,
            "yaml_promotion_ready": False,
            "yaml_promotion_block_reason": "WF-0002 YAML promotion gate is not implemented; BS-0000 remains a review placeholder.",
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
        "belief_shift_issue_fixture_review_ready": issue_fixture_review_ready,
        "belief_shift_issue_fixture_error": issue_fixture_error,
        "created_issue_review_ready": created_issue_review_ready,
        "created_issue_error": created_issue_error,
        "placeholder_rejection_enforced": placeholder_rejected,
        "placeholder_rejection_error": placeholder_rejection_error,
        "missing_required_artifacts": missing_artifacts,
        "writeback_performed": True,
        "github_issue_writeback_performed": True,
        "yaml_writeback_performed": False,
        "belief_shift_issue_created": True,
        "yaml_object_created": False,
        "meaning_atom_created": False,
        "generation_preflight_contract_created": True,
        "generation_gate_created": True,
        "issue_creation_gate_created": True,
        "validation_passed": validation_passed,
        "next_action": next_action,
    }


def render_text(status: dict[str, Any]) -> str:
    source = status["source"]
    lines = [
        f"workflow_id: {status['workflow_id']}",
        f"source_human_truth_id: {source['human_truth_id']}",
        f"input_fixture_valid: {str(status['input_fixture_valid']).lower()}",
        f"belief_shift_issue_fixture_review_ready: {str(status['belief_shift_issue_fixture_review_ready']).lower()}",
        f"created_issue_30_review_ready: {str(status['created_issue_review_ready']).lower()}",
        f"placeholder_rejection_enforced: {str(status['placeholder_rejection_enforced']).lower()}",
        f"source_review_fixture_promotion_ready: {str(source['review_fixture_promotion_ready']).lower()}",
        f"uses_live_issue_reference: {str(source['uses_live_issue_reference']).lower()}",
        f"writeback_performed: {str(status['writeback_performed']).lower()}",
        f"github_issue_writeback_performed: {str(status['github_issue_writeback_performed']).lower()}",
        f"yaml_writeback_performed: {str(status['yaml_writeback_performed']).lower()}",
        f"belief_shift_issue_created: {str(status['belief_shift_issue_created']).lower()}",
        f"yaml_object_created: {str(status['yaml_object_created']).lower()}",
        f"generation_preflight_contract_created: {str(status['generation_preflight_contract_created']).lower()}",
        f"generation_gate_created: {str(status['generation_gate_created']).lower()}",
        f"issue_creation_gate_created: {str(status['issue_creation_gate_created']).lower()}",
        f"validation_passed: {str(status['validation_passed']).lower()}",
        f"next_action: {status['next_action']}",
    ]
    if status["input_fixture_error"]:
        lines.append(f"input_fixture_error: {status['input_fixture_error']}")
    if status["belief_shift_issue_fixture_error"]:
        lines.append(f"belief_shift_issue_fixture_error: {status['belief_shift_issue_fixture_error']}")
    if status["created_issue_error"]:
        lines.append(f"created_issue_error: {status['created_issue_error']}")
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
