# WF-0002 Belief Movement Issue Creation Gate

This document records the n8n workflow that creates a review-facing Belief Shift GitHub issue.

GitHub remains the source of truth.

n8n creates the issue, but the issue is the durable artifact.

It does not write YAML.

---

## Workflow

```text
name: LOGOS WF-0002 Belief Movement Issue Creation Gate
id: wjiTK4Ov1nY1EndY
active: false
```

Purpose:

```text
Create a structured Belief Shift candidate issue only after the issue body satisfies the WF-0002 generation preflight contract.
```

This workflow does not create or update YAML objects.

It does not create Meaning Atom YAML.

It does not create learning or law artifacts.

---

## Nodes

```text
01 Controlled Issue Creation Webhook
02 Validate And Build Belief Shift Issue
03 POST GitHub Issue
04 Build Issue Response
05 Respond Issue Creation JSON
```

---

## Safety Contract

The request must include:

```json
{
  "confirm_issue_creation": "CREATE_WF_0002_BELIEF_SHIFT_ISSUE",
  "title": "",
  "issue_body": ""
}
```

The issue body must satisfy:

```text
scripts/validate_wf_0002_belief_shift_issue.py
```

The workflow requires:

```text
title starts with BS-
LOGOS ID is BS-0000 or stable BS-####
Source Human Truth ID is stable HT-####
Source Human Truth ID is not HT-0000
Generation evidence states no YAML writeback
Generation evidence states no learning or law artifact
```

---

## GitHub API Call

Endpoint:

```text
POST /repos/deflagyn/LOGOS-Engine/issues
```

Auth:

```text
n8n GitHub credential
```

Do not hardcode a token in workflow JSON.

---

## Current State

```text
created: true
active: false
controlled_issue_creation_tested: true
placeholder_source_rejection_tested: true
writeback_performed: false
yaml_object_created: false
meaning_atom_created: false
```

Created issue:

```text
https://github.com/deflagyn/LOGOS-Engine/issues/30
```

Test evidence:

```text
automation/n8n/wf-0002/writeback/belief-movement-issue-creation-gate-test-2026-07-02.md
testing/fixtures/wf-0002-issue-30.md
```

---

## Operation Protocol

For a controlled issue creation:

```text
1. Activate only this workflow if webhook execution is required.
2. POST the required confirmation payload, title and issue body.
3. Verify status=belief_shift_issue_created.
4. Verify issue_url points to deflagyn/LOGOS-Engine.
5. Verify writes_yaml=false.
6. Deactivate the workflow immediately after the controlled run.
7. Review the created issue before promoting any YAML object.
```

Do not use this gate to create YAML objects.

Do not use this gate to create Meaning Atom YAML.

Do not use this gate to create learning or law candidates.
