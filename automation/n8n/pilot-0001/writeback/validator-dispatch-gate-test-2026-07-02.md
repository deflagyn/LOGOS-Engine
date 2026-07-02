# PILOT-0001 Validator Dispatch Gate Controlled Test

Date: 2026-07-02

Purpose:

```text
Prove that the n8n validator dispatch gate can activate, dispatch the GitHub validator, and return to inactive state.
```

---

## Workflow

```text
name: LOGOS PILOT-0001 Validator Dispatch Gate
id: oWQbN9u1VI4AS6rq
```

---

## Pre-Test State

```text
active: false
node_count: 5
```

The workflow had a connection-shape issue from initial API creation:

```text
incorrect: main: [{...}]
correct:   main: [[{...}]]
```

Initial activation attempts failed before webhook execution with:

```text
object is not iterable (cannot read property Symbol(Symbol.iterator))
```

Fix:

```text
Updated workflow through n8n API PUT with canonical nested connection arrays.
```

No webhook was executed before the connection fix.

---

## Activation Smoke Test

Result:

```text
activation_smoke: success
active_after_activate: true
active_after_deactivate: false
deactivation_error: null
```

Purpose:

```text
Confirm the workflow can be published and unpublished cleanly before dispatching GitHub Actions.
```

---

## Controlled Dispatch Test

Request:

```json
{
  "confirm_dispatch": "VALIDATE_LOGOS_CATALOG",
  "ref": "main"
}
```

n8n response:

```text
started_at_utc: 2026-07-02T13:51:17.6348464Z
dispatch_status: validator_dispatch_requested
validator_status: dispatched
final_active: false
deactivation_error: null
```

GitHub Action created:

```text
run_id: 28595297447
event: workflow_dispatch
created_at: 2026-07-02T13:51:20Z
url: https://github.com/deflagyn/LOGOS-Engine/actions/runs/28595297447
result: success
```

Interpretation:

```text
The n8n validator dispatch gate is proven end-to-end for dispatching validate-catalog.yml on main.
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

The gate dispatches GitHub Actions successfully, but it still does not poll the final run result itself.

Current behavior:

```text
validator_status: dispatched
```

External verification used:

```text
GitHub CLI run list/watch
```

Future improvement:

```text
Add run polling or a follow-up GitHub Action status lookup node.
```

