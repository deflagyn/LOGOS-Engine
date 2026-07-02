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
Dispatch the GitHub Action workflow validate-catalog.yml for deflagyn/LOGOS-Engine on main and perform a status lookup before responding.
```

This workflow does not write pilot artifacts.

It is a gate between n8n writeback and downstream trust.

---

## Nodes

```text
01 Controlled Validator Dispatch Webhook
02 Validate Dispatch Request
03 Dispatch Validate LOGOS Catalog
04 Wait Before Lookup 1
05 Lookup Validator Runs 1
06 Wait Before Lookup 2
07 Lookup Validator Runs 2
08 Wait Before Lookup 3
09 Lookup Validator Runs 3
10 Build Validator Status Response
11 Respond Validator Status JSON
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
controlled_dispatch_tested: true
status_lookup_tested: true
bounded_polling_tested: true
```

Creation evidence:

```text
automation/n8n/pilot-0001/writeback/validator-dispatch-gate-created-2026-07-02.md
```

Controlled test evidence:

```text
automation/n8n/pilot-0001/writeback/validator-dispatch-gate-test-2026-07-02.md
```

Polling test evidence:

```text
automation/n8n/pilot-0001/writeback/validator-dispatch-gate-polling-test-2026-07-02.md
```

Bounded polling test evidence:

```text
automation/n8n/pilot-0001/writeback/validator-dispatch-gate-bounded-polling-test-2026-07-02.md
```

---

## Operation Protocol

For a controlled test:

```text
1. Confirm no other LOGOS writeback workflow is running.
2. Activate only this workflow if webhook execution is required.
3. POST the required confirmation payload.
4. Wait for the gate response with validator_run_status and validator_run_conclusion.
5. Deactivate the workflow immediately after the controlled test.
6. Record run URL and result in issue #27.
```

Do not use this gate to bypass local or repository validation.

Do not enable learning or law review from this gate.

---

## Known Limit

This workflow performs bounded GitHub Actions lookup after dispatch.

Current polling mode:

```text
bounded_3_attempts_15s_interval
```

If the validator run completes within the lookup window, the response includes:

```text
validator_status: success | failure | cancelled | skipped
validator_run_url
validator_run_conclusion
```

If the validator run is still running after all attempts, the response may still be:

```text
validator_status: in_progress
```

Future improvement:

```text
Add conditional branching to stop lookup attempts early after completion, if the graph remains readable.
```
