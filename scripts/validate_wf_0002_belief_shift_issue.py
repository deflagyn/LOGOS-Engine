#!/usr/bin/env python3
"""Validate a WF-0002 Belief Shift issue body without creating YAML."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from logos_engine.wf_0002_belief_movement import (  # noqa: E402
    validate_wf_0002_belief_shift_issue_body,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", "-i", required=True, help="Markdown issue body file, or '-' for stdin")
    parser.add_argument("--title", help="Optional issue title to validate")
    args = parser.parse_args(argv)

    try:
        if args.input == "-":
            body = sys.stdin.read()
        else:
            body = Path(args.input).read_text(encoding="utf-8")
        issue = validate_wf_0002_belief_shift_issue_body(body, title=args.title)
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print("WF-0002 Belief Shift issue body passed review-readiness validation.")
    print(f"logos_id: {issue.logos_id}")
    print(f"source_human_truth_id: {issue.source_human_truth_id}")
    print(f"status: {issue.status}")
    print(f"scope: {issue.scope}")
    print("writeback_performed: false")
    print("yaml_object_created: false")
    return 0


if __name__ == "__main__":
    sys.exit(main())
