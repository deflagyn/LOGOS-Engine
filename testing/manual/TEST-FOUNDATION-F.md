# Manual Test — Foundation F

Owner issue: #16

Status: draft

---

## Scope

Workflow design files in `automation/workflows/`.

---

## Test 1 — Workflow Completeness

Purpose:

```text
Check that every workflow has purpose, input, output and acceptance criteria.
```

Steps:

1. Open each workflow file.
2. Check purpose.
3. Check input.
4. Check output.
5. Check manual dry run.
6. Check acceptance criteria.

Expected result:

```text
Every workflow can be understood before it is automated.
```

---

## Test 2 — Chain Dry Run

Purpose:

```text
Check that one idea can move through the designed chain.
```

Steps:

1. Start with one raw idea.
2. Convert it into a structured candidate.
3. Create a draft output.
4. Review it.
5. Add sample metrics.
6. Produce a learning note.

Expected result:

```text
The original idea remains traceable through all steps.
```

---

## Test 3 — Source of Truth

Purpose:

```text
Check that GitHub remains source of truth.
```

Expected result:

```text
Every workflow creates or updates a GitHub artifact.
```

---

## Result

Design files created. Dry run evidence pending.
