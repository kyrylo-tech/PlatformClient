from http.client import HTTPResponse
from typing import TYPE_CHECKING

from ._default import BaseMethods, BaseClass
from ..types import SafeUUID

if TYPE_CHECKING:
    from ..client import PlatformClient


class LessonMethods(BaseMethods):
    path = "/CompanyBranchLesson"

    async def GetDetails(
        self,
        branch_id: SafeUUID | str,
        lesson_id: SafeUUID | str
    ) -> HTTPResponse:
        """
        Endpoint: /CompanyBranchLesson/CompanyBranchLesson/GetDetails

        Body:
        {
            "companyBranchId": branch_id,
            "lessonId": lesson_id
        }
        """
        return await self.client.send_request(
            f"{self.path}/GetDetails",
            {
                "companyBranchId": str(branch_id),
                "lessonId": str(lesson_id)
            }
        )


class BoundLessonMethods:
    def __init__(self, methods: LessonMethods, branch_id: SafeUUID | str):
        self.methods = methods
        self.branch_id = branch_id

    async def GetDetails(self, lesson_id: SafeUUID | str):
        return await self.methods.GetDetails(self.branch_id, lesson_id)


class LessonClass(BaseClass[LessonMethods]):
    BranchId: SafeUUID

    def __init__(self, client: "PlatformClient", branch_id: SafeUUID | str, lesson_id: SafeUUID | str):
        super().__init__(client, lesson_id, LessonMethods)
        self.BranchId = branch_id

    async def GetDetails(self):
        return await self.methods.GetDetails(self.BranchId, self.Id)
