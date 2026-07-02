# LOGOS Learning Model

This document defines how LOGOS converts experiment results into structured learning.

Learning is not a report of numbers.

Learning is a decision about what the system now understands better.

---

## Purpose

The learning layer protects LOGOS from two errors:

1. treating one result as universal truth;
2. ignoring useful signals because they are not yet a law.

---

## Learning Chain

```text
Experiment
→ Metrics
→ Qualitative Signals
→ Interpretation
→ Decision
→ Next Iteration
→ Law Candidate Review
```

---

## What Counts as Learning

A result becomes learning only when it answers:

```text
What happened?
Why might it have happened?
What belief, meaning or story pattern moved?
What should we do next?
What should not be concluded yet?
```

---

## Learning Object

A learning object should include:

```yaml
id: LEARN-0000
type: learning
status: draft
source_experiment: EXP-0000
summary: ""
what_happened: ""
interpretation: ""
decision: ""
next_iteration: ""
law_candidate_review:
  decision: no | watch | promote
  reason: ""
confidence: low | medium | high
```

---

## Confidence Levels

### Low

Use when the signal is interesting but weak or isolated.

### Medium

Use when the signal is clear but not yet repeated enough.

### High

Use when the pattern repeats and supports a decision.

High confidence is still not automatically a law.

---

## Learning Decisions

Allowed decisions:

```text
continue
stop
change
repeat
compare
promote_to_law_candidate
archive
```

---

## What Not To Do

Do not say:

```text
This worked once, therefore it is a law.
```

Do not say:

```text
Views were high, therefore the meaning worked.
```

Do not say:

```text
The result was weak, therefore the idea is false.
```

---

## Test Plan

Purpose:

```text
Check whether an experiment can become a structured learning object.
```

Input:

```text
One scored experiment and qualitative notes.
```

Expected output:

```text
One learning object with decision, confidence and next iteration.
```

Manual test:

```text
Use a sample experiment and fill the learning object structure.
```

Acceptance criteria:

```text
The learning explains what happened and what to do next without overclaiming.
```

Evidence:

```text
A sample learning file.
```

Future automation:

```text
n8n drafts learning objects from weekly report data.
```
