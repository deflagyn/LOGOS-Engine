# WF-0002 Belief Movement Issue Creation Gate Controlled Test

Date: 2026-07-02

Purpose:

```text
Prove that n8n can create a review-facing WF-0002 Belief Shift issue without writing YAML or creating downstream artifacts.
```

---

## Workflow

```text
name: LOGOS WF-0002 Belief Movement Issue Creation Gate
id: wjiTK4Ov1nY1EndY
active_after_test: false
node_count: 5
```

---

## Rejection Test

Mutation:

```text
Source Human Truth ID: HT-0000
```

n8n execution:

```text
execution_id: 1111
status: error
failed_node: 02 Validate And Build Belief Shift Issue
workflow_final_active: false
```

Interpretation:

```text
The issue creation gate rejects placeholder Human Truth IDs before the GitHub POST node.
```

---

## Valid Issue Creation Test

Input:

```text
testing/fixtures/wf-0002-belief-shift-issue.md
```

n8n execution:

```text
execution_id: 1112
status: success
final_node: 05 Respond Issue Creation JSON
```

n8n response:

```text
status: belief_shift_issue_created
issue_number: 30
issue_url: https://github.com/deflagyn/LOGOS-Engine/issues/30
logos_id: BS-0000
source_human_truth_id: HT-0100
writes_yaml: false
creates_meaning_atom: false
learning_allowed: false
workflow_final_active: false
```

Created issue:

```text
https://github.com/deflagyn/LOGOS-Engine/issues/30
```

Local fixture:

```text
testing/fixtures/wf-0002-issue-30.md
```

---

## Safety

```text
Only LOGOS WF-0002 Belief Movement Issue Creation Gate was briefly activated.
The workflow was deactivated immediately after controlled tests.
Final workflow state is active=false.
One GitHub Belief Shift issue was created for review.
No Belief Shift YAML object was written.
No Meaning Atom YAML object was written.
No learning artifact was created.
No law review artifact was created.
No VPS reboot was performed.
No Docker, n8n, nginx, Postgres or service restart was performed.
No secret value was committed or pasted into issue comments.
```

---

## Remaining Limit

This gate creates only a review-facing issue.

Future WF-0002 YAML promotion must be a separate reviewed gate.
