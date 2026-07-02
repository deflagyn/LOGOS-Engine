# CODEX PROJECT BRIEF — LOGOS Engine

This document explains the logic, philosophy, architecture and working rules of LOGOS Engine for Codex and other coding agents.

It is intentionally detailed.

Use it to understand what this repository is, what it is not, how to work inside it, and how to avoid damaging the core idea.

---

## 1. One-Sentence Definition

LOGOS Engine is a universal system for discovering, structuring, testing and evolving meaning through traceable belief shifts.

---

## 2. What LOGOS Is Not

LOGOS is not a normal marketing repository.

LOGOS is not a slogan generator.

LOGOS is not a campaign folder.

LOGOS is not a content factory.

LOGOS is not tied to one product.

LOGOS is not DeflaGyn.

DeflaGyn is only the first reference runtime.

The engine must remain universal.

---

## 3. The Core Mission

The mission is:

```text
Build a universal meaning engine, not a one-product marketing folder.
```

The system should help transform raw human observations into structured, testable meaning systems.

The central result is not a post, script, video or ad.

The central result is a structured change in belief.

---

## 4. The Core Formula

The full LOGOS chain is:

```text
Human Truth
→ Human Contradiction
→ Belief Shift
→ Meaning Atom
→ Story Pattern
→ Emotional Result
→ Content
→ Experiment
→ Learning
→ Law
```

This chain is the backbone of the repository.

Most serious outputs should be traceable backward through this chain.

If a piece of content cannot explain which belief shift it carries, it is not mature LOGOS output.

---

## 5. The Most Important Operating Law

```text
LOGOS does not create content.
LOGOS creates structured belief change.
Content is only the runtime expression of that change.
```

This rule should guide all work in the repository.

When in doubt, do not ask:

```text
What content should we make?
```

Ask:

```text
What human truth are we revealing?
What contradiction are we resolving?
What belief shift are we moving?
What meaning atom carries that shift?
How will we test whether it worked?
```

---

## 6. Philosophical Foundation

LOGOS assumes that people rarely change behavior from information alone.

Information becomes powerful when it becomes meaning.

Meaning becomes behavior when it resolves a contradiction inside identity, fear, desire, dignity, belonging or responsibility.

The system therefore starts from human truth, not product claims.

Good LOGOS work reveals something the audience already recognizes but has not yet organized into a clear belief.

---

## 7. LOGOS and Meaning TRIZ

LOGOS is inspired by the logic of TRIZ.

Classical TRIZ resolves contradictions in technical systems.

LOGOS resolves contradictions in meaning systems.

A technical contradiction might be:

```text
The part must be stronger, but also lighter.
```

A LOGOS contradiction might be:

```text
The person believes they care for themselves, but their behavior shows an ignored area.
```

This is why Human Contradiction is a core object.

The goal is not to attack the person.

The goal is to help the person reach a more coherent self-understanding.

---

## 8. Ideal Meaning Result

The ideal meaning result is:

```text
The person arrives at the intended belief as if it were their own discovery.
```

This is why LOGOS prefers:

- simple images;
- familiar situations;
- gentle contradictions;
- identity expansion;
- emotional recognition;
- respect instead of pressure.

A strong meaning atom should feel obvious after it is heard.

---

## 9. The Product Is Not the Hero

In LOGOS, the product is not the hero.

The human transformation is the hero.

The product may support the transformation, but it should not replace the meaning.

If an idea collapses when the product is removed, it is advertising, not meaning.

This rule is crucial for all runtime work.

---

## 10. Runtime vs Universal Engine

A runtime is a concrete application of LOGOS.

Examples:

```text
client
product
movement
service
educational project
brand
```

The first reference runtime is DeflaGyn.

However:

```text
A runtime can teach the engine.
A runtime must not trap the engine.
```

Universal files live in:

```text
constitution/
ontology/
engine/
triz/
laws/
patterns/
schemas/
validation/
testing/
automation/
```

Runtime files live in:

```text
clients/<client>/
```

Do not move a runtime-specific insight into universal LOGOS unless it has a strong reason or evidence.

---

## 11. Foundation-First Decision

The project made an explicit architecture decision:

```text
Build the universal LOGOS foundation first.
Return to DeflaGyn only after the foundation gate is strong enough.
```

See:

```text
decisions/ADR-0001-foundation-first.md
```

This decision protects the project from becoming a narrow campaign archive.

Codex should respect this decision.

Do not start producing DeflaGyn runtime content unless a human explicitly changes the current project priority.

---

## 12. Core Object Types

### Observation

