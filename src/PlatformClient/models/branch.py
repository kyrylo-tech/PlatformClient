from typing import TYPE_CHECKING

from ._default import BaseClass, BaseMethods
from .api import APIClass, APIMethods, BoundAPIMethods
from .member_content import BoundMemberContent, MemberContentMethods
from ..types import SafeUUID


if TYPE_CHECKING:
    from ..client import PlatformClient

class BranchMethods(BaseMethods):
    path = "CompanyBranch"

    def __init__(self, client: "PlatformClient"):
        super().__init__(client)
        self.API = APIMethods(client)
        self.MemberContent = MemberContentMethods(client)

    async def GetAccess(self, branch_id: SafeUUID | str):
        return await self.client.send_request(
            f"/{self.path}/GetAccess",
            str(branch_id)
        )

class BranchClass(BaseClass[BranchMethods]):
    path = "CompanyBranch"

    def __init__(self, client: "PlatformClient", branch_id: SafeUUID | str):
        super().__init__(client, branch_id, BranchMethods)
        self.API = BoundAPIMethods(APIMethods(client), branch_id)
        self.MemberContent = BoundMemberContent(MemberContentMethods(client), branch_id)

    def GetAPI(self, api_id: SafeUUID | str) -> APIClass:
        return APIClass(self.client, self.Id, api_id)

    async def GetAccess(self):
        return await self.methods.GetAccess(self.Id)

