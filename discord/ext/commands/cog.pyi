from ._types import BotT, ContextT
from .core import Command
from discord import app_commands
from typing import Any, Callable, Dict, Generator, List, Tuple, Type, TypeVar, Union

FuncT = TypeVar('FuncT', bound=Callable[..., Any])
CM = TypeVar('CM', bound='CogMeta')

class CogMeta(type):
    __cog_name__: str
    __cog_settings__: Dict[str, Any]
    __cog_commands__: List[Command[Any, Any, Any, Any]]
    __cog_is_app_commands_group__: bool
    __cog_app_commands__: List[Union[app_commands.Group, app_commands.Command[Any, ..., Any]]]
    __cog_listeners__: List[Tuple[str, str]]
    def __new__(cls: Type[CM], *args: Any, **kwargs: Any) -> CM: ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @classmethod
    def qualified_name(cls) -> str: ...

C = TypeVar('C', bound='Cog')

class Cog(metaclass=CogMeta):
    __cog_name__: str
    __cog_settings__: Dict[str, Any]
    __cog_commands__: List[Command[Any, Any, Any, Any]]
    __cog_app_commands__: List[Union[app_commands.Group, app_commands.Command[Any, ..., Any]]]
    __cog_listeners__: List[Tuple[str, str]]
    __discord_app_commands_group_children__: List[Union[app_commands.Group, app_commands.Command[Any, ..., Any]]]
    module: str
    def __new__(cls: Type[C], *args: Any, **kwargs: Any) -> C: ...
    def get_commands(self: C) -> List[Command[C, Any, ..., Any]]: ...
    @property
    def qualified_name(self) -> str: ...
    @property
    def description(self) -> str: ...
    @description.setter
    def description(self, description: str) -> None: ...
    __cog_description__: str
    def walk_commands(self) -> Generator[Command[C, Any, ..., Any], None, None]: ...
    def get_listeners(self) -> List[Tuple[str, Callable[..., Any]]]: ...
    @classmethod
    def listener(cls, name: str = ...) -> Callable[[FuncT], FuncT]: ...
    def has_error_handler(self) -> bool: ...
    async def cog_load(self) -> None: ...
    async def cog_unload(self) -> None: ...
    def bot_check_once(self, ctx: ContextT) -> bool: ...
    def bot_check(self, ctx: ContextT) -> bool: ...
    def cog_check(self, ctx: ContextT) -> bool: ...
    async def cog_command_error(self, ctx: ContextT, error: Exception) -> None: ...
    async def cog_before_invoke(self, ctx: ContextT) -> None: ...
    async def cog_after_invoke(self, ctx: ContextT) -> None: ...
