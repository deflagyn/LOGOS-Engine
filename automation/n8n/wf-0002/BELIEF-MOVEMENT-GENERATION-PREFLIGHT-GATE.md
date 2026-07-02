# WF-0002 Belief Movement Generation Preflight Gate

This document records the n8n preflight-only workflow for future WF-0002 Belief Shift issue creation.

GitHub remains the source of truth.

This workflow validates a review-facing Belief Shift issue body.

It does not create a GitHub issue.

It does not write YAML.

---

## Workflow

```text
name: LOGOS WF-0002 Belief Movement Generation Preflight Gate
id: uBrha0GALDy3HfSC
active: false
```

Purpose:

```text
Block premature Belief Shift issue creation unless the generated issue body satisfies the WF-0002 review-readiness contract.
```

This workflow does not create GitHub issues.

It does not create Belief Shift YAML.

It does not create Meaning Atom YAML.

It does not create learning or law artifacts.

---

## Nodes

```text
01 Controlled Generation Preflight Webhook
02 Validate Belief Shift Issue Body
03 Respond Generation Preflight JSON
```

---

## Safety Contract

The request must include:

```json
{
  "confirm_generation_preflight": "PREFLIGHT_WF_0002_BELIEF_SHIFT_ISSUE",
  "title": "",
  "issue_body": ""
}
```

The issue body must satisfy the local review-readiness contract:

```text
scripts/validate_wf_0002_belief_shift_issue.py
```

Review-readiness requires:

```text
Belief Shift issue body contains all required sections
LOGOS ID is BS-0000 or stable BS-####
Source Human Truth ID is stable HT-####
Source Human Truth ID is not HT-0000
scope is universal or runtime
generation evidence states no YAML writeback
generation evidence states no learning or law artifact
```

---

## Current State

```text
created: true
active: false
valid_preflight_tested: true
placeholder_source_rejection_tested: true
writeback_performed: false
github_issue_created: false
yaml_object_created: false
```

Test evidence:

```text
automation/n8n/wf-0002/writeback/belief-movement-generation-preflight-gate-test-2026-07-02.md
```

---

## Operation Protocol

For a controlled preflight:

```text
1. Activate only this workflow if webhook execution is required.
2. POST the required confirmation payload, title and issue body.
3. Verify status=belief_shift_generation_preflight_passed.
4. Verify creates_github_issue=false.
5. Verify creates_yaml_object=false.
6. Deactivate the workflow immediately after the controlled preflight.
7. Do not create or promote any object from this preflight output alone.
```

Do not use this gate to create GitHub issues.

Do not use this gate to create YAML objects.

Do not use this gate to create learning or law candidates.
