from http.client import HTTPResponse
from typing import TYPE_CHECKING, List

from .sprint import SprintClass
from .task import TaskClass
from ...query_builder import QueryBuilder
from ...types import SafeUUID, UserAccess
from .._default import BaseMethods, BaseClass

if TYPE_CHECKING:
    from ...client import PlatformClient


class SubTask:
    Name: str
    IsDone: bool

    def __init__(self, name: str, is_done: bool = False):
        self.Name = name
        self.IsDone = is_done

    def to_dict(self):
        return {
            "Name": self.Name,
            "IsDone": self.IsDone
        }


class BoardMethods(BaseMethods):
    path = "/CompanyBranchBoard"

    async def GetList(self, branch_id: SafeUUID | str, filter_query: None | dict | QueryBuilder = None, is_my: bool = False):
        """
        Endpoint: /CompanyBranchBoard/CompanyBranchBoard/Get

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

    async def GetDetails(self, branch_id: SafeUUID | str, board_id: SafeUUID | str):
        """
        Endpoint: /CompanyBranchBoard/CompanyBranchBoard/GetDetails

        Body:
        ``{ "companyBranchId": branch_id, "BoardId": board_id }``

        :param branch_id: Branch ID
        :param board_id: Board ID
        """
        return await self.client.send_request(
            f"{self.path}/GetDetails",
            { "CompanyBranchId": str(branch_id), "boardId": str(board_id) }
        )

    async def Create(self, branch_id: SafeUUID | str, board_id: SafeUUID | str, name: str, description: str = "",
         manager_user_id: SafeUUID | str = None, have_sprints: bool = True, have_tasks: bool = True, have_users: bool = True):
        """
        Endpoint: /CompanyBranchBoard/CompanyBranchBoard/Create

        Body:
        ``{ "companyBranchId": branch_id, "data": { "name": name, "description": description, "access": access } }``

        :param branch_id:
        :param board_id:
        :param name:
        :param description:
        :param manager_user_id:
        :param have_sprints:
        :param have_tasks:
        :param have_users:
        :return:
        """
        return await self.client.send_request(
            f"{self.path}/Create",
            {"CompanyBranchId": str(branch_id), "BoardId": str(board_id),
             "Data": {
                "Name": name,
                "Description": description,
                "ManagerUserId": str(manager_user_id),
                "HaveSprints": have_sprints,
                "HaveTasks": have_tasks,
                "HaveUsers": have_users
            } }
        )

    async def Edit(self, branch_id: SafeUUID | str, board_id: SafeUUID | str, name: str, description: str = "",
         manager_user_id: SafeUUID | str = None, have_sprints: bool = True, have_tasks: bool = True, have_users: bool = True, frozen: bool = False):
        """
        Endpoint: /CompanyBranchBoard/CompanyBranchBoard/Create

        Body:
        ``{ "companyBranchId": branch_id, "data": { "name": name, "description": description, "access": access } }``

        :param branch_id:
        :param board_id:
        :param name:
        :param description:
        :param manager_user_id:
        :param have_sprints:
        :param have_tasks:
        :param have_users:
        :param frozen:
        :return:
        """
        return await self.client.send_request(
            f"{self.path}/Create",
            {"CompanyBranchId": str(branch_id), "BoardId": str(board_id),
             "Data": {
                "Name": name,
                "Description": description,
                "ManagerUserId": str(manager_user_id),
                "HaveSprints": have_sprints,
                "HaveTasks": have_tasks,
                "HaveUsers": have_users,
                "Frozen": frozen
            } }
        )

    async def CreateTask(self, branch_id: SafeUUID | str, board_id: SafeUUID | str,
        sprint_id: SafeUUID | str, state_id: SafeUUID | str,
        name: str, description: str = "",
        sub_tasks=None,
        user_members: List[SafeUUID | str] = None,
        target_user_students: List[SafeUUID | str] = None,
        user_id: SafeUUID | str = None
    ):
        """
        Endpoint: /CompanyBranchBoard/CompanyBranchBoard/CreateTask
        Body:
        ``{ "companyBranchId": branch_id, "data": { "name": name, "description": description, "access": access } }``
        """
        if sub_tasks is None:
            sub_tasks = []
        if user_members is None:
            user_members = []
        if target_user_students is None:
            target_user_students = []

        return await self.client.send_request(
            f"{self.path}/CreateTask",
            {
                "CompanyBranchId": str(branch_id), "BoardId": str(board_id),
                "Data": {
                    "Name": name,
                    "Description": description,
                    "SubTask": sub_tasks,
                    "UserMembers": user_members,
                    "TargetUserStudents": target_user_students,
                    "SprintId": str(sprint_id),
                    "StateId": str(state_id),
                    "UserId": str(user_id) if user_id else None
                }
            }
        )





class BoundBoardMethods:
    def __init__(self, methods: BoardMethods, branch_id: SafeUUID | str):
        self.methods = methods
        self.branch_id = branch_id

    async def GetList(self, filter_query=None):
        return await self.methods.GetList(self.branch_id, filter_query)

    async def GetDetails(self, role_id: SafeUUID | str):
        return await self.methods.GetDetails(self.branch_id, role_id)

    async def Create(self, board_id: SafeUUID | str, name: str, description: str = "",
         manager_user_id: SafeUUID | str = None, have_sprints: bool = True, have_tasks: bool = True, have_users: bool = True):
        return await self.methods.Create(self.branch_id, board_id, name, description,
            manager_user_id, have_sprints, have_tasks, have_users)

    async def Edit(self, board_id: SafeUUID | str, name: str, description: str = "",
            manager_user_id: SafeUUID | str = None, have_sprints: bool = True, have_tasks: bool = True, have_users: bool = True, frozen: bool = False):
            return await self.methods.Edit(self.branch_id, board_id, name, description,
                manager_user_id, have_sprints, have_tasks, have_users, frozen)


class BoardClass(BaseClass[BoardMethods]):
    BranchId: SafeUUID

    def __init__(self, client: "PlatformClient", branch_id: SafeUUID | str, role_id: SafeUUID | str):
        super().__init__(client, role_id, BoardMethods)
        self.BranchId = branch_id

    def GetTask(self, task_id: SafeUUID | str):
        return TaskClass(self.client, self.BranchId, self.Id, task_id)

    def GetSprint(self, sprint_id: SafeUUID | str):
        return SprintClass(self.client, self.BranchId, self.Id, sprint_id)



    async def GetDetails(self):
        return await self.methods.GetDetails(self.BranchId, self.Id)

    async def Edit(self, name: str, description: str = "",
            manager_user_id: SafeUUID | str = None, have_sprints: bool = True, have_tasks: bool = True, have_users: bool = True, frozen: bool = False):
            return await self.methods.Edit(self.BranchId, self.Id, name, description,
                manager_user_id, have_sprints, have_tasks, have_users, frozen)

    async def Create(self, name: str, description: str = "",
            manager_user_id: SafeUUID | str = None, have_sprints: bool = True, have_tasks: bool = True, have_users: bool = True):
            return await self.methods.Create(self.BranchId, self.Id, name, description,
                manager_user_id, have_sprints, have_tasks, have_users)