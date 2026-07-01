# LOGOS Validation Plan

This document defines how LOGOS objects should be checked before they become part of the working catalog.

The goal is simple:

> Keep LOGOS structured, traceable and useful.

---

## Validation Layers

Every important object should pass four layers.

```text
Structure
→ Traceability
→ Meaning Quality
→ Runtime Safety
```

---

## 1. Structure Check

The object must have required fields.

Minimum fields:

- id;
- type;
- status;
- language;
- title;
- client or universal scope;
- notes or explanation.

For specialized objects, extra fields are required.

Example:

A Belief Shift must have:

- old belief;
- new belief;
- emotional result;
- connected Human Truth or Human Contradiction.

---

## 2. Traceability Check

Every mature object should connect backward and forward.

A script should connect to:

- Belief Shift;
- Meaning Atom;
- Story Pattern;
- Experiment.

A Learning should connect to:

- Experiment;
- metrics;
- decision;
- possible Law Candidate.

---

## 3. Meaning Quality Check

The object should answer:

- Is this a real human truth or only a marketing claim?
- Is there a clear contradiction?
- Is the belief shift understandable?
- Can the meaning atom survive without a product?
- Is the emotional result clear?
- Does it respect the person?

---

## 4. Runtime Safety Check

Client-specific objects must follow client safety rules.

For healthcare runtimes, unsupported medical claims must be avoided.

For financial runtimes, unsupported financial promises must be avoided.

For social or civic runtimes, harmful escalation should be avoided.

---

## Validation Statuses

```text
not_checked
needs_revision
valid_for_draft
valid_for_testing
valid_for_runtime
rejected
```

---

## Manual Validation First

At the foundation stage, validation may be manual.

Later, validation should become automatic through schemas and scripts.

---

## Future Automation

Planned validation automation:

- schema validation;
- missing relationship detection;
- duplicate ID detection;
- status consistency checks;
- client safety checklist;
- experiment completeness check.

---

## Final Rule

If an object cannot be traced, tested or reused, it is not yet a mature LOGOS object.
