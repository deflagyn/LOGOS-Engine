# TEST-FOUNDATION-I — Reference Integrity Layer

Purpose:

```text
Verify that LOGOS validation detects duplicate object IDs, broken declared references and missing reference paths without requiring generated PILOT-0001 artifacts.
```

---

## Normal Validation

Input:

```text
Current repository state
```

Commands:

```bash
python scripts/validate_catalog.py .
python -m logos_engine.validate .
```

Expected output:

```text
LOGOS validation passed.
```

Acceptance criteria:

```text
Both direct script execution and package mode pass.
The valid reference fixture resolves existing IDs and file paths.
Ignored .example fixtures do not affect normal validation.
```

Evidence:

```text
testing/fixtures/reference-integrity/valid-chain.yaml
```

Future automation:

```text
GitHub Actions runs the same validator before trusting generated pilot artifacts.
```

---

## Broken Reference Manual Test

1. Copy the broken fixture to an active YAML file:

```bash
Copy-Item testing/fixtures/reference-integrity/broken-reference.yaml.example testing/fixtures/reference-integrity/broken-reference.yaml
```

2. Run:

```bash
python scripts/validate_catalog.py .
```

3. Expected result:

```text
LOGOS validation found issues:
[ERROR] testing/fixtures/reference-integrity/broken-reference.yaml: broken reference HT-DOES-NOT-EXIST ...
[ERROR] testing/fixtures/reference-integrity/broken-reference.yaml: broken reference MA-DOES-NOT-EXIST ...
[ERROR] testing/fixtures/reference-integrity/broken-reference.yaml: reference path does not exist ...
```

4. Remove the temporary active fixture:

```bash
Remove-Item testing/fixtures/reference-integrity/broken-reference.yaml
```

---

## Duplicate ID Manual Test

1. Copy both duplicate fixtures to active YAML files:

```bash
Copy-Item testing/fixtures/reference-integrity/duplicate-id-a.yaml.example testing/fixtures/reference-integrity/duplicate-id-a.yaml
Copy-Item testing/fixtures/reference-integrity/duplicate-id-b.yaml.example testing/fixtures/reference-integrity/duplicate-id-b.yaml
```

2. Run:

```bash
python scripts/validate_catalog.py .
```

3. Expected result:

```text
LOGOS validation found issues:
[ERROR] testing/fixtures/reference-integrity/duplicate-id-b.yaml: duplicate object id HT-FIXTURE-DUPLICATE-0001; first seen in testing/fixtures/reference-integrity/duplicate-id-a.yaml
```

4. Remove temporary active fixtures:

```bash
Remove-Item testing/fixtures/reference-integrity/duplicate-id-a.yaml
Remove-Item testing/fixtures/reference-integrity/duplicate-id-b.yaml
```

---

## PILOT-0001 Compatibility

PILOT-0001 files are optional until n8n creates them.

When any expected pilot YAML artifact exists under:

```text
pilots/PILOT-0001/input/
pilots/PILOT-0001/output/
```

the validator checks the required fields for that artifact.

Acceptance criteria:

```text
Repository validation passes before pilot artifacts exist.
Generated pilot artifacts must be structured before validation can pass.
```

