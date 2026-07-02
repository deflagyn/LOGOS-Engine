# WF-0001 Idea Intake Schema Parity Test

Date: 2026-07-02

Purpose:

```text
Prove that the n8n WF-0001 validation node rejects payload classes that the repository schema also rejects.
```

Repository schema:

```text
schemas/wf-0001-idea-intake.schema.yaml
```

---

## Workflow

```text
name: LOGOS WF-0001 Idea Intake Issue Gate
id: s00B4QAhJ3MYZ1tq
active_after_test: false
node_count: 5
```

Updated node:

```text
02 Validate And Build Human Truth Issue
```

Runtime validation now checks:

```text
unknown fields are rejected
language length must be 2 to 16 characters
optional fields must be text when provided
scope must be universal or runtime
title_suffix must be non-empty when provided and 120 characters or fewer
```

---

## Rejection Test 1

Mutation:

```text
Payload included unexpected_runtime_field.
```

n8n execution:

```text
execution_id: 1098
status: error
failed_node: 02 Validate And Build Human Truth Issue
error: unexpected_runtime_field [line 16]
workflow_final_active: false
```

Interpretation:

```text
The n8n gate rejects fields outside the repository schema contract before GitHub issue creation.
```

---

## Rejection Test 2

Mutation:

```text
language: language-name-that-is-too-long
```

n8n execution:

```text
execution_id: 1099
status: error
failed_node: 02 Validate And Build Human Truth Issue
error: language must be 2 to 16 characters [line 33]
workflow_final_active: false
```

Interpretation:

```text
The n8n gate enforces the same language length boundary as the repository schema.
```

---

## GitHub Issue Check

Latest issues after the rejection tests:

```text
#29 HT-0000: Intake must preserve raw observations before interpretation
#28 FOUNDATION-I: Reference Integrity Layer
#27 PILOT-0001: Raw meaning end-to-end system run
```

Interpretation:

```text
No new GitHub issue was created by the rejection tests.
```

---

## Safety

```text
Only LOGOS WF-0001 Idea Intake Issue Gate was briefly activated.
The workflow was deactivated immediately after controlled rejection tests.
Final workflow state is active=false.
No GitHub issue was created.
No YAML object was written.
No PILOT-0001 artifact was written.
No learning artifact was created.
No law review artifact was created.
No VPS reboot was performed.
No Docker, n8n, nginx, Postgres or service restart was performed.
No secret value was committed or pasted into issue comments.
```

