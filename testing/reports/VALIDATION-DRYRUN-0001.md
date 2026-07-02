# VALIDATION-DRYRUN-0001 — Developer Validation Layer

Owner issue: #17

Status: first workflow error addressed, rerun pending

---

## Purpose

Record the first validation design check for Foundation G.

---

## Created Validation Layer

```text
pyproject.toml
logos_engine/__init__.py
logos_engine/schemas.py
logos_engine/validate.py
scripts/validate_catalog.py
.github/workflows/validate-catalog.yml
testing/manual/TEST-FOUNDATION-G.md
```

---

## What the Validator Checks

```text
1. Required foundation files exist.
2. Core schema files exist.
3. YAML files parse correctly.
4. Object YAML files include id, type and status.
5. Workflow design files include required sections.
6. Test-first governance files exist.
```

---

## Manual Run Command

```text
python -m pip install -e .
python scripts/validate_catalog.py .
```

---

## GitHub Action

```text
Actions → Validate LOGOS Catalog → Run workflow
```

---

## First Workflow Error

The first GitHub Actions run failed.

Most likely reason found in the repository setup:

```text
pyproject.toml had project metadata but no build-system configuration.
```

This can break:

```text
python -m pip install -e .
```

---

## Fix Applied

Added to `pyproject.toml`:

```text
[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"
```

Also added package discovery:

```text
[tool.setuptools.packages.find]
include = ["logos_engine*"]
```

Fix commit:

```text
4bb08f45390d173a0eab664861ce0ac9d7721e0b
```

---

## Current Result

```text
Install configuration fixed.
Workflow rerun pending.
```

---

## Next Evidence Needed

A GitHub Actions rerun log or local validation output.
