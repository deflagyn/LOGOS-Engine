# WF-0005 — Metrics Collector

## Purpose

Collect experiment metrics and attach them to the correct LOGOS experiment.

Metrics are feedback from reality.

They are not the final interpretation.

---

## Input

```text
Experiment ID
Platform metrics
Qualitative notes
Date range
```

---

## Output

```text
Structured metrics block
Updated experiment issue or file
Ready input for weekly learning report
```

---

## n8n Draft Nodes

```text
Schedule or Webhook
Fetch experiment list
Collect metrics from sheet or manual input
Normalize metrics
Update GitHub issue or file
Return summary
```

---

## Manual Dry Run

1. Select one experiment.
2. Prepare sample metrics.
3. Fill the metrics section manually.
4. Check if the weekly report can use it.

---

## Acceptance Criteria

```text
Given an experiment and metrics,
When the process runs,
Then structured metrics are attached to the right experiment.
```

---

## Test Plan

Purpose:

```text
Check whether experiment data can be captured in a reusable format.
```

Input:

```text
One experiment and one metrics set.
```

Expected output:

```text
One structured metrics block.
```

Evidence:

```text
Updated issue, file or report.
```

Future automation:

```text
n8n reads Google Sheets or platform exports and updates GitHub.
```
