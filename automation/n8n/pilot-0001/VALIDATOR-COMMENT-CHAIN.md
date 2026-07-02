# PILOT-0001 Validator Comment Chain

This document records the controlled n8n chain that calls the validator gate, then passes its result into the issue comment gate.

---

## Workflow

```text
name: LOGOS PILOT-0001 Validator Comment Chain
id: fiHf9XFu8zfPHWzl
active: false
```

Purpose:

```text
Run a controlled validator check and write the validator result evidence to issue #27.
```

This workflow does not write pilot artifacts.

It orchestrates existing controlled gates:

```text
Validator Dispatch Gate -> Issue Comment Gate
```

---

## Nodes

```text
01 Controlled Chain Webhook
02 Validate Chain Request
03 Call Validator Dispatch Gate
04 Build Issue Comment Request
05 Call Issue Comment Gate
06 Build Chain Response
07 Respond Chain JSON
```

---

## Safety Contract

The request must include:

```json
{
  "confirm_chain": "RUN_PILOT_0001_VALIDATOR_COMMENT_CHAIN",
  "ref": "main"
}
```

Hard-coded limits:

```text
pilot_id: PILOT-0001
issue_number: 27
ref: main
```

The workflow rejects:

```text
missing confirmation
non-main ref
validator result other than success
```

---

## Current State

```text
created: true
active: false
controlled_chain_tested: true
```

Test evidence:

```text
automation/n8n/pilot-0001/writeback/validator-comment-chain-test-2026-07-02.md
```

---

## Operation Protocol

For a controlled run:

```text
1. Confirm no broader LOGOS workflow is running.
2. Activate Validator Dispatch Gate.
3. Activate Issue Comment Gate.
4. Activate Validator Comment Chain.
5. POST the required confirmation payload to the chain.
6. Wait for the chain response.
7. Deactivate all three workflows immediately after the controlled run.
8. Verify all three workflows are active=false.
9. Record validator run URL and issue comment URL in repository evidence.
```

Do not use this chain to write pilot artifacts.

Do not use this chain to create learning or law review.

