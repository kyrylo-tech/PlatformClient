from http.client import HTTPResponse
from typing import TYPE_CHECKING

from ._default import BaseMethods, BaseClass
from ..query_builder import QueryBuilder
from ..types import SafeUUID

if TYPE_CHECKING:
    from ..client import PlatformClient


class TagMethods(BaseMethods):
    path = "/CompanyBranchTag"

    async def Get(self, branch_id: SafeUUID | str,
                  filter_query: None | dict | QueryBuilder = None):
        """
        Endpoint: /CompanyBranchTag/CompanyBranchTag/Get
        Body:
        ``{ "companyBranchId": branch_id, "data": filter_query }``
        """
        new_filter_query = filter_query or {}
        if isinstance(new_filter_query, QueryBuilder):
            new_filter_query = new_filter_query.build()
        return await self.client.send_request(
            f"{self.path}/Get",
            {"companyBranchId": branch_id, "data": new_filter_query }
        )

    async def GetDetails(self, branch_id: SafeUUID | str,
                         tag_id: SafeUUID | str) -> HTTPResponse:
        """
        Endpoint: /CompanyBranchTag/CompanyBranchTag/GetDetails
        Body:
        ``{ "companyBranchId": branch_id, "tagId": tag_id }``
        :param branch_id: Branch ID
        :param tag_id: Tag ID
        """
        return await self.client.send_request(
            f"{self.path}/GetDetails",
            { "companyBranchId": str(branch_id), "tagId": str(tag_id) }
        )


class BoundTagMethods:
    def __init__(self, methods: TagMethods, branch_id: SafeUUID | str):
        self.methods = methods
        self.branch_id = branch_id

    async def Get(self, filter_query=None):
        return await self.methods.Get(self.branch_id, filter_query)

    async def GetDetails(self, tag_id: SafeUUID | str):
        return await self.methods.GetDetails(self.branch_id, tag_id)


class TagClass(BaseClass[TagMethods]):
    BranchId: SafeUUID

    def __init__(self, client: "PlatformClient",
                 branch_id: SafeUUID | str, tag_id: SafeUUID | str):
        super().__init__(client, tag_id, TagMethods)
        self.BranchId = branch_id

    async def GetDetails(self):
        return await self.methods.GetDetails(self.BranchId, self.Id)