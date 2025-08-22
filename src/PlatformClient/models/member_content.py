from typing import TYPE_CHECKING, Literal, Any, Dict
from http.client import HTTPResponse

from ..query_builder import QueryBuilder
from ..types import SafeUUID
from ._default import BaseMethods, BaseClass
from ..utils import PlatformResponse

if TYPE_CHECKING:
    from ..client import PlatformClient


ContentKind = Literal["Course", "Lesson", "Test", "WebContent", "Survey", "Game", "Event"]

_KIND_TO_TOKEN = {
    "Course": "Course",
    "Lesson": "Lesson",
    "Test": "Test",
    "WebContent": "WebContent",
    "Survey": "Survey",
    "Game": "Game",
    "Event": "Event",
}


def _kind_token(kind: ContentKind) -> str:
    try:
        return _KIND_TO_TOKEN[kind]
    except KeyError:
        raise ValueError(f"Unsupported content kind: {kind!r}. "
                         f"Use one of: {', '.join(_KIND_TO_TOKEN.keys())}")


class MemberContentMethods(BaseMethods):
    """
    Адаптивний клієнт для /api/CompanyBranch/MemberContent/*
    Формує назву ендпоінта зі значення kind.
    """
    path = "/CompanyBranchMemberContent"

    # ---------- LOW-LEVEL ----------
    async def _post(self, endpoint: str, body: Dict[str, Any]) -> PlatformResponse:
        return await self.client.send_request(f"{self.path}/{endpoint}", body)

    # ---------- GENERIC (4 методи) ----------
    async def GetAccessGrants(
        self,
        branch_id: SafeUUID | str,
        kind: ContentKind,
        filter_query: None | dict | QueryBuilder = None
    ) -> PlatformResponse:
        """
        POST /CompanyBranch/MemberContent/Get{Kind}AccessGrants
        Body: {"companyBranchId": ..., "data": {...}}
        """
        token = _kind_token(kind)

        new_filter_query = filter_query or {}
        if isinstance(new_filter_query, QueryBuilder):
            new_filter_query = new_filter_query.build()

        return await self._post(
            f"Get{token}AccessGrants",
            {"companyBranchId": str(branch_id), "data": new_filter_query},
        )

    async def GetAccessGrantHistory(
        self,
        branch_id: SafeUUID | str,
        kind: ContentKind,
        filter_query: None | dict | QueryBuilder = None
    ) -> HTTPResponse:
        """
        POST /CompanyBranch/MemberContent/Get{Kind}AccessGrantHistory
        Body: {"companyBranchId": ..., "data": {...}}
        """
        token = _kind_token(kind)

        new_filter_query = filter_query or {}
        if isinstance(new_filter_query, QueryBuilder):
            new_filter_query = new_filter_query.build()

        return await self._post(
            f"Get{token}AccessGrantHistory",
            {"companyBranchId": str(branch_id), "data": new_filter_query},
        )

    async def AccessGrant(
        self,
        branch_id: SafeUUID | str,
        kind: ContentKind,
        user_id: SafeUUID | str,
        entity_id: SafeUUID | str,
        count: int = 0,
        description: str = "string",
        expire_time: str = None,
    ) -> HTTPResponse:
        """
        POST /CompanyBranch/MemberContent/{Kind}AccessGrant
        Body: {"companyBranchId": ..., "data": {...}}
        Приклад data: {"memberId": "...", "itemId": "...", "expiresAt": "..."}.
        """
        token = _kind_token(kind)

        if expire_time is None:
            expire_time = "2025-08-20T13:05:44.664Z"

        return await self._post(
            f"{token}AccessGrant",
            {
                "companyBranchId": str(branch_id),
                "data": {
                    "description": "string",
                    "userId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "entityId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "expireTime": "2025-08-20T13:05:44.664Z",
                    "count": 0
                }
            },
        )

    async def AccessRecall(
        self,
        branch_id: SafeUUID | str,
        kind: ContentKind,
        data: dict,
    ) -> HTTPResponse:
        """
        POST /CompanyBranch/MemberContent/{Kind}AccessRecall
        Body: {"companyBranchId": ..., "data": {...}}
        Приклад data: {"memberId": "...", "itemId": "..."}.
        """
        token = _kind_token(kind)
        return await self._post(
            f"{token}AccessRecall",
            {"companyBranchId": str(branch_id), "data": data},
        )


# --------- Зручний «bound»-фасад по гілці ----------
class BoundMemberContent:
    def __init__(self, methods: MemberContentMethods, branch_id: SafeUUID | str):
        self.methods = methods
        self.branch_id = branch_id

    async def GetAccessGrants(self, kind: ContentKind, filter_query = None):
        return await self.methods.GetAccessGrants(self.branch_id, kind, filter_query)

    async def GetAccessGrantHistory(self, kind: ContentKind, filter_query = None):
        return await self.methods.GetAccessGrantHistory(self.branch_id, kind, filter_query)

    async def AccessGrant(self, kind: ContentKind, data: dict):
        return await self.methods.AccessGrant(self.branch_id, kind, data)

    async def AccessRecall(self, kind: ContentKind, data: dict):
        return await self.methods.AccessRecall(self.branch_id, kind, data)


# --------- Опціональний клас-обгортка під конкретний item (якщо треба) ----------
class MemberContentItem(BaseClass[MemberContentMethods]):
    """
    Якщо у твоєму флоу зручно «прив’язатися» до конкретного itemId (курсу/уроку/тесту),
    можна зберігати його в полі Id і прокидати в data автоматично.
    """
    BranchId: SafeUUID
    Kind: ContentKind

    def __init__(self, client: "PlatformClient", branch_id: SafeUUID | str, kind: ContentKind, item_id: SafeUUID | str):
        super().__init__(client, item_id, MemberContentMethods)
        self.BranchId = branch_id
        self.Kind = kind

    async def GetAccessGrants(self, extra: dict | None = None):
        data = {"itemId": str(self.Id), **(extra or {})}
        return await self.methods.GetAccessGrants(self.BranchId, self.Kind, data)

    async def GetAccessGrantHistory(self, extra: dict | None = None):
        data = {"itemId": str(self.Id), **(extra or {})}
        return await self.methods.GetAccessGrantHistory(self.BranchId, self.Kind, data)

    async def AccessGrant(self, payload: dict):
        data = {"itemId": str(self.Id), **payload}
        return await self.methods.AccessGrant(self.BranchId, self.Kind, data)

    async def AccessRecall(self, payload: dict):
        data = {"itemId": str(self.Id), **payload}
        return await self.methods.AccessRecall(self.BranchId, self.Kind, data)
