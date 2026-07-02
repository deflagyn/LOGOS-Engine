"""Shared constants for LOGOS catalog validation."""

from __future__ import annotations

from pathlib import Path

FOUNDATION_REQUIRED_FILES = [
    Path("README.md"),
    Path("catalog.okf.yaml"),
    Path("constitution/LOGOS-CONSTITUTION.md"),
    Path("constitution/AXIOM-INDEX.md"),
    Path("ontology/OBJECTS.md"),
    Path("ontology/ID-CONVENTIONS.md"),
    Path("ontology/GLOSSARY.md"),
    Path("ontology/RELATIONSHIPS.md"),
    Path("ontology/OBJECT-LIFECYCLE.md"),
    Path("ontology/UNIVERSAL-VS-RUNTIME.md"),
    Path("engine/ENGINE-FLOW.md"),
    Path("triz/MEANING-TRIZ.md"),
    Path("validation/VALIDATION-PLAN.md"),
    Path("validation/CATALOG-RULES.md"),
    Path("validation/QUALITY-GATES.md"),
    Path("testing/TEST-FIRST-GOVERNANCE.md"),
    Path("testing/MODULE-TEST-TEMPLATE.md"),
    Path("testing/FOUNDATION-TEST-MATRIX.md"),
]

CORE_SCHEMA_FILES = [
    Path("schemas/logos-object.schema.yaml"),
    Path("schemas/human-truth.schema.yaml"),
    Path("schemas/human-contradiction.schema.yaml"),
    Path("schemas/belief-shift.schema.yaml"),
    Path("schemas/meaning-atom.schema.yaml"),
    Path("schemas/story-pattern.schema.yaml"),
    Path("schemas/experiment.schema.yaml"),
    Path("schemas/product-profile.schema.yaml"),
]

WORKFLOW_REQUIRED_SECTIONS = [
    "## Purpose",
    "## Input",
    "## Output",
    "## Manual Dry Run",
    "## Acceptance Criteria",
]

OBJECT_REQUIRED_FIELDS = [
    "id",
    "type",
    "status",
]

EXCLUDED_DIRS = {
    ".git",
    ".venv",
    "node_modules",
    "__pycache__",
}
