#!/usr/bin/env python3
"""Validate a WF-0001 GitHub issue body without promoting it to YAML."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from logos_engine.wf_0001_issue import validate_wf_0001_issue_body  # noqa: E402


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
        issue = validate_wf_0001_issue_body(body, title=args.title)
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print("WF-0001 issue body passed review-readiness validation.")
    print(f"logos_id: {issue.logos_id}")
    print(f"status: {issue.status}")
    print(f"scope: {issue.scope}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

