# PILOT-0001 GitHub Writeback

This document defines how n8n writes PILOT-0001 artifacts back to GitHub.

---

## GitHub API Auth

Use one GitHub token stored in n8n credentials or environment.

Required capabilities:

```text
contents: read/write
issues: read/write
actions: write if dispatching validator workflow
```

Never hardcode the token in workflow JSON.

---

## Target Repository

```text
deflagyn/LOGOS-Engine
```

Default branch:

```text
main
```

---

## Write Strategy

For every file path:

```text
1. Try GET contents path.
2. If 404, create file.
3. If exists, update file using sha.
4. Record commit sha in run summary.
```

---

## Required Paths

```text
pilots/PILOT-0001/input/raw-meaning.yaml
pilots/PILOT-0001/output/meaning-edges.yaml
pilots/PILOT-0001/output/human-truth.yaml
pilots/PILOT-0001/output/human-contradiction.yaml
pilots/PILOT-0001/output/belief-shift.yaml
pilots/PILOT-0001/output/meaning-atoms.yaml
pilots/PILOT-0001/output/story-pattern.md
pilots/PILOT-0001/output/script-draft.md
pilots/PILOT-0001/output/experiment-plan.yaml
pilots/PILOT-0001/output/learning.md
pilots/PILOT-0001/output/law-review.md
pilots/PILOT-0001/RUN-LOG.md
```

---

## Commit Messages

Use predictable messages:

```text
PILOT-0001 preserve raw meaning
PILOT-0001 add meaning edges
PILOT-0001 add LOGOS objects
PILOT-0001 add runtime draft
PILOT-0001 add experiment plan
PILOT-0001 add learning and law review
PILOT-0001 update run log
```

---

## Issue Comment

After execution, comment on issue #27:

```text
PILOT-0001 run completed.
Run ID:
Files created:
Validator result:
Next action:
```

If the run fails:

```text
PILOT-0001 run failed.
Run ID:
Failed node:
Error:
Files created before failure:
Next fix:
```

---

## Validator Dispatch

Preferred API call:

```text
POST /repos/deflagyn/LOGOS-Engine/actions/workflows/validate-catalog.yml/dispatches
```

Body:

```json
{
  "ref": "main"
}
```

If workflow status polling is not implemented in MVP, record:

```text
validator_status: dispatched
```

---

## Protection Rule

The raw meaning file must not be overwritten by derived outputs.

Only update it when correcting metadata, never to rewrite the raw text.
