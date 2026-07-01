# n8n Runtime

n8n is not the source of truth for LOGOS.

GitHub is the source of truth.

n8n is the first automation runtime: the nervous system that moves LOGOS objects through the pipeline.

---

## Recommended Roles

```text
GitHub = source of truth / memory
n8n = workflow automation / nervous system
VPS = execution environment / body
AI models = generation and analysis layer
Google Sheets = temporary metric input
```

---

## MVP Workflows

### 1. Idea Intake

Input:

- Telegram message;
- form submission;
- manual webhook.

Output:

- `human_truth` or `raw_observation` object saved to GitHub.

---

### 2. Belief Shift Generator

Input:

- Human Truth;
- Human Contradiction;
- client profile.

Output:

- structured Belief Shift YAML;
- Meaning Atom candidates;
- emotional target.

---

### 3. Ukrainian Script Generator

Input:

- Belief Shift;
- Story Pattern;
- DeflaGyn product profile;
- forbidden claims list.

Output:

- 40–50 second Ukrainian avatar script;
- visual notes;
- soft CTA;
- safety check.

---

### 4. Medical Claim Checker

Input:

- Ukrainian script.

Output:

- pass / revise / reject;
- risky phrases;
- safer alternatives.

---

### 5. Metrics Collector

Input:

- Google Sheet row or manual data input.

Metrics:

- platform;
- views;
- average watch time;
- completion rate;
- likes;
- comments;
- saves;
- shares;
- profile clicks;
- repeated comments;
- quoted phrases.

Output:

- updated experiment file;
- score;
- learning note.

---

### 6. Weekly Learning Report

Output:

- strongest Belief Shifts;
- strongest hooks;
- strongest Story Patterns;
- weak ideas to archive;
- Law Candidates.

---

## First Runtime Stack

Recommended VPS deployment:

```text
Docker Compose
├── n8n
├── PostgreSQL for n8n
├── nginx / reverse proxy
├── SSL
└── backups
```

Later additions:

```text
PostgreSQL + pgvector
FastAPI logos-api
Neo4j or Qdrant
Redis
Dashboard
```

---

## Rule

n8n should not become the brain.

It should only execute the LOGOS process.
