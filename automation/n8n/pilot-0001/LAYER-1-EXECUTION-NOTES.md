# PILOT-0001 Layer 1 Execution Notes

Date: 2026-07-02

Status: Layer 1 preview executed through temporary controlled trigger

---

## Purpose

Record how Layer 1 can and cannot be executed safely on the current live n8n runtime.

Layer 1 is:

```text
Manual Trigger
-> Config
-> Fetch GitHub Issue #27
-> Extract Raw Meaning
-> Build raw-meaning.yaml preview
```

---

## Input

```text
n8n workflow id: nFIbtlA2pYrA4MXb
GitHub issue #27
n8n API key from local secrets
```

---

## Output

Expected Layer 1 output after manual execution:

```text
raw_text extracted from issue #27
raw_text_source = raw_meaning_block
target_path = pilots/PILOT-0001/input/raw-meaning.yaml
raw_meaning_yaml preview
writeback_enabled = false
layer_1_status = raw_meaning_yaml_preview_built
```

---

## Execution Attempts

### Public n8n API

Finding:

```text
The public n8n API exposes workflow CRUD and execution listing, but no direct workflow run endpoint.
```

Result:

```text
Cannot run the workflow through public API key alone.
```

### Temporary Controlled Webhook Preview

Workflow:

```text
name: LOGOS PILOT-0001 Layer 1 Preview Trigger
id: AHsnijaOOPm8HaJl
```

Behavior:

```text
Webhook -> read-only GitHub issue #27 fetch -> raw meaning extraction -> raw-meaning.yaml preview -> JSON response
```

Result:

```text
HTTP 200
layer_1_status = raw_meaning_yaml_preview_built
target_path = pilots/PILOT-0001/input/raw-meaning.yaml
writeback_enabled = false
raw_text_source = raw_meaning_block
```

Post-run state:

```text
workflow active = false
```

### Internal REST Endpoint

Attempt:

```text
POST /rest/workflows/nFIbtlA2pYrA4MXb/run
```

Result:

```text
HTTP 401 unauthorized
```

Interpretation:

```text
The internal run endpoint requires browser/session authentication, not the public API key.
```

### n8n CLI In Running Container

Attempt:

```text
docker exec n8n-compose-n8n-1 n8n execute --id=nFIbtlA2pYrA4MXb --rawOutput
```

Result:

```text
n8n Task Broker's port 5679 is already in use.
```

Interpretation:

```text
The live n8n service already owns the Task Broker port.
Do not restart or change the service while other projects are being tested.
Do not keep using CLI execution on the live container for this pilot.
```

---

## Acceptance Criteria

```text
No VPS reboot was performed.
No Docker or n8n service restart was performed.
No GitHub writeback was executed.
Workflow remains inactive.
Writeback and LLM nodes remain disabled.
Execution boundary is documented.
```

---

## Manual Test

Recommended safe execution path:

```text
Open n8n UI with an authenticated browser session.
Open workflow LOGOS PILOT-0001 System Run.
Run manual execution.
Inspect Node 06 output.
Confirm raw_meaning_yaml preserves the Raw Meaning block from issue #27.
Do not enable Node 12 until preview is reviewed.
```

---

## Evidence

```text
Workflow remains active=false.
Nodes 07-14 remain disabled except Node 12 was renamed as pending writeback and remains disabled.
No pilot files were written to GitHub.
Expected Node 06 output is recorded in automation/n8n/pilot-0001/previews/raw-meaning.expected.yaml.example.
Live preview output is recorded in automation/n8n/pilot-0001/previews/layer1-live-preview.json.
Live preview raw_text matches the expected preview raw_text.
Real n8n writeback artifact is now pilots/PILOT-0001/input/raw-meaning.yaml.
```

---

## Future Automation Path

Options for the next step:

```text
1. Configure GitHub write credential in n8n.
2. Enable only raw-meaning.yaml writeback.
3. Write pilots/PILOT-0001/input/raw-meaning.yaml.
4. Dispatch validator and comment result on issue #27.
```