A raw noticing before formalization.

It may be messy and incomplete.

It is not yet a strategy.

---

### Human Truth

A stable observation about human behavior, fear, desire, identity or contradiction.

A Human Truth should feel recognizable.

Example:

```text
People give more attention to what they see every day.
```

---

### Human Contradiction

A tension between what a person believes about themselves and how they act.

Example:

```text
I believe I care for myself, but I ignore parts of myself that are not visible.
```

This is the LOGOS analogue of a TRIZ contradiction.

---

### Belief Shift

The central operational unit of LOGOS.

Format:

```text
Old frame → New frame
```

Example:

```text
Self-care is mainly visible care → True self-care does not end at the surface
```

---

### Meaning Atom

A compact phrase or idea that carries a Belief Shift.

A Meaning Atom is not just a slogan.

It is compressed belief movement.

---

### Story Pattern

A reusable narrative structure that delivers a Meaning Atom.

It is not the final script.

It is the reusable skeleton behind many scripts.

---

### Emotional Result

The emotional state that the audience should experience after the meaning movement.

Examples:

```text
calm recognition
relief
dignity
self-respect
responsibility without panic
```

---

### Script

A platform-specific expression of LOGOS objects.

A script must link back to the objects that generated it.

---

### Experiment

A real-world test of a Human Truth, Belief Shift, Meaning Atom, Story Pattern or script.

An experiment must produce learning.

Views alone are not learning.

---

### Learning

A structured conclusion from an experiment.

Learning explains:

```text
what happened
why it may have happened
what should change next
whether a Law Candidate is justified
```

---

### Law Candidate

A repeated pattern that may become a LOGOS Law.

It is not yet a law.

---

### LOGOS Law

A validated principle that improves future LOGOS decisions.

No idea becomes a law because it sounds beautiful.

A law requires repeated evidence.

---

## 13. IDs and Traceability

Every meaningful object should have a stable ID.

Examples:

```text
HT-0001
HC-0001
BS-0001
MA-0001
SP-0001
SCRIPT-0001
EXP-0001
LEARN-0001
LC-0001
LAW-0001
```

IDs are stable.

Titles may change.

Relationships should reference IDs, not only titles.

A mature output should answer:

```text
Which Human Truth does this come from?
Which Human Contradiction does it resolve?
Which Belief Shift does it move?
Which Meaning Atom does it carry?
Which Story Pattern does it use?
Which Experiment tested it?
What did we learn?
```

---

## 14. Repository Structure

Important folders:

```text
constitution/       foundational principles and axioms
ontology/           object definitions and relationships
schemas/            machine-readable object schemas
engine/             engine flow and operating logic
triz/               meaning TRIZ concepts
patterns/           story patterns
laws/               laws and law candidates
learning/           future learning system
validation/         quality and catalog rules
testing/            test-first governance and test evidence
automation/         n8n workflow design and GitHub automation
foundation/         progress notes for foundation work
projects/           GitHub Project management docs
audits/             audits and state reviews
clients/            runtime-specific implementations
logos_engine/       Python validation package
scripts/            developer scripts
.github/            workflows and issue templates
```

---

## 15. GitHub / n8n / VPS Model

The working model is:

```text
GitHub = brain / source of truth
GitHub Issues = active work items
GitHub Project = operational board
n8n = nervous system / execution layer
VPS = body / runtime environment
```

n8n should not become the source of truth.

n8n should execute workflows and write results back to GitHub.

---

## 16. Test-First Rule

Every new module, workflow, schema or stage must include a test plan.

A module is not complete only because a file exists.

It is complete when we can check that it works as intended.

Every module should define:

```text
Purpose
Input
Output
Acceptance criteria
Manual test
Evidence
Future automation
```

See:

```text
testing/TEST-FIRST-GOVERNANCE.md
testing/MODULE-TEST-TEMPLATE.md
testing/FOUNDATION-TEST-MATRIX.md
```

---

## 17. Validation Layer

The repository contains a Python validation layer.

Run:

```bash
python -m pip install -e .
python scripts/validate_catalog.py .
```

The validator currently checks:

```text
required foundation files
core schema files
YAML parsing
object YAML required fields
workflow document sections
test-first governance files
```

The validation layer is still early.

Do not remove checks to make validation pass.

Fix the underlying structure unless the check is clearly wrong.

---

## 18. Automation Workflow Design

The current workflow set is:

```text
WF-0001 Idea Intake
WF-0002 Belief Movement Generator
WF-0003 Script Generator
WF-0004 Review Checker
WF-0005 Metrics Collector
WF-0006 Weekly Learning Report
```

