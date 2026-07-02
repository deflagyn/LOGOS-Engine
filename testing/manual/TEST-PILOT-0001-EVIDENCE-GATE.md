# TEST-PILOT-0001 — Evidence Gate

Date: 2026-07-02

Status: manual test

Related:

```text
pilots/PILOT-0001/experiment/TEST-PROTOCOL.md
pilots/PILOT-0001/experiment/response-template.yaml
pilots/PILOT-0001/RUN-MANIFEST.yaml
logos_engine/validate.py
```

---

## Purpose

Confirm that PILOT-0001 cannot silently move from experiment planning into learning or law review without real evidence.

The validator should protect this boundary:

```text
experiment plan candidate
-> real responses
-> learning candidate
-> law review later
```

It should reject:

```text
experiment plan candidate
-> learning.md with zero responses
```

---

## Normal Validation

Run:

```text
python scripts\validate_catalog.py .
python -m logos_engine.validate .
```

Expected result:

```text
LOGOS validation passed.
LOGOS validation passed.
```

---

## Manual Failure Check

To test the guard manually, temporarily create:

```text
pilots/PILOT-0001/output/learning.md
```

Then run:

```text
python scripts\validate_catalog.py .
```

Expected error:

```text
PILOT-0001 learning/law artifact requires at least 3 real responses; found 0
```

Remove the temporary file after the check.

---

## Response File Check

A real response must live under:

```text
pilots/PILOT-0001/experiment/responses/
```

It must include:

```text
id
type: experiment_response
status
pilot_id: PILOT-0001
experiment_id: EXP-PILOT-0001
personal_data_removed: true
```

It must not set:

```text
evidence_boundary.creates_learning: true
evidence_boundary.creates_law_candidate: true
evidence_boundary.creates_logos_law: true
evidence_boundary.law_promotion_allowed: true
```

---

## Manifest Check

`RUN-MANIFEST.yaml` must keep:

```text
current_boundary.real_response_count
```

in sync with actual response YAML files.

If the folder has zero real response YAML files, the manifest must say:

```text
real_response_count: 0
learning_created: false
law_candidate_created: false
logos_law_created: false
```

---

## Acceptance

The evidence gate is working when:

```text
normal repository validation passes
temporary learning.md fails without real responses
invalid response files fail
manifest response count drift fails
```

