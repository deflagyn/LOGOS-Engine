# PILOT-0001 Validator Comment Chain Controlled Test

Date: 2026-07-02

Purpose:

```text
Prove that n8n can run the controlled validator gate, pass its result to the issue comment gate, and return a single chain response.
```

---

## Workflows

Validator gate:

```text
name: LOGOS PILOT-0001 Validator Dispatch Gate
id: oWQbN9u1VI4AS6rq
```

Issue comment gate:

```text
name: LOGOS PILOT-0001 Issue Comment Gate
id: UwkfEOmygkX4BBe5
```

Chain:

```text
name: LOGOS PILOT-0001 Validator Comment Chain
id: fiHf9XFu8zfPHWzl
```

---

## Activation Smoke Test

Chain smoke result:

```text
activation_smoke: success
active_after_activate: true
active_after_deactivate: false
deactivation_error: null
```

---

## Controlled Chain Test

Request:

```json
{
  "confirm_chain": "RUN_PILOT_0001_VALIDATOR_COMMENT_CHAIN",
  "ref": "main"
}
```

n8n chain response:

```text
status: validator_success_commented
validator_status: success
validator_run_id: 28611724244
validator_run_url: https://github.com/deflagyn/LOGOS-Engine/actions/runs/28611724244
validator_run_conclusion: success
polling_mode: bounded_3_attempts_15s_interval
selected_attempt: 2
issue_comment_url: https://github.com/deflagyn/LOGOS-Engine/issues/27#issuecomment-4869170239
issue_comment_id: 4869170239
deactivation_errors: []
```

Final workflow states:

```text
Validator Dispatch Gate active=false node_count=11
Issue Comment Gate active=false node_count=5
Validator Comment Chain active=false node_count=7
```

Interpretation:

```text
The controlled chain is proven end-to-end for validator dispatch, validator status observation, and issue #27 evidence comment.
```

---

## Safety

```text
Only the three controlled gate/chain workflows were briefly activated.
All three workflows were deactivated immediately after the controlled run.
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

The chain currently requires the validator gate and issue comment gate to be active during the controlled run.

Future improvement:

```text
Promote this into the System Run only after the same safety guarantees are preserved and the graph remains readable.
```

