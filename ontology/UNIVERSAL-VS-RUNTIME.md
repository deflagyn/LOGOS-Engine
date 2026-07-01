# Universal vs Runtime Boundary

This document defines the boundary between universal LOGOS knowledge and runtime-specific implementation.

This boundary protects LOGOS from becoming too attached to one client or product.

---

## Universal LOGOS

Universal LOGOS contains principles, objects, methods and patterns that can work across categories.

Examples:

- Human Truth as an object type;
- Belief Shift as the operational atom;
- Meaning Atom as compressed belief movement;
- Story Pattern as reusable narrative structure;
- Law promotion discipline;
- Meaning TRIZ as contradiction logic.

Universal LOGOS should remain product-agnostic.

---

## Runtime

A runtime is a concrete application of LOGOS.

Examples:

- a healthcare product;
- an IT service;
- an educational project;
- a civic movement;
- a personal brand.

Runtime files live inside:

```text
clients/<client>/
```

---

## Reference Runtime

A reference runtime is a real-world implementation used to test and improve the engine.

DeflaGyn is the first reference runtime.

It helps test LOGOS, but it must not define LOGOS.

---

## Runtime-Specific Object

A runtime-specific object is designed for one client, audience, language or category.

Example:

```text
A Ukrainian women's health script for a healthcare runtime.
```

This object should stay inside its runtime unless it proves broader value.

---

## Universal Promotion

A runtime-specific object may be promoted to universal LOGOS only when it satisfies at least one condition:

1. it works across more than one client;
2. it expresses a general human pattern;
3. it improves the system method;
4. it becomes a reusable Story Pattern, Law Candidate or Law;
5. it is not dependent on product-specific context.

---

## Promotion Example

Runtime-specific:

```text
A phrase created for one client and one language.
```

Possible universal form:

```text
A strong reframe expands a familiar identity without attacking the existing one.
```

The first belongs to runtime.

The second may become universal after evidence.

---

## Demotion Rule

If a supposedly universal object only works inside one runtime, it should be demoted or marked as runtime-specific.

Universal status is earned, not assumed.

---

## Folder Boundary

Universal files:

```text
constitution/
ontology/
engine/
triz/
laws/
patterns/
schemas/
validation/
```

Runtime files:

```text
clients/<client>/
```

Automation may be universal or runtime-specific depending on its purpose.

---

## Final Rule

A runtime can teach the engine.

But a runtime must not trap the engine.
