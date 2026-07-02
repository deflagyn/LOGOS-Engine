# PILOT-0001 Validator Dispatch Gate Bounded Polling Test

Date: 2026-07-02

Purpose:

```text
Prove that the n8n validator dispatch gate can perform bounded multi-attempt GitHub Actions status lookup after dispatch.
```

---

## Workflow

```text
name: LOGOS PILOT-0001 Validator Dispatch Gate
id: oWQbN9u1VI4AS6rq
active_after_test: false
node_count: 11
```

Nodes:

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

## Polling Mode

```text
bounded_3_attempts_15s_interval
```

Behavior:

```text
1. Dispatch validate-catalog.yml on main.
2. Wait 15 seconds.
3. Lookup recent workflow_dispatch runs.
4. Wait 15 seconds.
5. Lookup again.
6. Wait 15 seconds.
7. Lookup a third time.
8. Return the first completed matching run if found.
9. If no completed run is found, return the latest matching run and block downstream trust.
```

---

## Implementation Fix

The first bounded polling test failed before lookup because PowerShell interpolated JavaScript `$()` syntax while generating wait node code.

Failed execution:

```text
execution_id: 1085
failed_node: 04 Wait Before Lookup 1
error: Unexpected identifier 'Validate'
cause: generated JS became `const request = 02 Validate Dispatch Request.first().json`
```

Fix:

```text
Updated wait nodes using literal JavaScript so `$('02 Validate Dispatch Request')` is preserved.
```

Final workflow state after the failed attempt:

```text
active: false
```

---

## Successful Controlled Test

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
validator_run_id: 28609662029
validator_run_url: https://github.com/deflagyn/LOGOS-Engine/actions/runs/28609662029
validator_run_status: completed
validator_run_conclusion: success
polling_mode: bounded_3_attempts_15s_interval
selected_attempt: 2
attempts_count: 2
final_active: false
deactivation_error: null
```

Interpretation:

```text
The validator completed by the second lookup attempt.
The gate returned a final success result directly in the n8n webhook response.
```

---

## Safety

```text
Only LOGOS PILOT-0001 Validator Dispatch Gate was briefly activated.
The workflow was deactivated immediately after each controlled POST.
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

The gate now has bounded polling, but it still does not branch early in the n8n graph.

The current implementation always runs the configured lookup chain, then the response builder selects the first completed matching run.

Future improvement:

```text
Add conditional branching to stop lookup attempts early after completion, if the graph remains readable.
```

