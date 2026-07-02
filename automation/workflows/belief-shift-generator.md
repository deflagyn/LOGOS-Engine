# WF-0002 — Belief Movement Generator

## Purpose

Create a structured before to after meaning movement from a Human Truth.

---

## Input

```text
Human Truth ID
Audience context
Scope
```

---

## Output

```text
Belief Shift issue
Meaning Atom draft
Emotional result draft
```

---

## n8n Draft Nodes

```text
Trigger
Fetch source object
Draft before frame
Draft after frame
Draft meaning atom
Create GitHub issue
Return issue URL
```

---

## Manual Dry Run

1. Select one Human Truth.
2. Write before frame.
3. Write after frame.
4. Draft one Meaning Atom.
5. Create one issue.
6. Check clarity.

---

## Acceptance Criteria

```text
Given a Human Truth,
When the process runs,
Then one structured issue exists with before, after, meaning atom and test plan.
```

---

## Test Plan

Purpose:

```text
Check whether a Human Truth can become a usable meaning movement.
```

Input:

```text
One Human Truth candidate.
```

Expected output:

```text
One structured issue.
```

Evidence:

```text
A test issue or dry-run file.
```

Future automation:

```text
n8n drafts the issue and waits for human review.
```
