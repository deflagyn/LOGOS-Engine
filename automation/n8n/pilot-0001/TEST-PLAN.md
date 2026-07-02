# PILOT-0001 n8n Test Plan

Owner issue: #27

Purpose: verify that the system, not the assistant manually, can process one raw meaning end to end.

---

## Test 1 — GitHub Issue Fetch

Input:

```text
issue_number = 27
```

Expected:

```text
n8n fetches issue title and body.
```

Pass criteria:

```text
raw meaning is present in node output.
```

---

## Test 2 — Raw Meaning Preservation

Expected:

```text
raw_text equals the original issue text exactly.
```

Pass criteria:

```text
pilots/PILOT-0001/input/raw-meaning.yaml exists and contains unchanged raw_text.
```

---

## Test 3 — Meaning Edges

Expected:

```text
At least three meaning edges are generated.
```

Pass criteria:

```text
meaning-edges.yaml exists and references raw_text.
```

---

## Test 4 — LOGOS Objects

Expected:

```text
Human Truth, Human Contradiction, Belief Shift, Meaning Atoms and Story Pattern are generated.
```

Pass criteria:

```text
Each object references pilot_id, source_issue and raw_text.
```

---

## Test 5 — Runtime Draft

Expected:

```text
A derived script draft is created.
```

Pass criteria:

```text
The draft explains what was preserved and what was changed.
```

---

## Test 6 — Experiment Plan

Expected:

```text
Experiment plan exists and law_promotion_allowed is false.
```

Pass criteria:

```text
The plan can be scored later using the existing scoring model.
```

---

## Test 7 — Learning and Law Review

Expected:

```text
Learning draft and law review are created.
```

Pass criteria:

```text
Law review does not create a LOGOS Law from one pilot run.
```

---

## Test 8 — GitHub Writeback

Expected:

```text
All files are created or updated in GitHub.
```

Pass criteria:

```text
Issue #27 receives run summary with file list.
```

---

## Test 9 — Validator

Expected:

```text
Validate LOGOS Catalog workflow is dispatched or local validator is run.
```

Pass criteria:

```text
Validator passes or reports actionable issues.
```

---

## Final Acceptance Criteria

```text
The system run creates traceable artifacts from raw meaning to learning.
Raw meaning remains preserved.
Derived outputs are not treated as replacement source.
GitHub remains source of truth.
No secrets are exposed.
```
