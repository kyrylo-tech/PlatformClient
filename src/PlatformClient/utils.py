import http.client
import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .client import PlatformClient


def sync_request(client: "PlatformClient",
                 endpoint: str,
                 body: dict | str | None = None
) -> http.client.HTTPResponse:
    headers = {
        'Content-Type': 'application/json',
        "api_id": str(client.api_id),
        "api_access_token": client.api_access_token
    }
    body_data = body if body is not None else {}
    if isinstance(body, dict): body_data = json.dumps(body)

    try:
        conn = http.client.HTTPSConnection(client.host)

        if client.debug_logs:
            print(f"[⌛] {client.host}{endpoint} : {headers} : {body_data}")

        conn.request("POST", endpoint, body=body_data, headers=headers)
        response = conn.getresponse()
        return response
    except Exception as e:
        raise e