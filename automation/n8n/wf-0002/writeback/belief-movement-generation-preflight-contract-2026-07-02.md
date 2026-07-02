# WF-0002 Belief Movement Generation Preflight Contract Evidence

Date: 2026-07-02

Purpose:

```text
Prove that WF-0002 has a review-facing Belief Shift issue body contract before any n8n GitHub issue creation or YAML writeback gate is built.
```

---

## Files

```text
logos_engine/wf_0002_belief_movement.py
scripts/validate_wf_0002_belief_shift_issue.py
testing/fixtures/wf-0002-belief-shift-issue.md
automation/n8n/wf-0002/BELIEF-MOVEMENT-GENERATION-PREFLIGHT-CONTRACT.md
```

---

## Valid Fixture Test

Command:

```text
python scripts\validate_wf_0002_belief_shift_issue.py --input testing\fixtures\wf-0002-belief-shift-issue.md --title "BS-0000: Preserve before interpreting"
```

Result:

```text
WF-0002 Belief Shift issue body passed review-readiness validation.
logos_id: BS-0000
source_human_truth_id: HT-0100
status: candidate
scope: universal
writeback_performed: false
yaml_object_created: false
```

---

## Rejection Coverage

Unit tests cover:

```text
HT-0000 placeholder Source Human Truth ID is rejected
missing no-YAML evidence is rejected
```

---

## Boundary

```text
No GitHub issue was created.
No Belief Shift YAML object was written.
No Meaning Atom YAML object was written.
No learning or law artifact was created.
No n8n generation gate was created in this step.
No VPS reboot was performed.
No Docker, n8n, nginx, Postgres or service restart was performed.
```

Future WF-0002 n8n implementation must use this contract before creating a review-facing Belief Shift issue.
