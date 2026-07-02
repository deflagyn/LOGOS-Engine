# WF-0001 Promotion Readiness Preflight Gate

This document records the n8n preflight-only workflow for future WF-0001 Human Truth YAML promotion.

GitHub remains the source of truth.

This workflow checks whether an issue is allowed to enter a future promotion gate.

It does not write YAML.

---

## Workflow

```text
name: LOGOS WF-0001 Promotion Readiness Preflight Gate
id: a8peB0KHbGvAj3gg
active: false
```

Purpose:

```text
Block premature YAML promotion unless a WF-0001 issue has a stable HT ID, promotable status and explicit review attestation.
```

This workflow does not create GitHub issues.

It does not create or update YAML objects.

It does not create learning or law artifacts.

---

## Nodes

```text
01 Controlled Promotion Preflight Webhook
02 Validate Promotion Readiness
03 Respond Promotion Preflight JSON
```

---

## Safety Contract

The request must include:

```json
{
  "confirm_promotion_preflight": "PREFLIGHT_WF_0001_HUMAN_TRUTH_PROMOTION",
  "review_attestation": "REVIEWED_WF_0001_HUMAN_TRUTH_FOR_YAML_PROMOTION",
  "title": "",
  "issue_body": ""
}
```

The issue body must satisfy the local promotion-readiness contract:

```text
scripts/validate_wf_0001_promotion_readiness.py
```

Promotion-readiness requires:

```text
WF-0001 issue body passes review-readiness validation
LOGOS ID is stable HT-####
LOGOS ID is not HT-0000
issue title starts with the stable LOGOS ID
status is candidate, draft, testing or validated
review_attestation is present and exact
```

---

## Current State

```text
created: true
active: false
placeholder_rejection_tested: true
reviewed_stable_preflight_tested: true
writeback_performed: false
```

Test evidence:

```text
automation/n8n/wf-0001/writeback/promotion-readiness-preflight-gate-test-2026-07-02.md
```

---

## Operation Protocol

For a controlled preflight:

```text
1. Activate only this workflow if webhook execution is required.
2. POST the required confirmation payload, review attestation, title and issue body.
3. Verify status=promotion_readiness_preflight_passed only for reviewed stable HT issues.
4. Verify writeback_performed=false.
5. Verify creates_yaml_object=false.
6. Deactivate the workflow immediately after the controlled preflight.
7. Do not promote any issue from this preflight output alone.
```

Issue #29 is intentionally rejected by this preflight because it still uses `HT-0000`.

Do not use this gate to create YAML objects.

Do not use this gate to create learning or law candidates.

