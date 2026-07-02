# WF-0001 Idea Intake Issue Review Readiness

Date: 2026-07-02

Purpose:

```text
Prove that the GitHub issue created by WF-0001 can be validated as structured review input before any YAML object promotion.
```

This is not a promotion gate.

It does not create a Human Truth YAML object.

It only checks whether the issue body has the required sections for human review.

---

## Source Issue

```text
issue: #29
url: https://github.com/deflagyn/LOGOS-Engine/issues/29
title: HT-0000: Intake must preserve raw observations before interpretation
```

Local fixture:

```text
testing/fixtures/wf-0001-issue-29.md
```

---

## Validator

```text
scripts/validate_wf_0001_issue.py
logos_engine/wf_0001_issue.py
```

Command:

```text
python scripts\validate_wf_0001_issue.py --input testing\fixtures\wf-0001-issue-29.md --title "HT-0000: Intake must preserve raw observations before interpretation"
```

Result:

```text
WF-0001 issue body passed review-readiness validation.
logos_id: HT-0000
status: candidate
scope: universal
```

---

## Required Sections

```text
LOGOS ID
Status
Scope
Source or context
Raw observation
Human Truth candidate
Test plan
Intake evidence
```

Validation also checks:

```text
LOGOS ID is HT-0000 or a stable HT-#### identifier
Status is a known LOGOS issue status
Scope is universal or runtime
Intake evidence names the WF-0001 n8n issue gate
Intake evidence states no YAML object writeback happened
Intake evidence states no learning or law artifact was created
```

---

## Rejection Coverage

Unit tests cover:

```text
missing Human Truth candidate section is rejected
invalid scope is rejected
```

---

## Boundary

```text
Review-ready issue does not equal validated Human Truth.
Review-ready issue does not create a YAML object.
Review-ready issue does not create learning, law candidates or LOGOS Laws.
```

Future promotion to YAML must be a separate reviewed gate.

