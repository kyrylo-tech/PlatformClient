from http.client import HTTPResponse
from typing import TYPE_CHECKING

from ..query_builder import QueryBuilder
from ..types import SafeUUID, UserAccess
from ._default import BaseMethods, BaseClass

if TYPE_CHECKING:
    from ..client import PlatformClient


class APIMethods(BaseMethods):
    path = "/CompanyBranchAPI"

    async def GetList(self, branch_id: SafeUUID | str, filter_query: None | dict | QueryBuilder = None):
        """
        Endpoint: /CompanyBranchAPI/CompanyBranchAPI/Get

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

    async def GetDetails(self, branch_id: SafeUUID | str, api_id: SafeUUID | str) -> HTTPResponse:
        """
        Endpoint: /CompanyBranchAPI/CompanyBranchAPI/GetDetails

        Body:
        ``{ "companyBranchId": branch_id, "apiId": api_id }``

        :param branch_id: Branch ID
        :param api_id: API ID
        """
        return await self.client.send_request(
            f"{self.path}/GetDetails",
            { "CompanyBranchId": str(branch_id), "ApiId": str(api_id) }
        )

    async def Create(self, branch_id: SafeUUID | str, name: str, access: list[UserAccess]) -> HTTPResponse:
        """
        Endpoint: /CompanyBranchAPI/CompanyBranchAPI/Create

        Body:
        ``{ "companyBranchId": branch_id, "data": { "name": name, "access": access } }``

        :param branch_id:
        :param name:
        :param access:
        :return:
        """
        return await self.client.send_request(
            f"{self.path}/Create",
            {"CompanyBranchId": str(branch_id), "Data": {"Name": name, "Access": access} }
        )

    async def Edit(self, branch_id: SafeUUID | str, api_id: SafeUUID | str, new_name: str = None, new_access: list[UserAccess] = None) -> HTTPResponse:
        """
        Endpoint: /CompanyBranchAPI/CompanyBranchAPI/ResetToken

        Body:
        ``{ "companyBranchId": branch_id, "data": { "name": new_name, "access": new_access }, "apiId": api_id }``

        :param branch_id: Branch ID
        :param api_id: API ID
        :param new_name: Name that rewrites on new_name
        :param new_access: Access list that rewrites on new_access
        """
        return await self.client.send_request(
            f"{self.path}/Edit",
            { "CompanyBranchId": str(branch_id), "Data": { "Name": new_name, "Access": new_access }, "ApiId": str(api_id) }
        )

    async def ResetToken(self, branch_id: SafeUUID | str, api_id: SafeUUID | str) -> HTTPResponse:
        """
        Endpoint: /CompanyBranchAPI/CompanyBranchAPI/ResetToken

        Body:
        ``{ "companyBranchId": branch_id, "apiId": api_id }``

        :param branch_id: Branch ID
        :param api_id: API ID
        """
        return await self.client.send_request(
            f"{self.path}/ResetToken",
            { "CompanyBranchId": str(branch_id), "ApiId": str(api_id) }
        )

    async def Remove(self, branch_id: SafeUUID | str, api_id: SafeUUID | str):
        """
        Endpoint: /CompanyBranchAPI/CompanyBranchAPI/Remove

        Body:
        ``{ "companyBranchId": branch_id, "apiId": api_id }``

        :param branch_id:
        :param api_id:
        """
        return await self.client.send_request(
            f"{self.path}/Remove",
            { "CompanyBranchId": str(branch_id), "ApiId": str(api_id) }
        )

    async def GetVariables(self, branch_id: SafeUUID | str, api_id: SafeUUID | str):
        """
        Endpoint: /CompanyBranchAPI/CompanyBranchAPI/GetVariables
        :param branch_id:
        :param api_id:
        :return:
        """
        return await self.client.send_request(
            f"{self.path}/GetVariables",
            { "CompanyBranchId": str(branch_id), "ApiId": str(api_id) }
        )

    async def SetVariable(self, branch_id: SafeUUID | str, api_id: SafeUUID | str, name: str, value: str):
        """
        Endpoint: /CompanyBranchAPI/CompanyBranchAPI/SetVariable
        :param branch_id:
        :param api_id:
        :param name: Variable name
        :param value: Variable value
        :return:
        """
        return await self.client.send_request(
            f"{self.path}/SetVariable",
            { "CompanyBranchId": str(branch_id), "ApiId": str(api_id), "Data": { "Name": name, "Value": value } }
        )

    async def SetVariables(self, branch_id: SafeUUID | str, api_id: SafeUUID | str, variables: list[dict[str, str]]):
        """
        Endpoint: /CompanyBranchAPI/CompanyBranchAPI/SetVariables
        :param branch_id:
        :param api_id:
        :param variables:
        :return:
        """
        return await self.client.send_request(
            f"{self.path}/SetVariables",
            {"CompanyBranchId": str(branch_id), "ApiId": str(api_id), "Data": variables }
        )



class BoundAPIMethods:
    def __init__(self, methods: APIMethods, branch_id: SafeUUID | str):
        self.methods = methods
        self.branch_id = branch_id

    async def GetList(self, filter_query=None):
        return await self.methods.GetList(self.branch_id, filter_query)

    async def Create(self, name: str, access: list[UserAccess]):
        return await self.methods.Create(self.branch_id, name, access)

    async def Edit(self, api_id: SafeUUID | str, new_name=None, new_access=None):
        return await self.methods.Edit(self.branch_id, api_id, new_name, new_access)

    async def GetDetails(self, api_id: SafeUUID | str):
        return await self.methods.GetDetails(self.branch_id, api_id)

    async def ResetToken(self, api_id: SafeUUID | str):
        return await self.methods.ResetToken(self.branch_id, api_id)

    async def Remove(self, api_id: SafeUUID | str):
        return await self.methods.Remove(self.branch_id, api_id)

    async def GetVariables(self, api_id: SafeUUID | str):
        return await self.methods.GetVariables(self.branch_id, api_id)

    async def SetVariable(self, api_id: SafeUUID | str, name: str, value: str):
        return await self.methods.SetVariable(self.branch_id, api_id, name, value)

    async def SetVariables(self, api_id: SafeUUID | str, variables: list[dict[str, str]]):
        return await self.methods.SetVariables(self.branch_id, api_id, variables)


class APIClass(BaseClass[APIMethods]):
    BranchId: SafeUUID

    def __init__(self, client: "PlatformClient", branch_id: SafeUUID | str, api_id: SafeUUID | str):
        super().__init__(client, api_id, APIMethods)
        self.BranchId = branch_id

    async def GetDetails(self):
        return await self.methods.GetDetails(self.BranchId, self.Id)

    async def Edit(self, name: str = None, access: list[str] = None) -> HTTPResponse:
        return await self.methods.Edit(self.BranchId, self.Id, new_name=name, new_access=access)

    async def ResetToken(self):
        return await self.methods.ResetToken(self.BranchId, self.Id)

    async def Remove(self):
        return await self.methods.Remove(self.BranchId, self.Id)

    async def GetVariables(self):
        return await self.methods.GetVariables(self.BranchId, self.Id)

    async def SetVariable(self, name: str, value: str):
        return await self.methods.SetVariable(self.BranchId, self.Id, name, value)

    async def SetVariables(self, variables: list[dict[str, str]]):
        return await self.methods.SetVariables(self.BranchId, self.Id, variables)
