# Admin Raw Synthesis V2 - 2026-07-06

## Purpose

Move the admin preview from a field-copy artifact to a raw LOGOS/TRIZ reasoning artifact.

## Problem

The previous raw output avoided polished topic templates, but it was too mechanical:

```text
contradiction_candidate: old_belief_input conflicts with raw_observation
```

This was not enough system work.

## Output

The preview now returns:

```text
LOGOS_RAW_SYNTHESIS_V2
raw_observation:
audience_context_input:
old_belief_input:
new_belief_input:
operator_candidate:
triz_move_candidate:
contradiction_raw:
resource_inventory_input:
belief_shift_candidate_raw:
boundary_input:
validation_gap:
status: raw_system_candidate_not_final_copy
```

The output is intentionally raw. It is not polished copy and not a final LOGOS object.

## Acceptance Criteria

- No hand-written topic templates are required per new theme.
- The system performs visible logical work beyond copying input fields.
- Rough user wording remains visible as input.
- The output exposes contradiction, available resources, candidate operator and validation gap.
- Human review still decides what becomes a real LOGOS object.

## Evidence

For:

```text
raw_meaning: все самое ценное человек получает бесплатно
audience_context: достигатор
```

The system returns:

```text
operator_candidate: already_available_resource
contradiction_raw: что ему чегото не хватает для счастья <-> все самое ценное человек получает бесплатно
resource_inventory_input: руки ноги голова целая есть здоровье, время, знания, жизненный опыт. значит все хорошо
validation_gap: check_that_shift_does_not_become_forced_new_paradigm
```

## Boundary

Preview-only.

No GitHub issue was created.
No YAML object was written.
No learning or law artifact was created.
