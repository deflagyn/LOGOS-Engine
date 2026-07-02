"""Validation CLI for the LOGOS Engine catalog."""

from __future__ import annotations

import argparse
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


def check_object_files(root: Path) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    seen_ids: dict[str, str] = {}

    for path in iter_files(root, (".yaml", ".yml")):
        data, error = load_yaml_file(path)
        if error or not isinstance(data, dict):
            continue

        object_id = data.get("id")
        relative_path = rel(root, path)

        if object_id:
            if object_id in seen_ids:
                issues.append(
                    ValidationIssue(
                        severity="ERROR",
                        path=relative_path,
                        message=f"duplicate object id {object_id}; first seen in {seen_ids[object_id]}",
                    )
                )
            else:
                seen_ids[str(object_id)] = relative_path

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
    issues.extend(check_required_files(root))
    issues.extend(check_yaml_parsing(root))
    issues.extend(check_object_files(root))
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
