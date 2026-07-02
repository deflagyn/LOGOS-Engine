# WF-0001 — Idea Intake

## Purpose

Turn a raw idea or observation into a structured LOGOS candidate.

This workflow is the front door of LOGOS.

---

## Input

```text
Raw idea
Source
Language
Runtime or universal scope
Optional context
```

---

## Output

One of:

```text
Observation candidate
Human Truth candidate
Human Contradiction candidate
```

Primary GitHub output:

```text
New GitHub Issue using the Human Truth template
```

Later output:

```text
YAML object file after review
```

---

## n8n Draft Nodes

```text
Webhook or Telegram Trigger
Normalize Input
Classify Scope
Draft Human Truth
Create GitHub Issue
Return Issue URL
```

Current implemented n8n gate:

```text
name: LOGOS WF-0001 Idea Intake Issue Gate
id: s00B4QAhJ3MYZ1tq
active: false
```

Current implementation boundary:

```text
Controlled webhook input
→ validate required fields and confirmation string
→ build Human Truth issue body
→ create GitHub Issue
→ return issue URL
```

Repository payload contract:

```text
schemas/wf-0001-idea-intake.schema.yaml
testing/fixtures/wf-0001-idea-intake.json.example
scripts/validate_wf_0001_idea_intake.py
```

Evidence:

```text
automation/n8n/wf-0001/IDEA-INTAKE-ISSUE-GATE.md
automation/n8n/wf-0001/writeback/idea-intake-issue-gate-test-2026-07-02.md
https://github.com/deflagyn/LOGOS-Engine/issues/29
```

Limit:

```text
This first gate does not use an LLM node.
The payload must include the Human Truth candidate and test plan.
```

---

## Manual Dry Run

1. Take one raw idea.
2. Rewrite it as a Human Truth candidate.
3. Create an issue with the Human Truth template.
4. Link the issue to the Project board.
5. Record whether the candidate is clear enough for review.

---

## Acceptance Criteria

```text
Given a raw idea,
When the workflow processes it,
Then a structured GitHub issue exists with ID placeholder, source, observation, Human Truth candidate and test plan.
```

---

## Test Plan

Purpose:

```text
Check whether raw ideas can enter LOGOS without becoming loose notes.
```

Input:

```text
One raw idea.
```

Expected output:

```text
One structured issue.
```

Evidence:

```text
A test issue or dry-run file.
```

Current evidence:

```text
GitHub issue #29 was created by n8n from a controlled WF-0001 payload.
```

Future automation:

```text
n8n creates the issue directly from Telegram or webhook input.
```
