# PILOT-0001 Preview Artifacts

This folder contains reviewed expected outputs for n8n preview nodes.

These files are not the real generated pilot artifacts.

Real pilot artifacts must be written under:

```text
pilots/PILOT-0001/
```

---

## Current Preview

```text
raw-meaning.expected.yaml
```

Purpose:

```text
Provide a reviewed expected output for Node 06 — Build Raw Meaning YAML Preview.
```

Source:

```text
GitHub issue #27 Raw Meaning block
```

Rule:

```text
Do not treat this as n8n writeback evidence.
Use it to compare against n8n execution output before enabling raw-meaning.yaml writeback.
```

---

## Manual Test

1. Run Layer 1 in n8n UI or a controlled trigger.
2. Inspect Node 06 output.
3. Compare:

```text
target_path
raw_meaning_yaml
writeback_enabled
layer_1_status
```

4. Approve Node 12 only if the preview preserves the raw meaning exactly.

---

## Live Preview Evidence

Live preview captured:

```text
layer1-live-preview.json
```

Source workflow:

```text
name: LOGOS PILOT-0001 Layer 1 Preview Trigger
id: AHsnijaOOPm8HaJl
```

Result:

```text
layer_1_status = raw_meaning_yaml_preview_built
target_path = pilots/PILOT-0001/input/raw-meaning.yaml
writeback_enabled = false
raw_text_source = raw_meaning_block
```

Comparison:

```text
live raw_text equals raw-meaning.expected.yaml raw_text
```

The temporary controlled workflow was deactivated after the preview call.
