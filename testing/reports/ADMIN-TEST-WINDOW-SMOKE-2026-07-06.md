# Admin Test Window Smoke Test

Date: 2026-07-06

Purpose:

```text
Prove that the local admin test window can accept raw meaning and return a bounded LOGOS preview without writing GitHub issues or YAML objects.
```

---

## Server

Command:

```text
python scripts\admin_test_server.py --host 127.0.0.1 --port 8765
```

URL:

```text
http://127.0.0.1:8765/admin/
```

---

## Page Smoke

Result:

```text
GET /admin/ -> 200
page contains LOGOS Admin Test
```

---

## API Smoke

Endpoint:

```text
POST /api/admin/preview
```

Input:

```text
raw_meaning: Если человек получает безопасное пространство, у него появляются силы действовать спокойнее.
audience_context: первый личный тест
language: ru
scope: universal
desired_change: От защиты к спокойному действию.
risk_notes: Может прозвучать как долг.
source: local admin smoke test
```

Result:

```text
Human Truth candidate returned
WF-0001 review issue preview returned
WF-0002 ready: false
no_yaml_writeback: true
no_github_issue_created: true
```

---

## Boundary

```text
No GitHub issue was created.
No YAML object was written.
No n8n workflow was activated.
No VPS reboot was performed.
No Docker, n8n, nginx, Postgres or service restart was performed.
```
