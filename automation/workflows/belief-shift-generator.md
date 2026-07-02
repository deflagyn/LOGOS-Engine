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
testing/fixtures/wf-0002-belief-shift-issue.md
scripts/validate_wf_0002_belief_shift_issue.py
scripts/wf_0002_status.py
```

Evidence:

```text
automation/n8n/wf-0002/BELIEF-MOVEMENT-INPUT-CONTRACT.md
automation/n8n/wf-0002/BELIEF-MOVEMENT-INPUT-PREVIEW-GATE.md
automation/n8n/wf-0002/BELIEF-MOVEMENT-GENERATION-PREFLIGHT-CONTRACT.md
automation/n8n/wf-0002/BELIEF-MOVEMENT-GENERATION-PREFLIGHT-GATE.md
automation/n8n/wf-0002/BELIEF-MOVEMENT-ISSUE-CREATION-GATE.md
automation/n8n/wf-0002/writeback/belief-movement-input-contract-2026-07-02.md
automation/n8n/wf-0002/writeback/belief-movement-input-preview-gate-test-2026-07-02.md
automation/n8n/wf-0002/writeback/belief-movement-status-readiness-2026-07-02.md
automation/n8n/wf-0002/writeback/belief-movement-generation-preflight-contract-2026-07-02.md
automation/n8n/wf-0002/writeback/belief-movement-generation-preflight-gate-test-2026-07-02.md
automation/n8n/wf-0002/writeback/belief-movement-issue-creation-gate-test-2026-07-02.md
testing/fixtures/wf-0002-issue-30.md
```

Current boundary:

```text
This contract validates input only.
It does not create a Belief Shift issue.
It does not create YAML objects.
HT-0000 placeholder Human Truth IDs are rejected.
The current fixture traces to a local reviewed-stable HT-0100 fixture, not to live issue #29.
The generation preflight contract validates a review-facing Belief Shift issue body before any future n8n GitHub issue creation node.
The n8n generation preflight gate is implemented and inactive.
The n8n issue creation gate created issue #30 and is inactive.
Issue #30 remains a review-facing BS-0000 candidate, not a YAML object.
```

Current n8n preview gate:

```text
name: LOGOS WF-0002 Belief Movement Input Preview Gate
id: Rue7sAU14UMv1hTr
active: false
```

Current n8n generation preflight gate:

```text
name: LOGOS WF-0002 Belief Movement Generation Preflight Gate
id: uBrha0GALDy3HfSC
active: false
```

Current n8n issue creation gate:

```text
name: LOGOS WF-0002 Belief Movement Issue Creation Gate
id: wjiTK4Ov1nY1EndY
active: false
created_issue: https://github.com/deflagyn/LOGOS-Engine/issues/30
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
