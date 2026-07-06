# Admin VPS Preview Deploy - 2026-07-06

## Purpose

Deploy the accepted local LOGOS admin preview harness to the VPS without changing the active n8n runtime.

## Input

Current repository commit:

```text
b46dcb5 Separate admin dialogue input from system synthesis
```

## Output

The repository was cloned on the VPS into:

```text
/home/n8n/logos-admin-preview
```

The admin preview process runs on the VPS as:

```text
python3 scripts/admin_test_server.py --host 127.0.0.1 --port 8765
```

It is intentionally bound to VPS localhost only.

## Local Access

A local SSH tunnel can expose the VPS-local preview to the operator machine:

```text
http://127.0.0.1:8766/admin/
```

The tunnel forwards:

```text
local 127.0.0.1:8766 -> VPS 127.0.0.1:8765
```

The helper script is local-only and ignored by Git:

```text
.secrets/vps-admin-tunnel.py
```

## Acceptance Criteria

- VPS process serves the admin page.
- `/api/admin/preview` returns a system-synthesized Belief Shift and Meaning Atom.
- n8n, Docker, Traefik, nginx and Postgres are not restarted.
- The preview is not publicly exposed without an auth layer.
- No secrets are committed.

## Evidence

VPS checks:

```text
remote user: n8n
n8n container: running
deploy path: /home/n8n/logos-admin-preview
admin preview bind: 127.0.0.1:8765
local tunnel URL: http://127.0.0.1:8766/admin/
```

VPS validation passed:

```text
python3 -m unittest discover -s tests
python3 scripts/validate_catalog.py .
python3 -m logos_engine.validate .
```

Tunnel smoke response:

```text
draft_status=preview_candidate
meaning_atom=Безопасность без давления возвращает ресурс для спокойного вклада в отношения.
```

## Boundary

This is a preview deployment only.

No GitHub issue was created from the admin test.
No YAML object was written.
No learning or law artifact was created.
No n8n workflow was activated or restarted.
No VPS reboot or Docker restart was performed.

## Future Automation Path

Before making this public, add an explicit access-control layer such as Traefik basic auth or another authenticated route.
