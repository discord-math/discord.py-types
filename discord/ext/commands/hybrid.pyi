import discord
from ._types import BotT, CogT, ContextT as ContextT, Coro, _Bot
from .context import Context
from .cog import Cog
from .core import Command, Group
from discord.app_commands.commands import AutocompleteCallback, ChoiceT
from typing import Any, Callable, ClassVar, Concatenate, Generic, Optional, ParamSpec, TypeVar, Union

T = TypeVar('T')
U = TypeVar('U')
CommandT = TypeVar('CommandT', bound='Command[Any, Any, Any, Any]')
GroupT = TypeVar('GroupT', bound='Group[Any, Any, Any, Any]')
P = ParamSpec('P')
P2 = ParamSpec('P2')

class _CallableDefault:
    func: Callable[[Context[_Bot]], Any]
    def __init__(self, func: Callable[[Context[_Bot]], Any]) -> None: ...
    @property # type: ignore
    def __class__(self) -> Any: ...

HAC = TypeVar('HAC', bound='HybridAppCommand[Any, Any, Any, Any]')

class HybridAppCommand(discord.app_commands.Command[CogT, P, T], Generic[CogT, ContextT, P, T]): # type: ignore
    wrapped: Command[CogT, ContextT, Any, T]
    binding: Optional[CogT]
    def __init__(self, wrapped: Command[CogT, ContextT, Any, T]) -> None: ...
    def copy(self: HAC) -> HAC: ...

class HybridCommand(Command[CogT, ContextT, P, T]): # type: ignore
    __commands_is_hybrid__: ClassVar[bool]
    app_command: HybridAppCommand[CogT, ContextT, P, T]
    def __init__(self, func: Union[Callable[Concatenate[CogT, ContextT, P], Coro[T]], Callable[Concatenate[ContextT, P], Coro[T]]], **kwargs: Any) -> None: ...
    @property
    def cog(self) -> CogT: ...
    @cog.setter
    def cog(self, value: CogT) -> None: ...
    async def can_run(self, ctx: Context[BotT]) -> bool: ...
    def autocomplete(self, name: str) -> Callable[[AutocompleteCallback[CogT, ChoiceT]], AutocompleteCallback[CogT, ChoiceT]]: ...

class HybridGroup(Group[CogT, ContextT, P, T]): # type: ignore
    __commands_is_hybrid__: ClassVar[bool]
    invoke_without_command: bool
    app_command: discord.app_commands.Group
    fallback: Optional[str]
    def __init__(self, *args: Any, fallback: Optional[str] = ..., **attrs: Any) -> None: ...
    @property
    def cog(self) -> CogT: ...
    @cog.setter
    def cog(self, value: CogT) -> None: ...
    async def can_run(self, ctx: Context[BotT]) -> bool: ...
    def autocomplete(self, name: str) -> Callable[[AutocompleteCallback[CogT, ChoiceT]], AutocompleteCallback[CogT, ChoiceT]]: ...
    def add_command(self, command: Union[HybridGroup[CogT, ContextT, ..., Any], HybridCommand[CogT, ContextT, ..., Any]]) -> None: ... # type: ignore
    def remove_command(self, name: str) -> Optional[Command[CogT, ContextT, ..., Any]]: ...
    def command(self, name: str = ..., *args: Any, **kwargs: Any) -> Callable[[Union[Callable[Concatenate[CogT, ContextT, P2], Coro[T]], Callable[Concatenate[ContextT, P2], Coro[T]]]], HybridCommand[CogT, P2, U]]: ... # type: ignore
    def group(self, name: str = ..., *args: Any, **kwargs: Any) -> Callable[[Union[Callable[Concatenate[CogT, ContextT, P2], Coro[T]], Callable[Concatenate[ContextT, P2], Coro[T]]]], HybridGroup[CogT, P2, U]]: ... # type: ignore

def hybrid_command(name: str = ..., **attrs: Any) -> Callable[[Union[Callable[Concatenate[CogT, ContextT, P], Coro[T]], Callable[Concatenate[ContextT, P], Coro[T]]]], HybridCommand[CogT, ContextT, P, T]]: ...
def hybrid_group(name: str = ..., **attrs: Any) -> Callable[[Union[Callable[Concatenate[CogT, ContextT, P], Coro[T]], Callable[Concatenate[ContextT, P], Coro[T]]]], HybridGroup[CogT, ContextT, P, T]]: ...
