# PILOT-0001 n8n Implementation Plan

Status: ready for implementation

Related:

```text
#27 PILOT-0001: Raw meaning end-to-end system run
#28 FOUNDATION-I: Reference Integrity Layer
```

---

## Purpose

Create the first live LOGOS runtime loop in n8n.

This stage should prove that LOGOS can move from raw meaning to validator-facing GitHub artifacts through the system, not through manual assistant interpretation.

The goal is not to automate everything.

The goal is one narrow, traceable, reversible run:

```text
GitHub Issue #27
-> n8n
-> raw meaning preservation
-> LOGOS YAML artifacts
-> GitHub writeback
-> validator
-> issue comment with result
```

---

## Input

```text
GitHub issue #27
Local secrets in .secrets/vps-n8n-access.md
n8n API access
GitHub API token stored in n8n credentials or environment
PILOT-0001 prompt and node specs
```

Secrets must never be committed.

---

## Output

Required validator-facing artifacts:

```text
pilots/PILOT-0001/input/raw-meaning.yaml
pilots/PILOT-0001/output/meaning-edges.yaml
pilots/PILOT-0001/output/human-truth.yaml
pilots/PILOT-0001/output/human-contradiction.yaml
pilots/PILOT-0001/output/belief-shift.yaml
pilots/PILOT-0001/output/meaning-atoms.yaml
pilots/PILOT-0001/output/story-pattern.yaml
pilots/PILOT-0001/output/experiment-plan.yaml
```

Human-readable artifacts:

```text
pilots/PILOT-0001/output/script-draft.md
pilots/PILOT-0001/output/learning.md
pilots/PILOT-0001/output/law-review.md
pilots/PILOT-0001/RUN-LOG.md
```

Recommended run manifest:

```text
pilots/PILOT-0001/RUN-MANIFEST.yaml
```

---

## Core Principle

n8n is not the source of truth.

GitHub remains the source of truth.

n8n is the execution layer that reads from GitHub, processes the run, writes artifacts back to GitHub and reports evidence.

---

## Implementation Plan

### 1. Fix The PILOT-0001 Contract

Before implementation, confirm the exact file contract.

Rule:

```text
YAML = validator-facing LOGOS object artifact
Markdown = optional human-readable explanation
```

The required Story Pattern artifact is:

```text
pilots/PILOT-0001/output/story-pattern.yaml
```

Optional explanation:

```text
pilots/PILOT-0001/output/story-pattern.md
```

### 2. Create The n8n Workflow Disabled

Create the workflow through the n8n API, but do not activate it.

Initial nodes:

```text
Manual Trigger
Config
Fetch GitHub Issue #27
Extract Raw Meaning
Preserve Raw Meaning
Generate Meaning Edges
Generate LOGOS Objects
Generate Runtime Draft
Generate Experiment Plan
Generate Learning / Law Review
GitHub Writeback
Trigger GitHub Validator
Comment Result on Issue #27
```

Use manual execution first.

Do not add Telegram or public webhook triggers in the first run.

### 3. Make Raw Meaning Preservation The First Hard Gate

The workflow must preserve raw meaning before any LLM interpretation.

Target shape:

```yaml
id: RM-PILOT-0001
type: raw_meaning
pilot_id: PILOT-0001
source_issue: 27
raw_text: |
  original text exactly
preserve_author_voice: true
source_must_remain: true
axiom: AX-021
```

If raw meaning is not saved, the workflow must stop.

### 4. Use Strict LLM Output Contracts

LLM nodes must return structured artifacts only.

Every generated LOGOS object should include:

```text
id
type
status
pilot_id
source_issue
source_raw_meaning_id
trace_to_previous
derived_interpretation
test_note
```

The LLM must not return conversational commentary in object nodes.

### 5. Write Back To GitHub With Create-Or-Update

For each target path:

```text
GET contents path
if 404 -> create file
if exists -> update file using sha
collect commit sha
```

Protection rule:

```text
raw-meaning.yaml must never be overwritten with derived text.
```

### 6. Trigger Repository Validation

After writeback, trigger:

```text
Validate LOGOS Catalog
```

Preferred workflow:

```text
POST /repos/deflagyn/LOGOS-Engine/actions/workflows/validate-catalog.yml/dispatches
```

Initial MVP may record:

```text
validator_status: dispatched
```

Current validator gate now performs bounded status lookup after dispatch and reports:

```text
polling_mode: bounded_3_attempts_15s_interval
validator_status: success | failure | cancelled | skipped | in_progress
validator_run_url: GitHub Actions run URL
```

Future improvement:

```text
Add conditional branching to stop lookup attempts early after completion, if the graph remains readable.
```

### 7. Comment On Issue #27

The final issue comment must be an evidence summary, not a generic success message.

Required fields:

