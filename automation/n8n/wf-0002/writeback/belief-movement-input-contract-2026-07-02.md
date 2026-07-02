# WF-0002 Belief Movement Input Contract Evidence

Date: 2026-07-02

Purpose:

```text
Prove that WF-0002 has a repository-level input contract before any generator, issue creation or YAML writeback automation is built.
```

---

## Files

```text
schemas/wf-0002-belief-movement-input.schema.yaml
logos_engine/wf_0002_belief_movement.py
scripts/validate_wf_0002_belief_movement_input.py
testing/fixtures/wf-0002-belief-movement-input.json.example
```

---

## Valid Fixture Test

Command:

```text
python scripts\validate_wf_0002_belief_movement_input.py --input testing\fixtures\wf-0002-belief-movement-input.json.example
```

Result:

```text
WF-0002 belief movement input schema passed.
writeback_performed: false
creates_belief_shift_issue: false
creates_yaml_object: false
```

---

## Rejection Coverage

Unit tests cover:

```text
HT-0000 placeholder source_human_truth_id is rejected
unexpected generation output fields are rejected
```

---

## Boundary

```text
No Belief Shift issue was created.
No Meaning Atom draft issue was created.
No YAML object was written.
No n8n workflow was created for WF-0002 in this step.
No learning or law artifact was created.
```

Future WF-0002 n8n implementation must use this contract before drafting or writing any downstream artifact.

