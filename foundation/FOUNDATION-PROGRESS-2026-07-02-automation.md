# Foundation Progress — Automation Runtime Design

Date: 2026-07-02

Owner issue: #16

---

## Purpose

Design the first n8n runtime layer for LOGOS.

GitHub remains the source of truth.

n8n will execute workflows and write results back to GitHub.

---

## Files Created

```text
automation/workflows/README.md
automation/workflows/idea-intake.md
automation/workflows/belief-shift-generator.md
automation/workflows/script-generator.md
automation/workflows/claim-checker.md
automation/workflows/metrics-collector.md
automation/workflows/weekly-learning-report.md
testing/manual/TEST-FOUNDATION-F.md
automation/samples/DRYRUN-0001-foundation-f.md
```

Implementation evidence added:

```text
automation/n8n/wf-0001/IDEA-INTAKE-ISSUE-GATE.md
automation/n8n/wf-0001/PROMOTION-READINESS-PREFLIGHT-GATE.md
automation/n8n/wf-0001/writeback/idea-intake-issue-gate-test-2026-07-02.md
automation/n8n/wf-0001/writeback/idea-intake-schema-parity-test-2026-07-02.md
automation/n8n/wf-0001/writeback/idea-intake-issue-review-readiness-2026-07-02.md
automation/n8n/wf-0001/writeback/idea-intake-promotion-readiness-2026-07-02.md
automation/n8n/wf-0001/writeback/promotion-readiness-preflight-gate-test-2026-07-02.md
automation/n8n/wf-0001/writeback/wf-0001-status-readiness-2026-07-02.md
automation/n8n/wf-0002/BELIEF-MOVEMENT-INPUT-CONTRACT.md
automation/n8n/wf-0002/BELIEF-MOVEMENT-INPUT-PREVIEW-GATE.md
automation/n8n/wf-0002/writeback/belief-movement-input-contract-2026-07-02.md
automation/n8n/wf-0002/writeback/belief-movement-input-preview-gate-test-2026-07-02.md
schemas/wf-0001-idea-intake.schema.yaml
schemas/wf-0002-belief-movement-input.schema.yaml
testing/fixtures/wf-0001-idea-intake.json.example
testing/fixtures/wf-0001-issue-29.md
testing/fixtures/wf-0001-issue-reviewed-stable.md
testing/fixtures/wf-0002-belief-movement-input.json.example
scripts/validate_wf_0001_idea_intake.py
scripts/validate_wf_0001_issue.py
scripts/validate_wf_0001_promotion_readiness.py
scripts/wf_0001_status.py
scripts/validate_wf_0002_belief_movement_input.py
```

---

## Workflow Set

```text
WF-0001 Idea Intake
WF-0002 Belief Movement Generator
WF-0003 Script Generator
WF-0004 Review Checker
WF-0005 Metrics Collector
WF-0006 Weekly Learning Report
```

---

## What Works Now

- Each workflow has purpose, input and output.
- Each workflow has a manual dry run section.
- Each workflow identifies its GitHub artifact.
- A simulated chain dry run exists.
- The chain can move from raw idea to learning report in design form.
- WF-0001 has a controlled n8n webhook that creates a structured GitHub Human Truth candidate issue.

---

## Test Evidence

Manual test plan:

```text
testing/manual/TEST-FOUNDATION-F.md
```

Dry run sample:

```text
automation/samples/DRYRUN-0001-foundation-f.md
```

n8n implementation test:

```text
workflow: LOGOS WF-0001 Idea Intake Issue Gate
workflow_id: s00B4QAhJ3MYZ1tq
success_execution_id: 1096
rejection_execution_id: 1097
schema_parity_rejection_execution_ids: 1098, 1099
created_issue: https://github.com/deflagyn/LOGOS-Engine/issues/29
```

Local schema test:

```text
python scripts\validate_wf_0001_idea_intake.py --input testing\fixtures\wf-0001-idea-intake.json.example
```

Issue review-readiness test:

```text
python scripts\validate_wf_0001_issue.py --input testing\fixtures\wf-0001-issue-29.md --title "HT-0000: Intake must preserve raw observations before interpretation"
```

Promotion-readiness guard:

```text
python scripts\validate_wf_0001_promotion_readiness.py --input testing\fixtures\wf-0001-issue-29.md --title "HT-0000: Intake must preserve raw observations before interpretation" --review-attestation REVIEWED_WF_0001_HUMAN_TRUTH_FOR_YAML_PROMOTION
```

Expected:

```text
Issue #29 is rejected for promotion because HT-0000 is only a placeholder.
```

n8n promotion preflight:

```text
workflow: LOGOS WF-0001 Promotion Readiness Preflight Gate
workflow_id: a8peB0KHbGvAj3gg
placeholder_rejection_execution_id: 1100
reviewed_stable_success_execution_id: 1101
writeback_performed: false
```

WF-0001 status:

```text
python scripts\wf_0001_status.py
validation_passed: true
next_action: assign_stable_ht_id_or_collect_next_real_idea
```

WF-0002 input contract:

```text
python scripts\validate_wf_0002_belief_movement_input.py --input testing\fixtures\wf-0002-belief-movement-input.json.example
writeback_performed: false
creates_belief_shift_issue: false
creates_yaml_object: false
```

WF-0002 n8n preview:

```text
workflow: LOGOS WF-0002 Belief Movement Input Preview Gate
workflow_id: Rue7sAU14UMv1hTr
valid_preview_execution_id: 1102
placeholder_rejection_execution_id: 1103
writeback_performed: false
```

---

## Pending

- Add Telegram or form intake after the controlled webhook path remains stable.
- Add optional Human Truth drafting only behind a review gate.
- Promote reviewed issues into YAML object files through a separate gate.
- Build WF-0002 n8n preview only after the input contract remains stable.

---

## Decision

Group F is design-complete and WF-0001 now has a first controlled n8n implementation.

The next technical phase should harden WF-0001, then convert the remaining workflow designs into n8n workflows one by one.
