# PILOT-0001 Response Intake Preview Gate

This document records the dedicated n8n workflow that previews PILOT-0001 response intake without writing artifacts.

---

## Workflow

```text
name: LOGOS PILOT-0001 Response Intake Preview Gate
id: b3wLpAMf6JKd0j92
active: false
```

Purpose:

```text
Validate cleaned response JSON and return a normalized response preview before any repository writeback.
```

This workflow does not write response YAML.

It does not update `RUN-MANIFEST.yaml`.

It does not create learning or law artifacts.

---

## Nodes

```text
01 Controlled Response Preview Webhook
02 Validate Response Input Preview
03 Respond Preview JSON
```

---

## Safety Contract

The request must include:

```json
{
  "confirm_preview": "PREVIEW_PILOT_0001_RESPONSE_INPUT",
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
```

---

## Current State

```text
created: true
active: false
valid_preview_tested: true
simulated_response_rejection_tested: true
```

Test evidence:

```text
automation/n8n/pilot-0001/writeback/response-intake-preview-gate-test-2026-07-02.md
```

---

## Operation Protocol

For a controlled preview:

```text
1. Activate only this workflow if webhook execution is required.
2. POST the required confirmation payload and cleaned response JSON.
3. Verify status=response_input_preview_valid.
4. Verify writeback_performed=false.
5. Verify creates_response_file=false.
6. Deactivate the workflow immediately after the controlled preview.
7. Write no response artifact from preview output.
```

Do not use this gate to create fake response evidence.

Do not use this gate to bypass `scripts/create_pilot_response.py`.

