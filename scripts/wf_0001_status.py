#!/usr/bin/env python3
"""Report WF-0001 readiness without mutating repository or n8n state."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from logos_engine.wf_0001_idea_intake import validate_wf_0001_idea_intake  # noqa: E402
from logos_engine.wf_0001_issue import (  # noqa: E402
    PROMOTION_REVIEW_ATTESTATION,
    validate_wf_0001_issue_body,
    validate_wf_0001_promotion_readiness,
)


REQUIRED_ARTIFACTS = [
    "automation/workflows/idea-intake.md",
    "automation/n8n/wf-0001/IDEA-INTAKE-ISSUE-GATE.md",
    "automation/n8n/wf-0001/PROMOTION-READINESS-PREFLIGHT-GATE.md",
    "automation/n8n/wf-0001/writeback/idea-intake-issue-gate-test-2026-07-02.md",
    "automation/n8n/wf-0001/writeback/idea-intake-schema-parity-test-2026-07-02.md",
    "automation/n8n/wf-0001/writeback/idea-intake-issue-review-readiness-2026-07-02.md",
    "automation/n8n/wf-0001/writeback/idea-intake-promotion-readiness-2026-07-02.md",
    "automation/n8n/wf-0001/writeback/promotion-readiness-preflight-gate-test-2026-07-02.md",
    "schemas/wf-0001-idea-intake.schema.yaml",
    "testing/fixtures/wf-0001-idea-intake.json.example",
    "testing/fixtures/wf-0001-issue-29.md",
    "testing/fixtures/wf-0001-issue-reviewed-stable.md",
    "scripts/validate_wf_0001_idea_intake.py",
    "scripts/validate_wf_0001_issue.py",
    "scripts/validate_wf_0001_promotion_readiness.py",
]

ISSUE_29_TITLE = "HT-0000: Intake must preserve raw observations before interpretation"
REVIEWED_STABLE_TITLE = "HT-0100: Intake must preserve raw observations before interpretation"


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


def build_status(root: Path) -> dict[str, Any]:
    missing_artifacts = [
        path for path in REQUIRED_ARTIFACTS if not (root / path).exists()
    ]

    payload_fixture = root / "testing" / "fixtures" / "wf-0001-idea-intake.json.example"
    issue_29_fixture = root / "testing" / "fixtures" / "wf-0001-issue-29.md"
    stable_fixture = root / "testing" / "fixtures" / "wf-0001-issue-reviewed-stable.md"

    payload_valid, payload_error = check(
        validate_wf_0001_idea_intake,
        load_json(payload_fixture),
    )

    issue_29_body = issue_29_fixture.read_text(encoding="utf-8")
    issue_29_review_ready, issue_29_review_error = check(
        validate_wf_0001_issue_body,
        issue_29_body,
        title=ISSUE_29_TITLE,
    )

    issue_29_promotion_ready, issue_29_promotion_error = check(
        validate_wf_0001_promotion_readiness,
        issue_29_body,
        title=ISSUE_29_TITLE,
        review_attestation=PROMOTION_REVIEW_ATTESTATION,
    )

    stable_body = stable_fixture.read_text(encoding="utf-8")
    stable_promotion_ready, stable_promotion_error = check(
        validate_wf_0001_promotion_readiness,
        stable_body,
        title=REVIEWED_STABLE_TITLE,
        review_attestation=PROMOTION_REVIEW_ATTESTATION,
    )

    validation_passed = (
        not missing_artifacts
        and payload_valid
        and issue_29_review_ready
        and not issue_29_promotion_ready
        and stable_promotion_ready
    )

    if missing_artifacts:
        next_action = "restore_missing_wf_0001_artifacts"
    elif not payload_valid or not issue_29_review_ready or not stable_promotion_ready:
        next_action = "fix_wf_0001_validation_contract"
    elif issue_29_promotion_ready:
        next_action = "review_unexpected_issue_29_promotion_readiness"
    else:
        next_action = "assign_stable_ht_id_or_collect_next_real_idea"

    return {
        "workflow_id": "WF-0001",
        "intake_issue_gate": {
            "name": "LOGOS WF-0001 Idea Intake Issue Gate",
            "n8n_id": "s00B4QAhJ3MYZ1tq",
            "expected_active": False,
        },
        "promotion_preflight_gate": {
            "name": "LOGOS WF-0001 Promotion Readiness Preflight Gate",
            "n8n_id": "a8peB0KHbGvAj3gg",
            "expected_active": False,
        },
        "created_issue": {
            "number": 29,
            "url": "https://github.com/deflagyn/LOGOS-Engine/issues/29",
            "title": ISSUE_29_TITLE,
            "review_ready": issue_29_review_ready,
            "promotion_ready": issue_29_promotion_ready,
            "promotion_block_reason": issue_29_promotion_error,
        },
        "payload_fixture_valid": payload_valid,
        "payload_fixture_error": payload_error,
        "reviewed_stable_fixture_promotion_ready": stable_promotion_ready,
        "reviewed_stable_fixture_error": stable_promotion_error,
        "missing_required_artifacts": missing_artifacts,
        "validation_passed": validation_passed,
        "next_action": next_action,
    }


def render_text(status: dict[str, Any]) -> str:
    created_issue = status["created_issue"]
    lines = [
        f"workflow_id: {status['workflow_id']}",
        f"payload_fixture_valid: {str(status['payload_fixture_valid']).lower()}",
        f"issue_29_review_ready: {str(created_issue['review_ready']).lower()}",
        f"issue_29_promotion_ready: {str(created_issue['promotion_ready']).lower()}",
        f"reviewed_stable_fixture_promotion_ready: {str(status['reviewed_stable_fixture_promotion_ready']).lower()}",
        f"validation_passed: {str(status['validation_passed']).lower()}",
        f"next_action: {status['next_action']}",
    ]
    if created_issue["promotion_block_reason"]:
        lines.append(f"issue_29_promotion_block_reason: {created_issue['promotion_block_reason']}")
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

