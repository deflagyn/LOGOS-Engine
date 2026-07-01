# Foundation Progress — Operations Layer

Date: 2026-07-01

Owner issue: #15

Test evidence: #20

---

## Purpose

Create the first operations layer for LOGOS.

The goal is to make LOGOS work manageable through:

- GitHub issue templates;
- experiment scoring;
- weekly learning reports;
- test-first evidence.

---

## Files Created

```text
.github/ISSUE_TEMPLATE/config.yml
.github/ISSUE_TEMPLATE/human-truth.yaml
.github/ISSUE_TEMPLATE/belief-shift.yaml
.github/ISSUE_TEMPLATE/experiment.yaml
.github/ISSUE_TEMPLATE/script.yaml
experiments/scoring-model.md
experiments/weekly-learning-report-template.md
testing/manual/TEST-FOUNDATION-E.md
experiments/samples/EXP-SAMPLE-0001-foundation-e-scoring.md
experiments/reports/WR-SAMPLE-0001-foundation-e.md
```

---

## What Works Now

- Human Truth issues can be structured.
- Belief Shift issues can be structured.
- Experiment issues can be structured.
- Script issues can be structured.
- Experiment scoring model can produce a 0-100 score.
- Weekly report template can convert metrics into learning.
- Sample experiment scored 76/100.
- Sample weekly report produced structured learning.

---

## Tests Performed

Manual sample test:

```text
experiments/samples/EXP-SAMPLE-0001-foundation-e-scoring.md
```

Weekly learning sample:

```text
experiments/reports/WR-SAMPLE-0001-foundation-e.md
```

Test tracking issue:

```text
#20 TEST-0002: Foundation E sample scoring and report
```

---

## Pending Test

GitHub UI issue form rendering still needs to be checked manually:

```text
New Issue → choose each LOGOS template → confirm fields render correctly
```

This is pending because API-created issues do not prove that the GitHub UI form renders correctly.

---

## Decision

Group E is implementation-complete but remains open until UI issue-template rendering is confirmed.

---

## Next Group

Move to Group F:

```text
#16 FOUNDATION-F: Automation Runtime Design
```

The next task is to design n8n workflows with test plans from the beginning.
