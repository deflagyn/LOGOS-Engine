#!/usr/bin/env python3
"""Entrypoint for LOGOS catalog validation."""

from __future__ import annotations

import sys

from logos_engine.validate import main


if __name__ == "__main__":
    sys.exit(main())
