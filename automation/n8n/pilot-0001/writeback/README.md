# PILOT-0001 Writeback Evidence

This folder records n8n writeback evidence without storing secrets.

---

## Raw Meaning Writeback

Controlled n8n workflow:

```text
name: LOGOS PILOT-0001 Raw Meaning Writeback
id: yosTQyMXEYP6urYn
active after run: false
```

Target:

```text
pilots/PILOT-0001/input/raw-meaning.yaml
```

Result:

```text
status: raw_meaning_writeback_completed
commit_sha: 0d90663cc799e247c5936d4eb6b058f1fe0eb92f
```

Safety:

```text
Only raw-meaning.yaml was written.
No LLM nodes were executed.
No full artifact writeback was enabled.
No VPS reboot or service restart was performed.
```

---

## Meaning Edges Writeback

Controlled n8n workflow:

```text
name: LOGOS PILOT-0001 Meaning Edges Writeback
id: idkqB0Z4NXdkH3ZQ
active after run: false
```

Target:

```text
pilots/PILOT-0001/output/meaning-edges.yaml
```

Result:

```text
status: meaning_edges_writeback_completed
commit_sha: 2438361ed68dfccd9621bef7aa138fec52cd07d3
```

Validation checks:

```text
id: ME-PILOT-0001
type: meaning_edges
status: candidate
source_raw_meaning_id: RM-PILOT-0001
edge_count: 4
law_promotion_allowed: false
```

Safety:

```text
Only meaning-edges.yaml was written.
No LOGOS object generation nodes were executed.
No script, experiment, learning or law artifacts were created.
No VPS reboot or service restart was performed.
```

---

## LOGOS Objects Writeback

Controlled n8n workflow:

```text
name: LOGOS PILOT-0001 LOGOS Objects Writeback
id: FGniLSGgR60qsYWT
active after run: false
```

Targets:

```text
pilots/PILOT-0001/output/human-truth.yaml
pilots/PILOT-0001/output/human-contradiction.yaml
pilots/PILOT-0001/output/belief-shift.yaml
pilots/PILOT-0001/output/meaning-atoms.yaml
pilots/PILOT-0001/output/story-pattern.yaml
```

Result:

```text
status: logos_objects_writeback_completed
```

Commit SHAs:

```text
human_truth: 45c0703597a6420a1bf9f72789e02a8fe7ddd8a3
human_contradiction: 9d3e2893357bd5b093d12e82ba842b8b5a498dde
belief_shift: 8e221acd61affa423ee3863d17c38be920754725
meaning_atoms: 162373c10a88e565cbf6c27add42d4373f1786f7
story_pattern: a7611d460d8d51308f439cf0b66049ec6170d66a
```

Validation checks:

```text
HT-PILOT-0001 -> RM-PILOT-0001, ME-PILOT-0001
HC-PILOT-0001 -> HT-PILOT-0001
BS-PILOT-0001 -> HT-PILOT-0001, HC-PILOT-0001
MA-PILOT-0001 -> BS-PILOT-0001
SP-PILOT-0001 -> MA-PILOT-0001
all objects status: candidate
review_required: true
law_promotion_allowed: false
```

Safety:

```text
Only LOGOS object candidate YAML artifacts were written.
No script, experiment, learning or law artifacts were created.
No VPS reboot or service restart was performed.
```

Implementation note:

```text
First attempt failed before writing files because n8n HTTP Request body expressions used `={ ... }` instead of `={{ ... }}`.
The workflow was corrected and rerun successfully.
```

---

## Runtime Draft Writeback

Controlled n8n workflow:

```text
name: LOGOS PILOT-0001 Runtime Draft Writeback
id: cnCw7fqTaXxJkFvm
active after run: false
```

Target:

```text
pilots/PILOT-0001/output/script-draft.md
```

Result:

```text
status: runtime_draft_writeback_completed
writeback_scope: script_draft_only
commit_sha: 159ccc24f7b4ff071c8031d60bd816cb1eeae9bb
content_sha: 151283a194acac4d7d7aca009fcaba25cc95094d
```

Traceability:

```text
RM-PILOT-0001
ME-PILOT-0001
HT-PILOT-0001
HC-PILOT-0001
BS-PILOT-0001
MA-PILOT-0001
SP-PILOT-0001
```

Safety:

```text
Only script-draft.md was written.
No experiment, learning or law artifacts were created.
No VPS reboot or service restart was performed.
Workflow inactive after the controlled run.
```

Implementation note:

```text
First activation attempt failed before execution because n8n needed corrected connection nesting and a webhookId.
Second execution reached the workflow but failed before writeback because script-draft.md did not exist and the GET-existing node returned 404.
The first successful run skipped GET-existing and created script-draft.md only.
```
