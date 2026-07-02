# PILOT-0001 Connection Flow

Date verified: 2026-07-02

This document records the safe operational flow for connecting to the VPS and n8n runtime.

It must not contain secrets.

---

## Purpose

Provide Codex with a repeatable connection procedure for PILOT-0001 without committing credentials.

---

## Secret Source

Local-only credential file:

```text
.secrets/vps-n8n-access.md
```

This path is intentionally ignored by Git.

Never copy values from this file into committed docs, issues, workflow JSON, logs or terminal output.

---

## Input

Required local values:

```text
VPS SSH host or URL
VPS SSH user
VPS SSH password or key path
n8n URL
n8n API key
```

If the VPS host is stored as a URL, use its hostname for SSH.

If SSH port is empty, default to:

```text
22
```

---

## SSH Flow

1. Read `.secrets/vps-n8n-access.md`.
2. Parse the `VPS SSH` section.
3. Normalize host:

```text
URL -> hostname
plain host -> host as-is
```

4. Connect through SSH using password or key authentication.
5. Verify identity and runtime:

```bash
whoami
hostname
uname -srm
docker ps
```

---

## n8n Runtime Checks

After SSH connects, verify the n8n container:

```bash
docker ps --format '{{.Names}}|{{.Image}}|{{.Status}}|{{.Ports}}' | grep -i n8n
docker exec n8n-compose-n8n-1 n8n --version
```

Expected current runtime:

```text
n8n version: 2.10.4
n8n container: n8n-compose-n8n-1
n8n local port: 127.0.0.1:5678->5678/tcp
reverse proxy: Traefik on 80/443
```

---

## n8n API Check

Use the API key from the local secrets file only as an HTTP header:

```text
X-N8N-API-KEY: <local secret>
```

Check:

```text
GET /api/v1/workflows?limit=1
```

Current result:

```text
HTTP 200 OK
```

Interpretation:

```text
The public n8n endpoint is reachable and the current API key is accepted.
SSH access, the n8n container and read-only API access are verified.
```

---

## Output

A successful connection check should confirm:

```text
SSH works
Docker is reachable
n8n container is running
n8n version is known
n8n public API either authenticates or returns an actionable auth error
```

---

## Acceptance Criteria

```text
Codex can SSH into the VPS without exposing credentials.
Codex can verify the running n8n container.
Codex can test n8n API authentication without printing the API key.
Any auth failure is recorded as a known operational issue.
```

---

## Manual Test

Run a quiet connection script that:

```text
reads .secrets/vps-n8n-access.md
normalizes the SSH host
connects over SSH
runs identity and docker checks
tests n8n /api/v1/workflows with X-N8N-API-KEY
prints only status, never secrets
```

---

## Evidence

Verified on 2026-07-02:

```text
SSH_OK=True
remote user: n8n
remote hostname: n8n
kernel: Linux 6.8.0-124-generic x86_64
n8n container: running
n8n version: 2.10.4
n8n API: authenticated read-only checks return HTTP 200
workflows endpoint: HTTP 200
credentials endpoint: HTTP 200
```

---

## Future Automation Path

For PILOT-0001 deployment:

```text
1. Use read-only API checks before any workflow write.
2. Create or update the PILOT-0001 workflow through n8n API only after explicit approval.
3. Do not reboot or restart VPS services during active project testing.
4. If API write fails, diagnose without restarting containers unless explicitly approved.
5. Keep GitHub as source of truth for generated artifacts and run evidence.
```
