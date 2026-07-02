# PILOT-0001 Responses

Status: waiting_for_real_responses

This folder is reserved for real qualitative responses collected with:

```text
pilots/PILOT-0001/experiment/response-template.yaml
```

Do not add simulated responses here.

Do not include personal contact data.

Each real response file should:

```text
use a unique id
use type: experiment_response
use status: collected
reference EXP-PILOT-0001
set personal_data_removed: true
keep evidence_boundary.creates_learning: false
keep evidence_boundary.creates_law_candidate: false
keep evidence_boundary.creates_logos_law: false
```

Learning can be drafted only after at least three real response YAML files exist.

---

## Recommended Local Intake

Validate the JSON input first:

```text
python scripts\validate_pilot_response_input.py --input response.json
```

Use:

```text
python scripts\create_pilot_response.py --input response.json
```

The script:

```text
creates the next RESPONSE-PILOT-0001-000N.yaml file
requires personal_data_removed: true
rejects simulated_response: true
sets all learning/law boundary flags to false
updates RUN-MANIFEST.yaml real_response_count
```

Dry run:

```text
python scripts\validate_pilot_response_input.py --input testing/fixtures/pilot-0001-response-input.json.example
python scripts\create_pilot_response.py --input testing/fixtures/pilot-0001-response-input.json.example --dry-run
```

Schema:

```text
schemas/pilot-response-input.schema.yaml
```

---

## Check Readiness

Use:

```text
python scripts\pilot_0001_status.py
```

Expected before real responses:

```text
response_count: 0
learning_allowed: false
next_action: collect_real_responses
```
