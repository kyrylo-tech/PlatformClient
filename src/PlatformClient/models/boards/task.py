from http.client import HTTPResponse
from typing import TYPE_CHECKING

from ...query_builder import QueryBuilder
from ...types import SafeUUID, UserAccess
from .._default import BaseMethods, BaseClass

if TYPE_CHECKING:
    from ...client import PlatformClient


class TaskMethods(BaseMethods):
    path = "/CompanyBranchTask"

    async def GetList(self, branch_id: SafeUUID | str, filter_query: None | dict | QueryBuilder = None, is_my: bool = False):
        """
        Endpoint: /CompanyBranchTask/CompanyBranchTask/Get

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

    async def GetDetails(self, branch_id: SafeUUID | str, task_id: SafeUUID | str):
        """
        Endpoint: /CompanyBranchTask/CompanyBranchTask/GetDetails

        Body:
        ``{ "companyBranchId": branch_id, "TaskId": task_id }``

        :param branch_id: Branch ID
        :param task_id: Task ID
        """
        return await self.client.send_request(
            f"{self.path}/GetDetails",
            { "CompanyBranchId": str(branch_id), "taskId": str(task_id) }
        )






class BoundTaskMethods:
    def __init__(self, methods: TaskMethods, branch_id: SafeUUID | str):
        self.methods = methods
        self.branch_id = branch_id

    async def GetDetails(self, role_id: SafeUUID | str):
        return await self.methods.GetDetails(self.branch_id, role_id)



class TaskClass(BaseClass[TaskMethods]):
    BranchId: SafeUUID

    def __init__(self, client: "PlatformClient", branch_id: SafeUUID | str, role_id: SafeUUID | str):
        super().__init__(client, role_id, TaskMethods)
        self.BranchId = branch_id

    def GetTask(self, task_id: SafeUUID | str):
        task = TaskClass(self.client, self.BranchId, self.Id, task_id)
        return task

    async def GetDetails(self):
        return await self.methods.GetDetails(self.BranchId, self.Id)
