from typing import TYPE_CHECKING, Literal, Any, Dict
from http.client import HTTPResponse

from ..types import SafeUUID
from ._default import BaseMethods, BaseClass

if TYPE_CHECKING:
    from ..client import PlatformClient


ContentKind = Literal["course", "lesson", "test", "webcontent", "survey"]

_KIND_TO_TOKEN = {
    "course": "Course",
    "lesson": "Lesson",
    "test": "Test",
    "webcontent": "WebContent",
    "survey": "Survey",
    "game": "Game",
    "event": "Event",
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
    path = "/CompanyBranch/MemberContent"

    # ---------- LOW-LEVEL ----------
    async def _post(self, endpoint: str, body: Dict[str, Any]) -> HTTPResponse:
        return await self.client.send_request(f"{self.path}/{endpoint}", body)

    # ---------- GENERIC (4 методи) ----------
    async def GetAccessGrants(
        self,
        branch_id: SafeUUID | str,
        kind: ContentKind,
        data: dict | None = None,
    ) -> HTTPResponse:
        """
        POST /CompanyBranch/MemberContent/Get{Kind}AccessGrants
        Body: {"companyBranchId": ..., "data": {...}}
        """
        token = _kind_token(kind)
        return await self._post(
            f"Get{token}AccessGrants",
            {"companyBranchId": str(branch_id), "data": data or {}},
        )

    async def GetAccessGrantHistory(
        self,
        branch_id: SafeUUID | str,
        kind: ContentKind,
        data: dict | None = None,
    ) -> HTTPResponse:
        """
        POST /CompanyBranch/MemberContent/Get{Kind}AccessGrantHistory
        Body: {"companyBranchId": ..., "data": {...}}
        """
        token = _kind_token(kind)
        return await self._post(
            f"Get{token}AccessGrantHistory",
            {"companyBranchId": str(branch_id), "data": data or {}},
        )

    async def AccessGrant(
        self,
        branch_id: SafeUUID | str,
        kind: ContentKind,
        data: dict,
    ) -> HTTPResponse:
        """
        POST /CompanyBranch/MemberContent/{Kind}AccessGrant
        Body: {"companyBranchId": ..., "data": {...}}
        Приклад data: {"memberId": "...", "itemId": "...", "expiresAt": "..."}.
        """
        token = _kind_token(kind)
        return await self._post(
            f"{token}AccessGrant",
            {"companyBranchId": str(branch_id), "data": data},
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

    async def GetAccessGrants(self, kind: ContentKind, data: dict | None = None):
        return await self.methods.GetAccessGrants(self.branch_id, kind, data)

    async def GetAccessGrantHistory(self, kind: ContentKind, data: dict | None = None):
        return await self.methods.GetAccessGrantHistory(self.branch_id, kind, data)

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
