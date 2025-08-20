from typing import TYPE_CHECKING, TypeVar, Generic, Type

from ..types import SafeUUID

if TYPE_CHECKING:
    from ..client import PlatformClient

class BaseMethods:
    def __init_subclass__(cls):
        if not hasattr(cls, 'path'):
            cls.path = cls.__name__.replace("Methods", "")
        super().__init_subclass__()

    def __init__(self, client: "PlatformClient"):
        self.client = client

T_Methods = TypeVar("T_Methods", bound=BaseMethods)

class BaseClass(Generic[T_Methods]):
    Id: SafeUUID
    client: "PlatformClient"
    methods: T_Methods
    path: str = ""

    def __init__(self, client: "PlatformClient", object_id: SafeUUID | str, methods_class: Type[T_Methods]):
        self.client = client
        self.Id = SafeUUID(object_id)
        self.methods = methods_class(client)