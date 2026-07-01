# LOGOS Catalog Rules

This document defines the rules for keeping the LOGOS repository clean and useful.

LOGOS must not become a folder of disconnected notes.

---

## 1. Source of Truth

Repository files are the source of truth.

GitHub Issues are for active work.

GitHub Projects are for workflow visibility.

n8n is for automation.

---

## 2. One Object, One File

Every mature LOGOS object should have one primary file.

Avoid spreading the same object across many files.

If an object is discussed in issues, the file remains the final structured form.

---

## 3. IDs Are Mandatory

Every mature object needs a stable ID.

Examples:

- HT-0001
- HC-0001
- BS-0001
- MA-0001
- EXP-0001

No serious object should exist only by title.

---

## 4. Traceability Is Mandatory

Every mature object must connect to related objects.

Example:

```yaml
connected_objects:
  human_truth: HT-0001
  human_contradiction: HC-0001
  belief_shift: BS-0001
  meaning_atom: MA-0001
```

---

## 5. Client-Specific Stays Client-Specific

Client-specific objects must stay inside:

```text
clients/<client>/
```

They are not universal until explicitly promoted.

---

## 6. Universal Objects Need Review

An object can become universal only when it works beyond one client or has a strong general reason.

Universal objects should not be created casually.

---

## 7. No Law Without Evidence

A LOGOS Law must be supported by repeated evidence.

Until then, it remains a candidate.

---

## 8. No Runtime Expansion Before Foundation

Runtime-specific production should not outrun the foundation.

The foundation gate must be respected.

---

## 9. Human and Machine Readability

Important knowledge should be written in both human-readable and machine-readable formats when possible.

Recommended pair:

```text
Markdown for explanation
YAML / OKF for structure
```

---

## 10. Avoid Duplication

If an object already exists, extend it instead of creating a near-duplicate.

If a duplicate is created by mistake, close or archive one version clearly.

---

## 11. Keep Titles Flexible

Titles may change.

IDs should not.

---

## 12. Document Decisions

Architectural decisions should be stored as ADR files.

Example:

```text
decisions/ADR-0001-foundation-first.md
```

---

## 13. Separate Idea From Evidence

Do not mix:

- intuition;
- hypothesis;
- experiment;
- learning;
- law.

Each stage has its own meaning and maturity level.

---

## 14. Protect the Mission

Every major addition should support the core mission:

> LOGOS creates structured belief change through meaning.

If a file does not support this mission, it should not be added.
