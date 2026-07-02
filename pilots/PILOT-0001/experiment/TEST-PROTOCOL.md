# PILOT-0001 Experiment Test Protocol

Date: 2026-07-02

Status: ready_for_manual_execution

Related:

```text
pilots/PILOT-0001/output/experiment-plan.yaml
pilots/PILOT-0001/output/script-draft.md
pilots/PILOT-0001/review/script-draft-review.md
```

---

## Purpose

Run a small qualitative test of `EXP-PILOT-0001` without pretending that the test has already produced learning.

This protocol exists to collect evidence for the meaning movement:

```text
safe space
-> rest and attachment
-> resource recovery
-> metaphorical expansion
-> voluntary shared return
```

The test checks whether people understand the movement without reading it as pressure, debt or manipulation.

---

## Input

```text
pilots/PILOT-0001/output/script-draft.md
pilots/PILOT-0001/output/experiment-plan.yaml
pilots/PILOT-0001/experiment/response-template.yaml
```

---

## Output

Expected future output after real respondents answer:

```text
pilots/PILOT-0001/experiment/responses/
```

Do not create learning from empty or simulated responses.

---

## Participants

Recommended first pass:

```text
3-5 respondents
qualitative review only
no performance claims
no paid-media interpretation
```

Participants should be able to comment on:

```text
meaning clarity
emotional reading
voluntary boundaries
possible manipulation reading
```

---

## Test Material

Show only the draft script section from:

```text
pilots/PILOT-0001/output/script-draft.md
```

Do not show the full LOGOS object chain to respondents during the first read.

Reason:

```text
The test should reveal whether the runtime expression carries the belief shift by itself.
```

---

## Moderator Instructions

1. Give the respondent the draft script.
2. Ask them to read it once without explanation.
3. Ask the four qualitative questions from `experiment-plan.yaml`.
4. Record answers using `response-template.yaml`.
5. Ask follow-up only for clarification, not persuasion.
6. Do not explain the intended meaning until after the response is recorded.

---

## Required Questions

```text
1. Что, по вашему ощущению, изменилось у героя после безопасного пространства?
2. Выглядит ли отдача в финале добровольной или обязанной? Почему?
3. Есть ли в сцене ощущение давления, долга или манипуляции? Где именно?
4. Как вы понимаете метафору расширения возможностей в этой сцене?
```

---

## Meaning Signals To Score

Score each from `0` to `5`.

```text
voluntary_safety
recovery_as_resource
non_coercive_return
boundary_awareness
metaphorical_expansion
```

Scoring guide:

```text
0 = absent or contradicted
1 = barely present
2 = weak / unclear
3 = present but not strong
4 = clear
5 = very clear and independently articulated
```

---

## Failure Signals

Record explicitly if a respondent reads the draft as:

```text
woman owes safety
man owes return
relationship as transaction
resource sharing as payment
expansion as domination
safety as manipulation
```

These are not embarrassing failures.

They are the point of the test.

---

## Acceptance Criteria

The test is valid only if:

```text
at least 3 real responses are recorded
each response uses response-template.yaml
negative readings are preserved, not edited away
no learning is written before responses exist
no law review is written before responses exist
```

---

## Manual Test

Before running with respondents:

```text
python scripts\validate_catalog.py .
python -m logos_engine.validate .
```

After responses are collected:

```text
confirm every response file has respondent_id
confirm every response references EXP-PILOT-0001
confirm no response file contains secrets or personal contact data
confirm learning remains absent until responses are reviewed
```

---

## Evidence

Future evidence should include:

```text
response files
response count
date collected
moderator notes
validation result
issue #27 update
```

---

## Boundary

This protocol does not create:

```text
Learning
Law Candidate
LOGOS Law
Performance claim
Universal relationship claim
```

Learning may be drafted only after real response files exist.

