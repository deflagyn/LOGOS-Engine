# LOGOS Evidence Criteria

This document defines what evidence is required before a pattern can become a Law Candidate or LOGOS Law.

The purpose is to protect LOGOS from turning attractive ideas into rules too early.

---

## Core Rule

No LOGOS Law without repeated evidence.

A beautiful idea is not enough.

A strong result once is not enough.

---

## Maturity Path

```text
Idea
→ Hypothesis
→ Experiment
→ Learning
→ Repeated Signal
→ Law Candidate
→ LOGOS Law
```

---

## Evidence Types

### Quantitative Evidence

Examples:

```text
completion rate
average watch time
saves
shares
comments
profile clicks
follows
repeat performance
```

### Qualitative Evidence

Examples:

```text
phrase repetition
recognition comments
new questions
people tagging others
objections that reveal a boundary
people applying the idea to themselves
```

### Operational Evidence

Examples:

```text
the pattern improves future scripts
the pattern helps choose between variants
the pattern predicts a stronger direction
the pattern prevents repeated mistakes
```

---

## Law Candidate Requirements

A pattern may become a Law Candidate when:

```text
1. it appears in more than one experiment;
2. it has at least one measurable signal;
3. it has at least one qualitative signal;
4. it has a clear boundary condition;
5. it can guide a future decision.
```

---

## LOGOS Law Requirements

A Law Candidate may become a LOGOS Law when:

```text
1. it repeats across contexts or formats;
2. it remains useful after review;
3. it has documented supporting experiments;
4. it has clear conditions of use;
5. it improves future generation or evaluation.
```

---

## Boundary Conditions

Every Law Candidate must say:

```text
applies_when:
does_not_apply_when:
evidence:
risks:
next_review:
```

---

## Rejection Conditions

A candidate should not become a law when:

```text
evidence is isolated
evidence is unclear
the result cannot be repeated
the pattern only works in one narrow case
the rule would encourage unsafe or manipulative behavior
```

---

## Test Plan

Purpose:

```text
Check whether evidence criteria prevent premature law promotion.
```

Input:

```text
One sample learning object.
```

Expected output:

```text
Decision: no promotion, watch, Law Candidate or Law.
```

Manual test:

```text
Apply these criteria to a sample learning object.
```

Acceptance criteria:

```text
The decision is explainable and does not overclaim.
```

Evidence:

```text
A sample law review file.
```

Future automation:

```text
n8n can flag possible Law Candidates, but human review decides promotion.
```
