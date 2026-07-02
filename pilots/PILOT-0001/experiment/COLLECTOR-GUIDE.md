# PILOT-0001 Response Collector Guide

Status: ready_for_real_response_collection

Related:

```text
pilots/PILOT-0001/experiment/RESPONDENT-PACKET.md
pilots/PILOT-0001/experiment/response-template.yaml
scripts/create_pilot_response.py
scripts/pilot_0001_status.py
```

---

## Purpose

Collect real qualitative responses without creating fake evidence, personal-data leakage, learning or law claims.

---

## Collection Flow

1. Give the respondent `RESPONDENT-PACKET.md`.
2. Ask them to read only the `Draft Script` section from `script-draft.md`.
3. Record answers to the four questions.
4. Remove personal contact data.
5. Convert the cleaned response to JSON.
6. Run the intake script.
7. Run validation.
8. Commit the response only if validation passes.

---

## JSON Input Shape

Use this shape for a cleaned real response:

```json
{
  "response_date": "2026-07-02",
  "respondent_id": "R001",
  "respondent_context": "anonymous qualitative reviewer",
  "personal_data_removed": true,
  "simulated_response": false,
  "answers": {
    "q1_changed_in_hero": "",
    "q2_return_voluntary_or_obligated": "",
    "q3_pressure_debt_or_manipulation": "",
    "q4_meaning_of_expansion_metaphor": ""
  },
  "meaning_signal_scores": {
    "voluntary_safety": 0,
    "recovery_as_resource": 0,
    "non_coercive_return": 0,
    "boundary_awareness": 0,
    "metaphorical_expansion": 0
  },
  "failure_signals": {
    "woman_owes_safety": false,
    "man_owes_return": false,
    "relationship_as_transaction": false,
    "resource_sharing_as_payment": false,
    "expansion_as_domination": false,
    "safety_as_manipulation": false,
    "notes": null
  },
  "raw_quotes": [],
  "moderator_notes": null
}
```

Replace blank answers and scores with the respondent's real answers.

---

## Create A Response YAML

Run:

```text
python scripts\create_pilot_response.py --input path\to\cleaned-response.json
```

Expected output:

```text
created pilots/PILOT-0001/experiment/responses/RESPONSE-PILOT-0001-000N.yaml
updated pilots/PILOT-0001/RUN-MANIFEST.yaml real_response_count=N
```

---

## Check Readiness

Run:

```text
python scripts\pilot_0001_status.py
```

Before three real responses:

```text
learning_allowed: false
next_action: collect_real_responses
```

After three valid real responses:

```text
learning_allowed: true
next_action: draft_learning_candidate_from_real_responses
```

---

## Validation

Run:

```text
python -m unittest discover -s tests
python scripts\validate_catalog.py .
```

Do not commit response files unless both pass.

---

## Boundaries

Do not create:

```text
learning.md
law-review.md
law candidate
LOGOS Law
```

until the status command says learning is allowed.

