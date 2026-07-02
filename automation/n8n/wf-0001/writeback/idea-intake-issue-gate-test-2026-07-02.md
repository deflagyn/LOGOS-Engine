# WF-0001 Idea Intake Issue Gate Controlled Test

Date: 2026-07-02

Purpose:

```text
Prove that n8n can turn a controlled raw idea payload into a structured GitHub Human Truth candidate issue while keeping GitHub as source of truth.
```

---

## Workflow

```text
name: LOGOS WF-0001 Idea Intake Issue Gate
id: s00B4QAhJ3MYZ1tq
active_after_test: false
node_count: 5
```

Repository contract:

```text
schemas/wf-0001-idea-intake.schema.yaml
testing/fixtures/wf-0001-idea-intake.json.example
scripts/validate_wf_0001_idea_intake.py
```

---

## Activation Smoke Test

Result:

```text
activation_smoke: success
active_after_activate: true
active_after_deactivate: false
deactivation_error: null
```

---

## Successful Issue Creation Test

Input:

```text
confirm_intake: CREATE_WF_0001_HUMAN_TRUTH_ISSUE
scope: universal
source: WF-0001 controlled n8n implementation test on 2026-07-02
```

n8n execution:

```text
execution_id: 1096
status: success
final_node: 05 Respond Idea Intake JSON
```

n8n response:

```text
status: idea_intake_issue_created
issue_number: 29
issue_url: https://github.com/deflagyn/LOGOS-Engine/issues/29
writes_yaml: false
learning_allowed: false
workflow_final_active: false
```

Created issue title:

```text
HT-0000: Intake must preserve raw observations before interpretation
```

Issue body contains:

```text
LOGOS ID
Status
Scope
Source or context
Raw observation
Human Truth candidate
Meaning resources
Test plan
Connected objects
Intake evidence
```

Interpretation:

```text
WF-0001 now has a real n8n-to-GitHub issue creation path for controlled Human Truth candidate intake.
```

---

## Local Schema Test

Command:

```text
python scripts\validate_wf_0001_idea_intake.py --input testing\fixtures\wf-0001-idea-intake.json.example
```

Result:

```text
WF-0001 idea intake schema passed.
```

Rejection coverage:

```text
missing confirm_intake is rejected
unknown scope is rejected
```

---

## Rejection Test

Mutation:

```text
Payload omitted confirm_intake.
```

n8n execution:

```text
execution_id: 1097
status: error
failed_node: 02 Validate And Build Human Truth Issue
error: confirm_intake must equal CREATE_WF_0001_HUMAN_TRUTH_ISSUE [line 3]
workflow_final_active: false
```

Interpretation:

```text
The gate rejects accidental or unconfirmed webhook posts before GitHub issue creation.
```

---

## Safety

```text
Only LOGOS WF-0001 Idea Intake Issue Gate was briefly activated.
The workflow was deactivated immediately after controlled tests.
Final workflow state is active=false.
One GitHub issue was created as the source-of-truth artifact.
No YAML object was written.
No PILOT-0001 artifact was written.
No learning artifact was created.
No law review artifact was created.
No VPS reboot was performed.
No Docker, n8n, nginx, Postgres or service restart was performed.
No secret value was committed or pasted into issue comments.
```

---

## Remaining Limits

```text
This workflow does not draft the Human Truth candidate with an LLM.
The payload must include the candidate text and test plan.
The created issue still requires human review before any YAML object is promoted.
Telegram/form intake is not connected yet.
```
