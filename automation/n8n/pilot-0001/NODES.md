# PILOT-0001 n8n Nodes

This document defines the node-level workflow for PILOT-0001.

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

Output:

```json
{
  "pilot_id": "PILOT-0001",
  "issue_number": 27,
  "repo": "deflagyn/LOGOS-Engine"
}
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
model = env.LOGOS_LLM_MODEL
```

---

## Node 03 — Fetch Pilot Issue

Type:

```text
HTTP Request
```

Purpose:

```text
Fetch GitHub issue #27 using GitHub API.
```

Method:

```text
GET
```

URL:

```text
https://api.github.com/repos/deflagyn/LOGOS-Engine/issues/27
```

Auth:

```text
GitHub token from n8n credentials or environment.
```

Output required:

```text
issue.title
issue.body
issue.html_url
```

---

## Node 04 — Extract Raw Meaning

Type:

```text
Code
```

Purpose:

```text
Extract the Raw Meaning block from issue body.
```

Output fields:

```json
{
  "raw_text": "",
  "source_issue": 27,
  "author_intent": "preserve raw meaning",
  "axiom": "AX-021"
}
```

Hard rule:

```text
Do not rewrite raw_text.
```

---

## Node 05 — Preserve Raw Meaning File

Type:

```text
HTTP Request
```

Purpose:

```text
Create GitHub file with raw meaning preserved exactly.
```

Target path:

```text
pilots/PILOT-0001/input/raw-meaning.yaml
```

Content must include:

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
```

---

## Node 06 — Generate Meaning Edges

Type:

```text
LLM HTTP Request
```

Prompt:

```text
Use PROMPTS.md / P01_MEANING_EDGES
```

Output path:

```text
pilots/PILOT-0001/output/meaning-edges.yaml
```

---

## Node 07 — Generate LOGOS Objects

Type:

```text
LLM HTTP Request
```

Prompt:

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

---

## Node 08 — Generate Runtime Draft

Type:

```text
LLM HTTP Request
```

Prompt:

```text
Use PROMPTS.md / P03_RUNTIME_DRAFT
```

Output path:

```text
pilots/PILOT-0001/output/script-draft.md
```

---

## Node 09 — Generate Experiment Plan

Type:

```text
LLM HTTP Request
```

Prompt:

```text
Use PROMPTS.md / P04_EXPERIMENT_PLAN
```

Output path:

```text
pilots/PILOT-0001/output/experiment-plan.yaml
```

---

## Node 10 — Generate Learning and Law Review

Type:

```text
LLM HTTP Request
```

Prompt:

```text
Use PROMPTS.md / P05_LEARNING_REVIEW
```

Output paths:

```text
pilots/PILOT-0001/output/learning.md
pilots/PILOT-0001/output/law-review.md
```

---

## Node 11 — GitHub Writeback

Type:

```text
HTTP Request nodes
```

Purpose:

```text
Create or update all pilot files in GitHub.
```

Rules:

```text
Use create file when missing.
Use update file when existing.
Never overwrite raw meaning with derived text.
```

---

## Node 12 — Run Validator

Type:

```text
Execute Command or GitHub Actions dispatch
```

Preferred during MVP:

```text
Trigger GitHub Action: Validate LOGOS Catalog
```

Alternative on VPS:

```text
python scripts/validate_catalog.py .
```

---

## Node 13 — Comment on Pilot Issue

Type:

```text
HTTP Request
```

Purpose:

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
