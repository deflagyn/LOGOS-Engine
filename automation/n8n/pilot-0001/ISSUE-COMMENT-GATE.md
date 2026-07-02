# PILOT-0001 Issue Comment Gate

This document records the dedicated n8n workflow that posts controlled evidence comments to GitHub issue #27.

---

## Workflow

```text
name: LOGOS PILOT-0001 Issue Comment Gate
id: UwkfEOmygkX4BBe5
active: false
```

Purpose:

```text
Post a controlled evidence summary to issue #27 after validator or runtime checks.
```

This workflow does not write pilot artifacts.

It is an issue-comment layer only.

---

## Nodes

```text
01 Controlled Issue Comment Webhook
02 Validate And Build Comment
03 POST Issue Comment
04 Build Comment Response
05 Respond Issue Comment JSON
```

---

## Safety Contract

The request must include:

```json
{
  "confirm_comment": "COMMENT_PILOT_0001_ISSUE_27",
  "issue_number": 27,
  "comment_kind": "controlled_test"
}
```

Allowed comment kinds:

```text
controlled_test
validator_result
```

For `validator_result`, the payload should include:

```text
validator_status
validator_run_id
validator_run_url
validator_run_status
validator_run_conclusion
polling_mode
selected_attempt
```

Hard-coded limits:

```text
repo: deflagyn/LOGOS-Engine
issue_number: 27
```

The workflow rejects:

```text
missing confirmation
issue number other than 27
unsupported comment kind
validator run URL outside deflagyn/LOGOS-Engine Actions runs
```

---

## GitHub API Call

Endpoint:

```text
POST /repos/deflagyn/LOGOS-Engine/issues/27/comments
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
controlled_comment_tested: true
validator_result_tested: true
```

Creation and test evidence:

```text
automation/n8n/pilot-0001/writeback/issue-comment-gate-test-2026-07-02.md
automation/n8n/pilot-0001/writeback/issue-comment-gate-validator-result-test-2026-07-02.md
```

---

## Operation Protocol

For a controlled comment:

```text
1. Confirm no broader LOGOS workflow is running.
2. Activate only this workflow if webhook execution is required.
3. POST the required confirmation payload.
4. Verify the GitHub issue comment URL.
5. Deactivate the workflow immediately after the controlled test.
6. Record comment URL and result in repository evidence.
```

Do not use this gate to create learning or law review.

Do not use this gate to write pilot artifacts.
