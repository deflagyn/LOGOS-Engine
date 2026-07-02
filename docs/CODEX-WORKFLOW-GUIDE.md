# CODEX WORKFLOW GUIDE — How To Work Effectively In LOGOS Engine

This guide is practical.

It tells Codex what to do when assigned tasks in this repository.

For philosophy and full context, read:

```text
docs/CODEX-PROJECT-BRIEF.md
AGENTS.md
```

---

## 1. Start Every Task With Orientation

Before editing, identify:

```text
Which foundation group does this task belong to?
Which issue tracks it?
Which files are source of truth?
What test proves success?
```

If the task does not clearly map to a group, create or propose a tracking issue before major changes.

---

## 2. Working Order

Use this order:

```text
Read context
→ identify source-of-truth files
→ make smallest useful change
→ update tests or test plans
→ run validation
→ update issue/progress note
```

Do not make wide rewrites unless the task explicitly asks for architecture cleanup.

---

## 3. Validation Command

Run:

```bash
python -m pip install -e .
python scripts/validate_catalog.py .
```

If validation fails, report the exact output and fix the cause.

---

## 4. How To Add A New Module

Every new module must include:

```text
Purpose
Input
Output
Acceptance criteria
Manual test
Evidence
Future automation
```

Use:

```text
testing/MODULE-TEST-TEMPLATE.md
```

---

## 5. How To Add A New LOGOS Object

A new object should have:

```text
stable ID
type
status
language
scope
connected objects
test plan or validation logic
```

If it belongs to a runtime, put it in:

```text
clients/<client>/
```

If it is universal, put it in a future universal object folder only when justified.

---

## 6. How To Work With Issues

Issues are active work items.

Use existing issue numbers when possible:

```text
#10 master foundation issue
#15 operations layer
#16 automation runtime design
#17 developer validation layer
#18 learning and laws
#22 validation first run
```

If you finish a meaningful unit, update or create evidence.

---

## 7. How To Work With n8n Workflows

n8n is an execution layer.

Workflow design files live in:

```text
automation/workflows/
```

Every workflow must write back to GitHub.

A workflow that stores the final result only in n8n is incomplete.

---

## 8. How To Work With Runtime Clients

Do not expand runtime-specific content unless the task explicitly asks.

Current priority remains universal foundation.

DeflaGyn is a reference runtime, not the engine itself.

---

## 9. How To Improve Validation

Good validator improvements:

```text
check duplicate IDs
check missing required fields
check missing test plan sections
check broken object references
check invalid YAML
check runtime object in wrong folder
```

Bad validator changes:

```text
remove checks to make errors disappear
make validation too broad to be actionable
hardcode one client as universal logic
```

---

## 10. Finish A Task Properly

A task is complete when:

```text
files are updated
validation was run or reason for not running is stated
issue/progress note is updated when needed
test evidence exists or pending test is clearly documented
```

---

## 11. Final Reminder

LOGOS is not about producing more text.

LOGOS is about making meaning traceable, testable and learnable.
