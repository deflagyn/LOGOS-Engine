# AGENTS.md — LOGOS Engine Instructions for Codex

This file gives coding agents the minimum context needed to work effectively in this repository.

Read this first, then read:

```text
docs/CODEX-PROJECT-BRIEF.md
roadmap/FOUNDATION-TASK-GROUPS.md
audits/AUDIT-2026-07-02-chat-to-github.md
```

---

## Project Identity

LOGOS Engine is a universal meaning-engineering system.

It is not a normal marketing repository.

It is not a single-client campaign folder.

It is a structured system for discovering, modeling, testing and improving belief shifts through meaning.

Core formula:

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

Most important rule:

```text
LOGOS does not create content.
LOGOS creates structured belief change.
Content is only the runtime expression of that change.
```

---

## Foundation-First Rule

Do not expand client-specific runtime work before the universal foundation is complete.

DeflaGyn is the first reference runtime, but it must not define the engine.

Universal engine first.

Runtime expansion later.

See:

```text
decisions/ADR-0001-foundation-first.md
ontology/UNIVERSAL-VS-RUNTIME.md
```

---

## Source of Truth

Use this hierarchy:

```text
Repository files = source of truth
GitHub Issues = active work items
GitHub Project = workflow visibility
n8n = future execution layer
```

Do not treat n8n, comments or generated scripts as final truth unless the result is written back into repository files or tracked issues.

---

## How To Work

When adding or changing a module, include:

```text
Purpose
Input
Output
Acceptance criteria
Manual test
Evidence
Future automation path
```

Every meaningful change should update at least one of:

```text
project documentation
schema
test plan
issue
progress note
```

---

## Testing Commands

Run the repository validator:

```bash
python -m pip install -e .
python scripts/validate_catalog.py .
```

GitHub Action:

```text
Actions → Validate LOGOS Catalog → Run workflow
```

If validation fails, fix the cause rather than hiding the error.

---

## Important Files

Project brief:

```text
docs/CODEX-PROJECT-BRIEF.md
```

Audit:

```text
audits/AUDIT-2026-07-02-chat-to-github.md
```

Foundation progress:

```text
foundation/
```

Ontology:

```text
ontology/
```

Schemas:

```text
schemas/
```

Testing:

```text
testing/
```

Automation design:

```text
automation/workflows/
```

Developer validation:

```text
logos_engine/
scripts/validate_catalog.py
```

---

## Do Not Do

Do not turn LOGOS into ordinary advertising copy.

Do not make the product the hero.

Do not promote runtime-specific material into universal principles without evidence.

Do not create laws from intuition.

Do not create content without traceability to LOGOS objects.

Do not remove test plans from modules.

Do not bypass validation when it reports useful problems.

---

## Current Priority

Nearest critical tasks:

```text
1. Run Validate LOGOS Catalog and record output in #22.
2. Improve weak issue templates after UI testing.
3. Implement WF-0001 Idea Intake in n8n.
4. Build Foundation H: Learning and Laws.
5. Seed universal object library.
```

---

## Tone and Philosophy

Work slowly and structurally.

Preserve the mission.

Prefer traceability over speed.

Prefer tested learning over beautiful speculation.

Prefer universal engine logic over runtime convenience.
