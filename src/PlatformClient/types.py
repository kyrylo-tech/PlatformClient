from enum import Enum
from typing import Literal
from uuid import UUID

class SafeUUID(UUID):
    def __new__(cls, value):
        if isinstance(value, UUID):
            return value
        if isinstance(value, str):
            try:
                return UUID(value)
            except ValueError:
                raise ValueError(f"Invalid UUID string: '{value}'")
        raise TypeError(f"Expected str or UUID, got {type(value)}")


UserAccessType = Literal[
    "SearchMembers", "ViewMembers", "SearchManagers", "ViewManagers", "ManageManagers", "SearchStudents",
    "ViewStudents", "ManageStudents", "ViewStudentLeads", "ManageStudentLeads", "ViewStudentCustomers",
    "ManageStudentCustomers", "SearchTeachers", "ViewTeachers", "ManageTeachers", "CreateManagers",
    "ModifyManagers", "RemoveManagers", "CreateTeachers", "CreateTeachersOwned", "ModifyTeachers",
    "RemoveTeachers", "ModifyStudents", "RemoveStudents", "CreateStudentLeads", "CreateStudentLeadsOwned",
    "ModifyStudentLeads", "RemoveStudentLeads", "ModifyStudentCustomers", "RemoveStudentCustomers",
    "SearchRoles", "ViewRoles", "ManageRoles", "CreateRoles", "ModifyRoles", "RemoveRoles", "SearchGroups",
    "ViewGroups", "ManageGroups", "CreateGroups", "ModifyGroups", "RemoveGroups", "ViewSales", "ManageSales",
    "CreateSales", "CreateSalesOwned", "ModifySales", "RemoveSales", "SearchLessons", "ViewLessons",
    "ManageLessons", "CreateLessons", "CreateLessonsOwned", "ModifyLessons", "RemoveLessons",
    "SearchLessonTypes", "ViewLessonTypes", "ManageLessonTypes", "CreateLessonTypes", "ModifyLessonTypes",
    "RemoveLessonTypes", "SearchCourses", "ViewCourses", "ManageCourses", "CreateCourses", "ModifyCourses",
    "RemoveCourses", "ViewSchedules", "ManageSchedules", "CreateSchedules", "CreateSchedulesOwned",
    "ModifySchedules", "RemoveSchedules", "SearchProducts", "ViewProducts", "ManageProducts",
    "CreateProducts", "ModifyProducts", "RemoveProducts", "SearchDirections", "ViewDirections",
    "ManageDirections", "CreateDirections", "ModifyDirections", "RemoveDirections", "ManageChats",
    "CreateChats", "ModifyChats", "RemoveChats", "ViewStaticLocalizations", "ManageStaticLocalizations",
    "CreateStaticLocalizations", "ModifyStaticLocalizations", "RemoveStaticLocalizations", "ViewTriggers",
    "ManageTriggers", "CreateTriggers", "ModifyTriggers", "RemoveTriggers", "ViewScheduleFunctions",
    "ManageScheduleFunctions", "CreateScheduleFunctions", "ModifyScheduleFunctions",
    "RemoveScheduleFunctions", "SearchEvents", "ViewEvents", "ManageEvents", "CreateEvents", "ModifyEvents",
    "RemoveEvents", "SearchTags", "ViewTags", "ManageTags", "CreateTags", "ModifyTags", "RemoveTags",
    "SearchBoards", "ViewBoards", "ManageBoards", "CreateBoards", "ModifyBoards", "RemoveBoards",
    "ViewTelegramBots", "ManageTelegramBots", "CreateTelegramBots", "ModifyTelegramBots",
    "RemoveTelegramBots", "ViewVariables", "ManageVariables", "CreateVariables", "ModifyVariables",
    "RemoveVariables", "ManageAPI", "SearchCurrencies", "ManageCurrencies", "ViewCurrencies",
    "CreateCurrencies", "ModifyCurrencies", "RemoveCurrencies", "ManageHomeworks", "ViewHomeworks",
    "CreateHomeworks", "ModifyHomeworks", "RemoveHomeworks", "SearchTests", "ManageTests", "ViewTests",
    "CreateTests", "ModifyTests", "RemoveTests", "ManageTestResults", "ViewTestResults", "ModifyTestResults",
    "RemoveTestResults", "SearchDepartments", "ManageDepartments", "ViewDepartments", "CreateDepartments",
    "ModifyDepartments", "RemoveDepartments", "ManageSupports", "ViewSupports", "ModifySupports",
    "CreateCategorySupports", "TakeTicketSupports", "SearchWebContent", "ViewWebContent", "ManageWebContent",
    "CreateWebContent", "ModifyWebContent", "RemoveWebContent", "SearchSurveys", "ManageSurveys",
    "ViewSurveys", "CreateSurveys", "ModifySurveys", "RemoveSurveys", "ManageRegularFunctions",
    "ViewRegularFunctions", "CreateRegularFunctions", "ModifyRegularFunctions", "RemoveRegularFunctions",
    "SearchDashboards", "ManageDashboards", "ViewDashboards", "CreateDashboards", "ModifyDashboards",
    "RemoveDashboards", "SearchGames", "ManageGames", "ViewGames", "CreateGames", "ModifyGames",
    "RemoveGames", "SearchAcquirings", "ManageAcquirings", "ViewAcquirings", "CreateAcquirings",
    "ModifyAcquirings", "RemoveAcquirings", "ViewMenuSettings", "ManageMenuSettings", "SearchTemplateValues",
    "ManageTemplateValues", "ViewTemplateValues", "CreateTemplateValues", "ModifyTemplateValues",
    "RemoveTemplateValues"
]

