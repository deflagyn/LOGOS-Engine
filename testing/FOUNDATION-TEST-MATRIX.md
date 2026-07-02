# Foundation Test Matrix

This matrix defines how we test each foundation group.

---

## Group A — Language and Identity

Status: done

Test:

- every core term has a definition;
- every object type has an ID convention;
- axioms describe how LOGOS thinks.

Evidence:

- `ontology/GLOSSARY.md`
- `ontology/ID-CONVENTIONS.md`
- `constitution/AXIOM-INDEX.md`
- issue `#11`

---

## Group B — Ontology and Relationships

Status: done

Test:

- object chain is clear;
- lifecycle statuses are defined;
- universal and runtime boundaries are separated.

Evidence:

- `ontology/RELATIONSHIPS.md`
- `ontology/OBJECT-LIFECYCLE.md`
- `ontology/UNIVERSAL-VS-RUNTIME.md`
- issue `#12`

---

## Group C — Initial Schemas

Status: done

Test:

- core object schemas exist;
- each schema defines required fields;
- schemas can later support validation automation.

Evidence:

- `schemas/README.md`
- core schema files
- issue `#13`

---

## Group D — Validation Discipline

Status: done

Test:

- validation plan exists;
- catalog rules exist;
- quality gates exist.

Evidence:

- `validation/VALIDATION-PLAN.md`
- `validation/CATALOG-RULES.md`
- `validation/QUALITY-GATES.md`
- issue `#14`

---

## Group E — Operations Layer

Status: next

Test:

- issue templates can create structured issues;
- scoring model can compare experiments;
- weekly learning template can convert metrics into learning.

Expected evidence:

- issue `#15`
- created templates
- one manual test issue created from a template

---

## Group F — Automation Runtime Design

Status: in progress

Test:

- every workflow has input, output and test plan;
- n8n remains runtime layer;
- GitHub remains source of truth.
- WF-0001 can create a structured GitHub issue through n8n.

Expected evidence:

- issue `#16`
- workflow design files
- at least one dry-run workflow description
- `automation/n8n/wf-0001/IDEA-INTAKE-ISSUE-GATE.md`
- `automation/n8n/wf-0001/writeback/idea-intake-issue-gate-test-2026-07-02.md`
- issue `#29`

---

## Group G — Developer Validation Layer

Status: backlog

Test:

- validation script runs locally;
- validation GitHub Action runs in CI;
- duplicate IDs and missing fields are detected.

Expected evidence:

- issue `#17`
- workflow run
- validation report

---

## Group H — Learning and Laws

Status: backlog

Test:

- learning model exists;
- metric signal map exists;
- evidence criteria exist;
- a Law Candidate cannot become a Law without evidence.

Expected evidence:

- issue `#18`
- learning model files
- one sample learning note

---

## Final Test Rule

Every future module gets its own test block before it is considered complete.
