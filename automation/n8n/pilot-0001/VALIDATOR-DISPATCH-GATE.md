# PILOT-0001 Validator Dispatch Gate

This document records the dedicated n8n workflow that dispatches the repository validator after controlled writeback steps.

---

## Workflow

```text
name: LOGOS PILOT-0001 Validator Dispatch Gate
id: oWQbN9u1VI4AS6rq
active: false
```

Purpose:

```text
Dispatch the GitHub Action workflow validate-catalog.yml for deflagyn/LOGOS-Engine on main.
```

This workflow does not write pilot artifacts.

It is a gate between n8n writeback and downstream trust.

---

## Nodes

```text
01 Controlled Validator Dispatch Webhook
02 Validate Dispatch Request
03 Dispatch Validate LOGOS Catalog
04 Build Dispatch Response
05 Respond Validator Dispatch JSON
```

---

## Safety Contract

The dispatch request must include:

```json
{
  "confirm_dispatch": "VALIDATE_LOGOS_CATALOG",
  "ref": "main"
}
```

Hard-coded limits:

```text
repo: deflagyn/LOGOS-Engine
workflow: validate-catalog.yml
ref: main
```

The workflow rejects:

```text
missing confirmation
repo override
workflow override
non-main ref
```

---

## GitHub API Call

Endpoint:

```text
POST /repos/deflagyn/LOGOS-Engine/actions/workflows/validate-catalog.yml/dispatches
```

Body:

```json
{
  "ref": "main"
}
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
executed_by_codex: false
```

Creation evidence:

```text
automation/n8n/pilot-0001/writeback/validator-dispatch-gate-created-2026-07-02.md
```

---

## Operation Protocol

For a controlled test:

```text
1. Confirm no other LOGOS writeback workflow is running.
2. Activate only this workflow if webhook execution is required.
3. POST the required confirmation payload.
4. Verify GitHub Action run creation.
5. Deactivate the workflow immediately after the controlled test.
6. Record run URL and result in issue #27.
```

Do not use this gate to bypass local or repository validation.

Do not enable learning or law review from this gate.

---

## Known Limit

This workflow dispatches the validator but does not yet poll the GitHub Action result.

Until polling is implemented, the response should be treated as:

```text
validator_status: dispatched
```

The final pass/fail result must still be read from GitHub Actions.

