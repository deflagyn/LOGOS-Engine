# PILOT-0001 n8n Workflow Status

Date: 2026-07-02

Status: raw meaning, meaning edges, LOGOS objects, runtime draft and experiment plan written by controlled n8n workflows

---

## Purpose

Record the current n8n implementation state for PILOT-0001 without storing secrets.

This file is evidence that the first safe workflow shell exists before any writeback or LLM execution is enabled.

---

## n8n Workflow

```text
name: LOGOS PILOT-0001 System Run
id: nFIbtlA2pYrA4MXb
active: false
nodes: 14
disabled nodes: 8
```

---

## Input

```text
GitHub Issue #27
n8n API key from local secrets
PILOT-0001 node specification
PILOT-0001 implementation plan
```

Secrets remain only in:

```text
.secrets/vps-n8n-access.md
```

---

## Output

Created an inactive n8n workflow with:

```text
01 Manual Trigger
02 Config
03 Preflight Checklist
04 Fetch GitHub Issue #27
05 Extract Raw Meaning
06 Build Raw Meaning YAML Preview
07 Generate Meaning Edges
08 Generate LOGOS Objects
09 Generate Runtime Draft
10 Generate Experiment Plan
11 Generate Learning And Law Review
12 GitHub Writeback
13 Trigger Validator
14 Comment Result On Issue #27
```

Nodes 04-06 are enabled read-only / preview-only Layer 1 nodes.

Nodes 07-11 remain disabled placeholders.

Node 12 is now a disabled pending node for the first controlled writeback:

```text
pilots/PILOT-0001/input/raw-meaning.yaml
```

Nodes 13-14 remain disabled placeholders.

---

## Acceptance Criteria

```text
Workflow exists in n8n.
Workflow is inactive.
No writeback node is enabled.
No LLM node is enabled.
No webhook or Telegram trigger is active.
No VPS reboot or service restart was performed.
Workflow remains inactive.
```

---

## Manual Test

Read-only n8n API check:

```text
GET /api/v1/workflows/nFIbtlA2pYrA4MXb
```

Observed:

```text
status: 200
active: false
nodes: 14
disabled_nodes: 8
first nodes:
  - 01 Manual Trigger
  - 02 Config
  - 03 Preflight Checklist
Layer 1 nodes:
  - 04 Fetch GitHub Issue #27
  - 05 Extract Raw Meaning
  - 06 Build Raw Meaning YAML Preview
last node:
  - 14 Comment Result On Issue #27
```

Execution attempts:

```text
Public n8n API: no workflow run endpoint is exposed.
Internal /rest workflow run endpoint: HTTP 401 with API key, requires browser/session auth.
n8n CLI inside running container: not used further because `n8n execute` conflicts with the live Task Broker port.
No service restart or reboot was attempted.
```

---

## Evidence

```text
Workflow created through n8n API.
Workflow was verified through n8n API.
Layer 1 read-only nodes were wired through n8n API.
The workflow has not been executed for GitHub writes.
Node 12 was marked as pending for raw-meaning.yaml writeback only.
```

---

## Known Limits

```text
This is a Layer 1 workflow, not the full runtime.
Raw meaning writeback is not enabled yet.
LLM nodes are not wired yet.
Validator dispatch is not wired yet.
Layer 1 manual execution needs n8n UI/session access or a later controlled trigger.
```

---

## Next Step

Layer 1 preview was executed through a temporary controlled trigger and matched the expected raw text.

Raw meaning writeback completed:

```text
pilots/PILOT-0001/input/raw-meaning.yaml
```

Runtime draft writeback completed:

```text
pilots/PILOT-0001/output/script-draft.md
```

Controlled runtime draft workflow:

```text
name: LOGOS PILOT-0001 Runtime Draft Writeback
id: cnCw7fqTaXxJkFvm
active after run: false
commit_sha: 159ccc24f7b4ff071c8031d60bd816cb1eeae9bb
```

Experiment plan writeback completed:

```text
pilots/PILOT-0001/output/experiment-plan.yaml
```

Controlled experiment plan workflow:

```text
name: LOGOS PILOT-0001 Experiment Plan Writeback
id: idsqmy1mYrkh0gZn
active after run: false
commit_sha: c8e5146d3a2dbf96762a0bc34a0d9da0be03b170
```

Next step:

```text
Create RUN-MANIFEST.yaml
-> then stop before learning/law unless real experiment evidence exists
```

Keep learning, law review and full writeback disabled.
