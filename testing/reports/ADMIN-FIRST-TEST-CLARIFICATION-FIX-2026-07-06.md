# Admin First Test Clarification Fix

Date: 2026-07-06

Purpose:

```text
Record the fix for the first local admin test where the page produced a confident preview too early.
```

---

## Problem

The first raw meaning test used this shape:

```text
safe space from a woman
-> rest and attachment
-> more resources
-> capture new territories
-> share resources with the woman
```

The page produced a `preview_candidate` because `desired_change` and `risk_notes` were prefilled as real textarea values.

That made the test look resolved even when the operator had not supplied those clarifications.

---

## Fix

```text
desired_change and risk_notes are now empty by default and shown only as placeholders.
```

The backend now detects risk signals in the raw meaning:

```text
woman owes safety
transactional return
domination / territory capture
attachment as dependency
```

If either desired change or risk notes are missing, the preview status becomes:

```text
needs_clarification
```

and the Story Pattern is not assembled yet.

---

## Verified Behavior

For the first test input:

```text
draft_status: needs_clarification
needs_clarification: true
story_pattern_draft: Черновик не собран...
```

The Dialogue tab asks follow-up questions about:

```text
who should recognize themselves
what belief should stop
what belief should start
woman not being obliged to give safety
territory capture as non-dominating metaphor
voluntary return not looking like payment
```

---

## Boundary

```text
No GitHub issue was created.
No YAML object was written.
No n8n workflow was activated.
No VPS reboot or service restart was performed.
```
