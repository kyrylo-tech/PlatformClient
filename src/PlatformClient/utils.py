import http.client
import json
import re
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .client import PlatformClient


class PlatformResponse:
    def __init__(self, resp: http.client.HTTPResponse):
        self._raw: bytes = resp.read()
        self.status: int = resp.status
        self.reason: str = resp.reason
        self.headers: dict[str, str] = {k: v for k, v in resp.getheaders()}
        self.ok: bool = 200 <= resp.status < 300

    def _encoding(self) -> str:
        ct = self.headers.get("Content-Type", "")
        m = re.search(r"charset=([^\s;]+)", ct, re.I)
        return (m.group(1) if m else "utf-8").strip('"').strip()

    def text(self, errors: str = "strict") -> str:
        return self._raw.decode(self._encoding(), errors=errors)

    def json(self) -> dict:
        try:
            return json.loads(self.text())
        except json.JSONDecodeError as e:
            snippet = self._raw[:200].decode(self._encoding(), errors="replace")
            raise ValueError(f"Response is not valid JSON (status {self.status}): {snippet}") from e

    def bytes(self) -> bytes:
        return self._raw


def sync_request(
    client: "PlatformClient",
    endpoint: str,
    body: dict | str | None = None,
    *,
    method: str = "POST",
    timeout: Optional[float] = 30.0,
) -> PlatformResponse:
    headers = {
        "Content-Type": "application/json",
        "api_id": str(client.api_id),
        "api_access_token": client.api_access_token,
    }

    if isinstance(body, dict):
        body_data = json.dumps(body)
    elif isinstance(body, str):
        body_data = body
    else:
        body_data = "{}"

    conn = http.client.HTTPSConnection(client.host, timeout=timeout)
    try:
        if getattr(client, "debug_logs", False):
            print(f"[⌛] {client.host}{endpoint} : {headers} : {body_data}")

        conn.request(method.upper(), endpoint, body=body_data, headers=headers)
        resp = conn.getresponse()
        return PlatformResponse(resp)
    finally:
        conn.close()
