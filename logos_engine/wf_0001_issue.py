"""Validation helpers for WF-0001 GitHub issue bodies."""

from __future__ import annotations

import re
from dataclasses import dataclass


REQUIRED_SECTIONS = [
    "LOGOS ID",
    "Status",
    "Scope",
    "Source or context",
    "Raw observation",
    "Human Truth candidate",
    "Test plan",
    "Intake evidence",
]

ALLOWED_STATUS = {
    "raw",
    "candidate",
    "draft",
    "testing",
    "validated",
    "rejected",
    "archived",
}

ALLOWED_SCOPE = {"universal", "runtime"}
LOGOS_ID_PATTERN = re.compile(r"^HT-(?:0000|[0-9]{4,})$")


@dataclass(frozen=True)
class Wf0001Issue:
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


def parse_issue_sections(body: str) -> dict[str, str]:
    """Parse a GitHub issue body into level-two Markdown sections."""

    sections: dict[str, list[str]] = {}
    current: str | None = None

    for line in body.splitlines():
        if line.startswith("## "):
            current = line[3:].strip()
            sections.setdefault(current, [])
            continue
        if current is not None:
            sections[current].append(line)

    return {heading: "\n".join(lines).strip() for heading, lines in sections.items()}


def validate_wf_0001_issue_body(body: str, title: str | None = None) -> Wf0001Issue:
    """Validate that a WF-0001 GitHub issue body is ready for human review."""

    sections = parse_issue_sections(body)
    errors: list[str] = []

    for section in REQUIRED_SECTIONS:
        value = sections.get(section)
        if value is None:
            errors.append(f"missing section: {section}")
        elif not value.strip():
            errors.append(f"empty section: {section}")

    if errors:
        raise ValueError("WF-0001 issue validation failed: " + "; ".join(errors))

    issue = Wf0001Issue(sections=sections)

    if not LOGOS_ID_PATTERN.match(issue.logos_id):
        errors.append("LOGOS ID must be HT-0000 or a stable HT-#### identifier")

    if issue.status not in ALLOWED_STATUS:
        errors.append(f"Status must be one of: {', '.join(sorted(ALLOWED_STATUS))}")

    if issue.scope not in ALLOWED_SCOPE:
        errors.append("Scope must be universal or runtime")

    evidence = sections["Intake evidence"]
    if "Workflow: LOGOS WF-0001 Idea Intake Issue Gate" not in evidence:
        errors.append("Intake evidence must name the WF-0001 n8n issue gate")
    if "no YAML object writeback" not in evidence:
        errors.append("Intake evidence must state that no YAML object writeback happened")
    if "no learning or law artifact" not in evidence:
        errors.append("Intake evidence must state that no learning or law artifact was created")

    if title is not None and not title.startswith("HT-"):
        errors.append("Issue title must start with HT-")

    if errors:
        raise ValueError("WF-0001 issue validation failed: " + "; ".join(errors))

    return issue

