# WF-0001 Idea Intake Issue Gate

This document records the first implemented n8n workflow for the universal LOGOS automation layer.

GitHub remains the source of truth.

n8n creates the issue, but the issue is the durable artifact.

---

## Workflow

```text
name: LOGOS WF-0001 Idea Intake Issue Gate
id: s00B4QAhJ3MYZ1tq
active: false
```

Purpose:

```text
Turn a controlled raw idea payload into a structured GitHub Human Truth candidate issue.
```

This workflow does not write YAML objects.

It does not create learning or law artifacts.

It does not rewrite raw meaning into a validated LOGOS object.

---

## Nodes

```text
01 Controlled Idea Intake Webhook
02 Validate And Build Human Truth Issue
03 POST GitHub Issue
04 Build Issue Response
05 Respond Idea Intake JSON
```

---

## Safety Contract

The request must include:

```json
{
  "confirm_intake": "CREATE_WF_0001_HUMAN_TRUTH_ISSUE",
  "raw_idea": "",
  "source": "",
  "language": "",
  "scope": "universal",
  "human_truth_candidate": "",
  "test_plan": ""
}
```

Allowed scope values:

```text
universal
runtime
```

Optional fields:

```text
optional_context
meaning_resources
connected_objects
title_suffix
```

The workflow requires `human_truth_candidate` as input.

It does not use an LLM node yet.

This keeps the first implementation focused on intake discipline and GitHub issue creation.

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
missing_confirm_rejection_tested: true
```

Created issue:

```text
https://github.com/deflagyn/LOGOS-Engine/issues/29
```

Test evidence:

```text
automation/n8n/wf-0001/writeback/idea-intake-issue-gate-test-2026-07-02.md
```

---

## Operation Protocol

For a controlled intake:

```text
1. Activate only this workflow if webhook execution is required.
2. POST the required confirmation payload and structured idea fields.
3. Verify status=idea_intake_issue_created.
4. Verify issue_url points to deflagyn/LOGOS-Engine.
5. Deactivate the workflow immediately after the controlled run.
6. Review the created issue before promoting any object file.
```

Do not use this gate to create YAML objects.

Do not use this gate to create learning or law candidates.

Do not add Telegram/form intake until this controlled webhook path remains stable.

