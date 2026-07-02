# PILOT-0001 Memory Model

This document defines what memory the n8n workflow should use.

Memory must support traceability, not replace GitHub as source of truth.

---

## Memory Layers

### 1. Run Memory

Short-lived memory for one n8n execution.

Stores:

```text
pilot_id
run_id
source_issue
raw_text
meaning_edges
object_ids
created_paths
validator_result
```

Location:

```text
n8n execution data
```

---

### 2. GitHub Memory

Permanent memory.

Stores:

```text
raw meaning file
LOGOS object files
runtime drafts
experiment plan
learning draft
law review
issue comments
```

Location:

```text
GitHub repository
```

This is the source of truth.

---

### 3. Optional Vector Memory

Not required for PILOT-0001 MVP.

Future use:

```text
similar raw meanings
similar belief shifts
reused meaning atoms
law candidate comparison
```

Possible storage:

```text
PostgreSQL + pgvector
Qdrant
```

---

## Required Memory Fields

Every generated artifact must include:

```text
pilot_id
source_issue
source_raw_meaning_id
source_raw_text
created_by_workflow
created_at
trace_to_previous
```

---

## Raw Text Rule

The raw text must be stored once as source and referenced everywhere else.

Derived artifacts may include a copy of raw_text for readability, but the canonical source is:

```text
pilots/PILOT-0001/input/raw-meaning.yaml
```

---

## Execution ID

Each n8n run should create:

```text
run_id = PILOT-0001-YYYYMMDD-HHMMSS
```

Every GitHub writeback should include the run_id.

---

## Prompt Memory

LLM nodes should receive only relevant memory:

```text
raw_text
required previous artifacts
AX-021 rule
output format
```

Do not pass the entire repository into every node.

---

## Future Persistent Memory Table

For later VPS implementation:

```sql
logos_runs(
  run_id text primary key,
  pilot_id text,
  source_issue integer,
  status text,
  started_at timestamp,
  finished_at timestamp,
  github_paths jsonb,
  validator_result text
)

logos_artifacts(
  id text primary key,
  run_id text,
  artifact_type text,
  github_path text,
  source_artifact_id text,
  created_at timestamp
)
```

---

## Test Plan

Purpose:

```text
Check that memory preserves traceability from raw meaning to final learning.
```

Acceptance criteria:

```text
Every artifact can point back to raw-meaning.yaml and issue #27.
```
