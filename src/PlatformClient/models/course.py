from http.client import HTTPResponse
from typing import TYPE_CHECKING
from ..query_builder import QueryBuilder
from ..types import SafeUUID, UserAccess
from ._default import BaseMethods, BaseClass

if TYPE_CHECKING:
    from ..client import PlatformClient


class CourseMethods(BaseMethods):
    path = "/CompanyBranchCourse"

    async def Get(self, branch_id: SafeUUID | str,
                  filter_query: None | dict | QueryBuilder = None):
        """
        Endpoint: /CompanyBranchCourse/CompanyBranchCourse/Get
        Body:
        ``{ "companyBranchId": branch_id, "data": filter_query }``
        """
        new_filter_query = filter_query or {}
        if isinstance(new_filter_query, QueryBuilder):
            new_filter_query = new_filter_query.build()
        return await self.client.send_request(
            f"{self.path}/Get",
            {"companyBranchId": branch_id, "data": new_filter_query}
        )

    async def GetDetails(self, branch_id: SafeUUID | str,
                         course_id: SafeUUID | str) -> HTTPResponse:
        """
        Endpoint: /CompanyBranchCourse/CompanyBranchCourse/GetDetails
        Body:
        ``{ "companyBranchId": branch_id, "courseId": course_id }``
        :param branch_id: Branch ID
        :param course_id: Course ID
        """
        return await self.client.send_request(
            f"{self.path}/GetDetails",
            { "companyBranchId": str(branch_id),
              "courseId": str(course_id) }
        )

    async def GetVariables(self, branch_id: SafeUUID | str,
                           course_id: SafeUUID | str) -> HTTPResponse:
        """
        Endpoint: /CompanyBranchCourse/CompanyBranchCourse/GetVariables
        Body:
        ``{ "companyBranchId": branch_id, "courseId": course_id }``
        :param branch_id: Branch ID
        :param course_id: Course ID
        """
        return await self.client.send_request(
            f"{self.path}/GetVariables",
            { "companyBranchId": str(branch_id),
              "courseId": str(course_id) }
        )


class BoundCourseMethods:
    def __init__(self, methods: CourseMethods, branch_id: SafeUUID | str):
        self.methods = methods
        self.branch_id = branch_id

    async def Get(self, filter_query=None):
        return await self.methods.Get(self.branch_id, filter_query)

    async def GetDetails(self, course_id: SafeUUID | str):
        return await self.methods.GetDetails(self.branch_id, course_id)

    async def GetVariables(self, course_id: SafeUUID | str):
        return await self.methods.GetVariables(self.branch_id, course_id)


class CourseClass(BaseClass[CourseMethods]):
    BranchId: SafeUUID

    def __init__(self, client: "PlatformClient", branch_id: SafeUUID | str,
                 course_id: SafeUUID | str):
        super().__init__(client, course_id, CourseMethods)
        self.BranchId = branch_id

    async def GetDetails(self):
        return await self.methods.GetDetails(self.BranchId, self.Id)

    async def GetVariables(self):
        return await self.methods.GetVariables(self.BranchId, self.Id)
