# LOGOS Foundation Task Groups

This document defines the grouped work required before expanding any runtime, including DeflaGyn.

The goal is to protect the original mission:

> LOGOS is not a marketing folder.  
> LOGOS is a system for discovering, structuring, testing and evolving meaning.

---

## Foundation Principle

Build the universal engine first.

A runtime client can test the engine, but it must not define the engine.

DeflaGyn remains the first reference runtime, but the foundation must be strong enough to work later for other products, services, movements and cultural systems.

---

## Group A — Language and Identity of the System

### Purpose

Create the language of LOGOS.

No system can scale if its core words are unstable.

### Files

- `ontology/GLOSSARY.md`
- `ontology/ID-CONVENTIONS.md`
- `constitution/AXIOM-INDEX.md`

### Outcome

Everyone working with LOGOS understands the same terms:

- Human Truth
- Human Contradiction
- Belief Shift
- Meaning Atom
- Story Pattern
- Experiment
- Learning
- LOGOS Law

---

## Group B — Ontology and Relationships

### Purpose

Define how LOGOS objects connect.

### Files

- `ontology/RELATIONSHIPS.md`
- `ontology/OBJECT-LIFECYCLE.md`

### Outcome

Every object has a place in the system and a clear path from raw observation to validated law.

---

## Group C — Schemas and Machine-Readable Structure

### Purpose

Make LOGOS readable by both humans and machines.

### Files

- `schemas/human-truth.schema.yaml`
- `schemas/human-contradiction.schema.yaml`
- `schemas/belief-shift.schema.yaml`
- `schemas/meaning-atom.schema.yaml`
- `schemas/story-pattern.schema.yaml`
- `schemas/experiment.schema.yaml`
- `schemas/product-profile.schema.yaml`

### Outcome

LOGOS objects can be validated automatically.

---

## Group D — Validation and Catalog Discipline

### Purpose

Prevent the repository from becoming a loose collection of notes.

### Files

- `validation/VALIDATION-PLAN.md`
- `validation/CATALOG-RULES.md`
- `validation/QUALITY-GATES.md`

### Outcome

Every object must pass structure, clarity, safety and usefulness checks.

---

## Group E — Experiment Operations

### Purpose

Turn meaning into testable hypotheses.

### Files

- `.github/ISSUE_TEMPLATE/human-truth.yaml`
- `.github/ISSUE_TEMPLATE/belief-shift.yaml`
- `.github/ISSUE_TEMPLATE/experiment.yaml`
- `.github/ISSUE_TEMPLATE/script.yaml`
- `experiments/scoring-model.md`
- `experiments/weekly-learning-report-template.md`

### Outcome

Ideas move through GitHub Issues and Projects without chaos.

---

## Group F — Automation Runtime Design

### Purpose

Prepare n8n to become the first LOGOS execution layer.

### Files

- `automation/workflows/idea-intake.md`
- `automation/workflows/belief-shift-generator.md`
- `automation/workflows/script-generator.md`
- `automation/workflows/claim-checker.md`
- `automation/workflows/metrics-collector.md`
- `automation/workflows/weekly-learning-report.md`

### Outcome

n8n can move an idea through the LOGOS pipeline while GitHub remains the source of truth.

---

## Group G — Developer and Validation Layer

### Purpose

Create the first technical layer of LOGOS.

### Files

- `pyproject.toml`
- `logos_engine/schemas.py`
- `logos_engine/validate.py`
- `scripts/validate_catalog.py`
- `.github/workflows/validate-catalog.yml`

### Outcome

LOGOS becomes a maintainable system, not only a written philosophy.

---

## Group H — Learning and Laws

### Purpose

Turn repeated evidence into LOGOS Laws.

### Files

- `laws/LAW-PROMOTION-CRITERIA.md`
- `learning/LEARNING-MODEL.md`
- `learning/METRIC-SIGNAL-MAP.md`

### Outcome

No principle becomes a law without repeated evidence.

---

## Runtime Gate

Runtime expansion resumes only when Groups A–D are complete and Groups E–F have at least a working draft.

Until then, client-specific content production stays secondary.
