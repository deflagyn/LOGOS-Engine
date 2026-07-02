# PILOT-0001 Validator Dispatch Gate Polling Test

Date: 2026-07-02

Purpose:

```text
Prove that the n8n validator dispatch gate can dispatch validate-catalog.yml and return a GitHub Action status/conclusion in its own webhook response.
```

---

## Workflow

```text
name: LOGOS PILOT-0001 Validator Dispatch Gate
id: oWQbN9u1VI4AS6rq
active_after_test: false
node_count: 7
```

Nodes:

```text
01 Controlled Validator Dispatch Webhook
02 Validate Dispatch Request
03 Dispatch Validate LOGOS Catalog
04 Wait For Validator Run
05 Lookup Validator Runs
06 Build Validator Status Response
07 Respond Validator Status JSON
```

---

## Implementation Change

The gate was upgraded from dispatch-only response to:

```text
dispatch -> wait -> GitHub Actions run lookup -> status response
```

Polling mode:

```text
single_lookup_after_45s
```

The response now includes:

```text
validator_status
validator_run_id
validator_run_url
validator_run_status
validator_run_conclusion
polling_mode
```

---

## First Lookup Attempt

A first controlled test used:

```text
single_lookup_after_25s
```

n8n response:

```text
validator_run_id: 28595786635
validator_run_status: in_progress
validator_run_conclusion: null
validator_status: in_progress
```

External GitHub verification later showed:

```text
run_id: 28595786635
result: success
```

Decision:

```text
Increase wait time to 45 seconds for the MVP gate.
```

---

## Successful Polling Test

Request:

```json
{
  "confirm_dispatch": "VALIDATE_LOGOS_CATALOG",
  "ref": "main"
}
```

n8n response:

```text
status: validator_result_observed
validator_status: success
validator_run_id: 28595880528
validator_run_url: https://github.com/deflagyn/LOGOS-Engine/actions/runs/28595880528
validator_run_status: completed
validator_run_conclusion: success
polling_mode: single_lookup_after_45s
final_active: false
deactivation_error: null
```

Interpretation:

```text
The n8n gate can now return validator success/failure state when the GitHub Action completes within the lookup window.
```

---

## Safety

```text
Only LOGOS PILOT-0001 Validator Dispatch Gate was briefly activated.
The workflow was deactivated immediately after the controlled POST.
Final workflow state is active=false.
No PILOT-0001 writeback workflow was activated.
No System Run workflow was activated.
No pilot artifact was written.
No learning artifact was created.
No law review artifact was created.
No VPS reboot was performed.
No Docker, n8n, nginx, Postgres or service restart was performed.
No secret value was committed or pasted into issue comments.
```

---

## Remaining Limit

This is not yet a multi-attempt polling loop.

If GitHub Actions takes longer than the 45-second lookup window, the gate returns:

```text
validator_status: in_progress
```

Future improvement:

```text
Replace single lookup with bounded polling until completed, timeout or failure.
```

