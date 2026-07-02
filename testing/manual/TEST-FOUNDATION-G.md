# Manual Test — Foundation G Developer Validation Layer

Owner issue: #17

Status: active

---

## Scope

This test covers the developer validation layer:

```text
pyproject.toml
logos_engine/schemas.py
logos_engine/validate.py
scripts/validate_catalog.py
.github/workflows/validate-catalog.yml
```

---

## Test 1 — Local Validation Script

Purpose:

```text
Check that the validation script can run against the repository.
```

Manual steps:

```text
python -m pip install -e .
python scripts/validate_catalog.py .
```

Expected result:

```text
The script prints either validation passed or a clear list of issues.
```

---

## Test 2 — Required Files

Purpose:

```text
Check that foundation and schema files exist.
```

Expected result:

```text
Missing foundation files are reported as errors.
```

---

## Test 3 — YAML Parsing

Purpose:

```text
Check that YAML files can be parsed.
```

Expected result:

```text
Invalid YAML is reported with a file path.
```

---

## Test 4 — Object Required Fields

Purpose:

```text
Check that object YAML files include required fields.
```

Expected result:

```text
Object files missing id, type or status are reported.
```

---

## Test 5 — Workflow Sections

Purpose:

```text
Check that automation workflow design files include core sections.
```

Expected result:

```text
Workflow files missing purpose, input, output, manual dry run or acceptance criteria are reported.
```

---

## Test 6 — GitHub Action

Purpose:

```text
Check that catalog validation can run in GitHub Actions.
```

Manual steps:

```text
Actions → Validate LOGOS Catalog → Run workflow
```

Expected result:

```text
Workflow completes or reports actionable validation issues.
```

---

## Current Result

Files created.

First real workflow run is pending.
