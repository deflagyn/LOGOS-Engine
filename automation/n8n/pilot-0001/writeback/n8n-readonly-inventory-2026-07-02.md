# PILOT-0001 n8n Read-Only Inventory

Date: 2026-07-02

Purpose:

```text
Record Phase 0 n8n runtime inventory before additional PILOT-0001 implementation.
```

Safety:

```text
Read-only n8n API calls only.
No workflow execution.
No workflow activation.
No credential values recorded.
No VPS reboot.
No Docker, n8n, nginx, Postgres or service restart.
```

---

## Access Check

Source:

```text
.secrets/vps-n8n-access.md
```

Secret handling:

```text
Local file is ignored by git through .gitignore.
API key was used only as an HTTP header for read-only n8n API requests.
No secret value is written in this report.
```

Result:

```text
n8n API reachable.
GET /api/v1/workflows succeeded.
```

---

## LOGOS Workflows Found

```text
nFIbtlA2pYrA4MXb  LOGOS PILOT-0001 System Run                  active=false  nodes=14
AHsnijaOOPm8HaJl  LOGOS PILOT-0001 Layer 1 Preview Trigger     active=false  nodes=4
yosTQyMXEYP6urYn  LOGOS PILOT-0001 Raw Meaning Writeback       active=false  nodes=6
idkqB0Z4NXdkH3ZQ  LOGOS PILOT-0001 Meaning Edges Writeback     active=false  nodes=8
FGniLSGgR60qsYWT  LOGOS PILOT-0001 LOGOS Objects Writeback     active=false  nodes=13
cnCw7fqTaXxJkFvm  LOGOS PILOT-0001 Runtime Draft Writeback     active=false  nodes=16
idsqmy1mYrkh0gZn  LOGOS PILOT-0001 Experiment Plan Writeback   active=false  nodes=7
```

Interpretation:

```text
All PILOT-0001 LOGOS workflows are present and inactive.
This matches the current safety posture for controlled testing.
```

---

## Main System Run Structure

Workflow:

```text
name: LOGOS PILOT-0001 System Run
id: nFIbtlA2pYrA4MXb
active: false
node_count: 14
```

Nodes:

```text
01 Manual Trigger                         n8n-nodes-base.manualTrigger   enabled
02 Config                                 n8n-nodes-base.set             enabled
03 Preflight Checklist                    n8n-nodes-base.code            enabled
04 Fetch GitHub Issue #27                 n8n-nodes-base.httpRequest     enabled
05 Extract Raw Meaning                    n8n-nodes-base.code            enabled
06 Build Raw Meaning YAML Preview         n8n-nodes-base.code            enabled
07 Generate Meaning Edges                 n8n-nodes-base.noOp            disabled
08 Generate LOGOS Objects                 n8n-nodes-base.noOp            disabled
09 Generate Runtime Draft                 n8n-nodes-base.noOp            disabled
10 Generate Experiment Plan               n8n-nodes-base.noOp            disabled
11 Generate Learning And Law Review       n8n-nodes-base.noOp            disabled
12 Raw Meaning Writeback Pending          n8n-nodes-base.noOp            disabled
13 Trigger Validator                      n8n-nodes-base.noOp            disabled
14 Comment Result On Issue #27            n8n-nodes-base.noOp            disabled
```

Comparison:

```text
The live main workflow matches automation/n8n/pilot-0001/NODES.md at the node inventory level.
Nodes 07-14 remain placeholders or disabled gates in the main workflow.
Concrete writeback work is currently split into controlled dedicated workflows.
```

---

## Dedicated Writeback Workflow Structure

Raw Meaning Writeback:

```text
id: yosTQyMXEYP6urYn
active: false
nodes:
- Controlled Writeback Webhook
- Fetch GitHub Issue #27
- Prepare Raw Meaning PUT Body
- PUT raw-meaning.yaml
- Build Response
- Respond Writeback JSON
```

Meaning Edges Writeback:

```text
id: idkqB0Z4NXdkH3ZQ
active: false
nodes:
- Controlled Meaning Edges Webhook
- Get raw-meaning.yaml
- Prepare LLM Prompt
- Generate Meaning Edges
- Normalize Meaning Edges YAML
- PUT meaning-edges.yaml
- Build Response
- Respond Meaning Edges JSON
```

LOGOS Objects Writeback:

```text
id: FGniLSGgR60qsYWT
active: false
nodes:
- Controlled LOGOS Objects Webhook
- Get raw-meaning.yaml
- Get meaning-edges.yaml
- Prepare LOGOS Object Prompt
- Generate LOGOS Objects
- Normalize LOGOS Object YAML
- PUT human-truth.yaml
- PUT human-contradiction.yaml
- PUT belief-shift.yaml
- PUT meaning-atoms.yaml
- PUT story-pattern.yaml
- Build Response
- Respond LOGOS Objects JSON
```

Runtime Draft Writeback:

```text
id: cnCw7fqTaXxJkFvm
active: false
nodes:
- Controlled Runtime Draft Webhook
- Get raw-meaning.yaml
- Get meaning-edges.yaml
- Get human-truth.yaml
- Get human-contradiction.yaml
- Get belief-shift.yaml
- Get meaning-atoms.yaml
- Get story-pattern.yaml
- Prepare Runtime Draft Prompt
- Generate Runtime Draft
- Normalize Runtime Draft
- GET existing script-draft.md
- Build PUT Body
- PUT script-draft.md
- Build Response
- Respond Runtime Draft JSON
```

Experiment Plan Writeback:

```text
id: idsqmy1mYrkh0gZn
active: false
nodes:
- Controlled Experiment Plan Webhook
- Get script-draft.md
- Get script-draft-review.md
- Build Experiment Plan YAML
- PUT experiment-plan.yaml
- Build Response
- Respond Experiment Plan JSON
```

---

## Runtime Observations

```text
PILOT-0001 workflows are separated into a safe inactive main skeleton plus dedicated controlled writeback workflows.
Dedicated writeback workflows already contain concrete HTTP/code nodes.
The main System Run still documents the intended canonical chain but does not yet orchestrate the full sequence.
Validator dispatch and issue-comment result handling are still not implemented as live nodes in the main workflow.
Learning/law review remains blocked by evidence gate and must not be enabled from n8n yet.
```

---

## Next Safe Action

```text
Implement or verify a reusable GitHub writeback primitive and validator dispatch gate before enabling any broader n8n orchestration.
```

Do not proceed to learning or law review until real response evidence satisfies the repository gate.

