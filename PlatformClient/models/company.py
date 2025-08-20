from typing import TYPE_CHECKING

from ._default import BaseClass, BaseMethods
from .branch import BranchMethods, BranchClass
from ..types import SafeUUID


if TYPE_CHECKING:
    from ..client import PlatformClient

class CompanyMethods(BaseMethods):
    path = "Company"

    def __init__(self, client: "PlatformClient"):
        super().__init__(client)
        self.Branch = BranchMethods(client)

    def GetBranch(self, branch_id: SafeUUID | str):
        return BranchClass(self.client, branch_id)

    async def GetAccess(self, branch_id: SafeUUID | str):
        return await self.client.send_request(
            f"/{self.path}/GetAccess",
            str(branch_id)
        )

class CompanyClass(BaseClass[CompanyMethods]):
    path = "Company"

    def __init__(self, client: "PlatformClient", company_id: SafeUUID | str):
        super().__init__(client, company_id, CompanyMethods)

    def GetBranch(self, branch_id: SafeUUID | str):
        return BranchClass(self.client, branch_id)

    async def GetAccess(self):
        return await self.methods.GetAccess(self.Id)


