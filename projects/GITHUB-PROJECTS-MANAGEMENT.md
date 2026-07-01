# GitHub Projects Management for LOGOS Engine

This document defines how GitHub Projects should be used inside LOGOS Engine.

GitHub Projects is not the source of truth.

The repository files are the source of truth.

Projects are the operational layer that shows movement, status and accountability.

---

## 1. Role of GitHub Projects

Use GitHub Projects as a live operational board for ideas, experiments, scripts, metrics and learning cycles.

Do not use it as the main knowledge base.

```text
Repository files = truth / memory
Issues = active work items
Project = workflow visibility
n8n = automation runtime
```

---

## 2. Recommended Project

Project name:

```text
LOGOS Engine Roadmap
```

Recommended layout:

```text
Board + Table views
```

The board view should show the current stage of each idea.

The table view should show metadata: type, client, phase, language, confidence and score.

---

## 3. Main Pipeline

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

This pipeline mirrors the canonical LOGOS flow:

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

---

## 4. Recommended Fields

### Type

Single select:

- Human Truth
- Human Contradiction
- Belief Shift
- Meaning Atom
- Story Pattern
- Script
- Experiment
- Learning
- Law Candidate
- LOGOS Law
- Infrastructure
- Automation
- Documentation

### Client

Single select:

- Universal
- DeflaGyn
- Future Client

### Language

Single select:

- uk
- ru
- en
- mixed

### Phase

Single select:

- P00 Foundation
- P01 Ontology and Schemas
- P02 DeflaGyn Runtime
- P03 Experiment Ops
- P04 n8n Runtime
- P05 Validation CLI
- P06 Search Engine
- P07 Graph Engine
- P08 Generative Agent
- P09 Learning Engine
- P10 Multi-Client Runtime

### Confidence

Single select:

- Low
- Medium
- High

### Metric Score

Number field, 0–100.

### Target Date

Date field.

### Iteration

Iteration field for weekly experiment cycles.

---

## 5. Recommended Views

### Pipeline View

Board layout grouped by Status.

Purpose:

> See where every idea is in the LOGOS pipeline.

---

### Experiments View

Table layout filtered by Type = Experiment.

Purpose:

> Manage active content experiments.

---

### DeflaGyn Runtime View

Table layout filtered by Client = DeflaGyn.

Purpose:

> Track all DeflaGyn-specific implementation work.

---

### Law Candidates View

Table layout filtered by Status = Law Candidate.

Purpose:

> Review ideas that may become LOGOS Laws after repeated evidence.

---

### Weekly Iteration View

Table or board grouped by Iteration.

Purpose:

> Manage week-by-week publishing and testing cycles.

---

## 6. Issue Naming Rules

```text
HT-0000: Short title
HC-0000: Short title
BS-0000: Short title
MA-0000: Short title
SCRIPT-0000: Short title
EXP-0000: Short title
LEARN-0000: Short title
LC-0000: Short title
LAW-0000: Short title
```

Examples:

```text
HT-0001: Visible care vs invisible health
BS-0001: True self-care does not end at the surface
SCRIPT-0001: Справжня турбота не закінчується на поверхні
EXP-0001: True self-care does not end at the surface
```

---

## 7. Project README / Description

The GitHub Project should have this description:

```text
LOGOS Engine Roadmap tracks the evolution of ideas from raw human truth to tested belief shift, content experiment, learning and LOGOS Law.

Repository files are the source of truth. This project board is the operational layer.
```

---

## 8. Built-in Automations to Enable

Recommended automations:

1. When an issue is added to the project → Status = Inbox.
2. When an issue is closed → Status = Done / Archived.
3. When an issue with label `experiment` is added → Type = Experiment.
4. When an issue with label `script` is added → Type = Script.
5. When an issue with label `law-candidate` is added → Status = Law Candidate.
6. Auto-archive closed items after a defined period, if no longer needed in active views.

Later n8n can extend this with custom GitHub automation.

---

## 9. Single Source of Truth Rule

Only one place should own each kind of information.

- Full object definitions live in repository files.
- Current workflow status lives in GitHub Projects.
- Discussion lives in Issues.
- Metrics may start in Issues or Google Sheets, then move into experiment YAML.
- Final validated knowledge moves into repository files.

Avoid duplicating full truth across multiple places.

---

## 10. First Manual Setup Steps

1. Open GitHub profile or repository projects.
2. Create a new Project named `LOGOS Engine Roadmap`.
3. Choose Board or Table as the starting layout.
4. Add the custom fields from this document.
5. Create the Pipeline board view.
6. Create the Experiments table view.
7. Create the DeflaGyn Runtime view.
8. Add the master issue `ROADMAP-0001`.
9. Add open issues HT-0001, BS-0001, SCRIPT-0001, EXP-0001.
10. Start moving items through the pipeline after each real action.

---

## 11. LOGOS Rule

A Project item is not just a task.

A Project item is a hypothesis about human meaning moving through reality.

If it receives evidence, it evolves.

If it fails, it teaches.

If it repeats successfully, it may become a LOGOS Law.
