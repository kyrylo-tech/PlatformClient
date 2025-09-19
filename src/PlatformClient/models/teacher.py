from http.client import HTTPResponse
from typing import TYPE_CHECKING

from ..query_builder import QueryBuilder
from ..types import SafeUUID, UserAccess
from ._default import BaseMethods, BaseClass

if TYPE_CHECKING:
    from ..client import PlatformClient


class TeacherMethods(BaseMethods):
    path = "/CompanyBranchTeacher"

    async def GetList(self, branch_id: SafeUUID | str,
                      filter_query: None | dict | QueryBuilder = None,
                      is_my: bool = False):
        """
        Endpoint: /CompanyBranchTeacher/CompanyBranchTeacher/Get(My)

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
            {"companyBranchId": branch_id, "data": new_filter_query}
        )

    async def GetDetails(self, branch_id: SafeUUID | str,
                         teacher_id: SafeUUID | str) -> HTTPResponse:
        """
        Endpoint: /CompanyBranchTeacher/CompanyBranchTeacher/GetDetails

        Body:
        ``{ "companyBranchId": branch_id, "TeacherId": teacher_id }``

        :param branch_id: Branch ID
        :param teacher_id: Teacher ID
        """
        return await self.client.send_request(
            f"{self.path}/GetDetails",
            {"CompanyBranchId": str(branch_id),
             "teacherId": str(teacher_id)}
        )

    async def GetScheduleItemList(
            self, branch_id: SafeUUID | str,
            teacher_id: SafeUUID | str,
            filter_query: None | dict | QueryBuilder = None) -> HTTPResponse:
        """
        Endpoint: /CompanyBranchTeacher/GetScheduleItemList

        Body:
        ``{ "companyBranchId": branch_id,
        "data": filter_query,
        "teacherId": teacher_id }``

        :param branch_id: Branch ID
        :param teacher_id: Teacher ID
        :param filter_query: Filter query data
        """
        new_filter_query = filter_query or {}
        if isinstance(new_filter_query, QueryBuilder):
            new_filter_query = new_filter_query.build()

        return await self.client.send_request(
            f"{self.path}/GetScheduleItemList",
            {"companyBranchId": str(branch_id),
             "data": new_filter_query,
             "teacherId": str(teacher_id)}
        )

    async def GetSchedule(
            self, branch_id: SafeUUID | str,
            teacher_id: SafeUUID | str,
            filter_query: None | dict | QueryBuilder = None) -> HTTPResponse:
        """
        Endpoint: /CompanyBranchTeacher/CompanyBranchTeacher/GetSchedule

        Body:
        ``{ "companyBranchId": branch_id, "data": filter_query, "teacherId": teacher_id }``

        :param branch_id: Branch ID
        :param teacher_id: Teacher ID
        :param filter_query: Filter query data (e.g., {"from": "2025-08-28", "to": "2025-09-15"})
        """
        new_filter_query = filter_query or {}
        if isinstance(new_filter_query, QueryBuilder):
            new_filter_query = new_filter_query.build()

        return await self.client.send_request(
            f"{self.path}/GetSchedule",
            {"companyBranchId": str(branch_id),
             "data": new_filter_query,
             "teacherId": str(teacher_id)}
        )


class BoundTeacherMethods:
    def __init__(self, methods: TeacherMethods, branch_id: SafeUUID | str):
        self.methods = methods
        self.branch_id = branch_id

    async def GetList(self, filter_query=None, is_my: bool = False):
        return await self.methods.GetList(self.branch_id, filter_query,
                                          is_my=is_my)

    async def GetDetails(self, teacher_id: SafeUUID | str):
        return await self.methods.GetDetails(self.branch_id, teacher_id)

    async def GetScheduleItemList(self, teacher_id: SafeUUID | str,
                                  filter_query=None):
        return await self.methods.GetScheduleItemList(self.branch_id,
                                                      teacher_id, filter_query)

    async def GetSchedule(self, teacher_id: SafeUUID | str, filter_query=None):
        return await self.methods.GetSchedule(self.branch_id, teacher_id,
                                              filter_query)


class TeacherClass(BaseClass[TeacherMethods]):
    BranchId: SafeUUID

    def __init__(self, client: "PlatformClient", branch_id: SafeUUID | str,
                 teacher_id: SafeUUID | str):
        super().__init__(client, teacher_id, TeacherMethods)
        self.BranchId = branch_id

    async def GetDetails(self):
        return await self.methods.GetDetails(self.BranchId, self.Id)

    async def GetScheduleItemList(self, filter_query=None):
        return await self.methods.GetScheduleItemList(self.BranchId, self.Id,
                                                      filter_query)

    async def GetSchedule(self, filter_query=None):
        return await self.methods.GetSchedule(self.BranchId, self.Id,
                                              filter_query)
