# Foundation Progress — Automation Runtime Design

Date: 2026-07-02

Owner issue: #16

---

## Purpose

Design the first n8n runtime layer for LOGOS.

GitHub remains the source of truth.

n8n will execute workflows and write results back to GitHub.

---

## Files Created

```text
automation/workflows/README.md
automation/workflows/idea-intake.md
automation/workflows/belief-shift-generator.md
automation/workflows/script-generator.md
automation/workflows/claim-checker.md
automation/workflows/metrics-collector.md
automation/workflows/weekly-learning-report.md
testing/manual/TEST-FOUNDATION-F.md
automation/samples/DRYRUN-0001-foundation-f.md
```

---

## Workflow Set

```text
WF-0001 Idea Intake
WF-0002 Belief Movement Generator
WF-0003 Script Generator
WF-0004 Review Checker
WF-0005 Metrics Collector
WF-0006 Weekly Learning Report
```

---

## What Works Now

- Each workflow has purpose, input and output.
- Each workflow has a manual dry run section.
- Each workflow identifies its GitHub artifact.
- A simulated chain dry run exists.
- The chain can move from raw idea to learning report in design form.

---

## Test Evidence

Manual test plan:

```text
testing/manual/TEST-FOUNDATION-F.md
```

Dry run sample:

```text
automation/samples/DRYRUN-0001-foundation-f.md
```

---

## Pending

- Build real n8n workflows.
- Connect Telegram or webhook input.
- Connect GitHub issue creation.
- Test one real workflow end to end.

---

## Decision

Group F is design-complete but implementation is pending.

The next technical phase should convert these designs into n8n workflows one by one.
