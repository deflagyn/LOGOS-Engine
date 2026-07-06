# LOGOS Admin Test Window

Status: local_preview_ready

Purpose:

```text
Give the operator a local window for testing raw meaning before creating GitHub issues, YAML objects, learning or laws.
```

---

## Run

```text
python scripts\admin_test_server.py --host 127.0.0.1 --port 8765
```

Open:

```text
http://127.0.0.1:8765/admin/
```

---

## What It Does

```text
raw meaning
-> Human Truth candidate
-> Human Contradiction candidate
-> Belief Shift draft
-> Meaning Atom draft
-> Story Pattern draft
-> WF-0001 review issue preview
```

---

## Boundary

```text
local preview only
no GitHub issue created
no YAML object written
no Meaning Atom object written
no Learning or Law artifact created
WF-0002 remains blocked until a reviewed stable HT-#### source exists
```

The page is for personal testing and review.

It is not a production admin panel.

It is not an LLM-backed generator.

It is a local structured preview harness over existing LOGOS contracts.
