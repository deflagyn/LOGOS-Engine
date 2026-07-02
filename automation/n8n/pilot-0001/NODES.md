# PILOT-0001 n8n Nodes

This document defines the current node-level workflow for PILOT-0001.

Current n8n workflow:

```text
name: LOGOS PILOT-0001 System Run
id: nFIbtlA2pYrA4MXb
active: false
```

---

## Node 01 — Manual Trigger

Type:

```text
Manual Trigger
```

Purpose:

```text
Start the pilot run manually while the system is being tested.
```

Status:

```text
enabled
```

---

## Node 02 — Config

Type:

```text
Set
```

Fields:

```text
repo_full_name = deflagyn/LOGOS-Engine
pilot_id = PILOT-0001
issue_number = 27
branch = main
mode = skeleton_disabled_no_write
```

Status:

```text
enabled
```

---

## Node 03 — Preflight Checklist

Type:

```text
Code
```

Purpose:

```text
Create a safe preflight object before any network write or LLM processing.
```

Current behavior:

```text
No network writes.
No secrets.
No VPS restart.
Returns required checks and next safe step.
```

Status:

```text
enabled
```

---

## Node 04 — Fetch GitHub Issue #27

Type:

```text
HTTP Request
```

Purpose:

```text
Read GitHub issue #27 through the public GitHub REST API.
```

Method:

```text
GET
```

URL:

```text
https://api.github.com/repos/deflagyn/LOGOS-Engine/issues/27
```

Headers:

```text
Accept: application/vnd.github+json
X-GitHub-Api-Version: 2022-11-28
User-Agent: LOGOS-PILOT-0001-n8n
```

Auth:

```text
none
```

Output required:

```text
number
title
body
html_url
```

Status:

```text
enabled
read-only
```

---

## Node 05 — Extract Raw Meaning

Type:

```text
Code
```

Purpose:

```text
Extract the Raw Meaning block from issue #27 body.
```

Extraction rule:

```text
Prefer text between "Raw Meaning:" and "Author intent:".
If the marker is missing, fall back to the full issue body.
Fail if raw_text is empty.
```

Output fields:

```json
{
  "pilot_id": "PILOT-0001",
  "source_issue": 27,
  "source_issue_url": "",
  "source_issue_title": "",
  "raw_text": "",
  "raw_text_source": "raw_meaning_block",
  "author_intent": "preserve raw meaning, force, edge and author voice",
  "axiom": "AX-021"
}
```

Hard rule:

```text
Do not rewrite raw_text.
```

Status:

```text
enabled
read-only
```

---

## Node 06 — Build Raw Meaning YAML Preview

Type:

```text
Code
```

Purpose:

```text
Build the raw-meaning.yaml artifact content without writing it to GitHub.
```

Target path:

```text
pilots/PILOT-0001/input/raw-meaning.yaml
```

Preview content must include:

```yaml
id: RM-PILOT-0001
type: raw_meaning
pilot_id: PILOT-0001
source_issue: 27
raw_text: |
  original text here
preserve_author_voice: true
source_must_remain: true
axiom: AX-021
writeback_status: preview_only
```

Status:

```text
enabled
preview-only
no GitHub writeback
```

---

## Node 07 — Generate Meaning Edges

Type:

```text
NoOp placeholder
```

Future prompt:

```text
Use PROMPTS.md / P01_MEANING_EDGES
```

Output path:

```text
pilots/PILOT-0001/output/meaning-edges.yaml
```

Status:

```text
disabled
```

---

## Node 08 — Generate LOGOS Objects

Type:

```text
NoOp placeholder
```

Future prompt:

```text
Use PROMPTS.md / P02_LOGOS_OBJECTS
```

Validator-facing output paths:

```text
pilots/PILOT-0001/output/human-truth.yaml
pilots/PILOT-0001/output/human-contradiction.yaml
pilots/PILOT-0001/output/belief-shift.yaml
pilots/PILOT-0001/output/meaning-atoms.yaml
pilots/PILOT-0001/output/story-pattern.yaml
```

Optional human-readable output path:

```text
pilots/PILOT-0001/output/story-pattern.md
```

Rule:

```text
story-pattern.yaml is the required object artifact.
story-pattern.md is optional explanatory text only.
```

Status:

```text
disabled
```

---

## Node 09 — Generate Runtime Draft

Type:

```text
NoOp placeholder
```

Future prompt:

```text
Use PROMPTS.md / P03_RUNTIME_DRAFT
```

Output path:

```text
pilots/PILOT-0001/output/script-draft.md
```

Status:

```text
disabled
```

---

## Node 10 — Generate Experiment Plan

Type:

```text
NoOp placeholder
```

Future prompt:

```text
Use PROMPTS.md / P04_EXPERIMENT_PLAN
```

Output path:

```text
pilots/PILOT-0001/output/experiment-plan.yaml
```

Status:

```text
disabled
```

---

## Node 11 — Generate Learning And Law Review

Type:

```text
NoOp placeholder
```

Future prompt:

```text
Use PROMPTS.md / P05_LEARNING_REVIEW
```

Output paths:

```text
pilots/PILOT-0001/output/learning.md
pilots/PILOT-0001/output/law-review.md
```

Status:

```text
disabled
```

---

## Node 12 — GitHub Writeback

Type:

```text
NoOp placeholder
```

Future purpose:

```text
Create or update all pilot files in GitHub.
```

Rules:

```text
Use create file when missing.
Use update file when existing.
Never overwrite raw meaning with derived text.
Collect commit sha for run evidence.
```

Status:

```text
disabled
```

---

## Node 13 — Trigger Validator

Type:

```text
NoOp placeholder
```

Future purpose:

```text
Trigger GitHub Action: Validate LOGOS Catalog
```

Status:

```text
disabled
```

---

## Node 14 — Comment Result On Issue #27

Type:

```text
NoOp placeholder
```

Future purpose:

```text
Add run summary to issue #27.
```

Comment must include:

```text
run id
files created
validator result
next action
```

Status:

```text
disabled
```

