# Admin Raw System Synthesis - 2026-07-06

## Purpose

Remove topic-specific polished synthesis from the admin preview.

## Problem

The preview had started to reuse the previous relationship/safety wording for unrelated raw meanings.

Example:

```text
raw_meaning: все самое ценное мы получаем бесплатно
```

Incorrect output reused:

```text
Безопасность без давления...
```

## Output

The admin preview now returns a raw system artifact instead of a polished paragraph:

```text
LOGOS_RAW_SYNTHESIS
raw_observation:
old_belief_input:
new_belief_input:
operator_candidate:
contradiction_candidate:
resource_candidate:
boundary_input:
status: raw_system_candidate_not_final_copy
```

Meaning Atom also stays raw:

```text
MEANING_ATOM_RAW
operator_candidate:
claim:
status: candidate
```

## Acceptance Criteria

- The system does not require one hand-written theme description per new topic.
- User dialogue answers remain visible as input, not polished final output.
- The system output is raw enough for human review and later refinement.
- The new value/free-resource test does not reuse the previous relationship/safety frame.

## Evidence

Local module smoke for:

```text
все самое ценное мы получаем бесплатно
```

Returned:

```text
operator_candidate: already_available_resource
claim: все самое ценное мы получаем бесплатно
```

Local validation passed:

```text
python -m unittest discover -s tests
python scripts\validate_catalog.py .
python -m logos_engine.validate .
```

## Boundary

This is still preview-only.

No GitHub issue was created.
No YAML object was written.
No learning or law artifact was created.
