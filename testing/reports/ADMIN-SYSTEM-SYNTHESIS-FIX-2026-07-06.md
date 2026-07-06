# Admin System Synthesis Fix - 2026-07-06

## Purpose

Separate human dialogue answers from the system-generated LOGOS meaning output.

## Input

The admin test showed that `Новый смысл` could look like a direct copy of the user's dialogue answers, especially the `К:` desired-change field.

## Output

- Dialogue answers remain input/evidence.
- `New Frame` is now a system-synthesized Belief Shift.
- `Meaning Atom` is now a system-synthesized short meaning core.
- The preview opens the `Preview` tab after recalculation so the system result is visible immediately.

## Acceptance Criteria

- User dialogue wording is not treated as the system solution.
- Colloquial or rough user phrases do not appear as the final `Belief Shift`.
- The system output stays traceable to the raw meaning, desired change, and risk notes.
- WF-0002 and YAML promotion remain blocked.

## Manual Test

Submit the first personal test with dialogue answers that include rough phrasing in `От:` and `К:`.

Expected top preview:

```text
Новый смысл
Belief Shift: system synthesis
Смысловое ядро: system synthesis
```

The output should not directly copy the rough dialogue phrases.

## Evidence

Local validation passed:

```text
python -m unittest discover -s tests
python scripts\validate_catalog.py .
python -m logos_engine.validate .
```

Browser smoke passed on:

```text
http://127.0.0.1:8765/admin/
```

The first personal test produced a system Belief Shift and system meaning core without direct copying of the user's rough `К:` wording.

## Future Automation Path

n8n should preserve this separation:

```text
human answers = evidence/input
system synthesis = candidate LOGOS object
repository review = source of truth
```
