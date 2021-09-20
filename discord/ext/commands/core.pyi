from .errors import *
import inspect
from ._types import Check, Coro, Error, Hook, _BaseCommand
from .context import Context
from .cog import Cog
from .cooldowns import BucketType
from discord.message import Message
from typing import Any, Callable, Dict, Generator, List, Optional, Set, Tuple, Type, TypeVar, Union, overload
from typing_extensions import Concatenate

T = TypeVar('T')
CogT = TypeVar('CogT', bound='Cog')
CommandT = TypeVar('CommandT', bound='Command')
ContextT = TypeVar('ContextT', bound='Context')
GroupT = TypeVar('GroupT', bound='Group')
HookT = TypeVar('HookT', bound='Hook')
ErrorT = TypeVar('ErrorT', bound='Error')

class Command(_BaseCommand):
    __original_kwargs__: Dict[str, Any]
    name: str
    enabled: bool
    help: Optional[str]
    brief: Optional[str]
    usage: Optional[str]
    rest_is_raw: bool
    aliases: Union[List[str], Tuple[str, ...]]
    extras: Dict[str, Any]
    description: str
    hidden: bool
    checks: List[Check]
    require_var_positional: bool
    ignore_extra: bool
    cooldown_after_parsing: bool
    cog: Optional[Cog]
    parent: Optional[GroupMixin]
    module: str
    params: List[inspect.Parameter]
    def __init__(self, func: Callable[..., Coro[T]], **kwargs: Any) -> None: ...
    @property
    def callback(self) -> Callable[..., Coro[T]]: ...
    @callback.setter
    def callback(self, function: Callable[..., Coro[T]]) -> None: ...
    def add_check(self, func: Check) -> None: ...
    def remove_check(self, func: Check) -> None: ...
    def update(self, **kwargs: Any) -> None: ...
    async def __call__(self, context: Context, *args: Any, **kwargs: Any) -> T: ...
    def copy(self) -> Command: ...
    async def dispatch_error(self, ctx: Context, error: Exception) -> None: ...
    async def transform(self, ctx: Context, param: inspect.Parameter) -> Any: ...
    @property
    def clean_params(self) -> Dict[str, inspect.Parameter]: ...
    @property
    def full_parent_name(self) -> str: ...
    @property
    def parents(self) -> List[Group]: ...
    @property
    def root_parent(self) -> Optional[Group]: ...
    @property
    def qualified_name(self) -> str: ...
    async def call_before_hooks(self, ctx: Context) -> None: ...
    async def call_after_hooks(self, ctx: Context) -> None: ...
    async def prepare(self, ctx: Context) -> None: ...
    def is_on_cooldown(self, ctx: Context) -> bool: ...
    def reset_cooldown(self, ctx: Context) -> None: ...
    def get_cooldown_retry_after(self, ctx: Context) -> float: ...
    async def invoke(self, ctx: Context) -> None: ...
    async def reinvoke(self, ctx: Context, *, call_hooks: bool = ...) -> None: ...
    on_error: Error
    def error(self, coro: ErrorT) -> ErrorT: ...
    def has_error_handler(self) -> bool: ...
    def before_invoke(self, coro: HookT) -> HookT: ...
    def after_invoke(self, coro: HookT) -> HookT: ...
    @property
    def cog_name(self) -> Optional[str]: ...
    @property
    def short_doc(self) -> str: ...
    @property
    def signature(self) -> str: ...
    async def can_run(self, ctx: Context) -> bool: ...

class GroupMixin:
    all_commands: Any
    case_insensitive: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @property
    def commands(self) -> Set[Command]: ...
    def recursively_remove_all_commands(self) -> None: ...
    def add_command(self, command: Command) -> None: ...
    def remove_command(self, name: str) -> Optional[Command]: ...
    def walk_commands(self) -> Generator[Command, None, None]: ...
    def get_command(self, name: str) -> Optional[Command]: ...
    def command(self, name: str = ..., cls: Type[CommandT] = ..., *args: Any, **kwargs: Any) -> Callable[[Callable[..., Coro[Any]]], CommandT]: ...
    def group(self, name: str = ..., cls: Type[GroupT] = ..., *args: Any, **kwargs: Any) -> Callable[[Callable[..., Coro[Any]]], GroupT]: ...

class Group(GroupMixin, Command):
    invoke_without_command: Any
    def __init__(self, *args: Any, **attrs: Any) -> None: ...
    def copy(self) -> Group: ...
    async def invoke(self, ctx: Context) -> None: ...
    async def reinvoke(self, ctx: Context, *, call_hooks: bool = ...) -> None: ...


def command(name: str = ..., cls: Type[CommandT] = ..., **attrs: Any) -> Callable[[Callable[..., Coro[Any]]], CommandT]: ...
def group(name: str = ..., cls: Type[GroupT] = ..., **attrs: Any) -> Callable[[Callable[..., Coro[Any]]], GroupT]: ...
def check(predicate: Check) -> Callable[[T], T]: ...
def check_any(*checks: Check) -> Callable[[T], T]: ...
def has_role(item: Union[int, str]) -> Callable[[T], T]: ...
def has_any_role(*items: Union[int, str]) -> Callable[[T], T]: ...
def bot_has_role(item: int) -> Callable[[T], T]: ...
def bot_has_any_role(*items: int) -> Callable[[T], T]: ...
def has_permissions(**perms: bool) -> Callable[[T], T]: ...
def bot_has_permissions(**perms: bool) -> Callable[[T], T]: ...
def has_guild_permissions(**perms: bool) -> Callable[[T], T]: ...
def bot_has_guild_permissions(**perms: bool) -> Callable[[T], T]: ...
def dm_only() -> Callable[[T], T]: ...
def guild_only() -> Callable[[T], T]: ...
def is_owner() -> Callable[[T], T]: ...
def is_nsfw() -> Callable[[T], T]: ...
def cooldown(rate: int, per: float, type: Union[BucketType, Callable[[Message], Any]] = ...) -> Callable[[T], T]: ...
def dynamic_cooldown(cooldown: Union[BucketType, Callable[[Message], Any]], type: BucketType = ...) -> Callable[[T], T]: ...
def max_concurrency(number: int, per: BucketType = ..., *, wait: bool = ...) -> Callable[[T], T]: ...
def before_invoke(coro: Any) -> Callable[[T], T]: ...
def after_invoke(coro: Any) -> Callable[[T], T]: ...