class UserAccess(str, Enum):
    SearchMembers = "SearchMembers"
    ViewMembers = "ViewMembers"
    SearchManagers = "SearchManagers"
    ViewManagers = "ViewManagers"
    ManageManagers = "ManageManagers"
    SearchStudents = "SearchStudents"
    ViewStudents = "ViewStudents"
    ManageStudents = "ManageStudents"
    ViewStudentLeads = "ViewStudentLeads"
    ManageStudentLeads = "ManageStudentLeads"
    ViewStudentCustomers = "ViewStudentCustomers"
    ManageStudentCustomers = "ManageStudentCustomers"
    SearchTeachers = "SearchTeachers"
    ViewTeachers = "ViewTeachers"
    ManageTeachers = "ManageTeachers"
    CreateManagers = "CreateManagers"
    ModifyManagers = "ModifyManagers"
    RemoveManagers = "RemoveManagers"
    CreateTeachers = "CreateTeachers"
    CreateTeachersOwned = "CreateTeachersOwned"
    ModifyTeachers = "ModifyTeachers"
    RemoveTeachers = "RemoveTeachers"
    ModifyStudents = "ModifyStudents"
    RemoveStudents = "RemoveStudents"
    CreateStudentLeads = "CreateStudentLeads"
    CreateStudentLeadsOwned = "CreateStudentLeadsOwned"
    ModifyStudentLeads = "ModifyStudentLeads"
    RemoveStudentLeads = "RemoveStudentLeads"
    ModifyStudentCustomers = "ModifyStudentCustomers"
    RemoveStudentCustomers = "RemoveStudentCustomers"
    SearchRoles = "SearchRoles"
    ViewRoles = "ViewRoles"
    ManageRoles = "ManageRoles"
    CreateRoles = "CreateRoles"
    ModifyRoles = "ModifyRoles"
    RemoveRoles = "RemoveRoles"
    SearchGroups = "SearchGroups"
    ViewGroups = "ViewGroups"
    ManageGroups = "ManageGroups"
    CreateGroups = "CreateGroups"
    ModifyGroups = "ModifyGroups"
    RemoveGroups = "RemoveGroups"
    ViewSales = "ViewSales"
    ManageSales = "ManageSales"
    CreateSales = "CreateSales"
    CreateSalesOwned = "CreateSalesOwned"
    ModifySales = "ModifySales"
    RemoveSales = "RemoveSales"
    SearchLessons = "SearchLessons"
    ViewLessons = "ViewLessons"
    ManageLessons = "ManageLessons"
    CreateLessons = "CreateLessons"
    CreateLessonsOwned = "CreateLessonsOwned"
    ModifyLessons = "ModifyLessons"
    RemoveLessons = "RemoveLessons"
    SearchLessonTypes = "SearchLessonTypes"
    ViewLessonTypes = "ViewLessonTypes"
    ManageLessonTypes = "ManageLessonTypes"
    CreateLessonTypes = "CreateLessonTypes"
    ModifyLessonTypes = "ModifyLessonTypes"
    RemoveLessonTypes = "RemoveLessonTypes"
    SearchCourses = "SearchCourses"
    ViewCourses = "ViewCourses"
    ManageCourses = "ManageCourses"
    CreateCourses = "CreateCourses"
    ModifyCourses = "ModifyCourses"
    RemoveCourses = "RemoveCourses"
    ViewSchedules = "ViewSchedules"
    ManageSchedules = "ManageSchedules"
    CreateSchedules = "CreateSchedules"
    CreateSchedulesOwned = "CreateSchedulesOwned"
    ModifySchedules = "ModifySchedules"
    RemoveSchedules = "RemoveSchedules"
    SearchProducts = "SearchProducts"
    ViewProducts = "ViewProducts"
    ManageProducts = "ManageProducts"
    CreateProducts = "CreateProducts"
    ModifyProducts = "ModifyProducts"
    RemoveProducts = "RemoveProducts"
    SearchDirections = "SearchDirections"
    ViewDirections = "ViewDirections"
    ManageDirections = "ManageDirections"
    CreateDirections = "CreateDirections"
    ModifyDirections = "ModifyDirections"
    RemoveDirections = "RemoveDirections"
    ManageChats = "ManageChats"
    CreateChats = "CreateChats"
    ModifyChats = "ModifyChats"
    RemoveChats = "RemoveChats"
    ViewStaticLocalizations = "ViewStaticLocalizations"
    ManageStaticLocalizations = "ManageStaticLocalizations"
    CreateStaticLocalizations = "CreateStaticLocalizations"
    ModifyStaticLocalizations = "ModifyStaticLocalizations"
    RemoveStaticLocalizations = "RemoveStaticLocalizations"
    ViewTriggers = "ViewTriggers"
    ManageTriggers = "ManageTriggers"
    CreateTriggers = "CreateTriggers"
    ModifyTriggers = "ModifyTriggers"
    RemoveTriggers = "RemoveTriggers"
    ViewScheduleFunctions = "ViewScheduleFunctions"
    ManageScheduleFunctions = "ManageScheduleFunctions"
    CreateScheduleFunctions = "CreateScheduleFunctions"
    ModifyScheduleFunctions = "ModifyScheduleFunctions"
    RemoveScheduleFunctions = "RemoveScheduleFunctions"
    SearchEvents = "SearchEvents"
    ViewEvents = "ViewEvents"
    ManageEvents = "ManageEvents"
    CreateEvents = "CreateEvents"
    ModifyEvents = "ModifyEvents"
    RemoveEvents = "RemoveEvents"
    SearchTags = "SearchTags"
    ViewTags = "ViewTags"
    ManageTags = "ManageTags"
    CreateTags = "CreateTags"
    ModifyTags = "ModifyTags"
    RemoveTags = "RemoveTags"
    SearchBoards = "SearchBoards"
    ViewBoards = "ViewBoards"
    ManageBoards = "ManageBoards"
    CreateBoards = "CreateBoards"
    ModifyBoards = "ModifyBoards"
    RemoveBoards = "RemoveBoards"
    ViewTelegramBots = "ViewTelegramBots"
    ManageTelegramBots = "ManageTelegramBots"
    CreateTelegramBots = "CreateTelegramBots"
    ModifyTelegramBots = "ModifyTelegramBots"
    RemoveTelegramBots = "RemoveTelegramBots"
    ViewVariables = "ViewVariables"
    ManageVariables = "ManageVariables"
    CreateVariables = "CreateVariables"
    ModifyVariables = "ModifyVariables"
    RemoveVariables = "RemoveVariables"
    ManageAPI = "ManageAPI"
    SearchCurrencies = "SearchCurrencies"
    ManageCurrencies = "ManageCurrencies"
    ViewCurrencies = "ViewCurrencies"
    CreateCurrencies = "CreateCurrencies"
    ModifyCurrencies = "ModifyCurrencies"
    RemoveCurrencies = "RemoveCurrencies"
    ManageHomeworks = "ManageHomeworks"
    ViewHomeworks = "ViewHomeworks"
    CreateHomeworks = "CreateHomeworks"
    ModifyHomeworks = "ModifyHomeworks"
    RemoveHomeworks = "RemoveHomeworks"
    SearchTests = "SearchTests"
    ManageTests = "ManageTests"
    ViewTests = "ViewTests"
    CreateTests = "CreateTests"
    ModifyTests = "ModifyTests"
    RemoveTests = "RemoveTests"
    ManageTestResults = "ManageTestResults"
    ViewTestResults = "ViewTestResults"
    ModifyTestResults = "ModifyTestResults"
    RemoveTestResults = "RemoveTestResults"
    SearchDepartments = "SearchDepartments"
    ManageDepartments = "ManageDepartments"
    ViewDepartments = "ViewDepartments"
    CreateDepartments = "CreateDepartments"
    ModifyDepartments = "ModifyDepartments"
    RemoveDepartments = "RemoveDepartments"
    ManageSupports = "ManageSupports"
    ViewSupports = "ViewSupports"
    ModifySupports = "ModifySupports"
    CreateCategorySupports = "CreateCategorySupports"
    TakeTicketSupports = "TakeTicketSupports"
    SearchWebContent = "SearchWebContent"
    ViewWebContent = "ViewWebContent"
    ManageWebContent = "ManageWebContent"
    CreateWebContent = "CreateWebContent"
    ModifyWebContent = "ModifyWebContent"
    RemoveWebContent = "RemoveWebContent"
    SearchSurveys = "SearchSurveys"
    ManageSurveys = "ManageSurveys"
    ViewSurveys = "ViewSurveys"
    CreateSurveys = "CreateSurveys"
    ModifySurveys = "ModifySurveys"
    RemoveSurveys = "RemoveSurveys"
    ManageRegularFunctions = "ManageRegularFunctions"
    ViewRegularFunctions = "ViewRegularFunctions"
    CreateRegularFunctions = "CreateRegularFunctions"
    ModifyRegularFunctions = "ModifyRegularFunctions"
    RemoveRegularFunctions = "RemoveRegularFunctions"
    SearchDashboards = "SearchDashboards"
    ManageDashboards = "ManageDashboards"
    ViewDashboards = "ViewDashboards"
    CreateDashboards = "CreateDashboards"
    ModifyDashboards = "ModifyDashboards"
    RemoveDashboards = "RemoveDashboards"
    SearchGames = "SearchGames"
    ManageGames = "ManageGames"
    ViewGames = "ViewGames"
    CreateGames = "CreateGames"
    ModifyGames = "ModifyGames"
    RemoveGames = "RemoveGames"
    SearchAcquirings = "SearchAcquirings"
    ManageAcquirings = "ManageAcquirings"
    ViewAcquirings = "ViewAcquirings"
    CreateAcquirings = "CreateAcquirings"
    ModifyAcquirings = "ModifyAcquirings"
    RemoveAcquirings = "RemoveAcquirings"
    ViewMenuSettings = "ViewMenuSettings"
    ManageMenuSettings = "ManageMenuSettings"
    SearchTemplateValues = "SearchTemplateValues"
    ManageTemplateValues = "ManageTemplateValues"
    ViewTemplateValues = "ViewTemplateValues"
    CreateTemplateValues = "CreateTemplateValues"
    ModifyTemplateValues = "ModifyTemplateValues"
    RemoveTemplateValues = "RemoveTemplateValues"