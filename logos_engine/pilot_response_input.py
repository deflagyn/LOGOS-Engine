"""Validation helpers for PILOT-0001 response intake input."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import jsonschema
import yaml


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "pilot-response-input.schema.yaml"


def load_schema(path: Path = SCHEMA_PATH) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a YAML object")
    return data


def validate_pilot_response_input(data: dict[str, Any]) -> None:
    """Validate a PILOT-0001 response intake JSON object against the schema."""

    schema = load_schema()
    validator = jsonschema.Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(data), key=lambda error: list(error.path))
    if not errors:
        return

    rendered_errors = []
    for error in errors:
        path = ".".join(str(part) for part in error.path) or "<root>"
        rendered_errors.append(f"{path}: {error.message}")
    raise ValueError("response input schema validation failed: " + "; ".join(rendered_errors))

