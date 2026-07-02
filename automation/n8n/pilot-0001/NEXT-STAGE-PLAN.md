# PILOT-0001 Next Stage Plan

Date: 2026-07-02

Status: implementation plan

Related:

```text
#27 PILOT-0001: Raw meaning end-to-end system run
roadmap/FOUNDATION-I-REFERENCE-INTEGRITY.md
automation/n8n/pilot-0001/IMPLEMENTATION-PLAN.md
automation/n8n/pilot-0001/N8N-WORKFLOW-STATUS.md
```

---

## Purpose

Define the next implementation stage after Foundation I and the first controlled n8n writebacks.

This plan exists to prevent the next step from turning into uncontrolled automation.

The goal is not:

```text
put everything into n8n at once
```

The goal is:

```text
turn PILOT-0001 into a controlled, traceable LOGOS runtime loop
where every generated artifact is written back to GitHub,
validated by the repository,
and reviewed before any promotion to experiment, learning or law.
```

---

## Current State

Foundation I is implemented and the validator now protects reference integrity.

PILOT-0001 already has controlled n8n writeback evidence for:

```text
raw meaning
meaning edges
candidate LOGOS objects
```

Existing validator-facing artifacts:

```text
pilots/PILOT-0001/input/raw-meaning.yaml
pilots/PILOT-0001/output/meaning-edges.yaml
pilots/PILOT-0001/output/human-truth.yaml
pilots/PILOT-0001/output/human-contradiction.yaml
pilots/PILOT-0001/output/belief-shift.yaml
pilots/PILOT-0001/output/meaning-atoms.yaml
pilots/PILOT-0001/output/story-pattern.yaml
```

The next safe artifact is:

```text
pilots/PILOT-0001/output/script-draft.md
```

This artifact is runtime-facing and human-readable.
It must remain traceable to the YAML objects.

---

## Non-Negotiable Boundaries

```text
Do not reboot the VPS.
Do not restart Docker.
Do not restart n8n.
Do not change active VPS services.
Do not store secrets in Git.
Do not make n8n the source of truth.
Do not promote candidate objects to laws.
Do not create learning without an experiment.
Do not generate content that cannot trace back to LOGOS objects.
```

n8n may execute.

GitHub must remember.

The repository remains the final truth.

---

## Implementation Strategy

Use layered activation.

Each layer should be built, run once, deactivated, pulled locally, validated, documented, committed and reported in issue `#27`.

Do not keep temporary trigger workflows active after execution.

---

## Stage 0 - Close The Current Evidence Loop

### Purpose

Make sure the existing LOGOS object writeback is fully recorded before generating a runtime draft.

### Input

```text
current repository state
n8n workflow evidence
GitHub validation workflow
issue #27
```

### Output

```text
latest GitHub validation result recorded
issue #27 updated with LOGOS object writeback evidence
local repository clean or known-dirty only with intentional work
```

### Acceptance Criteria

```text
GitHub validation passes.
Issue #27 has a comment with files, commit SHAs and validation result.
All temporary controlled writeback workflows are inactive.
```

### Manual Test

```text
git status --short --branch
python scripts/validate_catalog.py .
python -m logos_engine.validate .
gh run list --workflow validate-catalog.yml --limit 3
```

### Evidence

```text
validation command output
GitHub Actions run URL
issue #27 comment URL
```

### Future Automation Path

Later, this can become an n8n "finalize run" node that polls validation and comments on the issue.

---

## Stage 1 - Runtime Draft Generation

### Purpose

Generate the first human-readable runtime expression from the structured LOGOS chain.

This is not the core LOGOS object layer.
It is only the first expression of the belief movement.

### Input

```text
raw-meaning.yaml
meaning-edges.yaml
human-truth.yaml
human-contradiction.yaml
belief-shift.yaml
meaning-atoms.yaml
story-pattern.yaml
```

### Output

```text
pilots/PILOT-0001/output/script-draft.md
```

### Required Draft Sections

