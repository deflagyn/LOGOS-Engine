# LOGOS ID Conventions

This document defines stable identifiers for LOGOS objects.

A LOGOS object must be easy to reference by people, GitHub Issues, Project items and future automation.

---

## Core Rule

Every meaningful object receives a stable ID.

The ID must not change when the title changes.

Titles are human-readable.

IDs are system-readable.

---

## Format

```text
PREFIX-0000
```

Examples:

```text
HT-0001
HC-0001
BS-0001
MA-0001
SP-0001
SCRIPT-0001
EXP-0001
LAW-0001
```

Use four digits at the start. If the system grows beyond 9999, extend naturally to five digits without renaming old objects.

---

## Prefixes

| Prefix | Object Type | Meaning |
|---|---|---|
| OBS | Observation | Raw noticing before formalization |
| HT | Human Truth | Stable observation about human behavior |
| HC | Human Contradiction | Tension between belief, identity and behavior |
| BS | Belief Shift | Old belief transformed into new belief |
| MA | Meaning Atom | Compact carrier of a belief shift |
| SP | Story Pattern | Reusable narrative structure |
| ER | Emotional Result | Target emotional state |
| IS | Identity Shift | New self-image that supports behavior |
| HAB | Habit | Repeated behavior after belief shift |
| PP | Product Profile | Product or runtime configuration |
| SCRIPT | Script | Platform-specific script |
| VP | Visual Prompt | Visual generation prompt |
| EXP | Experiment | Real-world test |
| LEARN | Learning | Interpretation from an experiment |
| LC | Law Candidate | Repeated pattern not yet validated as law |
| LAW | LOGOS Law | Validated principle |
| ADR | Architecture Decision Record | Strategic decision |
| WF | Workflow | Automation or process workflow |
| SCHEMA | Schema | Machine-readable object schema |

---

## File Naming

File names should include both ID and short slug.

```text
<ID>-<short-slug>.yaml
<ID>-<short-slug>.md
```

Examples:

```text
HT-0001-visible-care-invisible-health.yaml
BS-0001-care-not-surface.yaml
SCRIPT-0001-care-not-surface.md
EXP-0001-care-not-surface.okf.yaml
```

Rules:

- use lowercase slugs;
- use hyphens, not spaces;
- keep slugs short;
- do not rename files only because the wording improved.

---

## Issue Naming

GitHub Issues should follow:

```text
<ID>: Short title
```

Examples:

```text
HT-0001: Visible care vs invisible health
BS-0001: True self-care does not end at the surface
EXP-0001: True self-care does not end at the surface
ROADMAP-0001: Build LOGOS Engine phased system plan
```

---

## Relationship References

Inside YAML, related objects should be referenced by ID.

```yaml
connected_objects:
  human_truth: HT-0001
  human_contradiction: HC-0001
  belief_shift: BS-0001
  meaning_atom: MA-0001
  experiment: EXP-0001
```

Never use only a title as a reference. Titles change. IDs remain stable.

---

## Status Values

Recommended object statuses:

```text
raw
candidate
draft
testing
validated
rejected
archived
law_candidate
law
```

Status describes maturity, not beauty.

---

## Client-Specific Objects

Client-specific objects live inside:

```text
clients/<client>/objects/<object-type>/
```

Example:

```text
clients/deflagyn/objects/belief-shifts/BS-0001-care-not-surface.yaml
```

If an object becomes universal, it should be promoted out of the client folder into a universal folder later.

---

## Final Rule

The path and metadata carry context.

The ID carries identity.
