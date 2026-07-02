# PILOT-0001 n8n Implementation

Owner issue: #27

Purpose: build the first executable LOGOS system run in n8n.

This folder describes the n8n nodes, prompts, memory model, GitHub writeback and VPS deployment plan needed for Codex to implement the workflow through API and SSH.

---

## Target

Input:

```text
Raw meaning from GitHub issue #27
```

Output:

```text
A complete traceable LOGOS pilot run saved back to GitHub.
```

The workflow must not depend on the assistant manually interpreting the meaning.

n8n must execute the process.

---

## Source of Truth

```text
GitHub = source of truth
n8n = workflow runtime
VPS = execution environment
LLM = interpretation engine
Codex = deployment and implementation agent
```

---

## Required Files

```text
automation/n8n/pilot-0001/README.md
automation/n8n/pilot-0001/NODES.md
automation/n8n/pilot-0001/PROMPTS.md
automation/n8n/pilot-0001/MEMORY.md
automation/n8n/pilot-0001/GITHUB-WRITEBACK.md
automation/n8n/pilot-0001/VPS-DEPLOYMENT.md
automation/n8n/pilot-0001/TEST-PLAN.md
```

---

## Workflow Chain

```text
Manual Trigger or Webhook
→ Fetch Pilot Issue
→ Extract Raw Meaning
→ Preserve Raw Meaning
→ Generate Meaning Edges
→ Generate LOGOS Objects
→ Generate Runtime Drafts
→ Generate Experiment Plan
→ Generate Learning Draft
→ Generate Law Review
→ Write Artifacts to GitHub
→ Run Validator
→ Comment Result on Issue #27
```

---

## Non-Negotiable Rule

AX-021 applies to every node:

```text
Raw meaning must not be sterilized.
```

All derived outputs must preserve source traceability.

---

## Deployment Goal

Codex should be able to:

```text
1. connect to the VPS by SSH;
2. inspect n8n deployment;
3. create or update n8n workflow through API or local import;
4. configure environment variables;
5. run a test execution;
6. verify GitHub artifacts were created;
7. record result in issue #27.
```
