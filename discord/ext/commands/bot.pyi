import discord
import types
from . import errors
from ._types import BotT, Check, Coro, CoroFunc, MaybeAwaitable, _Bot
from .cog import Cog
from .context import Context
from .core import Command, GroupMixin
from .help import HelpCommand
from .hybrid import ContextT, HybridCommand, HybridGroup, P
from discord import app_commands
from discord.abc import Snowflake, User
from discord.interactions import Interaction
from discord.message import Message
from typing import Any, Callable, Collection, Concatenate, Dict, Iterable, List, Mapping, Optional, Type, TypeVar, Union, overload

_Prefix = Union[Iterable[str], str]
_PrefixCallable = Callable[[BotT, Message], MaybeAwaitable[_Prefix]]
PrefixType = Union[_Prefix, _PrefixCallable[BotT]]
T = TypeVar('T')
CFT = TypeVar('CFT', bound='CoroFunc')

def when_mentioned(bot: _Bot, msg: Message) -> List[str]: ...
def when_mentioned_or(*prefixes: str) -> Callable[[_Bot, Message], List[str]]: ...

BB = TypeVar('BB', bound=Union['Bot', 'AutoShardedBot'])

class BotBase(GroupMixin[None, Any]):
    command_prefix: PrefixType[_Bot]
    extra_events: Dict[str, List[CoroFunc]]
    description: str
    owner_id: Optional[int]
    owner_ids: Optional[Collection[int]]
    strip_after_prefix: bool
    def __init__(self, command_prefix: PrefixType[BotT], *, help_command: Optional[HelpCommand] = ..., tree_cls: Type[app_commands.CommandTree[Any]] = ..., description: Optional[str] = ..., intents: discord.Intents, **options: Any) -> None: ...
    def dispatch(self, event_name: str, *args: Any, **kwargs: Any) -> None: ...
    async def close(self) -> None: ...
    def add_command(self, command: Command[Any, Any, ..., Any]) -> None: ...
    def remove_command(self, name: str) -> Optional[Command[Any, Any, ..., Any]]: ...
    def hybrid_command(self, name: str = ..., *args: Any, **kwargs: Any) -> Callable[[Union[Callable[Concatenate[None, ContextT, P], Coro[T]], Callable[Concatenate[ContextT, P], Coro[T]]]], HybridCommand[None, ContextT, P, T]]: ...
    def hybrid_group(self, name: str = ..., *args: Any, **kwargs: Any) -> Callable[[Union[Callable[Concatenate[None, ContextT, P], Coro[T]], Callable[Concatenate[ContextT, P], Coro[T]]]], HybridGroup[None, ContextT, P, T]]: ...
    async def on_command_error(self, context: Context[BotT], exception: errors.CommandError) -> None: ...
    def check(self, func: T) -> T: ...
    def add_check(self, func: Check[ContextT], *, call_once: bool = ...) -> None: ...
    def remove_check(self, func: Check[ContextT], *, call_once: bool = ...) -> None: ...
    def check_once(self, func: CFT) -> CFT: ...
    async def can_run(self, ctx: Context[BotT], *, call_once: bool = ...) -> bool: ...
    async def is_owner(self, user: User) -> bool: ...
    def before_invoke(self, coro: CFT) -> CFT: ...
    def after_invoke(self, coro: CFT) -> CFT: ...
    def add_listener(self, func: CoroFunc, name: str = ...) -> None: ...
    def remove_listener(self, func: CoroFunc, name: str = ...) -> None: ...
    def listen(self, name: str = ...) -> Callable[[CFT], CFT]: ...
    async def add_cog(self, cog: Cog, *, override: bool = ..., guild: Optional[Snowflake] = ..., guilds: List[Snowflake] = ...) -> None: ...
    def get_cog(self, name: str) -> Optional[Cog]: ...
    async def remove_cog(self, name: str, *, guild: Optional[Snowflake] = ..., guilds: List[Snowflake] = ...) -> Optional[Cog]: ...
    @property
    def cogs(self) -> Mapping[str, Cog]: ...
    async def load_extension(self, name: str, *, package: Optional[str] = ...) -> None: ...
    async def unload_extension(self, name: str, *, package: Optional[str] = ...) -> None: ...
    async def reload_extension(self, name: str, *, package: Optional[str] = ...) -> None: ...
    @property
    def extensions(self) -> Mapping[str, types.ModuleType]: ...
    @property
    def help_command(self) -> Optional[HelpCommand]: ...
    @help_command.setter
    def help_command(self, value: Optional[HelpCommand]) -> None: ...
    @property
    def tree(self: BB) -> app_commands.CommandTree[BB]: ... # type: ignore
    async def get_prefix(self, message: Message) -> Union[List[str], str]: ...
    @overload
    async def get_context(self: BB, origin: Union[Message, Interaction]) -> Context[BB]: ... # type: ignore
    @overload
    async def get_context(self, origin: Union[Message, Interaction], *, cls: Type[ContextT]) -> ContextT: ...
    async def invoke(self, ctx: Context[BotT]) -> None: ...
    async def process_commands(self, message: Message) -> None: ...
    async def on_message(self, message: Message) -> None: ...

class Bot(BotBase, discord.Client): ... # type: ignore
class AutoShardedBot(BotBase, discord.AutoShardedClient): ... # type: ignore
