# PILOT-0001 VPS Deployment Plan

This document is for Codex or another implementation agent.

Goal: connect to the VPS, inspect n8n, create the PILOT-0001 workflow and run it.

---

## Required Access

Codex needs:

```text
SSH access to VPS
GitHub repository access
n8n API access or access to n8n workflow import directory
environment variable access for secrets
```

Do not store secrets in the repository.

---

## Expected VPS Stack

Preferred stack:

```text
Docker Compose
n8n
PostgreSQL for n8n
nginx or reverse proxy
SSL
backup volume
```

---

## Environment Variables

Use placeholders only:

```text
N8N_BASE_URL=
N8N_API_KEY=
GITHUB_TOKEN=
LOGOS_REPO=deflagyn/LOGOS-Engine
LOGOS_LLM_PROVIDER=
LOGOS_LLM_MODEL=
OPENAI_API_KEY=
```

Optional:

```text
LOGOS_RUN_MODE=pilot
LOGOS_DEFAULT_BRANCH=main
LOGOS_PILOT_ISSUE=27
```

---

## Codex SSH Checklist

After connecting to VPS:

```text
whoami
pwd
docker ps
docker compose ls
find / -maxdepth 3 -iname '*n8n*' 2>/dev/null
```

Then locate:

```text
docker-compose.yml
n8n data volume
.env file
reverse proxy config
```

---

## n8n API Check

Use:

```text
GET $N8N_BASE_URL/api/v1/workflows
```

Headers:

```text
X-N8N-API-KEY: $N8N_API_KEY
```

Expected:

```text
200 OK with workflow list
```

---

## Workflow Creation Strategy

Preferred:

```text
Create workflow through n8n API.
```

Fallback:

```text
Generate workflow JSON and import through n8n UI or CLI.
```

---

## Implementation Steps

```text
1. Clone or pull LOGOS-Engine repository on VPS.
2. Read automation/n8n/pilot-0001 docs.
3. Create n8n workflow: LOGOS PILOT-0001 System Run.
4. Configure credentials.
5. Add nodes from NODES.md.
6. Add prompts from PROMPTS.md.
7. Test issue fetch from GitHub.
8. Test raw meaning extraction.
9. Test GitHub file creation on a temporary path.
10. Run full workflow.
11. Dispatch validator.
12. Comment result on issue #27.
```

---

## Safety Rules

```text
Never echo secrets in logs.
Never commit .env files.
Never hardcode API keys in workflow nodes.
Never overwrite raw meaning with derived output.
```

---

## Success Criteria

```text
n8n workflow exists and is active or manually runnable.
PILOT-0001 artifacts are created in GitHub.
Issue #27 receives run summary.
Validator is dispatched or run.
No secrets are committed.
```
