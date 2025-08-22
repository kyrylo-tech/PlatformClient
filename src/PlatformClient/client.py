import asyncio
from http.client import HTTPResponse
from urllib.parse import urlparse

from .models.branch import BranchMethods, BranchClass
from .models.company import CompanyMethods
from .types import SafeUUID
from .utils import PlatformResponse


class PlatformClient:
    def __init__(self, url: str, api_id: SafeUUID | str, api_access_token: str):
        if not url.startswith("https://"):
            raise ValueError("URL must start with https://")

        parsed = urlparse(url)

        self.host: str = parsed.netloc
        self.base_path: str = parsed.path or ""

        self.api_id: SafeUUID = SafeUUID(api_id)
        self.api_access_token: str = api_access_token

        self.debug_logs = False

        self.Company = CompanyMethods(self)
        self.Branch = BranchMethods(self)

    def GetBranch(self, branch_id: SafeUUID | str):
        return BranchClass(self, branch_id)

    async def send_request(self, endpoint: str, params: dict | str | None = None) -> PlatformResponse:
        from .utils import sync_request
        path = f"{self.base_path}{endpoint}"
        return await asyncio.to_thread(sync_request, self, path, params)