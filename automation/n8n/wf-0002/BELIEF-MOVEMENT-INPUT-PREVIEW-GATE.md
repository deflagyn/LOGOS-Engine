# WF-0002 Belief Movement Input Preview Gate

This document records the first n8n workflow for WF-0002.

GitHub remains the source of truth.

This workflow validates and previews Belief Movement input only.

It does not generate a Belief Shift issue.

It does not write YAML.

---

## Workflow

```text
name: LOGOS WF-0002 Belief Movement Input Preview Gate
id: Rue7sAU14UMv1hTr
active: false
```

Purpose:

```text
Validate a reviewed stable Human Truth input before any future Belief Movement generator or writeback node runs.
```

This workflow does not create GitHub issues.

It does not create Belief Shift YAML.

It does not create Meaning Atom YAML.

It does not create learning or law artifacts.

---

## Nodes

```text
01 Controlled Belief Movement Input Webhook
02 Validate Belief Movement Input
03 Respond Belief Movement Preview JSON
```

---

## Safety Contract

The request must satisfy:

```text
schemas/wf-0002-belief-movement-input.schema.yaml
```

Required fields:

```text
confirm_movement_input
source_human_truth_id
source_human_truth
audience_context
language
scope
```

Hard boundary:

```text
source_human_truth_id must be a stable HT-#### ID.
HT-0000 placeholders are rejected.
```

---

## Current State

```text
created: true
active: false
valid_preview_tested: true
placeholder_rejection_tested: true
writeback_performed: false
belief_shift_issue_created: false
yaml_object_created: false
```

Test evidence:

```text
automation/n8n/wf-0002/writeback/belief-movement-input-preview-gate-test-2026-07-02.md
```

---

## Operation Protocol

For a controlled preview:

```text
1. Activate only this workflow if webhook execution is required.
2. POST a payload that satisfies the WF-0002 input contract.
3. Verify status=belief_movement_input_preview_valid.
4. Verify writeback_performed=false.
5. Verify creates_belief_shift_issue=false.
6. Verify creates_yaml_object=false.
7. Deactivate the workflow immediately after the controlled preview.
```

Do not use this gate to create Belief Shift issues.

Do not use this gate to create YAML objects.

Do not use this gate to create learning or law candidates.

