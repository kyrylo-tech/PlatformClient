from typing import TYPE_CHECKING
from ..query_builder import QueryBuilder
from ..types import SafeUUID
from ._default import BaseMethods, BaseClass
from ..utils import PlatformResponse

if TYPE_CHECKING:
    from ..client import PlatformClient


class BoardMethods(BaseMethods):
    path = "/CompanyBranchBoard"

    async def Get(self, branch_id: SafeUUID | str,
                  filter_query: None | dict | QueryBuilder = None):
        """
        Endpoint: /CompanyBranchBoard/Get
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
                         board_id: SafeUUID | str) -> PlatformResponse:
        """
        Endpoint: /CompanyBranchBoard/GetDetails
        Body:
        ``{ "companyBranchId": branch_id, "boardId": board_id }``
        :param branch_id: Branch ID
        :param board_id: Board ID
        """
        return await self.client.send_request(
            f"{self.path}/GetDetails",
            {"companyBranchId": str(branch_id),
             "boardId": str(board_id)}
        )

    async def Create(self, branch_id: SafeUUID | str,
                     name: str, description: str = None) -> PlatformResponse:
        """
        Endpoint: /CompanyBranchBoard/Create
        Body:
        ``{ "companyBranchId": branch_id,
        "data": { "name": name, "description": description } }``
        :param branch_id: Branch ID
        :param name: Board name
        :param description: Board description (optional)
        """
        data = {"name": name}
        if description is not None:
            data["description"] = description

        return await self.client.send_request(
            f"{self.path}/Create",
            {"companyBranchId": str(branch_id), "data": data}
        )

    async def Remove(self, branch_id: SafeUUID | str,
                     board_id: SafeUUID | str) -> PlatformResponse:
        """
        Endpoint: /CompanyBranchBoard/Remove
        Body:
        ``{ "companyBranchId": branch_id, "boardId": board_id }``
        :param branch_id: Branch ID
        :param board_id: Board ID
        """
        return await self.client.send_request(
            f"{self.path}/Remove",
            {"companyBranchId": str(branch_id),
             "boardId": str(board_id)}
        )

    async def Edit(self, branch_id: SafeUUID | str,
                   board_id: SafeUUID | str,
                   name: str, description: str = None,
                   manager_user_id: SafeUUID | str = None,
                   have_sprints: bool = None, have_tasks: bool = None,
                   have_users: bool = None,
                   frozen: bool = None) -> PlatformResponse:
        """
        Endpoint: /CompanyBranchBoard/Edit
        Body:
        ``{ "companyBranchId": branch_id,
        "boardId": board_id, "data": { ... } }``
        :param branch_id: Branch ID
        :param board_id: Board ID
        :param name: Board name (required)
        :param description: Board description (optional)
        :param manager_user_id: Manager user ID (optional)
        :param have_sprints: Enable sprints (optional)
        :param have_tasks: Enable tasks (optional)
        :param have_users: Enable users (optional)
        :param frozen: Freeze board (optional)
        """
        data = {"name": name}

        if description is not None:
            data["description"] = description
        if manager_user_id is not None:
            data["managerUserId"] = str(manager_user_id)
        if have_sprints is not None:
            data["haveSprints"] = have_sprints
        if have_tasks is not None:
            data["haveTasks"] = have_tasks
        if have_users is not None:
            data["haveUsers"] = have_users
        if frozen is not None:
            data["frozen"] = frozen

        return await self.client.send_request(
            f"{self.path}/Edit",
            {"companyBranchId": str(branch_id),
             "boardId": str(board_id),
             "data": data}
        )

    async def GetTags(
            self,
            branch_id: SafeUUID | str,
            board_id: SafeUUID | str,
            filter_query: None | dict | QueryBuilder = None
    ) -> PlatformResponse:
        """
        Endpoint: /CompanyBranchBoard/GetTags
        Body:
        ``{ "companyBranchId": branch_id,
        "boardId": board_id, "data": filter_query }``
        :param branch_id: Branch ID
        :param board_id: Board ID
        :param filter_query: Filter query (optional)
        """
        new_filter_query = filter_query or {}
        if isinstance(new_filter_query, QueryBuilder):
            new_filter_query = new_filter_query.build()

        return await self.client.send_request(
            f"{self.path}/GetTags",
            {"companyBranchId": str(branch_id),
             "boardId": str(board_id),
             "data": new_filter_query}
        )

    async def CreateTag(self, branch_id: SafeUUID | str,
                        board_id: SafeUUID | str,
                        name: str) -> PlatformResponse:
        """
        Endpoint: /CompanyBranchBoard/CreateTag
        Body:
        ``{ "companyBranchId": branch_id,
        "boardId": board_id, "data": { "name": name } }``
        :param branch_id: Branch ID
        :param board_id: Board ID
        :param name: Tag name
        """
        return await self.client.send_request(
            f"{self.path}/CreateTag",
            {"companyBranchId": str(branch_id),
             "boardId": str(board_id),
             "data": {"name": name}}
        )

    async def EditTag(self, branch_id: SafeUUID | str,
                      board_id: SafeUUID | str,
                      tag_id: SafeUUID | str, name: str) -> PlatformResponse:
        """
        Endpoint: /CompanyBranchBoard/EditTag
        Body:
        ``{ "companyBranchId": branch_id,
        "boardId": board_id, "data": { "name": name, "id": tag_id } }``
        :param branch_id: Branch ID
        :param board_id: Board ID
        :param tag_id: Tag ID
        :param name: New tag name
        """
        return await self.client.send_request(
            f"{self.path}/EditTag",
            {"companyBranchId": str(branch_id),
             "boardId": str(board_id),
             "data": {"name": name, "id": str(tag_id)}}
        )

    async def RemoveTag(self, branch_id: SafeUUID | str,
                        board_id: SafeUUID | str,
                        tag_id: SafeUUID | str) -> PlatformResponse:
        """
        Endpoint: /CompanyBranchBoard/RemoveTag
        Body:
        ``{ "companyBranchId": branch_id,
        "boardId": board_id, "data": tag_id }``
        :param branch_id: Branch ID
        :param board_id: Board ID
        :param tag_id: Tag ID
        """
        return await self.client.send_request(
            f"{self.path}/RemoveTag",
            {"companyBranchId": str(branch_id),
             "boardId": str(board_id),
             "data": str(tag_id)}
        )

    async def GetStates(
            self,
            branch_id: SafeUUID | str,
            board_id: SafeUUID | str,
            filter_query: None | dict | QueryBuilder = None
    ) -> PlatformResponse:
        """
        Endpoint: /CompanyBranchBoard/GetStates
        Body:
        ``{ "companyBranchId": branch_id,
        "boardId": board_id, "data": filter_query }``
        :param branch_id: Branch ID
        :param board_id: Board ID
        :param filter_query: Filter query (optional)
        """
        new_filter_query = filter_query or {}
        if isinstance(new_filter_query, QueryBuilder):
            new_filter_query = new_filter_query.build()

        return await self.client.send_request(
            f"{self.path}/GetStates",
            {"companyBranchId": str(branch_id),
             "boardId": str(board_id),
             "data": new_filter_query}
        )

    async def CreateState(self, branch_id: SafeUUID | str,
                          board_id: SafeUUID | str,
                          name: str) -> PlatformResponse:
        """
        Endpoint: /CompanyBranchBoard/CreateState
        Body:
        ``{ "companyBranchId": branch_id,
        "boardId": board_id, "data": { "name": name } }``
        :param branch_id: Branch ID
        :param board_id: Board ID
        :param name: State name
        """
        return await self.client.send_request(
            f"{self.path}/CreateState",
            {"companyBranchId": str(branch_id),
             "boardId": str(board_id),
             "data": {"name": name}}
        )

    async def EditState(self, branch_id: SafeUUID | str,
                        board_id: SafeUUID | str,
                        state_id: SafeUUID | str,
                        name: str) -> PlatformResponse:
        """
        Endpoint: /CompanyBranchBoard/EditState
        Body:
        ``{ "companyBranchId": branch_id,
        "boardId": board_id, "data": { "name": name, "id": state_id } }``
        :param branch_id: Branch ID
        :param board_id: Board ID
        :param state_id: State ID
        :param name: New state name
        """
        return await self.client.send_request(
            f"{self.path}/EditState",
            {"companyBranchId": str(branch_id),
             "boardId": str(board_id),
             "data": {"name": name, "id": str(state_id)}}
        )

    async def RemoveState(self, branch_id: SafeUUID | str,
                          board_id: SafeUUID | str,
                          state_id: SafeUUID | str) -> PlatformResponse:
        """
        Endpoint: /CompanyBranchBoard/RemoveState
        Body:
        ``{ "companyBranchId": branch_id,
        "boardId": board_id, "data": state_id }``
        :param branch_id: Branch ID
        :param board_id: Board ID
        :param state_id: State ID
        """
        return await self.client.send_request(
            f"{self.path}/RemoveState",
            {"companyBranchId": str(branch_id),
             "boardId": str(board_id),
             "data": str(state_id)}
        )

    async def GetSprints(
            self,
            branch_id: SafeUUID | str,
            board_id: SafeUUID | str,
            filter_query: None | dict | QueryBuilder = None
    ) -> PlatformResponse:
        """
        Endpoint: /CompanyBranchBoard/GetSprints
        Body:
        ``{ "companyBranchId": branch_id,
        "boardId": board_id, "data": filter_query }``
        :param branch_id: Branch ID
        :param board_id: Board ID
        :param filter_query: Filter query (optional)
        """
        new_filter_query = filter_query or {}
        if isinstance(new_filter_query, QueryBuilder):
            new_filter_query = new_filter_query.build()

        return await self.client.send_request(
            f"{self.path}/GetSprints",
            {"companyBranchId": str(branch_id),
             "boardId": str(board_id),
             "data": new_filter_query}
        )

    async def CreateSprint(self, branch_id: SafeUUID | str,
                           board_id: SafeUUID | str,
                           name: str, start_date: str, start_time: str,
                           end_date: str, end_time: str) -> PlatformResponse:
        """
        Endpoint: /CompanyBranchBoard/CreateSprint
        Body:
        ``{ "companyBranchId": branch_id, "boardId": board_id,
        "data": { "name": name, "startingAt": "...", "endAt": "..." } }``
        :param branch_id: Branch ID
        :param board_id: Board ID
        :param name: Sprint name
        :param start_date: Start date in format "2025-09-10"
        :param start_time: Start time in format "11:11"
        :param end_date: End date in format "2025-09-10"
        :param end_time: End time in format "11:11"
        """
        starting_at = f"{start_date}T{start_time}:00.000Z"
        end_at = f"{end_date}T{end_time}:00.000Z"

        return await self.client.send_request(
            f"{self.path}/CreateSprint",
            {"companyBranchId": str(branch_id),
             "boardId": str(board_id),
             "data": {
                 "name": name,
                 "startingAt": starting_at,
                 "endAt": end_at
             }}
        )

    async def EditSprint(self,
                         branch_id: SafeUUID | str,
                         board_id: SafeUUID | str,
                         sprint_id: SafeUUID | str,
                         name: str,
                         start_date: str,
                         start_time: str,
                         end_date: str,
                         end_time: str) -> PlatformResponse:
        """
        Endpoint: /CompanyBranchBoard/EditSprint
        Body:
        ``{ "companyBranchId": branch_id,
        "boardId": board_id, "data": {
        "name": name, "startingAt": "...",
        "endAt": "...", "id": sprint_id } }``
        :param branch_id: Branch ID
        :param board_id: Board ID
        :param sprint_id: Sprint ID
        :param name: Sprint name
        :param start_date: Start date in format "2025-09-10"
        :param start_time: Start time in format "11:11"
        :param end_date: End date in format "2025-09-10"
        :param end_time: End time in format "11:11"
        """
        starting_at = f"{start_date}T{start_time}:00.000Z"
        end_at = f"{end_date}T{end_time}:00.000Z"

        return await self.client.send_request(
            f"{self.path}/EditSprint",
            {"companyBranchId": str(branch_id),
             "boardId": str(board_id),
             "data": {
                 "name": name,
                 "startingAt": starting_at,
                 "endAt": end_at,
                 "id": str(sprint_id)
             }}
        )

    async def RemoveSprint(self, branch_id: SafeUUID | str,
                           board_id: SafeUUID | str,
                           sprint_id: SafeUUID | str) -> PlatformResponse:
        """
        Endpoint: /CompanyBranchBoard/RemoveSprint
        Body:
        ``{ "companyBranchId": branch_id,
        "boardId": board_id, "data": sprint_id }``
        :param branch_id: Branch ID
        :param board_id: Board ID
        :param sprint_id: Sprint ID
        """
        return await self.client.send_request(
            f"{self.path}/RemoveSprint",
            {"companyBranchId": str(branch_id),
             "boardId": str(board_id),
             "data": str(sprint_id)}
        )

    async def GetTasks(self, branch_id: SafeUUID | str,
                       board_id: SafeUUID | str,
                       filter_query: None | dict | QueryBuilder = None) -> PlatformResponse:
        """
        Endpoint: /CompanyBranchBoard/GetTasks
        Body:
        ``{ "companyBranchId": branch_id,
        "boardId": board_id, "data": filter_query }``
        """
        new_filter_query = filter_query or {}
        if isinstance(new_filter_query, QueryBuilder):
            new_filter_query = new_filter_query.build()

        return await self.client.send_request(
            f"{self.path}/GetTasks",
            {"companyBranchId": str(branch_id),
             "boardId": str(board_id),
             "data": new_filter_query}
        )

    async def GetTaskDetails(self, branch_id: SafeUUID | str,
                             board_id: SafeUUID | str,
                             task_id: SafeUUID | str) -> PlatformResponse:
        """
        Endpoint: /CompanyBranchBoard/GetTaskDetails
        Body:
        ``{ "companyBranchId": branch_id,
        "boardId": board_id, "taskId": task_id }``
        """
        return await self.client.send_request(
            f"{self.path}/GetTaskDetails",
            {"companyBranchId": str(branch_id),
             "boardId": str(board_id),
             "taskId": str(task_id)}
        )

    async def CreateTask(self, branch_id: SafeUUID | str,
                         board_id: SafeUUID | str,
                         name: str, state_id: SafeUUID | str,
                         sprint_id: SafeUUID | str = None) -> PlatformResponse:
        """
        Endpoint: /CompanyBranchBoard/CreateTask
        Body:
        ``{ "companyBranchId": branch_id,
        "boardId": board_id,
        "data": { "name": name, "stateId": state_id,
        "sprintId": sprint_id } }``
        """
        data = {"name": name, "stateId": str(state_id)}
        if sprint_id is not None:
            data["sprintId"] = str(sprint_id)

        return await self.client.send_request(
            f"{self.path}/CreateTask",
            {"companyBranchId": str(branch_id),
             "boardId": str(board_id),
             "data": data}
        )

    async def EditTaskName(self, branch_id: SafeUUID | str,
                           board_id: SafeUUID | str,
                           task_id: SafeUUID | str, name: str) -> PlatformResponse:
        """
        Endpoint: /CompanyBranchBoard/EditTaskName
        Body:
        ``{ "companyBranchId": branch_id,
        "boardId": board_id, "taskId": task_id, "data": name }``
        """
        return await self.client.send_request(
            f"{self.path}/EditTaskName",
            {"companyBranchId": str(branch_id),
             "boardId": str(board_id),
             "taskId": str(task_id),
             "data": name}
        )

    async def EditTaskDescription(self, branch_id: SafeUUID | str,
                                  board_id: SafeUUID | str,
                                  task_id: SafeUUID | str,
                                  description: str) -> PlatformResponse:
        """
        Endpoint: /CompanyBranchBoard/EditTaskDescription
        Body:
        ``{ "companyBranchId": branch_id,
        "boardId": board_id, "taskId": task_id, "data": description }``
        """
        return await self.client.send_request(
            f"{self.path}/EditTaskDescription",
            {"companyBranchId": str(branch_id),
             "boardId": str(board_id),
             "taskId": str(task_id),
             "data": description}
        )

    async def EditTaskEndTime(self, branch_id: SafeUUID | str,
                              board_id: SafeUUID | str,
                              task_id: SafeUUID | str, end_date: str,
                              end_time: str) -> PlatformResponse:
        """
        Endpoint: /CompanyBranchBoard/EditTaskEndTime
        Body:
        ``{ "companyBranchId": branch_id,
        "boardId": board_id, "taskId": task_id,
        "data": { "value": "..." } }``
        :param end_date: End date in format "2025-09-10"
        :param end_time: End time in format "11:41"
        """
        end_at = f"{end_date}T{end_time}:00.000Z"
        return await self.client.send_request(
            f"{self.path}/EditTaskEndTime",
            {"companyBranchId": str(branch_id),
             "boardId": str(board_id),
             "taskId": str(task_id),
             "data": {"value": end_at}}
        )

    async def EditTaskManager(self, branch_id: SafeUUID | str,
                              board_id: SafeUUID | str,
                              task_id: SafeUUID | str,
                              manager_id: SafeUUID | str) -> PlatformResponse:
        """
        Endpoint: /CompanyBranchBoard/EditTaskManager
        Body:
        ``{ "companyBranchId": branch_id,
        "boardId": board_id, "taskId": task_id,
        "data": { "value": manager_id } }``
        """
        return await self.client.send_request(
            f"{self.path}/EditTaskManager",
            {"companyBranchId": str(branch_id),
             "boardId": str(board_id),
             "taskId": str(task_id),
             "data": {"value": str(manager_id)}}
        )

    async def SetTaskOrder(self, branch_id: SafeUUID | str,
                           board_id: SafeUUID | str,
                           task_id: SafeUUID | str,
                           new_state_id: SafeUUID | str,
                           old_state_id: SafeUUID | str,
                           new_order: int = 0) -> PlatformResponse:
        """
        Endpoint: /CompanyBranchBoard/SetTaskOrder
        Body:
        ``{ "companyBranchId": branch_id,
        "boardId": board_id, "taskId": task_id,
        "data": { "newParentEntityId": new_state_id,
        "parentEntityId": old_state_id, "newOrder": new_order } }``
        """
        return await self.client.send_request(
            f"{self.path}/SetTaskOrder",
            {"companyBranchId": str(branch_id),
             "boardId": str(board_id),
             "taskId": str(task_id),
             "data": {
                 "newParentEntityId": str(new_state_id),
                 "parentEntityId": str(old_state_id),
                 "newOrder": new_order
             }}
        )

    async def RemoveTask(self, branch_id: SafeUUID | str,
                         board_id: SafeUUID | str,
                         task_id: SafeUUID | str) -> PlatformResponse:
        """
        Endpoint: /CompanyBranchBoard/RemoveTask
        Body:
        ``{ "companyBranchId": branch_id,
        "boardId": board_id, "taskId": task_id }``
        """
        return await self.client.send_request(
            f"{self.path}/RemoveTask",
            {"companyBranchId": str(branch_id),
             "boardId": str(board_id),
             "taskId": str(task_id)}
        )

    # Task Comments Methods
    async def GetTaskComments(self, branch_id: SafeUUID | str,
                              board_id: SafeUUID | str,
                              task_id: SafeUUID | str,
                              filter_query: None | dict | QueryBuilder = None) -> PlatformResponse:
        """
        Endpoint: /CompanyBranchBoard/GetTaskComments
        Body:
        ``{ "companyBranchId": branch_id,
        "boardId": board_id, "taskId": task_id, "data": filter_query }``
        """
        new_filter_query = filter_query or {}
        if isinstance(new_filter_query, QueryBuilder):
            new_filter_query = new_filter_query.build()

        return await self.client.send_request(
            f"{self.path}/GetTaskComments",
            {"companyBranchId": str(branch_id),
             "boardId": str(board_id),
             "taskId": str(task_id),
             "data": new_filter_query}
        )

    async def CreateTaskComment(self, branch_id: SafeUUID | str,
                                board_id: SafeUUID | str,
                                task_id: SafeUUID | str,
                                content: str) -> PlatformResponse:
        """
        Endpoint: /CompanyBranchBoard/CreateTaskComment
        Body:
        ``{ "companyBranchId": branch_id,
        "boardId": board_id, "taskId": task_id,
        "data": { "content": content } }``
        """
        return await self.client.send_request(
            f"{self.path}/CreateTaskComment",
            {"companyBranchId": str(branch_id),
             "boardId": str(board_id),
             "taskId": str(task_id),
             "data": {"content": content}}
        )

    async def EditTaskComment(self, branch_id: SafeUUID | str,
                              board_id: SafeUUID | str,
                              task_id: SafeUUID | str,
                              comment_id: SafeUUID | str,
                              content: str) -> PlatformResponse:
        """
        Endpoint: /CompanyBranchBoard/EditTaskComment
        Body:
        ``{ "companyBranchId": branch_id,
        "boardId": board_id, "taskId": task_id,
        "data": { "id": comment_id, "content": content } }``
        """
        return await self.client.send_request(
            f"{self.path}/EditTaskComment",
            {"companyBranchId": str(branch_id),
             "boardId": str(board_id),
             "taskId": str(task_id),
             "data": {"id": str(comment_id), "content": content}}
        )

    async def RemoveTaskComment(self, branch_id: SafeUUID | str,
                                board_id: SafeUUID | str,
                                task_id: SafeUUID | str,
                                comment_id: SafeUUID | str) -> PlatformResponse:
        """
        Endpoint: /CompanyBranchBoard/RemoveTaskComment
        Body:
        ``{ "companyBranchId": branch_id,
        "boardId": board_id, "taskId": task_id, "data": comment_id }``
        """
        return await self.client.send_request(
            f"{self.path}/RemoveTaskComment",
            {"companyBranchId": str(branch_id),
             "boardId": str(board_id),
             "taskId": str(task_id),
             "data": str(comment_id)}
        )

    # Task Tags and Students Methods
    async def AddTaskTag(self, branch_id: SafeUUID | str,
                         board_id: SafeUUID | str,
                         task_id: SafeUUID | str,
                         tag_id: SafeUUID | str) -> PlatformResponse:
        """
        Endpoint: /CompanyBranchBoard/AddTaskTag
        Body:
        ``{ "companyBranchId": branch_id,
        "boardId": board_id, "taskId": task_id, "data": tag_id }``
        """
        return await self.client.send_request(
            f"{self.path}/AddTaskTag",
            {"companyBranchId": str(branch_id),
             "boardId": str(board_id),
             "taskId": str(task_id),
             "data": str(tag_id)}
        )

    async def RemoveTaskTag(self, branch_id: SafeUUID | str,
                            board_id: SafeUUID | str,
                            task_id: SafeUUID | str,
                            tag_id: SafeUUID | str) -> PlatformResponse:
        """
        Endpoint: /CompanyBranchBoard/RemoveTaskTag
        Body:
        ``{ "companyBranchId": branch_id,
        "boardId": board_id, "taskId": task_id, "data": tag_id }``
        """
        return await self.client.send_request(
            f"{self.path}/RemoveTaskTag",
            {"companyBranchId": str(branch_id),
             "boardId": str(board_id),
             "taskId": str(task_id),
             "data": str(tag_id)}
        )

    async def AddTaskStudent(self, branch_id: SafeUUID | str,
                             board_id: SafeUUID | str,
                             task_id: SafeUUID | str,
                             student_id: SafeUUID | str) -> PlatformResponse:
        """
        Endpoint: /CompanyBranchBoard/AddTaskStudent
        Body:
        ``{ "companyBranchId": branch_id,
        "boardId": board_id, "taskId": task_id, "data": student_id }``
        """
        return await self.client.send_request(
            f"{self.path}/AddTaskStudent",
            {"companyBranchId": str(branch_id),
             "boardId": str(board_id),
             "taskId": str(task_id),
             "data": str(student_id)}
        )

    async def RemoveTaskStudent(self, branch_id: SafeUUID | str,
                                board_id: SafeUUID | str,
                                task_id: SafeUUID | str,
                                student_id: SafeUUID | str) -> PlatformResponse:
        """
        Endpoint: /CompanyBranchBoard/RemoveTaskStudent
        Body:
        ``{ "companyBranchId": branch_id,
        "boardId": board_id, "taskId": task_id, "data": student_id }``
        """
        return await self.client.send_request(
            f"{self.path}/RemoveTaskStudent",
            {"companyBranchId": str(branch_id),
             "boardId": str(board_id),
             "taskId": str(task_id),
             "data": str(student_id)}
        )

    # SubTask Methods
    async def CreateSubTask(self, branch_id: SafeUUID | str,
                            board_id: SafeUUID | str,
                            task_id: SafeUUID | str,
                            description: str) -> PlatformResponse:
        """
        Endpoint: /CompanyBranchBoard/CreateSubTask
        Body:
        ``{ "companyBranchId": branch_id,
        "boardId": board_id, "taskId": task_id,
        "data": { "description": description } }``
        """
        return await self.client.send_request(
            f"{self.path}/CreateSubTask",
            {"companyBranchId": str(branch_id),
             "boardId": str(board_id),
             "taskId": str(task_id),
             "data": {"description": description}}
        )

    async def EditSubTaskContent(self, branch_id: SafeUUID | str,
                                 board_id: SafeUUID | str,
                                 task_id: SafeUUID | str,
                                 subtask_id: SafeUUID | str,
                                 description: str) -> PlatformResponse:
        """
        Endpoint: /CompanyBranchBoard/EditSubTaskContent
        Body:
        ``{ "companyBranchId": branch_id,
        "boardId": board_id, "taskId": task_id,
        "data": { "id": subtask_id, "description": description } }``
        """
        return await self.client.send_request(
            f"{self.path}/EditSubTaskContent",
            {"companyBranchId": str(branch_id),
             "boardId": str(board_id),
             "taskId": str(task_id),
             "data": {"id": str(subtask_id), "description": description}}
        )

    async def RemoveSubTask(self, branch_id: SafeUUID | str,
                            board_id: SafeUUID | str,
                            task_id: SafeUUID | str,
                            subtask_id: SafeUUID | str) -> PlatformResponse:
        """
        Endpoint: /CompanyBranchBoard/RemoveSubTask
        Body:
        ``{ "companyBranchId": branch_id,
        "boardId": board_id, "taskId": task_id, "data": subtask_id }``
        """
        return await self.client.send_request(
            f"{self.path}/RemoveSubTask",
            {"companyBranchId": str(branch_id),
             "boardId": str(board_id),
             "taskId": str(task_id),
             "data": str(subtask_id)}
        )

    # Board Variables Methods
    async def GetVariables(self, branch_id: SafeUUID | str,
                           board_id: SafeUUID | str) -> PlatformResponse:
        """
        Endpoint: /CompanyBranchBoard/GetVariables
        Body:
        ``{ "companyBranchId": branch_id, "boardId": board_id }``
        """
        return await self.client.send_request(
            f"{self.path}/GetVariables",
            {"companyBranchId": str(branch_id),
             "boardId": str(board_id)}
        )

    async def SetVariable(self, branch_id: SafeUUID | str,
                          board_id: SafeUUID | str,
                          name: str, value: str) -> PlatformResponse:
        """
        Endpoint: /CompanyBranchBoard/SetVariable
        Body:
        ``{ "companyBranchId": branch_id,
        "boardId": board_id, "data": { "name": name, "value": value } }``
        """
        return await self.client.send_request(
            f"{self.path}/SetVariable",
            {"companyBranchId": str(branch_id),
             "boardId": str(board_id),
             "data": {"name": name, "value": value}}
        )


class BoundBoardMethods:
    def __init__(self, methods: BoardMethods, branch_id: SafeUUID | str):
        self.methods = methods
        self.branch_id = branch_id

    async def Get(self, filter_query=None):
        return await self.methods.Get(self.branch_id, filter_query)

    async def GetDetails(self, board_id: SafeUUID | str):
        return await self.methods.GetDetails(self.branch_id, board_id)

    async def Create(self, name: str, description: str = None):
        return await self.methods.Create(self.branch_id, name, description)

    async def Remove(self, board_id: SafeUUID | str):
        return await self.methods.Remove(self.branch_id, board_id)

    async def Edit(self,
                   board_id: SafeUUID | str,
                   name: str,
                   description: str = None,
                   manager_user_id: SafeUUID | str = None,
                   have_sprints: bool = None,
                   have_tasks: bool = None,
                   have_users: bool = None,
                   frozen: bool = None):
        return await self.methods.Edit(self.branch_id,
                                       board_id,
                                       name,
                                       description,
                                       manager_user_id,
                                       have_sprints,
                                       have_tasks,
                                       have_users,
                                       frozen)

    async def GetTags(self, board_id: SafeUUID | str, filter_query=None):
        return await self.methods.GetTags(self.branch_id, board_id,
                                          filter_query)

    async def CreateTag(self, board_id: SafeUUID | str, name: str):
        return await self.methods.CreateTag(self.branch_id, board_id, name)

    async def EditTag(self, board_id: SafeUUID | str, tag_id: SafeUUID | str,
                      name: str):
        return await self.methods.EditTag(self.branch_id, board_id, tag_id,
                                          name)

    async def RemoveTag(self, board_id: SafeUUID | str,
                        tag_id: SafeUUID | str):
        return await self.methods.RemoveTag(self.branch_id, board_id, tag_id)

    async def GetStates(self, board_id: SafeUUID | str, filter_query=None):
        return await self.methods.GetStates(self.branch_id,
                                            board_id,
                                            filter_query)

    async def CreateState(self, board_id: SafeUUID | str, name: str):
        return await self.methods.CreateState(self.branch_id, board_id, name)

    async def EditState(self, board_id: SafeUUID | str,
                        state_id: SafeUUID | str, name: str):
        return await self.methods.EditState(self.branch_id,
                                            board_id,
                                            state_id,
                                            name)

    async def RemoveState(self, board_id: SafeUUID | str,
                          state_id: SafeUUID | str):
        return await self.methods.RemoveState(self.branch_id, board_id,
                                              state_id)

    async def GetSprints(self, board_id: SafeUUID | str, filter_query=None):
        return await self.methods.GetSprints(self.branch_id,
                                             board_id,
                                             filter_query)

    async def CreateSprint(self,
                           board_id: SafeUUID | str,
                           name: str,
                           start_date: str,
                           start_time: str,
                           end_date: str,
                           end_time: str):
        return await self.methods.CreateSprint(self.branch_id,
                                               board_id, name,
                                               start_date,
                                               start_time,
                                               end_date,
                                               end_time)

    async def EditSprint(self,
                         board_id: SafeUUID | str,
                         sprint_id: SafeUUID | str,
                         name: str,
                         start_date: str,
                         start_time: str,
                         end_date: str,
                         end_time: str):
        return await self.methods.EditSprint(self.branch_id,
                                             board_id,
                                             sprint_id,
                                             name,
                                             start_date,
                                             start_time,
                                             end_date,
                                             end_time)

    async def RemoveSprint(self,
                           board_id: SafeUUID | str,
                           sprint_id: SafeUUID | str):
        return await self.methods.RemoveSprint(self.branch_id,
                                               board_id,
                                               sprint_id)

    async def GetTasks(self, board_id: SafeUUID | str, filter_query=None):
        return await self.methods.GetTasks(self.branch_id, board_id,
                                           filter_query)

    async def GetTaskDetails(self, board_id: SafeUUID | str,
                             task_id: SafeUUID | str):
        return await self.methods.GetTaskDetails(self.branch_id, board_id,
                                                 task_id)

    async def CreateTask(self, board_id: SafeUUID | str, name: str,
                         state_id: SafeUUID | str,
                         sprint_id: SafeUUID | str = None):
        return await self.methods.CreateTask(self.branch_id, board_id, name,
                                             state_id, sprint_id)

    async def EditTaskName(self, board_id: SafeUUID | str,
                           task_id: SafeUUID | str, name: str):
        return await self.methods.EditTaskName(self.branch_id, board_id,
                                               task_id, name)

    async def EditTaskDescription(self, board_id: SafeUUID | str,
                                  task_id: SafeUUID | str, description: str):
        return await self.methods.EditTaskDescription(self.branch_id, board_id,
                                                      task_id, description)

    async def EditTaskEndTime(self, board_id: SafeUUID | str,
                              task_id: SafeUUID | str, end_date: str,
                              end_time: str):
        return await self.methods.EditTaskEndTime(self.branch_id, board_id,
                                                  task_id, end_date, end_time)

    async def EditTaskManager(self, board_id: SafeUUID | str,
                              task_id: SafeUUID | str,
                              manager_id: SafeUUID | str):
        return await self.methods.EditTaskManager(self.branch_id, board_id,
                                                  task_id, manager_id)

    async def SetTaskOrder(self, board_id: SafeUUID | str,
                           task_id: SafeUUID | str,
                           new_state_id: SafeUUID | str,
                           old_state_id: SafeUUID | str, new_order: int = 0):
        return await self.methods.SetTaskOrder(self.branch_id, board_id,
                                               task_id, new_state_id,
                                               old_state_id, new_order)

    async def RemoveTask(self, board_id: SafeUUID | str,
                         task_id: SafeUUID | str):
        return await self.methods.RemoveTask(self.branch_id, board_id, task_id)

    # Task Comments Methods
    async def GetTaskComments(self, board_id: SafeUUID | str,
                              task_id: SafeUUID | str, filter_query=None):
        return await self.methods.GetTaskComments(self.branch_id, board_id,
                                                  task_id, filter_query)

    async def CreateTaskComment(self, board_id: SafeUUID | str,
                                task_id: SafeUUID | str, content: str):
        return await self.methods.CreateTaskComment(self.branch_id, board_id,
                                                    task_id, content)

    async def EditTaskComment(self, board_id: SafeUUID | str,
                              task_id: SafeUUID | str,
                              comment_id: SafeUUID | str, content: str):
        return await self.methods.EditTaskComment(self.branch_id, board_id,
                                                  task_id, comment_id, content)

    async def RemoveTaskComment(self, board_id: SafeUUID | str,
                                task_id: SafeUUID | str,
                                comment_id: SafeUUID | str):
        return await self.methods.RemoveTaskComment(self.branch_id, board_id,
                                                    task_id, comment_id)

    # Task Tags and Students Methods
    async def AddTaskTag(self, board_id: SafeUUID | str,
                         task_id: SafeUUID | str, tag_id: SafeUUID | str):
        return await self.methods.AddTaskTag(self.branch_id, board_id, task_id,
                                             tag_id)

    async def RemoveTaskTag(self, board_id: SafeUUID | str,
                            task_id: SafeUUID | str, tag_id: SafeUUID | str):
        return await self.methods.RemoveTaskTag(self.branch_id, board_id,
                                                task_id, tag_id)

    async def AddTaskStudent(self, board_id: SafeUUID | str,
                             task_id: SafeUUID | str,
                             student_id: SafeUUID | str):
        return await self.methods.AddTaskStudent(self.branch_id, board_id,
                                                 task_id, student_id)

    async def RemoveTaskStudent(self, board_id: SafeUUID | str,
                                task_id: SafeUUID | str,
                                student_id: SafeUUID | str):
        return await self.methods.RemoveTaskStudent(self.branch_id, board_id,
                                                    task_id, student_id)

    # SubTask Methods
    async def CreateSubTask(self, board_id: SafeUUID | str,
                            task_id: SafeUUID | str, description: str):
        return await self.methods.CreateSubTask(self.branch_id, board_id,
                                                task_id, description)

    async def EditSubTaskContent(self, board_id: SafeUUID | str,
                                 task_id: SafeUUID | str,
                                 subtask_id: SafeUUID | str, description: str):
        return await self.methods.EditSubTaskContent(self.branch_id, board_id,
                                                     task_id, subtask_id,
                                                     description)

    async def RemoveSubTask(self, board_id: SafeUUID | str,
                            task_id: SafeUUID | str,
                            subtask_id: SafeUUID | str):
        return await self.methods.RemoveSubTask(self.branch_id, board_id,
                                                task_id, subtask_id)

    # Board Variables Methods
    async def GetVariables(self, board_id: SafeUUID | str):
        return await self.methods.GetVariables(self.branch_id, board_id)

    async def SetVariable(self, board_id: SafeUUID | str, name: str,
                          value: str):
        return await self.methods.SetVariable(self.branch_id, board_id, name,
                                              value)


class BoardClass(BaseClass[BoardMethods]):
    BranchId: SafeUUID

    def __init__(self, client: "PlatformClient", branch_id: SafeUUID | str,
                 board_id: SafeUUID | str):
        super().__init__(client, board_id, BoardMethods)
        self.BranchId = branch_id

    async def GetDetails(self):
        return await self.methods.GetDetails(self.BranchId, self.Id)

    async def Remove(self):
        return await self.methods.Remove(self.BranchId, self.Id)

    async def Edit(self,
                   name: str,
                   description: str = None,
                   manager_user_id: SafeUUID | str = None,
                   have_sprints: bool = None,
                   have_tasks: bool = None,
                   have_users: bool = None,
                   frozen: bool = None):
        return await self.methods.Edit(self.BranchId,
                                       self.Id, name,
                                       description,
                                       manager_user_id,
                                       have_sprints,
                                       have_tasks,
                                       have_users,
                                       frozen)

    async def GetTags(self, filter_query=None):
        return await self.methods.GetTags(self.BranchId, self.Id, filter_query)

    async def CreateTag(self, name: str):
        return await self.methods.CreateTag(self.BranchId, self.Id, name)

    async def EditTag(self, tag_id: SafeUUID | str, name: str):
        return await self.methods.EditTag(self.BranchId, self.Id, tag_id, name)

    async def RemoveTag(self, tag_id: SafeUUID | str):
        return await self.methods.RemoveTag(self.BranchId, self.Id, tag_id)

    async def GetStates(self, filter_query=None):
        return await self.methods.GetStates(self.BranchId,
                                            self.Id,
                                            filter_query)

    async def CreateState(self, name: str):
        return await self.methods.CreateState(self.BranchId, self.Id, name)

    async def EditState(self, state_id: SafeUUID | str, name: str):
        return await self.methods.EditState(self.BranchId,
                                            self.Id,
                                            state_id,
                                            name)

    async def RemoveState(self, state_id: SafeUUID | str):
        return await self.methods.RemoveState(self.BranchId,
                                              self.Id,
                                              state_id)

    async def GetSprints(self, filter_query=None):
        return await self.methods.GetSprints(self.BranchId,
                                             self.Id,
                                             filter_query)

    async def CreateSprint(self,
                           name: str,
                           start_date: str,
                           start_time: str,
                           end_date: str,
                           end_time: str):
        return await self.methods.CreateSprint(self.BranchId,
                                               self.Id, name,
                                               start_date,
                                               start_time,
                                               end_date,
                                               end_time)

    async def EditSprint(self,
                         sprint_id: SafeUUID | str,
                         name: str,
                         start_date: str,
                         start_time: str,
                         end_date: str,
                         end_time: str):
        return await self.methods.EditSprint(self.BranchId,
                                             self.Id,
                                             sprint_id,
                                             name,
                                             start_date,
                                             start_time,
                                             end_date,
                                             end_time)

    async def RemoveSprint(self, sprint_id: SafeUUID | str):
        return await self.methods.RemoveSprint(self.BranchId,
                                               self.Id,
                                               sprint_id)

    async def GetTasks(self, filter_query=None):
        return await self.methods.GetTasks(self.BranchId, self.Id,
                                           filter_query)

    async def GetTaskDetails(self, task_id: SafeUUID | str):
        return await self.methods.GetTaskDetails(self.BranchId, self.Id,
                                                 task_id)

    async def CreateTask(self, name: str, state_id: SafeUUID | str,
                         sprint_id: SafeUUID | str = None):
        return await self.methods.CreateTask(self.BranchId, self.Id, name,
                                             state_id, sprint_id)

    async def EditTaskName(self, task_id: SafeUUID | str, name: str):
        return await self.methods.EditTaskName(self.BranchId, self.Id, task_id,
                                               name)

    async def EditTaskDescription(self, task_id: SafeUUID | str,
                                  description: str):
        return await self.methods.EditTaskDescription(self.BranchId, self.Id,
                                                      task_id, description)

    async def EditTaskEndTime(self, task_id: SafeUUID | str, end_date: str,
                              end_time: str):
        return await self.methods.EditTaskEndTime(self.BranchId, self.Id,
                                                  task_id, end_date, end_time)

    async def EditTaskManager(self, task_id: SafeUUID | str,
                              manager_id: SafeUUID | str):
        return await self.methods.EditTaskManager(self.BranchId, self.Id,
                                                  task_id, manager_id)

    async def SetTaskOrder(self, task_id: SafeUUID | str,
                           new_state_id: SafeUUID | str,
                           old_state_id: SafeUUID | str, new_order: int = 0):
        return await self.methods.SetTaskOrder(self.BranchId, self.Id, task_id,
                                               new_state_id, old_state_id,
                                               new_order)

    async def RemoveTask(self, task_id: SafeUUID | str):
        return await self.methods.RemoveTask(self.BranchId, self.Id, task_id)

    # Task Comments Methods
    async def GetTaskComments(self, task_id: SafeUUID | str,
                              filter_query=None):
        return await self.methods.GetTaskComments(self.BranchId, self.Id,
                                                  task_id, filter_query)

    async def CreateTaskComment(self, task_id: SafeUUID | str, content: str):
        return await self.methods.CreateTaskComment(self.BranchId, self.Id,
                                                    task_id, content)

    async def EditTaskComment(self, task_id: SafeUUID | str,
                              comment_id: SafeUUID | str, content: str):
        return await self.methods.EditTaskComment(self.BranchId, self.Id,
                                                  task_id, comment_id, content)

    async def RemoveTaskComment(self, task_id: SafeUUID | str,
                                comment_id: SafeUUID | str):
        return await self.methods.RemoveTaskComment(self.BranchId, self.Id,
                                                    task_id, comment_id)

    # Task Tags and Students Methods
    async def AddTaskTag(self, task_id: SafeUUID | str,
                         tag_id: SafeUUID | str):
        return await self.methods.AddTaskTag(self.BranchId, self.Id, task_id,
                                             tag_id)

    async def RemoveTaskTag(self, task_id: SafeUUID | str,
                            tag_id: SafeUUID | str):
        return await self.methods.RemoveTaskTag(self.BranchId, self.Id,
                                                task_id, tag_id)

    async def AddTaskStudent(self, task_id: SafeUUID | str,
                             student_id: SafeUUID | str):
        return await self.methods.AddTaskStudent(self.BranchId, self.Id,
                                                 task_id, student_id)

    async def RemoveTaskStudent(self, task_id: SafeUUID | str,
                                student_id: SafeUUID | str):
        return await self.methods.RemoveTaskStudent(self.BranchId, self.Id,
                                                    task_id, student_id)

    # SubTask Methods
    async def CreateSubTask(self, task_id: SafeUUID | str, description: str):
        return await self.methods.CreateSubTask(self.BranchId, self.Id,
                                                task_id, description)

    async def EditSubTaskContent(self, task_id: SafeUUID | str,
                                 subtask_id: SafeUUID | str, description: str):
        return await self.methods.EditSubTaskContent(self.BranchId, self.Id,
                                                     task_id, subtask_id,
                                                     description)

    async def RemoveSubTask(self, task_id: SafeUUID | str,
                            subtask_id: SafeUUID | str):
        return await self.methods.RemoveSubTask(self.BranchId, self.Id,
                                                task_id, subtask_id)

    # Board Variables Methods
    async def GetVariables(self):
        return await self.methods.GetVariables(self.BranchId, self.Id)

    async def SetVariable(self, name: str, value: str):
        return await self.methods.SetVariable(self.BranchId, self.Id, name,
                                              value)
