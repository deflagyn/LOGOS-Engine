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
