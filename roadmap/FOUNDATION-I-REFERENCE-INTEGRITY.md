# FOUNDATION-I — Reference Integrity Layer

Status: ready for Codex implementation

Owner: Codex / implementation agent

Related:

```text
#10 Foundation Gate
#27 PILOT-0001: Raw meaning end-to-end system run
```

---

## Executive Intent

LOGOS foundation is already built well enough to run the first pilot.

But before n8n starts generating pilot artifacts, the system must be protected from a false success.

A false success would look like this:

```text
n8n generates beautiful text files,
but the files are not actually connected into a traceable LOGOS chain.
```

FOUNDATION-I exists to prevent that.

The goal is not to add more content.

The goal is to make LOGOS trustworthy as an engine.

---

## Core Problem

The current validator checks:

```text
required files
YAML parsing
minimal fields
basic workflow sections
```

This is useful but not enough.

It does not deeply check reference integrity.

For PILOT-0001, this means disconnected artifacts may pass validation.

Example risks:

```text
Belief Shift references a missing Human Contradiction.
Meaning Atom has no source Belief Shift.
Experiment has no source script or meaning object.
Learning has no source experiment.
Law Review has no source learning.
Raw Meaning is lost after the first step.
```

---

## Desired Result

After this stage:

```text
A successful PILOT-0001 run cannot be fake-successful.
```

If n8n creates disconnected artifacts, the validator should catch the problem.

If the chain is traceable, validator should pass.

---

## Advantages

### 1. Protects against beautiful disconnected text

LOGOS should not become a folder of unrelated impressive documents.

Each object must belong to a chain.

### 2. Makes the system more engine-like

The system moves from file presence validation to relationship validation.

This is a major step from documentation to machinery.

### 3. Gives Codex a concrete engineering task

This stage is not philosophical.

It is a clear implementation layer:

```text
ID registry
reference validation
direct script execution fix
fixtures
tests
progress note
issue update
```

### 4. Improves readiness for n8n

n8n can generate many files quickly.

The validator must be ready before that generation starts.

---

## Tradeoffs and Risks

### Risk 1 — Overengineering

Codex must not build a heavy graph database, ORM or full ontology reasoner yet.

This stage should be simple and readable.

### Risk 2 — Over-strict validation

The validator must not break the current repository because older files are not fully migrated.

Strict checks should apply only to declared references and clear LOGOS objects.

### Risk 3 — Meaning edits

Codex must not rewrite conceptual content.

This task is about integrity checks, not improving meanings.

### Risk 4 — DeflaGyn runtime noise

Existing DeflaGyn files should not be aggressively refactored.

Only minimal safe fixes are allowed if validation requires them.

---

## Implementation Task For Codex

```text
Implement FOUNDATION-I: Reference Integrity Layer for LOGOS Engine.

Context:
LOGOS Engine foundation is already built. The next step is not to generate more content, but to make the system trustworthy before running PILOT-0001 in n8n.

Current problem:
The validator checks required files, YAML parsing and minimal fields, but it does not deeply validate reference integrity between LOGOS objects. This creates a risk that n8n will generate beautiful artifacts that are not actually connected.

Goal:
Strengthen validation so LOGOS can detect broken chains before we trust a system run.

Important principle:
Do not rewrite conceptual content unless needed for test fixtures or validator compatibility.
Do not change author meaning.
Do not touch DeflaGyn content unless validation requires a safe minimal fix.
Prefer small, readable, incremental changes.
```

---

## Required Outcomes

```text
1. Direct local script execution works.
2. Validator builds a repository-wide object ID registry.
3. Validator detects duplicate IDs.
4. Validator detects broken references where references are declared.
5. Validator supports PILOT-0001 artifacts.
6. Validator remains backward-compatible with existing foundation files.
7. Tests or dry-run reports prove the new checks work.
8. GitHub Action still passes.
```

---

## Task 1 — Fix Direct Local Validation Script

Problem:

```text
python -m logos_engine.validate .
```

works, but:

```text
python scripts/validate_catalog.py .
```

may fail without prior:

```text
pip install -e .
```

because `logos_engine` may not be on `sys.path`.

Implement a robust fix inside:

```text
scripts/validate_catalog.py
```

Recommended approach:

```python
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
```

Do not remove package mode.

Both commands must work:

```text
python -m logos_engine.validate .
python scripts/validate_catalog.py .
```

Acceptance criteria:

```text
Both commands run and return LOGOS validation passed on current repo.
```

---

## Task 2 — Add Object ID Registry

Extend:

```text
logos_engine/validate.py
```

Add a function that scans YAML files and collects LOGOS object IDs.

Target files:

```text
*.yaml
*.yml
```

Ignore:

```text
.git
.venv
node_modules
__pycache__
```

Registry entry should include:

```text
id
type
path
status
raw data
```

Only treat a YAML as a LOGOS object if it has at least:

```text
id
type
```

Do not treat every config YAML as a LOGOS object.

Expected internal shape:

```python
{
  "HT-0001": {
    "type": "human_truth",
    "path": "clients/...",
    "status": "draft",
    "data": {...}
  }
}
```

Acceptance criteria:

```text
Registry can be built without errors.
Duplicate IDs are detected and reported with both file paths.
```

