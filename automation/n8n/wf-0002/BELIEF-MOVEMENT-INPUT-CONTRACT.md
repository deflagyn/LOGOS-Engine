# WF-0002 Belief Movement Input Contract

This document records the repository-level input contract for future WF-0002 Belief Movement Generator automation.

GitHub remains the source of truth.

n8n must not generate Belief Shift issues or YAML objects from unreviewed placeholder Human Truth inputs.

---

## Contract

```text
schema: schemas/wf-0002-belief-movement-input.schema.yaml
validator: scripts/validate_wf_0002_belief_movement_input.py
fixture: testing/fixtures/wf-0002-belief-movement-input.json.example
```

Purpose:

```text
Validate the source Human Truth and audience context before any Belief Movement generator or writeback node runs.
```

---

## Required Input

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
schema_created: true
fixture_created: true
cli_validator_created: true
unit_tests_created: true
writeback_performed: false
belief_shift_issue_created: false
yaml_object_created: false
```

Evidence:

```text
automation/n8n/wf-0002/writeback/belief-movement-input-contract-2026-07-02.md
```

---

## Operation Protocol

For a controlled local validation:

```text
python scripts\validate_wf_0002_belief_movement_input.py --input testing\fixtures\wf-0002-belief-movement-input.json.example
```

Expected:

```text
WF-0002 belief movement input schema passed.
writeback_performed: false
creates_belief_shift_issue: false
creates_yaml_object: false
```

Do not use this contract to create Belief Shift YAML.

Do not use this contract to create Meaning Atom YAML.

Do not use this contract to create learning or law candidates.

