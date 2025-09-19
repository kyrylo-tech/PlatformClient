from http.client import HTTPResponse
from typing import TYPE_CHECKING, List, Dict, Optional

from ..query_builder import QueryBuilder
from ..types import SafeUUID
from ._default import BaseMethods, BaseClass

if TYPE_CHECKING:
    from ..client import PlatformClient


class GroupMethods(BaseMethods):
    path = "/CompanyBranchGroup"

    async def Get(self, branch_id: SafeUUID | str,
                  filter_query: None | dict | QueryBuilder = None) -> HTTPResponse:
        """
        Endpoint: /CompanyBranchGroup/Get

        Body:
        ``{ "companyBranchId": branch_id, "data": filter_query }``

        :param branch_id: Company Branch ID
        :param filter_query: Optional filter data
        """
        new_filter_query = filter_query or {}
        if isinstance(new_filter_query, QueryBuilder):
            new_filter_query = new_filter_query.build()

        return await self.client.send_request(
            f"{self.path}/Get",
            { "companyBranchId": str(branch_id),
              "data": new_filter_query }
        )

    async def GetDetails(self, branch_id: SafeUUID | str,
                         group_id: SafeUUID | str) -> HTTPResponse:
        """
        Endpoint: /CompanyBranchGroup/GetDetails

        Body:
        ``{ "companyBranchId": branch_id, "groupId": group_id }``

        :param branch_id: Company Branch ID
        :param group_id: Group ID
        """
        return await self.client.send_request(
            f"{self.path}/GetDetails",
            { "companyBranchId": str(branch_id),
              "groupId": str(group_id) }
        )

    from http.client import HTTPResponse
    from typing import TYPE_CHECKING, List, Dict, Optional

    from ..query_builder import QueryBuilder
    from ..types import SafeUUID
    from ._default import BaseMethods, BaseClass

    if TYPE_CHECKING:
        from ..client import PlatformClient

    class GroupMethods(BaseMethods):
        path = "/CompanyBranchGroup"

        async def Get(self, branch_id: SafeUUID | str,
                      filter_query: None | dict | QueryBuilder = None) -> HTTPResponse:
            """
            Endpoint: /CompanyBranchGroup/Get

            Body:
            ``{ "companyBranchId": branch_id, "data": filter_query }``

            :param branch_id: Company Branch ID
            :param filter_query: Optional filter data
            """
            new_filter_query = filter_query or {}
            if isinstance(new_filter_query, QueryBuilder):
                new_filter_query = new_filter_query.build()

            return await self.client.send_request(
                f"{self.path}/Get",
                {"companyBranchId": str(branch_id),
                 "data": new_filter_query}
            )

    async def Create(
            self,
            branch_id: SafeUUID | str,
            name: str,
            student_list: List[Dict[str, SafeUUID | str]],
            teacher_list: List[Dict[str, SafeUUID | str]],
            lesson_id: Optional[SafeUUID | str] = None,
            course_id: Optional[SafeUUID | str] = None
    ) -> HTTPResponse:
        """
        Endpoint: /CompanyBranchGroup/Create

        Body:
        ``{
            "companyBranchId": branch_id,
            "data": {
                "name": name,
                "lessonId": lesson_id,  # optional
                "courseId": course_id,  # optional
                "studentList": [{"studentUserId": "id"}, ...],
                "teacherList": [{"teacherUserId": "id"}, ...]
            }
        }``

        :param branch_id: Company Branch ID
        :param name: Group name
        :param student_list: List of student IDs in format
        [{"studentUserId": "id"}, ...]
        :param teacher_list: List of teacher IDs in format
        [{"teacherUserId": "id"}, ...]
        :param lesson_id: Optional lesson ID
        :param course_id: Optional course ID
        """
        data = {
            "name": name,
            "studentList": [
                {"studentUserId": str(student["studentUserId"])} for
                student in student_list],
            "teacherList": [
                {"teacherUserId": str(teacher["teacherUserId"])} for
                teacher in teacher_list]
        }

        if lesson_id is not None:
            data["lessonId"] = str(lesson_id)

        if course_id is not None:
            data["courseId"] = str(course_id)

        return await self.client.send_request(
            f"{self.path}/Create",
            {"companyBranchId": str(branch_id), "data": data}
        )


class BoundGroupMethods:
    def __init__(self, methods: GroupMethods, branch_id: SafeUUID | str):
        self.methods = methods
        self.branch_id = branch_id

    async def Get(self, filter_query=None):
        """Get groups with optional filter"""
        return await self.methods.Get(self.branch_id, filter_query)

    async def GetDetails(self, group_id: SafeUUID | str):
        """Get group details by ID"""
        return await self.methods.GetDetails(self.branch_id, group_id)

    async def Create(
            self,
            name: str,
            student_list: List[Dict[str, SafeUUID | str]],
            teacher_list: List[Dict[str, SafeUUID | str]],
            lesson_id: Optional[SafeUUID | str] = None,
            course_id: Optional[SafeUUID | str] = None
    ):
        """Create a new group"""
        return await self.methods.Create(
            self.branch_id, name, student_list, teacher_list, lesson_id,
            course_id
        )


class GroupClass(BaseClass[GroupMethods]):
    BranchId: SafeUUID

    def __init__(self, client: "PlatformClient", branch_id: SafeUUID | str,
                 group_id: SafeUUID | str):
        super().__init__(client, group_id, GroupMethods)
        self.BranchId = branch_id

    async def GetDetails(self):
        """Get details of this specific group"""
        return await self.methods.GetDetails(self.BranchId, self.Id)
