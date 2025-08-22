from http.client import HTTPResponse
from typing import TYPE_CHECKING

from ..query_builder import QueryBuilder
from ..types import SafeUUID, UserAccess
from ._default import BaseMethods, BaseClass

if TYPE_CHECKING:
    from ..client import PlatformClient


class ManagerMethods(BaseMethods):
    path = "/CompanyBranchManager"

    async def GetList(self, branch_id: SafeUUID | str, filter_query: None | dict | QueryBuilder = None):
        """
        Endpoint: /CompanyBranchManager/CompanyBranchManager/Get

        Body:
        ``{ "companyBranchId": branch_id, "data": filter_query }``
        """
        new_filter_query = filter_query or {}
        if isinstance(new_filter_query, QueryBuilder):
            new_filter_query = new_filter_query.build()

        return await self.client.send_request(
            f"{self.path}/Get",
            { "companyBranchId": branch_id, "data": new_filter_query }
        )

    async def GetDetails(self, branch_id: SafeUUID | str, manager_id: SafeUUID | str) -> HTTPResponse:
        """
        Endpoint: /CompanyBranchManager/CompanyBranchManager/GetDetails

        Body:
        ``{ "companyBranchId": branch_id, "ManagerId": manager_id }``

        :param branch_id: Branch ID
        :param manager_id: Manager ID
        """
        return await self.client.send_request(
            f"{self.path}/GetDetails",
            { "CompanyBranchId": str(branch_id), "managerId": str(manager_id) }
        )



class BoundManagerMethods:
    def __init__(self, methods: ManagerMethods, branch_id: SafeUUID | str):
        self.methods = methods
        self.branch_id = branch_id

    async def GetList(self, filter_query=None):
        return await self.methods.GetList(self.branch_id, filter_query)

    async def GetDetails(self, manager_id: SafeUUID | str):
        return await self.methods.GetDetails(self.branch_id, manager_id)


class ManagerClass(BaseClass[ManagerMethods]):
    BranchId: SafeUUID

    def __init__(self, client: "PlatformClient", branch_id: SafeUUID | str, manager_id: SafeUUID | str):
        super().__init__(client, manager_id, ManagerMethods)
        self.BranchId = branch_id

    async def GetDetails(self):
        return await self.methods.GetDetails(self.BranchId, self.Id)