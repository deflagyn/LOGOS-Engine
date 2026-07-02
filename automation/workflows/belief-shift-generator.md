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

Current repository input contract:

```text
schemas/wf-0002-belief-movement-input.schema.yaml
testing/fixtures/wf-0002-belief-movement-input.json.example
scripts/validate_wf_0002_belief_movement_input.py
scripts/wf_0002_status.py
```

Evidence:

```text
automation/n8n/wf-0002/BELIEF-MOVEMENT-INPUT-CONTRACT.md
automation/n8n/wf-0002/BELIEF-MOVEMENT-INPUT-PREVIEW-GATE.md
automation/n8n/wf-0002/writeback/belief-movement-input-contract-2026-07-02.md
automation/n8n/wf-0002/writeback/belief-movement-input-preview-gate-test-2026-07-02.md
automation/n8n/wf-0002/writeback/belief-movement-status-readiness-2026-07-02.md
```

Current boundary:

```text
This contract validates input only.
It does not create a Belief Shift issue.
It does not create YAML objects.
HT-0000 placeholder Human Truth IDs are rejected.
The current fixture traces to a local reviewed-stable HT-0100 fixture, not to live issue #29.
```

Current n8n preview gate:

```text
name: LOGOS WF-0002 Belief Movement Input Preview Gate
id: Rue7sAU14UMv1hTr
active: false
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
