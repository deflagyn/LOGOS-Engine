"""Validation helpers for WF-0002 belief movement input and issue drafts."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import jsonschema
import yaml

from logos_engine.wf_0001_issue import parse_issue_sections


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "wf-0002-belief-movement-input.schema.yaml"
REQUIRED_BELIEF_SHIFT_ISSUE_SECTIONS = [
    "LOGOS ID",
    "Status",
    "Scope",
    "Source Human Truth ID",
    "Source Human Truth",
    "Audience context",
    "Before frame",
    "After frame",
    "Belief Shift candidate",
    "Meaning Atom draft",
    "Emotional result draft",
    "Test plan",
    "Generation evidence",
]
ALLOWED_BELIEF_SHIFT_STATUS = {
    "raw",
    "candidate",
    "draft",
    "testing",
    "validated",
    "rejected",
    "archived",
}
ALLOWED_SCOPE = {"universal", "runtime"}
BELIEF_SHIFT_ID_PATTERN = re.compile(r"^BS-(?:0000|[0-9]{4,})$")
STABLE_HT_ID_PATTERN = re.compile(r"^HT-(?!0000$)[0-9]{4,}$")


@dataclass(frozen=True)
class Wf0002BeliefShiftIssue:
    sections: dict[str, str]

    @property
    def logos_id(self) -> str:
        return self.sections["LOGOS ID"].splitlines()[0].strip()

    @property
    def status(self) -> str:
        return self.sections["Status"].splitlines()[0].strip()

    @property
    def scope(self) -> str:
        return self.sections["Scope"].splitlines()[0].strip()

    @property
    def source_human_truth_id(self) -> str:
        return self.sections["Source Human Truth ID"].splitlines()[0].strip()


def load_schema(path: Path = SCHEMA_PATH) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a YAML object")
    return data


def validate_wf_0002_belief_movement_input(data: dict[str, Any]) -> None:
    """Validate a WF-0002 belief movement input JSON object against the schema."""

    schema = load_schema()
    validator = jsonschema.Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(data), key=lambda error: list(error.path))
    if not errors:
        return

    rendered_errors = []
    for error in errors:
        path = ".".join(str(part) for part in error.path) or "<root>"
        rendered_errors.append(f"{path}: {error.message}")
    raise ValueError(
        "WF-0002 belief movement input schema validation failed: "
        + "; ".join(rendered_errors)
    )


def validate_wf_0002_belief_shift_issue_body(
    body: str,
    title: str | None = None,
) -> Wf0002BeliefShiftIssue:
    """Validate that a WF-0002 Belief Shift issue body is ready for review."""

    sections = parse_issue_sections(body)
    errors: list[str] = []

    for section in REQUIRED_BELIEF_SHIFT_ISSUE_SECTIONS:
        value = sections.get(section)
        if value is None:
            errors.append(f"missing section: {section}")
        elif not value.strip():
            errors.append(f"empty section: {section}")

    if errors:
        raise ValueError(
            "WF-0002 Belief Shift issue validation failed: " + "; ".join(errors)
        )

    issue = Wf0002BeliefShiftIssue(sections=sections)

    if not BELIEF_SHIFT_ID_PATTERN.match(issue.logos_id):
        errors.append("LOGOS ID must be BS-0000 or a stable BS-#### identifier")

    if issue.status not in ALLOWED_BELIEF_SHIFT_STATUS:
        errors.append(
            "Status must be one of: "
            + ", ".join(sorted(ALLOWED_BELIEF_SHIFT_STATUS))
        )

    if issue.scope not in ALLOWED_SCOPE:
        errors.append("Scope must be universal or runtime")

    if not STABLE_HT_ID_PATTERN.match(issue.source_human_truth_id):
        errors.append(
            "Source Human Truth ID must be a stable HT-#### identifier and cannot be HT-0000"
        )

    evidence = sections["Generation evidence"]
    if "Workflow: LOGOS WF-0002 Belief Movement Generation Preflight" not in evidence:
        errors.append("Generation evidence must name the WF-0002 generation preflight")
    if "no YAML object writeback" not in evidence:
        errors.append("Generation evidence must state that no YAML object writeback happened")
    if "no learning or law artifact" not in evidence:
        errors.append("Generation evidence must state that no learning or law artifact was created")

    if title is not None and not title.startswith("BS-"):
        errors.append("Issue title must start with BS-")

    if errors:
        raise ValueError(
            "WF-0002 Belief Shift issue validation failed: " + "; ".join(errors)
        )

    return issue
