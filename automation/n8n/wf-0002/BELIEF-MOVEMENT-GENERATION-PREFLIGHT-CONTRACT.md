# WF-0002 Belief Movement Generation Preflight Contract

This document records the repository-level contract for the future WF-0002 n8n generation preflight gate.

GitHub remains the source of truth.

n8n may create a Belief Shift issue only after this issue body contract passes.

It must not write YAML objects from this step.

---

## Contract

```text
validator: scripts/validate_wf_0002_belief_shift_issue.py
fixture: testing/fixtures/wf-0002-belief-shift-issue.md
status: scripts/wf_0002_status.py
```

Purpose:

```text
Validate the review-facing Belief Shift issue body before any GitHub issue creation node runs.
```

---

## Required Issue Sections

```text
LOGOS ID
Status
Scope
Source Human Truth ID
Source Human Truth
Audience context
Before frame
After frame
Belief Shift candidate
Meaning Atom draft
Emotional result draft
Test plan
Generation evidence
```

Hard boundary:

```text
Source Human Truth ID must be a stable HT-#### ID.
HT-0000 placeholders are rejected.
The Belief Shift issue may use BS-0000 while it is still a review candidate.
YAML promotion must be a separate future gate.
```

---

## Current State

```text
issue_body_validator_created: true
issue_fixture_created: true
unit_tests_created: true
n8n_generation_gate_created: false
github_issue_created: false
yaml_object_created: false
learning_created: false
law_created: false
```

Evidence:

```text
automation/n8n/wf-0002/writeback/belief-movement-generation-preflight-contract-2026-07-02.md
```

---

## Operation Protocol

For controlled local validation:

```text
python scripts\validate_wf_0002_belief_shift_issue.py --input testing\fixtures\wf-0002-belief-shift-issue.md --title "BS-0000: Preserve before interpreting"
```

Expected:

```text
WF-0002 Belief Shift issue body passed review-readiness validation.
writeback_performed: false
yaml_object_created: false
```

Do not use this contract to create Belief Shift YAML.

Do not use this contract to create Meaning Atom YAML.

Do not use this contract to create learning or law candidates.

Future n8n gate:

```text
1. Receive a validated WF-0002 input payload.
2. Build a Belief Shift issue body.
3. Validate the issue body with this contract.
4. Create a GitHub issue only if validation passes.
5. Return the issue URL and keep YAML writeback false.
```
