# WF-0006 — Weekly Learning Report

## Purpose

Convert experiment metrics into structured LOGOS learning.

The report should explain what worked, what failed and what to test next.

---

## Input

```text
Experiments from the week
Scores
Metrics
Qualitative notes
Open questions
```

---

## Output

```text
Weekly learning report
Next actions
Possible Law Candidate notes
```

Primary GitHub output:

```text
Markdown report file or issue comment
```

---

## n8n Draft Nodes

```text
Weekly Schedule
Fetch recent experiments
Fetch metrics
Calculate scores
Draft learning report
Create GitHub file or comment
Return summary
```

---

## Manual Dry Run

1. Select one or more experiments.
2. Use the weekly report template.
3. Fill score summary.
4. Write learning and next actions.
5. Decide whether anything should become a Law Candidate.

---

## Acceptance Criteria

```text
Given experiment metrics,
When the report process runs,
Then a structured learning report exists with decisions and next actions.
```

---

## Test Plan

Purpose:

```text
Check whether metrics can become learning instead of only reporting.
```

Input:

```text
One scored experiment.
```

Expected output:

```text
One learning report.
```

Evidence:

```text
Weekly report file or issue comment.
```

Future automation:

```text
n8n drafts weekly report and requests human approval before publishing.
```