---

## Task 3 — Reference Integrity Validation

Add reference validation where references are explicitly declared.

Do not invent required references for old files that do not have reference fields yet.

Support common reference fields:

```text
source_id
source_ids
source_experiment
source_learning
source_issue
source_raw_meaning_id
human_truth_id
human_contradiction_id
belief_shift_id
meaning_atom_id
meaning_atom_ids
story_pattern_id
script_id
experiment_id
learning_id
law_candidate_id
trace_to_previous
linked_objects
references
```

Rules:

```text
If a field contains a value that looks like a LOGOS ID, validator checks whether that ID exists in the registry.
If a reference is numeric issue number or URL, do not validate it as object ID.
If a reference is empty, ignore it.
If a reference points to a file path, check that the path exists.
```

LOGOS ID detection should be conservative.

Suggested prefixes:

```text
HT-
HC-
BS-
MA-
SP-
SCRIPT-
EXP-
LEARN-
LAW-
RM-
ME-
PILOT-
```

Acceptance criteria:

```text
Broken object reference produces ERROR.
Existing object reference passes.
File path reference passes only if file exists.
```

Important:

```text
Do not make old markdown catalog references fail unless they are in YAML fields intended as references.
```

---

## Task 4 — PILOT-0001 Compatibility

The upcoming n8n run will create files under:

```text
pilots/PILOT-0001/input/
pilots/PILOT-0001/output/
```

Validator should support objects there.

Expected pilot artifacts:

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

Add validator expectations only when these files exist.

Do not fail because PILOT-0001 artifacts are not created yet.

When they exist, validate:

```text
raw-meaning.yaml has id, type, pilot_id, raw_text
meaning-edges.yaml has id, type, pilot_id, source_raw_meaning_id or raw_text
human-truth.yaml has id, type, status, pilot_id
human-contradiction.yaml has id, type, status, pilot_id
belief-shift.yaml has id, type, status, pilot_id
experiment-plan.yaml has id, type, status, pilot_id
```

Acceptance criteria:

```text
Validator passes now before pilot artifacts exist.
Validator can validate pilot artifacts after they are created.
```

---

## Task 5 — Add Structured Reference Test Fixtures

Create safe test fixtures under:

```text
testing/fixtures/reference-integrity/
```

Suggested files:

```text
valid-chain.yaml
broken-reference.yaml.example
duplicate-id-a.yaml.example
duplicate-id-b.yaml.example
```

Important:

Use `.example` for intentionally broken fixtures so current validator does not fail on them by default.

Add a manual test doc:

```text
testing/manual/TEST-FOUNDATION-I.md
```

It should explain:

```text
1. How to run validator normally.
2. How to temporarily copy or rename broken fixtures to test error detection.
3. Expected error messages.
4. How to remove test broken files after testing.
```

Acceptance criteria:

```text
Normal validation passes.
Manual test instructions exist.
Broken examples are documented but do not break default validation.
```

---

## Task 6 — Add Foundation-I Progress Note

Create:

```text
foundation/FOUNDATION-PROGRESS-2026-07-02-reference-integrity.md
```

Include:

```text
Purpose
Files changed
Validator capabilities added
Tests performed
Known limits
Next step: PILOT-0001 n8n runtime
```

Known limits should honestly say:

```text
The validator is still not a full ontology reasoner.
It validates declared references, not implicit meaning quality.
It does not judge whether a belief shift is philosophically strong.
```

---

## Task 7 — Create GitHub Issue

Create a GitHub issue:

```text
FOUNDATION-I: Reference Integrity Layer
```

Body should include:

```text
Purpose
Tasks
Files changed
Acceptance criteria
Test evidence
Relation to PILOT-0001 #27
```

After implementation, update it with:

```text
Status: Done
Validation commands run
Result
Known limits
Next action
```

Close only if validation passes.

---

## Task 8 — Run Validation

Run locally:

```text
python scripts/validate_catalog.py .
python -m logos_engine.validate .
```

Expected:

```text
LOGOS validation passed.
```

If validation fails, fix actual issues or explain why the validator is too strict and adjust.

Then GitHub Actions should also pass.

---

## Strict Non-Goals

```text
Do not build n8n workflow yet.
Do not create PILOT-0001 generated meaning artifacts yet.
Do not rewrite the raw meaning.
Do not improve DeflaGyn content.
Do not convert the whole repository into a database.
Do not add heavy dependencies unless absolutely necessary.
Do not make validator so strict that the existing repository fails because older files are not fully migrated.
```

---

## Definition of Done

```text
1. Direct script run works.
2. Package module run works.
3. Validator detects duplicate IDs.
4. Validator detects broken declared references.
5. Validator supports future PILOT-0001 artifacts.
6. Normal repository validation passes.
7. Manual reference integrity test doc exists.
8. Foundation-I progress note exists.
9. GitHub issue is updated with evidence.
10. Repository remains clean and ready for n8n PILOT-0001 implementation.
```

---

## Message Between The Lines

The real goal:

```text
After this task, a successful PILOT-0001 run cannot be fake-successful.
```

This layer protects LOGOS from becoming a folder of beautiful unrelated texts.

LOGOS must remain an engine where every meaning object has a place in the chain.
