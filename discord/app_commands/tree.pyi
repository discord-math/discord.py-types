from ..abc import Snowflake
from ..client import Client
from ..enums import AppCommandType
from ..interactions import Interaction
from .commands import Command, ContextMenu, ContextMenuCallback, Coro, Group, GroupT, P, T
from .errors import AppCommandError
from .models import AppCommand
from typing import Any, Callable, Concatenate, Coroutine, Generator, Generic, List, Literal, Optional, Sequence, TypeVar, Union, overload

ErrorFunc = Callable[[Interaction, AppCommandError], Coroutine[Any, Any, Any]]
ClientT = TypeVar('ClientT', bound='Client')

class CommandTree(Generic[ClientT]):
    client: ClientT
    def __init__(self, client: ClientT) -> None: ...
    async def fetch_commands(self, *, guild: Optional[Snowflake] = ...) -> List[AppCommand]: ...
    def copy_global_to(self, *, guild: Snowflake) -> None: ...
    def add_command(self, command: Union[Command[Any, ..., Any], ContextMenu, Group], *, guild: Optional[Snowflake] = ..., guilds: Sequence[Snowflake] = ..., override: bool = ...) -> None: ...
    @overload
    def remove_command(self, command: str, *, guild: Optional[Snowflake] = ..., type: Literal[AppCommandType.message, AppCommandType.user]) -> Optional[ContextMenu]: ...
    @overload
    def remove_command(self, command: str, *, guild: Optional[Snowflake] = ..., type: Literal[AppCommandType.chat_input] = ...) -> Optional[Union[Command[Any, ..., Any], Group]]: ...
    @overload
    def remove_command(self, command: str, *, guild: Optional[Snowflake] = ..., type: AppCommandType) -> Optional[Union[Command[Any, ..., Any], ContextMenu, Group]]: ...
    def clear_commands(self, *, guild: Optional[Snowflake], type: Optional[AppCommandType] = ...) -> None: ...
    @overload
    def get_command(self, command: str, *, guild: Optional[Snowflake] = ..., type: Literal[AppCommandType.message, AppCommandType.user]) -> Optional[ContextMenu]: ...
    @overload
    def get_command(self, command: str, *, guild: Optional[Snowflake] = ..., type: Literal[AppCommandType.chat_input] = ...) -> Optional[Union[Command[Any, ..., Any], Group]]: ...
    @overload
    def get_command(self, command: str, *, guild: Optional[Snowflake] = ..., type: AppCommandType) -> Optional[Union[Command[Any, ..., Any], ContextMenu, Group]]: ...
    @overload
    def get_commands(self, *, guild: Optional[Snowflake] = ..., type: Literal[AppCommandType.message, AppCommandType.user]) -> List[ContextMenu]: ... # type: ignore
    @overload
    def get_commands(self, *, guild: Optional[Snowflake] = ..., type: Literal[AppCommandType.chat_input]) -> List[Union[Command[Any, ..., Any], Group]]: ... # type: ignore
    @overload
    def get_commands(self, *, guild: Optional[Snowflake] = ..., type: AppCommandType) -> Union[List[Union[Command[Any, ..., Any], Group]], List[ContextMenu]]: ... # type: ignore
    @overload
    def get_commands(self, *, guild: Optional[Snowflake] = ..., type: Optional[AppCommandType] = ...) -> List[Union[Command[Any, ..., Any], Group, ContextMenu]]: ...
    @overload
    def walk_commands(self, *, guild: Optional[Snowflake] = ..., type: Literal[AppCommandType.message, AppCommandType.user]) -> Generator[ContextMenu, None, None]: ...
    @overload
    def walk_commands(self, *, guild: Optional[Snowflake] = ..., type: Literal[AppCommandType.chat_input] = ...) -> Generator[Union[Command[Any, ..., Any], Group], None, None]: ...
    @overload
    def walk_commands(self, *, guild: Optional[Snowflake] = ..., type: AppCommandType) -> Union[Generator[Union[Command[Any, ..., Any], Group], None, None], Generator[ContextMenu, None, None]]: ...
    async def on_error(self, interaction: Interaction, error: AppCommandError) -> None: ...
    def error(self, coro: ErrorFunc) -> ErrorFunc: ...
    def command(self, *, name: str = ..., description: str = ..., guild: Optional[Snowflake] = ..., guilds: Sequence[Snowflake] = ...) -> Callable[[Union[Callable[Concatenate[GroupT, 'Interaction', P], Coro[T]], Callable[Concatenate['Interaction', P], Coro[T]]]], Command[Group, P, T]]: ...
    def context_menu(self, *, name: str = ..., guild: Optional[Snowflake] = ..., guilds: Sequence[Snowflake] = ...) -> Callable[[ContextMenuCallback], ContextMenu]: ...
    async def sync(self, *, guild: Optional[Snowflake] = ...) -> List[AppCommand]: ...
    async def interaction_check(self, interaction: Interaction) -> bool: ...
    async def call(self, interaction: Interaction) -> None: ...
