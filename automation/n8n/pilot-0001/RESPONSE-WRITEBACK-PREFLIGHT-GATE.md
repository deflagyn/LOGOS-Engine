# PILOT-0001 Response Writeback Preflight Gate

This document records the dedicated n8n workflow that preflights future PILOT-0001 response writeback without writing artifacts.

---

## Workflow

```text
name: LOGOS PILOT-0001 Response Writeback Preflight Gate
id: zG9ST52p5Iml8TXq
active: false
```

Purpose:

```text
Validate that a cleaned response payload is eligible for future real response writeback before any repository mutation happens.
```

This workflow does not write response YAML.

It does not update `RUN-MANIFEST.yaml`.

It does not create learning or law artifacts.

---

## Nodes

```text
01 Controlled Response Writeback Preflight Webhook
02 Validate Real Response Writeback Preflight
03 Respond Preflight JSON
```

---

## Safety Contract

The request must include:

```json
{
  "confirm_writeback_preflight": "PREFLIGHT_PILOT_0001_REAL_RESPONSE_WRITEBACK",
  "real_response_attestation": "REAL_SANITIZED_RESPONSE_COLLECTED",
  "response_input": {}
}
```

The response input must satisfy the same boundary as the local intake schema:

```text
personal_data_removed: true
simulated_response: false
all four qualitative answers
all five meaning signal scores
scores as integers from 0 to 5
failure signal flags as booleans
raw_quotes as an array of strings when present
```

The extra `real_response_attestation` field is intentionally separate from the response object.

It prevents a test fixture or preview payload from being silently promoted into the real writeback path.

---

## Current State

```text
created: true
active: false
activation_smoke_tested: true
missing_real_response_attestation_rejection_tested: true
simulated_response_rejection_tested: true
successful_writeback_preflight_tested: false
```

Test evidence:

```text
automation/n8n/pilot-0001/writeback/response-writeback-preflight-gate-test-2026-07-02.md
```

---

## Operation Protocol

For a controlled preflight:

```text
1. Activate only this workflow if webhook execution is required.
2. POST the required confirmation payload, real response attestation and cleaned response JSON.
3. Verify status=response_writeback_preflight_passed.
4. Verify writeback_performed=false.
5. Verify ready_for_writeback=true.
6. Deactivate the workflow immediately after the controlled preflight.
7. Write no response artifact from preflight output.
```

Do not use this gate to create fake response evidence.

Do not run a successful preflight with a fixture unless the result is clearly marked as a synthetic contract test.

Do not use this gate to bypass `scripts/create_pilot_response.py`.

