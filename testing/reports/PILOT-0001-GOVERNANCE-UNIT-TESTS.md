# PILOT-0001 Governance Unit Tests

Date: 2026-07-02

Status: passed

---

## Purpose

Protect the PILOT-0001 governance layer with automated tests.

These tests cover the safeguards that prevent false success:

```text
learning before responses
broken declared path references
response intake drift
```

---

## Test Command

```text
python -m unittest discover -s tests
```

---

## Tested Cases

```text
test_learning_requires_three_real_responses
test_declared_path_reference_must_exist
test_response_intake_creates_real_response_and_updates_manifest
test_response_intake_rejects_personal_data_not_removed
test_response_intake_rejects_simulated_response
test_pilot_status_reports_waiting_for_responses
test_pilot_status_allows_learning_after_three_valid_responses
```

---

## Local Result

```text
Ran 7 tests
OK
```

---

## CI

GitHub Actions `Validate LOGOS Catalog` now runs:

```text
python -m unittest discover -s tests
python scripts/validate_catalog.py .
```

---

## Boundary

The tests use temporary repository copies.

They do not create real PILOT-0001 response evidence.
