#!/usr/bin/env python3
"""Run the local LOGOS admin test window."""

from __future__ import annotations

import argparse
import json
import mimetypes
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from logos_engine.admin_test import build_admin_preview  # noqa: E402


ADMIN_ROOT = ROOT / "admin"


class AdminHandler(BaseHTTPRequestHandler):
    server_version = "LOGOSAdminTest/0.1"

    def do_GET(self) -> None:  # noqa: N802
        if self.path in {"/", "/admin", "/admin/"}:
            self._send_file(ADMIN_ROOT / "meaning-test-admin.html")
            return
        if self.path.startswith("/admin/"):
            requested = self.path.split("?", 1)[0].removeprefix("/admin/")
            target = (ADMIN_ROOT / requested).resolve()
            if ADMIN_ROOT.resolve() in target.parents and target.exists():
                self._send_file(target)
                return
        self._send_json({"error": "not found"}, status=404)

    def do_POST(self) -> None:  # noqa: N802
        if self.path != "/api/admin/preview":
            self._send_json({"error": "not found"}, status=404)
            return

        try:
            payload = self._read_json()
            preview = build_admin_preview(payload)
        except Exception as exc:  # noqa: BLE001
            self._send_json({"error": str(exc)}, status=400)
            return

        self._send_json(preview.to_dict())

    def log_message(self, format: str, *args: Any) -> None:
        sys.stderr.write("%s - %s\n" % (self.address_string(), format % args))

    def _read_json(self) -> dict[str, Any]:
        raw_length = self.headers.get("Content-Length", "0")
        try:
            length = int(raw_length)
        except ValueError as exc:
            raise ValueError("invalid Content-Length") from exc
        raw = self.rfile.read(length)
        data = json.loads(raw.decode("utf-8"))
        if not isinstance(data, dict):
            raise ValueError("request body must be a JSON object")
        return data

    def _send_file(self, path: Path) -> None:
        content = path.read_bytes()
        content_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        self.send_response(200)
        self.send_header("Content-Type", f"{content_type}; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def _send_json(self, payload: dict[str, Any], status: int = 200) -> None:
        content = json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args(argv)

    server = ThreadingHTTPServer((args.host, args.port), AdminHandler)
    print(f"LOGOS admin test window: http://{args.host}:{args.port}/admin/")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping LOGOS admin test window.")
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
