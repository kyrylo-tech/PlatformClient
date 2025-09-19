from http.client import HTTPResponse
from typing import TYPE_CHECKING

from ..query_builder import QueryBuilder
from ..types import SafeUUID, UserAccess
from ._default import BaseMethods, BaseClass

if TYPE_CHECKING:
    from ..client import PlatformClient


class LeadMethods(BaseMethods):
    path = "/CompanyBranchLead"

    async def GetList(self, branch_id: SafeUUID | str, filter_query: None | dict | QueryBuilder = None, is_my: bool = False):
        """
        Endpoint: /CompanyBranchLead/CompanyBranchLead/Get(My)

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

    async def GetDetails(self, branch_id: SafeUUID | str, lead_id: SafeUUID | str) -> HTTPResponse:
        """
        Endpoint: /CompanyBranchLead/CompanyBranchLead/GetDetails

        Body:
        ``{ "companyBranchId": branch_id, "LeadId": lead_id }``

        :param branch_id: Branch ID
        :param lead_id: Lead ID
        """
        return await self.client.send_request(
            f"{self.path}/GetDetails",
            { "CompanyBranchId": str(branch_id), "leadId": str(lead_id) }
        )

    async def GetLeadGroups(
            self,
            branch_id: SafeUUID | str,
            lead_id: SafeUUID | str,
            filter_query: None | dict | QueryBuilder = None
    ) -> HTTPResponse:
        """
        Endpoint: /CompanyBranchLead/GetLeadGroups

        Body:
        ``{
            "companyBranchId": branch_id,
            "leadId": lead_id,
            "data": filter_query
        }``

        :param branch_id: Branch ID
        :param lead_id: Lead ID
        :param filter_query: Optional filter
        """
        new_filter_query = filter_query or {}
        if isinstance(new_filter_query, QueryBuilder):
            new_filter_query = new_filter_query.build()

        return await self.client.send_request(
            f"{self.path}/GetLeadGroups",
            {
                "companyBranchId": str(branch_id),
                "leadId": str(lead_id),
                "data": new_filter_query
            }
        )



class BoundLeadMethods:
    def __init__(self, methods: LeadMethods, branch_id: SafeUUID | str):
        self.methods = methods
        self.branch_id = branch_id

    async def GetList(self, filter_query=None, is_my: bool = False):
        return await self.methods.GetList(self.branch_id, filter_query, is_my=is_my)

    async def GetDetails(self, lead_id: SafeUUID | str):
        return await self.methods.GetDetails(self.branch_id, lead_id)

    async def GetLeadGroups(self, lead_id: SafeUUID | str, filter_query=None):
        return await self.methods.GetLeadGroups(
            self.branch_id,
            lead_id,
            filter_query=filter_query
        )


class LeadClass(BaseClass[LeadMethods]):
    BranchId: SafeUUID

    def __init__(self, client: "PlatformClient", branch_id: SafeUUID | str, lead_id: SafeUUID | str):
        super().__init__(client, lead_id, LeadMethods)
        self.BranchId = branch_id

    async def GetDetails(self):
        return await self.methods.GetDetails(self.BranchId, self.Id)