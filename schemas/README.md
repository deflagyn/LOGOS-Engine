# LOGOS Schemas

This folder contains machine-readable schemas for LOGOS objects.

Schemas are used to keep the catalog structured and prepare the system for future validation automation.

---

## Current Schemas

- `logos-object.schema.yaml` — general object schema
- `human-truth.schema.yaml`
- `human-contradiction.schema.yaml`
- `belief-shift.schema.yaml`
- `meaning-atom.schema.yaml`
- `story-pattern.schema.yaml`
- `experiment.schema.yaml`
- `pilot-response-input.schema.yaml` — intake JSON contract for PILOT-0001 real responses
- `wf-0001-idea-intake.schema.yaml` — intake JSON contract for WF-0001 GitHub issue creation
- `product-profile.schema.yaml`

---

## Purpose

Schemas help ensure that every LOGOS object has:

- stable ID;
- object type;
- status;
- language;
- title;
- required meaning fields;
- connected objects where relevant.

---

## Future Work

Planned next steps:

- add Pydantic models;
- add validation script;
- add GitHub Action validation;
- add object creation helpers;
- add duplicate ID detection;
- add relationship validation.

---

## Rule

Human-readable meaning remains primary.

Machine-readable structure protects scale.