```text
Source objects
Belief movement
Draft script
Traceability note
Ethical boundary
Review required
Not experiment evidence
Not learning
Not law
```

### Acceptance Criteria

```text
The draft references source object IDs.
The product is not the hero.
The human transformation remains the hero.
The draft does not claim evidence.
The draft does not create or imply a LOGOS Law.
The draft is written back by n8n, not manually pasted into GitHub.
The repository validator still passes after writeback.
```

### Manual Test

```text
read script-draft.md
check every referenced object ID exists
run repository validation
confirm issue #27 receives evidence
```

### Evidence

```text
n8n workflow ID
n8n execution evidence
GitHub commit SHA
validator result
issue #27 comment
```

### Future Automation Path

The draft generation node can later become a reusable `Generate Runtime Draft` node for any pilot, but only after PILOT-0001 proves traceability.

---

## Stage 2 - Experiment Plan Candidate

### Purpose

Create a test plan for the runtime draft without pretending that the draft has already produced learning.

### Input

```text
script-draft.md
story-pattern.yaml
meaning-atoms.yaml
belief-shift.yaml
```

### Output

```text
pilots/PILOT-0001/output/experiment-plan.yaml
```

### Required Fields

```text
id
type
status
pilot_id
source_issue
source_script
belief_shift_id
meaning_atom_id
story_pattern_id
hypothesis
test_channel
success_signals
meaning_signals
risk_notes
review_required
law_promotion_allowed: false
```

### Acceptance Criteria

```text
The experiment plan is a candidate.
It contains measurable signals.
It includes meaning quality signals, not only views or clicks.
It does not create learning yet.
It does not promote a law.
The validator passes.
```

### Manual Test

```text
confirm YAML parses
confirm references exist
confirm no learning/law language is used as proof
run repository validation
```

### Evidence

```text
experiment-plan.yaml commit SHA
validator run URL
issue #27 comment
```

### Future Automation Path

Later, experiment plans can create GitHub issues or project cards automatically.

---

## Stage 3 - Run Manifest

### Purpose

Add a machine-readable run record so PILOT-0001 can be audited without reconstructing everything from scattered commits.

### Output

```text
pilots/PILOT-0001/RUN-MANIFEST.yaml
```

### Suggested Shape

```yaml
id: RUN-PILOT-0001
type: pilot_run_manifest
pilot_id: PILOT-0001
source_issue: 27
status: candidate
started_at:
completed_at:
workflows:
  - name:
    n8n_workflow_id:
    active_after_run: false
artifacts:
  - path:
    commit_sha:
validation:
  local:
  github_action:
review:
  required: true
  law_promotion_allowed: false
```

### Acceptance Criteria

```text
Every generated artifact is listed.
Every writeback has a commit SHA where available.
Every workflow is recorded as inactive after controlled use.
Validation evidence is linked.
```

### Manual Test

```text
compare manifest artifact list with pilots/PILOT-0001/
confirm no secret values are present
run repository validation
```

### Future Automation Path

This becomes the audit spine for future pilots.

---

## Stage 4 - Learning And Law Review Placeholder

### Purpose

Prepare the structure for learning and law review without inventing evidence.

### Output

Optional placeholder files only after experiment planning is valid:

```text
pilots/PILOT-0001/output/learning.md
pilots/PILOT-0001/output/law-review.md
```

### Boundary

These files must say, in effect:

```text
No experiment result exists yet.
No learning can be concluded.
No law promotion is allowed.
```

### Acceptance Criteria

```text
No law is created.
No learning is claimed.
The files only define what evidence will be needed later.
```

### Future Automation Path

After a real experiment, n8n can collect metrics and generate a learning candidate.

---

## Advantages

```text
Keeps the active VPS safe because no reboot or restart is required.
Turns n8n into a controlled execution layer instead of a second source of truth.
Uses Foundation I immediately instead of letting validation sit unused.
Makes each failure small and debuggable.
Preserves raw meaning before interpretation.
Forces content to trace back to LOGOS objects.
Prevents premature learning and fake laws.
Creates evidence useful for future reusable workflow templates.
```

