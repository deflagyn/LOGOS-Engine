# WF-0003 — Script Generator

## Purpose

Turn approved LOGOS objects into a platform-specific draft script.

The script is not the source of truth.

It is a runtime expression of the LOGOS chain.

---

## Input

```text
Belief Shift ID
Meaning Atom ID
Story Pattern ID
Language
Platform
Runtime constraints
```

---

## Output

```text
Script draft
Linked objects
Test plan
Safety notes
```

Primary GitHub output:

```text
New GitHub Issue using the Script template
```

Later output:

```text
Script markdown file after approval
```

---

## n8n Draft Nodes

```text
Trigger
Fetch linked objects
Fetch runtime profile
Generate draft
Check structure
Create GitHub issue
Return issue URL
```

---

## Manual Dry Run

1. Select one Belief Shift and one Meaning Atom.
2. Select one format.
3. Draft a short script manually.
4. Check whether it traces back to the linked objects.
5. Create a Script issue.

---

## Acceptance Criteria

```text
Given approved LOGOS objects,
When the process runs,
Then a script issue exists with draft text, linked objects and test plan.
```

---

## Test Plan

Purpose:

```text
Check whether structured LOGOS objects can produce a draft script without losing traceability.
```

Input:

```text
Belief Shift, Meaning Atom and Story Pattern.
```

Expected output:

```text
One draft script issue.
```

Evidence:

```text
A test issue or dry-run file.
```

Future automation:

```text
n8n drafts the script and routes it through a review step.
```
