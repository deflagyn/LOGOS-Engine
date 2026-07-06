# Admin Serendipity Route - 2026-07-06

## Purpose

Make the LOGOS admin preview usable from the Serendipity VPS domain instead of only through a local SSH tunnel.

## Input

Requested operator URL:

```text
https://serendipity.83-150-204-190.sslip.io/admin/
```

Existing Serendipity admin is Directus and already owns `/admin/`.

## Output

LOGOS admin preview was exposed under the same Serendipity host without replacing Directus:

```text
https://serendipity.83-150-204-190.sslip.io/logos-admin/admin/
```

The admin preview API is available through the same prefix:

```text
https://serendipity.83-150-204-190.sslip.io/logos-admin/api/admin/preview
```

Directus received a visible collection:

```text
cc_logos_admin_tools
```

With an item:

```text
LOGOS Meaning Preview
```

That item links to the LOGOS admin preview URL.

## Deployment Shape

The LOGOS preview runs as a separate Docker Compose service:

```text
logos-admin-preview-logos-admin-preview-1
```

Traefik routes:

```text
Host(`serendipity.83-150-204-190.sslip.io`) && PathPrefix(`/logos-admin`)
```

The route strips `/logos-admin` before forwarding to the preview server.

## Acceptance Criteria

- Existing Directus `/admin/` remains intact.
- LOGOS preview is reachable through the Serendipity domain.
- The browser page uses the prefixed API path.
- Directus stores a collection entry pointing to the LOGOS preview.
- No n8n, Directus, Postgres, Redis or Traefik container restart is performed.
- No VPS reboot is performed.

## Evidence

Public HTML smoke:

```text
GET /logos-admin/admin/ -> 200 LOGOS Admin Test
```

Public API smoke:

```text
POST /logos-admin/api/admin/preview -> preview_candidate
meaning_atom=Безопасность без давления возвращает ресурс для спокойного вклада в отношения.
```

Directus metadata:

```text
collection=cc_logos_admin_tools
hidden=false
item=LOGOS Meaning Preview
status=preview
```

Container status:

```text
logos-admin-preview-logos-admin-preview-1 running
serendipity-directus-1 still running
n8n-compose-n8n-1 still running
```

## Boundary

This is still a preview tool.

No GitHub issue was created from this route.
No YAML object was written.
No learning or law artifact was created.
No n8n workflow was activated.
