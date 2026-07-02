# LOGOS Automation Workflows

This folder describes the future n8n runtime layer.

GitHub remains the source of truth.

n8n is the execution layer.

---

## Workflow Set

- `idea-intake.md`
- `belief-shift-generator.md`
- `script-generator.md`
- `claim-checker.md`
- `metrics-collector.md`
- `weekly-learning-report.md`

---

## Runtime Rule

Every workflow must define:

- purpose;
- input;
- output;
- GitHub artifact created or updated;
- manual dry run;
- acceptance criteria;
- future automation path.

---

## Test First

No workflow is considered ready until it has a manual dry run.

Automation should encode a working process, not guess one.

---

## Implemented n8n Gates

```text
WF-0001 Idea Intake Issue Gate
```

Evidence:

```text
automation/n8n/wf-0001/IDEA-INTAKE-ISSUE-GATE.md
automation/n8n/wf-0001/writeback/idea-intake-issue-gate-test-2026-07-02.md
```

---

## Implemented Repository Contracts

```text
WF-0002 Belief Movement Input Contract
```

Evidence:

```text
automation/n8n/wf-0002/BELIEF-MOVEMENT-INPUT-CONTRACT.md
automation/n8n/wf-0002/BELIEF-MOVEMENT-INPUT-PREVIEW-GATE.md
automation/n8n/wf-0002/writeback/belief-movement-input-contract-2026-07-02.md
automation/n8n/wf-0002/writeback/belief-movement-input-preview-gate-test-2026-07-02.md
automation/n8n/wf-0002/writeback/belief-movement-status-readiness-2026-07-02.md
scripts/wf_0002_status.py
```
