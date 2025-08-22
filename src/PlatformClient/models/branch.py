from typing import TYPE_CHECKING

from ._default import BaseClass, BaseMethods
from .api import APIClass, APIMethods, BoundAPIMethods
from .lead import LeadClass, LeadMethods, BoundLeadMethods
from .manager import ManagerMethods, BoundManagerMethods
from .member_content import BoundMemberContent, MemberContentMethods
from .role import RoleMethods, BoundRoleMethods
from .teacher import TeacherClass, TeacherMethods, BoundTeacherMethods
from ..types import SafeUUID


if TYPE_CHECKING:
    from ..client import PlatformClient

class BranchMethods(BaseMethods):
    path = "CompanyBranch"

    def __init__(self, client: "PlatformClient"):
        super().__init__(client)
        self.API = APIMethods(client)
        self.Leads = LeadMethods(client)
        self.Teachers = TeacherMethods(client)
        self.Managers = ManagerMethods(client)
        self.MemberContent = MemberContentMethods(client)
        self.Roles = RoleMethods(client)

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
        self.Leads = BoundLeadMethods(LeadMethods(client), branch_id)
        self.Teachers = BoundTeacherMethods(TeacherMethods(client), branch_id)
        self.Managers = BoundManagerMethods(ManagerMethods(client), branch_id)
        self.MemberContent = BoundMemberContent(MemberContentMethods(client), branch_id)
        self.Roles = BoundRoleMethods(RoleMethods(client), branch_id)

    def GetAPI(self, api_id: SafeUUID | str) -> APIClass:
        return APIClass(self.client, self.Id, api_id)

    def GetLead(self, lead_id: SafeUUID | str):
        return LeadClass(self.client, self.Id, lead_id)

    def GetTeacher(self, teacher_id: SafeUUID | str):
        return TeacherClass(self.client, self.Id, teacher_id)

    async def GetAccess(self):
        return await self.methods.GetAccess(self.Id)

