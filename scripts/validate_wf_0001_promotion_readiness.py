#!/usr/bin/env python3
"""Validate WF-0001 issue readiness for future YAML promotion without writing YAML."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from logos_engine.wf_0001_issue import (  # noqa: E402
    PROMOTION_REVIEW_ATTESTATION,
    validate_wf_0001_promotion_readiness,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", "-i", required=True, help="Markdown issue body file, or '-' for stdin")
    parser.add_argument("--title", help="Optional issue title to validate")
    parser.add_argument(
        "--review-attestation",
        required=True,
        help=f"Must equal {PROMOTION_REVIEW_ATTESTATION}",
    )
    args = parser.parse_args(argv)

    try:
        if args.input == "-":
            body = sys.stdin.read()
        else:
            body = Path(args.input).read_text(encoding="utf-8")
        issue = validate_wf_0001_promotion_readiness(
            body,
            title=args.title,
            review_attestation=args.review_attestation,
        )
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print("WF-0001 issue passed YAML promotion-readiness validation.")
    print(f"logos_id: {issue.logos_id}")
    print(f"status: {issue.status}")
    print(f"scope: {issue.scope}")
    print("writeback_performed: false")
    return 0


if __name__ == "__main__":
    sys.exit(main())

