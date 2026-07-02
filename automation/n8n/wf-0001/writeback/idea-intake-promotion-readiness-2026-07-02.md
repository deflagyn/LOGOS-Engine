# WF-0001 Idea Intake Promotion Readiness Guard

Date: 2026-07-02

Purpose:

```text
Prevent a review-ready WF-0001 GitHub issue from being promoted to YAML before it has a stable Human Truth ID and explicit human review attestation.
```

This is not a writeback gate.

It does not create or update a YAML object.

It only validates whether a future promotion gate is allowed to start.

---

## Validator

```text
scripts/validate_wf_0001_promotion_readiness.py
logos_engine/wf_0001_issue.py
```

Required attestation:

```text
REVIEWED_WF_0001_HUMAN_TRUTH_FOR_YAML_PROMOTION
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

## Placeholder Rejection

Source issue:

```text
issue: #29
title: HT-0000: Intake must preserve raw observations before interpretation
fixture: testing/fixtures/wf-0001-issue-29.md
```

Command:

```text
python scripts\validate_wf_0001_promotion_readiness.py --input testing\fixtures\wf-0001-issue-29.md --title "HT-0000: Intake must preserve raw observations before interpretation" --review-attestation REVIEWED_WF_0001_HUMAN_TRUTH_FOR_YAML_PROMOTION
```

Result:

```text
ERROR: WF-0001 promotion readiness validation failed: LOGOS ID must be a stable HT-#### identifier before YAML promotion; HT-0000 placeholder cannot be promoted to YAML
```

Interpretation:

```text
Issue #29 is review-ready but not promotion-ready.
```

---

## Reviewed Stable Fixture

Fixture:

```text
testing/fixtures/wf-0001-issue-reviewed-stable.md
```

Command:

```text
python scripts\validate_wf_0001_promotion_readiness.py --input testing\fixtures\wf-0001-issue-reviewed-stable.md --title "HT-0100: Intake must preserve raw observations before interpretation" --review-attestation REVIEWED_WF_0001_HUMAN_TRUTH_FOR_YAML_PROMOTION
```

Result:

```text
WF-0001 issue passed YAML promotion-readiness validation.
logos_id: HT-0100
status: candidate
scope: universal
writeback_performed: false
```

Interpretation:

```text
A reviewed issue with a stable HT ID can enter a future promotion gate, but this validator still performs no writeback.
```

---

## Boundary

```text
Promotion-ready does not mean automatically promoted.
Promotion-ready does not write YAML.
Promotion-ready does not create learning, law candidates or LOGOS Laws.
Future YAML promotion must be a separate reviewed writeback gate.
```

