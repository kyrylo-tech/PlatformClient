from http.client import HTTPResponse
from typing import TYPE_CHECKING

from .task import TaskClass
from ...query_builder import QueryBuilder
from ...types import SafeUUID, UserAccess
from .._default import BaseMethods, BaseClass

if TYPE_CHECKING:
    from ...client import PlatformClient


class SprintMethods(BaseMethods):
    path = "/CompanyBranchBoard/"

    async def GetList(self, branch_id: SafeUUID | str, filter_query: None | dict | QueryBuilder = None, is_my: bool = False):
        """
        Endpoint: /CompanyBranchSprint/CompanyBranchSprint/Get

        Body:
        ``{ "companyBranchId": branch_id, "data": filter_query }``
        """
        new_filter_query = filter_query or {}
        if isinstance(new_filter_query, QueryBuilder):
            new_filter_query = new_filter_query.build()

        path = "Get"
        if is_my: path += "My"

        return await self.client.send_request(
            f"{self.path}/{path}",
            { "companyBranchId": branch_id, "data": new_filter_query }
        )

    async def GetDetails(self, branch_id: SafeUUID | str, sprint_id: SafeUUID | str):
        """
        Endpoint: /CompanyBranchSprint/CompanyBranchSprint/GetDetails

        Body:
        ``{ "companyBranchId": branch_id, "SprintId": sprint_id }``

        :param branch_id: Branch ID
        :param sprint_id: Sprint ID
        """
        return await self.client.send_request(
            f"{self.path}/GetDetails",
            { "CompanyBranchId": str(branch_id), "sprintId": str(sprint_id) }
        )




class BoundSprintMethods:
    def __init__(self, methods: SprintMethods, branch_id: SafeUUID | str, board_id: SafeUUID | str):
        self.methods = methods
        self.branch_id = branch_id
        self.board_id = board_id




class SprintClass(BaseClass[SprintMethods]):
    BranchId: SafeUUID

    def __init__(self, client: "PlatformClient", branch_id: SafeUUID | str, sprint_id: SafeUUID | str):
        super().__init__(client, sprint_id, SprintMethods)
        self.BranchId = branch_id

    def GetTask(self, task_id: SafeUUID | str):
        return TaskClass(self.client, self.BranchId, self.Id, task_id)


    async def GetDetails(self):
        return await self.methods.GetDetails(self.BranchId, self.Id)

    async def Edit(self, name: str, description: str = "",
            manager_user_id: SafeUUID | str = None, have_sprints: bool = True, have_sprints: bool = True, have_users: bool = True, frozen: bool = False):
            return await self.methods.Edit(self.BranchId, self.Id, name, description,
                manager_user_id, have_sprints, have_sprints, have_users, frozen)

    async def Create(self, name: str, description: str = "",
            manager_user_id: SafeUUID | str = None, have_sprints: bool = True, have_sprints: bool = True, have_users: bool = True):
            return await self.methods.Create(self.BranchId, self.Id, name, description,
                manager_user_id, have_sprints, have_sprints, have_users)