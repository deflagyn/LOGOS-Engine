# Manual Test — Foundation E Operations Layer

Owner issue: #15

Status: draft test evidence

---

## Scope

This test covers the first Operations Layer files:

- issue templates;
- experiment scoring model;
- weekly learning report template.

---

## Files Under Test

```text
.github/ISSUE_TEMPLATE/human-truth.yaml
.github/ISSUE_TEMPLATE/belief-shift.yaml
.github/ISSUE_TEMPLATE/experiment.yaml
.github/ISSUE_TEMPLATE/script.yaml
experiments/scoring-model.md
experiments/weekly-learning-report-template.md
```

---

## Test 1 — Template Structure

Purpose:

```text
Check that each issue template captures the minimum required information.
```

Manual steps:

1. Open a new issue in GitHub.
2. Select each LOGOS template.
3. Confirm that required fields appear.
4. Confirm that the template includes a test plan field.

Acceptance criteria:

```text
Each template can create a structured issue that includes ID, purpose-related fields and a test plan.
```

Evidence:

```text
A test issue created from each template or a screenshot of the form.
```

Current result:

```text
Files created. UI test pending.
```

---

## Test 2 — Scoring Model

Purpose:

```text
Check that the scoring model can convert sample experiment data into a 0-100 score.
```

Manual steps:

1. Create a sample experiment.
2. Assign five partial scores.
3. Calculate total score.
4. Write the reason for every score.

Acceptance criteria:

```text
The score is explainable and leads to a next decision.
```

Current result:

```text
Model file created. Sample scoring still pending.
```

---

## Test 3 — Weekly Learning Report

Purpose:

```text
Check that weekly metrics can become structured learning.
```

Manual steps:

1. Take one sample experiment.
2. Fill the weekly report template.
3. Record strongest signals, weakest signals and next actions.

Acceptance criteria:

```text
The report explains what worked, what failed and what to test next.
```

Current result:

```text
Template file created. Sample report still pending.
```

---

## Next Action

Create one sample experiment and use it to test:

- scoring model;
- weekly report;
- issue template flow.