The first real implementation should be:

```text
WF-0001 Idea Intake
```

Expected first real workflow:

```text
Telegram or webhook input
→ normalize input
→ create structured GitHub issue
→ return issue URL
```

Acceptance:

```text
One real idea becomes one GitHub issue automatically.
```

---

## 19. Experiment Scoring

Experiments are scored using five blocks:

```text
Attention
Retention
Action
Meaning Signal
Learning Quality
```

Each block is scored from 0 to 20.

Total score is 0 to 100.

This prevents the system from treating views as proof.

Meaning signal and learning quality matter.

---

## 20. Learning and Laws

Learning and Laws are not fully implemented yet.

This is one of the most important remaining parts.

The rule is:

```text
No law without repeated evidence.
```

A beautiful idea is not a law.

A viral result is not a law.

A repeated evidence-supported pattern may become a Law Candidate.

A Law Candidate may become a LOGOS Law only after review.

---

## 21. Current State

Implemented:

```text
foundation-first decision
language and identity layer
ontology and relationship layer
initial schemas
validation discipline
test-first governance
operations layer
automation design layer
developer validation layer
implementation audit
Codex onboarding docs
```

Still pending:

```text
first real validation run
issue template UI quality pass
real n8n WF-0001 implementation
Learning and Laws foundation
universal object seed library
runtime normalization
```

---

## 22. How Codex Should Work In This Repo

Before editing, inspect:

```text
AGENTS.md
docs/CODEX-PROJECT-BRIEF.md
audits/AUDIT-2026-07-02-chat-to-github.md
roadmap/FOUNDATION-TASK-GROUPS.md
```

When implementing a task:

1. Identify the related Foundation group or issue.
2. Preserve the universal engine logic.
3. Add or update tests.
4. Run validation if code or YAML changed.
5. Update progress notes if the change is meaningful.
6. Do not silently change philosophy.
7. Do not promote runtime-specific material to universal without reason.

---

## 23. Preferred Codex Task Types

Good Codex tasks:

```text
Run validator and fix reported structural errors.
Improve issue templates without changing meaning.
Add missing schema fields with tests.
Implement WF-0001 n8n design files.
Create sample universal objects.
Add Learning and Laws model docs.
Improve Python validator.
Add relationship validation.
Create GitHub Action improvements.
```

Bad Codex tasks:

```text
Generate marketing content immediately.
Rewrite philosophy into generic brand language.
Delete documentation because it looks verbose.
Move DeflaGyn-specific ideas into universal folders without review.
Remove validation checks to avoid fixing structure.
Create laws without evidence.
```

---

## 24. Quality Bar

A change is good when it improves at least one of:

```text
clarity
traceability
testability
automation readiness
universal reusability
learning quality
validation strength
```

A change is bad when it increases:

```text
conceptual confusion
runtime lock-in
untracked content
untestable claims
duplicate objects
source-of-truth drift
```

---

## 25. Immediate Roadmap For Codex

### Step 1 — Run validation

```bash
python -m pip install -e .
python scripts/validate_catalog.py .
```

Fix output.

Record result in:

```text
#22 TEST-0004
```

---

### Step 2 — Improve issue templates

Improve:

```text
.github/ISSUE_TEMPLATE/belief-shift.yaml
.github/ISSUE_TEMPLATE/script.yaml
```

Add:

```text
.github/ISSUE_TEMPLATE/human-contradiction.yaml
.github/ISSUE_TEMPLATE/meaning-atom.yaml
.github/ISSUE_TEMPLATE/learning.yaml
.github/ISSUE_TEMPLATE/law-candidate.yaml
```

---

### Step 3 — Build Foundation H

Create:

```text
laws/EVIDENCE-CRITERIA.md
learning/LEARNING-MODEL.md
learning/METRIC-SIGNAL-MAP.md
learning/LAW-CANDIDATE-REVIEW.md
```

---

### Step 4 — Seed universal objects

Create a small universal object library:

```text
3 Human Truths
3 Human Contradictions
3 Belief Shifts
3 Meaning Atoms
3 Story Patterns
```

Do not use DeflaGyn as the only source.

---

### Step 5 — Implement first real n8n workflow

Implement or document implementation details for:

```text
WF-0001 Idea Intake
```

End-to-end proof:

```text
Raw idea → GitHub issue URL
```

---

## 26. Final Instruction

Protect the mission.

LOGOS is a system for structured meaning evolution.

Every file, test, schema, workflow and issue should make the system more traceable, testable and useful.

If a task does not support that, do not do it without asking for direction.
