# Admin Dialogue UX Fix - 2026-07-06

## Purpose

Make the first personal LOGOS admin test readable and interactive.

## Input

User screenshots showed that preview text was visually and structurally shortened, and the Dialogue tab listed questions without answer controls.

## Output

- Preview now renders the LOGOS chain as full-width text blocks.
- Raw Meaning is visible inside the preview output.
- Generated Human Truth and Meaning Atom drafts no longer receive premature `...` shortening.
- Dialogue questions now include answer textareas.
- Dialogue answers can be applied back into Audience, Desired Change, and Risk Notes, then the preview is recalculated.

## Acceptance Criteria

- The first raw personal test does not hide the core observation behind ellipses.
- The Dialogue tab supports direct answer entry.
- Applying dialogue answers keeps WF-0002 and YAML promotion blocked until human review.

## Manual Test

Open:

```text
http://127.0.0.1:8765/admin/
```

Submit the first raw personal meaning, open Dialogue, answer one or more questions, and click:

```text
Применить ответы и пересчитать
```

## Evidence

Local validation commands should pass:

```text
python -m unittest discover -s tests
python scripts\validate_catalog.py .
python -m logos_engine.validate .
```

## Future Automation Path

After the local dialogue pattern is accepted, n8n can reproduce the same state machine: raw input, clarification answers, reviewed Human Truth issue, then blocked YAML promotion until an HT-#### source exists.