---

## Disadvantages And Tradeoffs

```text
The process is slower than wiring the whole workflow at once.
There will be more small commits and issue comments.
Temporary n8n workflows may feel repetitive.
Manual review remains necessary.
Markdown runtime drafts are harder to validate than YAML objects.
GitHub Actions polling from n8n may add complexity.
The first pilot remains partly hardcoded around PILOT-0001 and issue #27.
```

These tradeoffs are acceptable because the current risk is not speed.

The current risk is false confidence.

---

## What Is Between The Lines

This stage is not really about n8n.

It is about whether LOGOS can survive contact with execution.

The hidden question:

```text
Can the engine produce runtime material without losing the belief-change chain?
```

The dangerous fake success:

```text
The draft sounds good,
but nobody can prove which Human Truth,
Human Contradiction,
Belief Shift,
Meaning Atom,
and Story Pattern produced it.
```

The deeper purpose of this stage is to make every beautiful sentence accountable.

---

## How To Improve This 10x

### 1. Add A Preflight Gate To Every Controlled Workflow

Check:

```text
GitHub auth
n8n credential presence
target branch
issue #27 availability
workflow active state
output path conflict
validator workflow availability
```

### 2. Add A Repository Pull Step Before Each Local Validation

After n8n writes to GitHub:

```text
git pull --ff-only
python scripts/validate_catalog.py .
```

This prevents local review from drifting away from the real source of truth.

### 3. Add Object ID Diffing

Before and after each writeback:

```text
list all LOGOS IDs
show added IDs
show changed IDs
fail on accidental duplicate IDs
```

### 4. Add A Draft Traceability Header

Every runtime draft should start with:

```text
source_raw_meaning_id:
human_truth_id:
human_contradiction_id:
belief_shift_id:
meaning_atom_id:
story_pattern_id:
```

This makes even Markdown auditable.

### 5. Add A "No Evidence Yet" Guard

Any node that writes learning or law review must check:

```text
experiment_result_exists == true
```

If false, it may only write a placeholder.

### 6. Add Safe Rerun Semantics

Use deterministic paths:

```text
same pilot_id + same artifact path = update
new evidence = append to writeback evidence
```

Do not create random duplicate files.

### 7. Add Failure Reports

On failure, n8n should write or comment:

```text
failed_node
failed_artifact
last_successful_commit
safe_to_rerun
manual_cleanup_needed
```

### 8. Add Validator Result Parsing

Instead of only saying validation failed, classify:

```text
missing field
broken reference
duplicate ID
invalid YAML
unexpected pilot artifact shape
```

### 9. Split LLM Generation From GitHub Writeback

For each generated artifact:

```text
generate
parse or inspect
repair if needed
review gate
writeback
validate
```

This keeps bad output from becoming repository state.

### 10. Convert PILOT-0001 Into A Reusable Template Only After Review

Do not generalize too early.

Promotion path:

```text
hardcoded PILOT-0001
-> configurable pilot_id and source_issue
-> reusable pilot runner
-> WF-0001/WF-0002/WF-0003 production pattern
```

---

## Recommended Order

```text
0. Confirm current validation and issue evidence.
1. Generate script-draft.md through n8n.
2. Validate repository and record evidence.
3. Add experiment-plan.yaml only after script draft review.
4. Add RUN-MANIFEST.yaml.
5. Add learning/law placeholders only if useful.
6. Convert the proven pieces into reusable workflow patterns.
```

---

## Definition Of Done

This stage is done when:

```text
script-draft.md exists and traces to LOGOS objects.
experiment-plan.yaml exists as a candidate, if approved for this stage.
RUN-MANIFEST.yaml records workflows, artifacts, commits and validation.
Repository validation passes locally and in GitHub Actions.
Issue #27 contains evidence comments.
All temporary controlled n8n workflows are inactive after use.
No VPS reboot or service restart was performed.
No learning or law was claimed without experiment evidence.
```

