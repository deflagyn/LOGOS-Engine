# LOGOS Test First Governance

Every LOGOS module must include a test plan at creation time.

A module is not complete only because a file exists.

It is complete when we can check that it works as intended.

---

## Rule

Every module must define:

- purpose;
- input;
- output;
- owner issue;
- acceptance criteria;
- manual test;
- future automated test.

---

## Required Test Block

Every module document should contain this section:

```text
## Test Plan

Purpose:

Input:

Expected output:

Manual test:

Acceptance criteria:

Evidence:

Future automation:
```

---

## Acceptance Criteria

Acceptance criteria should use simple language:

```text
Given a starting object,
When the module runs,
Then the expected output exists and can be traced.
```

---

## Test Types

### Structure test

Checks that required fields and files exist.

### Traceability test

Checks that the object connects to previous and next LOGOS objects.

### Meaning test

Checks that the object carries a real belief shift or meaning movement.

### Runtime test

Checks that the module works in a real runtime environment.

### Learning test

Checks that the result produces useful learning.

---

## Operating Rule

Manual test first.

Automation second.

The process must make sense before it is automated.

---

## Final Rule

Every important step must be testable, traceable and useful.
