# PILOT-0001 Response Intake Dry Run

Date: 2026-07-02

Status: passed

---

## Purpose

Verify that the local response intake script can build a valid response YAML preview without writing fake evidence into the repository.

---

## Command

```text
python scripts\create_pilot_response.py --input testing/fixtures/pilot-0001-response-input.json.example --dry-run
```

---

## Expected Result

```text
The script prints RESPONSE-PILOT-0001-0001 YAML.
No response file is created.
RUN-MANIFEST.yaml is not updated.
```

---

## Observed Result

```text
id: RESPONSE-PILOT-0001-0001
type: experiment_response
status: collected
pilot_id: PILOT-0001
experiment_id: EXP-PILOT-0001
personal_data_removed: true
evidence_boundary.creates_learning: false
evidence_boundary.creates_law_candidate: false
evidence_boundary.creates_logos_law: false
evidence_boundary.law_promotion_allowed: false
```

Repository check:

```text
pilots/PILOT-0001/experiment/responses/ contains only README.md
```

Conclusion:

```text
Dry run passed.
No fake response evidence was created.
```

---

## Additional Checks

Commands:

```text
python -m py_compile scripts\create_pilot_response.py logos_engine\validate.py
python scripts\validate_catalog.py .
python -m logos_engine.validate .
```

Result:

```text
py_compile passed.
LOGOS validation passed.
LOGOS validation passed.
```

---

## Path Reference Validation Check

Temporary file:

```text
testing/fixtures/reference-integrity/broken-source-path.tmp.yaml
```

Temporary content:

```yaml
id: TMP-PATH-REFERENCE-0001
type: test_fixture
status: invalid
source_path: missing/path/does-not-exist.md
```

Observed result:

```text
exit_code: 1
LOGOS validation found issues:
[ERROR] testing/fixtures/reference-integrity/broken-source-path.tmp.yaml: reference path does not exist: missing/path/does-not-exist.md
```

Cleanup:

```text
temporary broken-source-path.tmp.yaml removed
normal validation passed again
```

---

## Boundary

The fixture is only a dry-run input.

It is not real evidence and must not be committed under:

```text
pilots/PILOT-0001/experiment/responses/
```