```text
PILOT-0001 run completed / failed
Run ID
Files created or updated
Commit SHAs
Validator result
Broken references if any
Failed node if any
Next action
```

### 8. Keep Workflow Disabled Until Review

After the first manual run, keep the workflow disabled until the output is reviewed.

Activation decision comes later.

---

## Advantages

```text
Protects the active VPS project because no reboot or restart is needed.
Keeps GitHub as source of truth.
Uses Foundation-I validation immediately.
Makes disconnected artifacts visible.
Keeps the pilot small enough to debug.
Turns LOGOS from documentation into a working system loop.
```

---

## Risks

```text
n8n workflow may become long and hard to inspect.
LLM outputs may be invalid YAML.
GitHub writeback requires careful sha handling.
GitHub Action polling may complicate the MVP.
Issue #27 extraction may be brittle if the source text is not structured.
The system may still generate impressive but weak meaning unless review remains strict.
```

---

## What Is Between The Lines

This stage does not primarily test n8n.

It tests whether LOGOS can behave like an engine.

Before PILOT-0001, LOGOS is a strong architecture.

After PILOT-0001, it either becomes a working runtime loop or reveals where the architecture fails under execution.

The hidden failure mode is:

```text
n8n generates beautiful files
but the files are not traceable LOGOS objects
```

Foundation-I exists to catch that.

---

## How To Improve This Stage 10x

### 1. Add A Preflight Node

Check before any write:

```text
GitHub API auth
n8n API auth
target branch
issue #27 exists
validator workflow exists
output paths are writable
```

### 2. Add A Run Manifest

Create:

```text
pilots/PILOT-0001/RUN-MANIFEST.yaml
```

Suggested fields:

```yaml
run_id:
started_at:
source_issue:
files_created:
commits:
validator_run:
status:
failed_node:
safe_to_rerun:
```

### 3. Add Schema Repair

For each LLM YAML output:

```text
generate
-> parse YAML
-> if invalid, repair prompt
-> if still invalid, fail safely
```

### 4. Add Mini-Validation Inside n8n

Before GitHub writeback, check:

```text
id exists
type exists
pilot_id exists
source_raw_meaning_id exists
trace_to_previous exists
```

The repository validator remains the final gate.

### 5. Add Idempotency

Repeated runs should update known paths, not create chaos.

Rule:

```text
same pilot_id + same output path = update file
new run_id = append run evidence
```

### 6. Add Fail-Fast Gates

```text
If raw meaning is not saved, stop.
If LOGOS objects are invalid, stop.
If GitHub writeback fails, stop.
If validator dispatch fails, report failure.
```

### 7. Add Human Review Checkpoint

Generated objects should remain:

```text
status: candidate
review_required: true
law_promotion_allowed: false
```

### 8. Add Rollback Notes

Do not auto-delete files.

Record:

```text
files_created_before_failure
cleanup_required
safe_to_rerun
```

### 9. Parse Validator Results

Instead of only reporting failure, classify:

```text
broken reference
missing field
duplicate id
invalid YAML
```

### 10. Turn The Pilot Into A Reusable Template

Only after the first successful manual run:

```text
PILOT-0001 hardcoded
-> configurable pilot_id
-> configurable source_issue
-> configurable runtime
```

---

## Recommended MVP Layers

Build in three layers:

```text
Layer 1: Manual Trigger -> GitHub fetch -> raw meaning writeback
Layer 2: LLM objects -> GitHub writeback
Layer 3: validator dispatch -> issue comment
```

Run and review each layer manually before adding the next.

---

## Acceptance Criteria

```text
One issue #27 becomes one traceable pilot folder in GitHub.
Raw meaning is preserved before interpretation.
Validator-facing YAML artifacts are created.
GitHub validation passes or reports actionable errors.
Issue #27 receives a run summary with evidence.
n8n does not become the source of truth.
No VPS reboot or service restart is performed.
```

---

## Manual Test

1. Keep the n8n workflow disabled.
2. Run manual execution.
3. Confirm raw meaning file is written first.
4. Confirm output YAML artifacts are written.
5. Confirm `Validate LOGOS Catalog` is dispatched.
6. Confirm issue #27 receives a summary comment.
7. Confirm repository validation either passes or explains the chain break.

---

## Evidence

Evidence for successful completion should include:

```text
n8n execution ID
GitHub files created or updated
commit SHAs
validator run URL
issue #27 comment URL
```

---

## Future Automation Path

After a successful manual run:

```text
1. Add early-stop branching to the bounded GitHub Actions polling gate.
2. Add webhook trigger.
3. Add configurable pilot_id and source_issue.
4. Add Telegram intake only after the pilot template is stable.
5. Promote the workflow from pilot to reusable LOGOS intake/runtime pattern.
```
