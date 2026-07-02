# WF-0004 — Review Checker

## Purpose

Review draft outputs before runtime use.

---

## Input

```text
Draft output
Runtime profile
Review rules
Platform context
```

---

## Output

```text
Review result
Notes
Decision: pass / revise / reject
```

---

## n8n Draft Nodes

```text
Trigger
Fetch draft
Fetch review rules
Check draft
Write GitHub comment
Set review status
```

---

## Manual Dry Run

1. Select one draft output.
2. Compare it with review rules.
3. Mark lines that need revision.
4. Record pass, revise or reject.
5. Store result as an issue comment.

---

## Acceptance Criteria

```text
Given a draft output,
When the review runs,
Then a clear decision and notes are recorded.
```

---

## Test Plan

Purpose:

```text
Check whether draft outputs can be reviewed before publication.
```

Input:

```text
One draft output and one rules file.
```

Expected output:

```text
One review result.
```

Evidence:

```text
A test issue comment or dry-run file.
```

Future automation:

```text
n8n performs first review and sends uncertain cases to human review.
```
