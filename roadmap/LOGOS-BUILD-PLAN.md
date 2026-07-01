# LOGOS Engine Build Plan

This document is the human-readable roadmap for building LOGOS Engine.

The machine-readable version is stored in:

```text
roadmap/LOGOS-BUILD-PLAN.okf.yaml
```

---

## Mission

Build LOGOS Engine as a reusable meaning operating system.

The system should transform:

```text
Human Truth
→ Human Contradiction
→ Belief Shift
→ Meaning Atom
→ Story Pattern
→ Script
→ Experiment
→ Learning
→ Law
```

The goal is not to collect marketing ideas.

The goal is to build a structured system that discovers, tests and evolves meaning.

---

## Architectural Rule

LOGOS must stay universal.

DeflaGyn is the first reference runtime, not the whole system.

```text
LOGOS Engine
    ↓
Reference Runtime: DeflaGyn
    ↓
Ukrainian educational content experiments
```

---

## Phase P00 — Foundation / Philosophy

### Goal

Define what LOGOS is, why it exists and what it must never become.

### Key deliverables

- `README.md`
- `catalog.okf.yaml`
- `constitution/LOGOS-CONSTITUTION.md`
- `ontology/OBJECTS.md`
- `engine/ENGINE-FLOW.md`
- `triz/MEANING-TRIZ.md`

### Done when

- LOGOS has a clear definition.
- Core axioms are written.
- Product-first marketing is rejected.
- Belief Shift is defined as the central object.
- TRIZ adaptation is documented.

---

## Phase P01 — Ontology / Object Model / Schemas

### Goal

Turn LOGOS into a structured language.

### Deliverables

- strict object definitions;
- ID conventions;
- object relationships;
- separate schemas for each object type;
- validation rules.

### Objects to formalize

- Human Truth
- Human Contradiction
- Belief Shift
- Meaning Atom
- Story Pattern
- Emotional Result
- Identity Shift
- Habit
- Product Profile
- Experiment
- Learning
- Law Candidate
- LOGOS Law

---

## Phase P02 — DeflaGyn Reference Runtime

### Goal

Use DeflaGyn as the first real-world testbed.

### Current core belief shift

```text
Old belief:
Турбота про себе — це переважно те, що видно іншим.

New belief:
Справжня турбота про себе не закінчується на поверхні.
```

### Deliverables

- DeflaGyn product profile;
- forbidden claims;
- Ukrainian avatar scripts;
- podcast-style visual prompts;
- first experiment pack;
- first 10–20 videos;
- metrics and learnings.

---

## Phase P03 — Experiment Operations / GitHub Project Layer

### Goal

Make the movement of ideas visible.

### Recommended GitHub Project

Name:

```text
LOGOS Engine Roadmap
```

Columns:

```text
Inbox
→ Human Truth
→ Human Contradiction
→ Belief Shift
→ Meaning Atom
→ Script Ready
→ In Production
→ Published
→ Metrics Collected
→ Learning
→ Law Candidate
→ LOGOS Law
```

### Purpose

The repository stores knowledge.

GitHub Project tracks movement.

Issues represent active hypotheses, scripts, experiments and law candidates.

---

## Phase P04 — n8n Runtime MVP

### Goal

Use n8n on VPS as the first automation layer.

### Workflows

1. Idea Intake
2. Belief Shift Generator
3. Ukrainian Script Generator
4. Medical Claim Checker
5. Metrics Collector
6. Weekly Learning Report

### Rule

n8n is not the brain.

n8n is the nervous system.

GitHub remains the source of truth.

---

## Phase P05 — Validation / CLI / Developer Layer

### Goal

Prevent the catalog from turning into chaos.

### Deliverables

- Python package;
- Pydantic schemas;
- validation script;
- object generator;
- GitHub Action for validation;
- tests.

---

## Phase P06 — Searchable Knowledge Engine

### Goal

Make the system searchable by meaning.

### Stack candidate

- PostgreSQL
- pgvector
- FastAPI
- embedding ingestion pipeline

### Use cases

- find similar Belief Shifts;
- find scripts by emotional result;
- find experiments by story pattern;
- detect repeated successful phrases.

---

## Phase P07 — Graph Engine

### Goal

Represent LOGOS as a graph.

### Possible stack

- Neo4j
- or Postgres graph-like queries first

### Graph path

```text
Human Truth
→ Human Contradiction
→ Belief Shift
→ Meaning Atom
→ Script
→ Experiment
→ Learning
→ Law
```

---

## Phase P08 — Generative LOGOS Agent

### Goal

Build an AI workflow that can generate structured LOGOS outputs from a product profile or human problem.

### Possible stack

- LangGraph
- OpenAI / LLM layer
- validation layer
- GitHub writeback

### Expected output

- Human Truth candidates;
- Human Contradictions;
- Belief Shifts;
- Meaning Atoms;
- Ukrainian scripts;
- visual prompts;
- experiments;
- safety checks.

---

## Phase P09 — Learning Engine

### Goal

Turn metrics into knowledge.

### Logic

```text
Video published
→ metrics collected
→ qualitative signals analyzed
→ learning created
→ repeated pattern promoted to Law Candidate
→ validated Law
```

### Important metric types

- completion rate;
- average watch time;
- saves;
- shares;
- quoted phrases;
- repeated comments;
- profile clicks;
- followers.

---

## Phase P10 — Multi-Client Runtime

### Goal

Prove that LOGOS is not DeflaGyn-specific.

### Test

Apply LOGOS to a second and third category.

Possible future categories:

- healthcare product;
- IT service;
- education;
- civic movement;
- personal brand;
- social platform.

---

## Immediate Next Steps

1. Create GitHub Project: `LOGOS Engine Roadmap`.
2. Add issue templates.
3. Create the first visual variants for `SCRIPT-0001`.
4. Publish `EXP-0001`.
5. Collect first metrics.
6. Create week-01 DeflaGyn experiment pack.
7. Start designing n8n workflow: idea → belief shift → Ukrainian script → GitHub file.

---

## Strategic Reminder

LOGOS does not ask:

> What content should we make?

LOGOS asks:

> What belief must change?

Only after that do we create content.
