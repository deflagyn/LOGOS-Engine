"""Validation CLI for the LOGOS Engine catalog."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

from logos_engine.schemas import (
    CORE_SCHEMA_FILES,
    EXCLUDED_DIRS,
    FOUNDATION_REQUIRED_FILES,
    OBJECT_REQUIRED_FIELDS,
    WORKFLOW_REQUIRED_SECTIONS,
)


@dataclass(frozen=True)
class ValidationIssue:
    severity: str
    path: str
    message: str

    def render(self) -> str:
        return f"[{self.severity}] {self.path}: {self.message}"


@dataclass(frozen=True)
class ObjectRegistryEntry:
    object_id: str
    object_type: str
    path: str
    status: str | None
    data: dict[str, Any]


LOGOS_ID_RE = re.compile(
    r"\b(?:HT|HC|BS|MA|SP|SCRIPT|EXP|LEARN|LAW|LC|RM|ME|PILOT)-"
    r"[A-Z0-9]+(?:-[A-Z0-9]+)*\b"
)

REFERENCE_FIELD_NAMES = {
    "source_id",
    "source_ids",
    "source_experiment",
    "source_learning",
    "source_path",
    "source_script_path",
    "review_source_path",
    "source_raw_meaning_id",
    "human_truth_id",
    "human_contradiction_id",
    "belief_shift_id",
    "meaning_atom_id",
    "meaning_atom_ids",
    "story_pattern_id",
    "script_id",
    "experiment_id",
    "learning_id",
    "law_candidate_id",
    "trace_to_previous",
    "linked_objects",
    "connected_objects",
    "references",
    "story_patterns",
    "path",
}

PILOT_0001_EXPECTED_FILES = {
    Path("pilots/PILOT-0001/input/raw-meaning.yaml"): ["id", "type", "pilot_id", "raw_text"],
    Path("pilots/PILOT-0001/output/meaning-edges.yaml"): [
        "id",
        "type",
        "pilot_id",
    ],
    Path("pilots/PILOT-0001/output/human-truth.yaml"): ["id", "type", "status", "pilot_id"],
    Path("pilots/PILOT-0001/output/human-contradiction.yaml"): [
        "id",
        "type",
        "status",
        "pilot_id",
    ],
    Path("pilots/PILOT-0001/output/belief-shift.yaml"): ["id", "type", "status", "pilot_id"],
    Path("pilots/PILOT-0001/output/meaning-atoms.yaml"): ["id", "type", "status", "pilot_id"],
    Path("pilots/PILOT-0001/output/story-pattern.yaml"): ["id", "type", "status", "pilot_id"],
    Path("pilots/PILOT-0001/output/experiment-plan.yaml"): ["id", "type", "status", "pilot_id"],
}

PILOT_0001_RESPONSE_DIR = Path("pilots/PILOT-0001/experiment/responses")
PILOT_0001_LEARNING_PATHS = [
    Path("pilots/PILOT-0001/output/learning.md"),
    Path("pilots/PILOT-0001/output/law-review.md"),
]
PILOT_0001_MIN_RESPONSES_FOR_LEARNING = 3


def is_excluded(path: Path) -> bool:
    return any(part in EXCLUDED_DIRS for part in path.parts)


def iter_files(root: Path, suffixes: tuple[str, ...]) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        if path.is_file() and not is_excluded(path) and path.suffix in suffixes:
            files.append(path)
    return sorted(files)


def rel(root: Path, path: Path) -> str:
    return str(path.relative_to(root)).replace("\\", "/")


def load_yaml_file(path: Path) -> tuple[Any | None, str | None]:
    try:
        with path.open("r", encoding="utf-8") as handle:
            return yaml.safe_load(handle), None
    except Exception as exc:  # noqa: BLE001
        return None, str(exc)


def is_logos_object(data: Any) -> bool:
    return isinstance(data, dict) and bool(data.get("id")) and bool(data.get("type"))


def build_object_registry(
    root: Path,
) -> tuple[dict[str, ObjectRegistryEntry], list[ValidationIssue]]:
    registry: dict[str, ObjectRegistryEntry] = {}
    issues: list[ValidationIssue] = []

    for path in iter_files(root, (".yaml", ".yml")):
        data, error = load_yaml_file(path)
        if error or not is_logos_object(data):
            continue

        assert isinstance(data, dict)
        object_id = str(data["id"])
        relative_path = rel(root, path)
        entry = ObjectRegistryEntry(
            object_id=object_id,
            object_type=str(data["type"]),
            path=relative_path,
            status=str(data["status"]) if data.get("status") is not None else None,
            data=data,
        )

        if object_id in registry:
            issues.append(
                ValidationIssue(
                    severity="ERROR",
                    path=relative_path,
                    message=(
                        f"duplicate object id {object_id}; "
                        f"first seen in {registry[object_id].path}"
                    ),
                )
            )
            continue

        registry[object_id] = entry

    return registry, issues


def check_required_files(root: Path) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    for path in FOUNDATION_REQUIRED_FILES + CORE_SCHEMA_FILES:
        full_path = root / path
        if not full_path.exists():
            issues.append(
                ValidationIssue(
                    severity="ERROR",
                    path=str(path),
                    message="required foundation file is missing",
                )
            )
    return issues


def check_yaml_parsing(root: Path) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    for path in iter_files(root, (".yaml", ".yml")):
        _, error = load_yaml_file(path)
        if error:
            issues.append(
                ValidationIssue(
                    severity="ERROR",
                    path=rel(root, path),
                    message=f"YAML parse failed: {error}",
                )
            )
    return issues


def check_object_files(
    root: Path, registry: dict[str, ObjectRegistryEntry]
) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []

    for path in iter_files(root, (".yaml", ".yml")):
        data, error = load_yaml_file(path)
        if error or not isinstance(data, dict):
            continue

        relative_path = rel(root, path)

        is_object_path = "/objects/" in f"/{relative_path}"
        if is_object_path:
            for field in OBJECT_REQUIRED_FIELDS:
                if field not in data or data.get(field) in (None, ""):
                    issues.append(
                        ValidationIssue(
                            severity="ERROR",
                            path=relative_path,
                            message=f"object file missing required field: {field}",
                        )
                    )

        if is_logos_object(data):
            object_id = str(data["id"])
            if object_id not in registry:
                issues.append(
                    ValidationIssue(
                        severity="ERROR",
                        path=relative_path,
                        message=f"object id {object_id} could not be added to registry",
                    )
                )

    return issues


def looks_like_path(value: str) -> bool:
    if not value or value.startswith(("http://", "https://", "#")):
        return False
    if "\n" in value:
        return False
    normalized = value.replace("\\", "/")
    return "/" in normalized and bool(Path(normalized).suffix)


def iter_reference_values(value: Any) -> list[str]:
    values: list[str] = []
    if isinstance(value, str):
        if value.strip():
            values.append(value.strip())
    elif isinstance(value, list):
        for item in value:
            values.extend(iter_reference_values(item))
    elif isinstance(value, dict):
        for item in value.values():
            values.extend(iter_reference_values(item))
    return values


def check_reference_integrity(
    root: Path, registry: dict[str, ObjectRegistryEntry]
) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    seen_issues: set[tuple[str, str, str]] = set()

    def add_issue(path: str, field_path: str, message: str) -> None:
        key = (path, field_path, message)
        if key in seen_issues:
            return
        seen_issues.add(key)
        issues.append(ValidationIssue(severity="ERROR", path=path, message=message))

    def walk(data: Any, relative_path: str, field_path: str = "") -> None:
        if isinstance(data, dict):
            for key, value in data.items():
                child_path = f"{field_path}.{key}" if field_path else str(key)
                if key in REFERENCE_FIELD_NAMES:
                    for reference in iter_reference_values(value):
                        if looks_like_path(reference):
                            candidate = (root / reference).resolve()
                            try:
                                candidate.relative_to(root)
                            except ValueError:
                                add_issue(
                                    relative_path,
                                    child_path,
                                    f"reference path escapes repository root: {reference}",
                                )
                                continue
                            if not candidate.exists():
                                add_issue(
                                    relative_path,
                                    child_path,
                                    f"reference path does not exist: {reference}",
                                )
                            continue

                        for object_id in LOGOS_ID_RE.findall(reference):
                            if object_id not in registry:
                                add_issue(
                                    relative_path,
                                    child_path,
                                    (
                                        f"broken reference {object_id} in {child_path}; "
                                        "no matching LOGOS object id found"
                                    ),
                                )
                walk(value, relative_path, child_path)
        elif isinstance(data, list):
            for index, item in enumerate(data):
                child_path = f"{field_path}[{index}]"
                walk(item, relative_path, child_path)

    for path in iter_files(root, (".yaml", ".yml")):
        data, error = load_yaml_file(path)
        if error or not isinstance(data, dict):
            continue
        walk(data, rel(root, path))

    return issues


def check_pilot_artifacts(root: Path) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []

    for relative_path, required_fields in PILOT_0001_EXPECTED_FILES.items():
        path = root / relative_path
        if not path.exists():
            continue

        data, error = load_yaml_file(path)
        if error:
            continue
        if not isinstance(data, dict):
            issues.append(
                ValidationIssue(
                    severity="ERROR",
                    path=str(relative_path),
                    message="PILOT-0001 artifact must be a YAML object",
                )
            )
            continue

        for field in required_fields:
            if field not in data or data.get(field) in (None, ""):
                issues.append(
                    ValidationIssue(
                        severity="ERROR",
                        path=str(relative_path),
                        message=f"PILOT-0001 artifact missing required field: {field}",
                    )
                )

        if relative_path.name == "meaning-edges.yaml":
            if not data.get("source_raw_meaning_id") and not data.get("raw_text"):
                issues.append(
                    ValidationIssue(
                        severity="ERROR",
                        path=str(relative_path),
                        message=(
                            "PILOT-0001 meaning edges must include "
                            "source_raw_meaning_id or raw_text"
                        ),
                    )
                )

    return issues


def iter_pilot_0001_response_files(root: Path) -> list[Path]:
    response_dir = root / PILOT_0001_RESPONSE_DIR
    if not response_dir.exists():
        return []
    return sorted(
        path
        for path in response_dir.glob("*.yaml")
        if path.is_file() and not path.name.endswith(".example.yaml")
    )


def check_pilot_0001_evidence_gate(root: Path) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    response_files = iter_pilot_0001_response_files(root)
    real_response_count = 0

    for path in response_files:
        relative_path = rel(root, path)
        data, error = load_yaml_file(path)
        if error:
            continue
        if not isinstance(data, dict):
            issues.append(
                ValidationIssue(
                    severity="ERROR",
                    path=relative_path,
                    message="PILOT-0001 response must be a YAML object",
                )
            )
            continue

        required_fields = [
            "id",
            "type",
            "status",
            "pilot_id",
            "experiment_id",
            "personal_data_removed",
        ]
        for field in required_fields:
            if field not in data or data.get(field) in (None, ""):
                issues.append(
                    ValidationIssue(
                        severity="ERROR",
                        path=relative_path,
                        message=f"PILOT-0001 response missing required field: {field}",
                    )
                )

        if data.get("type") != "experiment_response":
            issues.append(
                ValidationIssue(
                    severity="ERROR",
                    path=relative_path,
                    message="PILOT-0001 response type must be experiment_response",
                )
            )
        if data.get("pilot_id") != "PILOT-0001":
            issues.append(
                ValidationIssue(
                    severity="ERROR",
                    path=relative_path,
                    message="PILOT-0001 response must reference pilot_id PILOT-0001",
                )
            )
        if data.get("experiment_id") != "EXP-PILOT-0001":
            issues.append(
                ValidationIssue(
                    severity="ERROR",
                    path=relative_path,
                    message="PILOT-0001 response must reference EXP-PILOT-0001",
                )
            )
        if data.get("status") == "blank_template":
            issues.append(
                ValidationIssue(
                    severity="ERROR",
                    path=relative_path,
                    message="blank response template must not be stored as a real response",
                )
            )
        if data.get("personal_data_removed") is not True:
            issues.append(
                ValidationIssue(
                    severity="ERROR",
                    path=relative_path,
                    message="PILOT-0001 response must set personal_data_removed: true",
                )
            )

        evidence_boundary = data.get("evidence_boundary", {})
        if isinstance(evidence_boundary, dict):
            for field in [
                "creates_learning",
                "creates_law_candidate",
                "creates_logos_law",
                "law_promotion_allowed",
            ]:
                if evidence_boundary.get(field) is True:
                    issues.append(
                        ValidationIssue(
                            severity="ERROR",
                            path=relative_path,
                            message=(
                                "PILOT-0001 response evidence_boundary must not "
                                f"set {field}: true"
                            ),
                        )
                    )

        if not issues or all(issue.path != relative_path for issue in issues):
            real_response_count += 1

    for relative_path in PILOT_0001_LEARNING_PATHS:
        if (root / relative_path).exists() and (
            real_response_count < PILOT_0001_MIN_RESPONSES_FOR_LEARNING
        ):
            issues.append(
                ValidationIssue(
                    severity="ERROR",
                    path=str(relative_path),
                    message=(
                        "PILOT-0001 learning/law artifact requires at least "
                        f"{PILOT_0001_MIN_RESPONSES_FOR_LEARNING} real responses; "
                        f"found {real_response_count}"
                    ),
                )
            )

    manifest_path = root / "pilots/PILOT-0001/RUN-MANIFEST.yaml"
    if manifest_path.exists():
        manifest, error = load_yaml_file(manifest_path)
        if not error and isinstance(manifest, dict):
            boundary = manifest.get("current_boundary", {})
            if isinstance(boundary, dict):
                declared_response_count = boundary.get("real_response_count")
                if declared_response_count != real_response_count:
                    issues.append(
                        ValidationIssue(
                            severity="ERROR",
                            path=rel(root, manifest_path),
                            message=(
                                "RUN-MANIFEST real_response_count must match "
                                f"response files; declared {declared_response_count}, "
                                f"found {real_response_count}"
                            ),
                        )
                    )
                if real_response_count < PILOT_0001_MIN_RESPONSES_FOR_LEARNING:
                    for field in [
                        "learning_created",
                        "law_candidate_created",
                        "logos_law_created",
                    ]:
                        if boundary.get(field) is True:
                            issues.append(
                                ValidationIssue(
                                    severity="ERROR",
                                    path=rel(root, manifest_path),
                                    message=(
                                        f"RUN-MANIFEST {field} cannot be true "
                                        f"before {PILOT_0001_MIN_RESPONSES_FOR_LEARNING} "
                                        "real responses exist"
                                    ),
                                )
                            )

    return issues


def check_workflow_docs(root: Path) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    workflow_dir = root / "automation" / "workflows"
    if not workflow_dir.exists():
        return issues

    for path in sorted(workflow_dir.glob("*.md")):
        if path.name == "README.md":
            continue
        text = path.read_text(encoding="utf-8")
        for section in WORKFLOW_REQUIRED_SECTIONS:
            if section not in text:
                issues.append(
                    ValidationIssue(
                        severity="ERROR",
                        path=rel(root, path),
                        message=f"workflow file missing section: {section}",
                    )
                )
    return issues


def check_test_first_docs(root: Path) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    required = [
        root / "testing" / "TEST-FIRST-GOVERNANCE.md",
        root / "testing" / "MODULE-TEST-TEMPLATE.md",
        root / "testing" / "FOUNDATION-TEST-MATRIX.md",
    ]
    for path in required:
        if not path.exists():
            issues.append(
                ValidationIssue(
                    severity="ERROR",
                    path=rel(root, path),
                    message="test-first governance file missing",
                )
            )
    return issues


def validate_repository(root: Path) -> list[ValidationIssue]:
    root = root.resolve()
    issues: list[ValidationIssue] = []
    registry, registry_issues = build_object_registry(root)
    issues.extend(check_required_files(root))
    issues.extend(check_yaml_parsing(root))
    issues.extend(registry_issues)
    issues.extend(check_object_files(root, registry))
    issues.extend(check_reference_integrity(root, registry))
    issues.extend(check_pilot_artifacts(root))
    issues.extend(check_pilot_0001_evidence_gate(root))
    issues.extend(check_workflow_docs(root))
    issues.extend(check_test_first_docs(root))
    return issues


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate the LOGOS Engine catalog.")
    parser.add_argument("root", nargs="?", default=".", help="Repository root path")
    args = parser.parse_args(argv)

    root = Path(args.root)
    issues = validate_repository(root)

    if not issues:
        print("LOGOS validation passed.")
        return 0

    print("LOGOS validation found issues:")
    for issue in issues:
        print(issue.render())

    has_error = any(issue.severity == "ERROR" for issue in issues)
    return 1 if has_error else 0


if __name__ == "__main__":
    sys.exit(main())
