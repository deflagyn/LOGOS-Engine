#!/usr/bin/env python3
"""Validate a PILOT-0001 response intake JSON file without writing artifacts."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from logos_engine.pilot_response_input import validate_pilot_response_input  # noqa: E402


def load_json(path: str) -> dict[str, Any]:
    if path == "-":
        raw = sys.stdin.read()
    else:
        raw = Path(path).read_text(encoding="utf-8")
    data = json.loads(raw)
    if not isinstance(data, dict):
        raise ValueError("input JSON must be an object")
    return data


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", "-i", required=True, help="JSON input file, or '-' for stdin")
    args = parser.parse_args(argv)

    try:
        data = load_json(args.input)
        validate_pilot_response_input(data)
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print("PILOT-0001 response input schema passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

