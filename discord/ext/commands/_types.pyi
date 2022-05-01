from .bot import AutoShardedBot as AutoShardedBot, Bot as Bot
from .cog import Cog as Cog
from .context import Context as Context
from .errors import CommandError as CommandError
from typing import Any, Awaitable, Callable, Coroutine, Optional, ParamSpec, TypeVar, Union

T = TypeVar('T')
P = ParamSpec('P')
# MaybeAwaitableFunc = Callable[P, 'MaybeAwaitable[T]']
_Bot = Union['Bot', 'AutoShardedBot']
Coro = Coroutine[Any, Any, T]
CoroFunc = Callable[..., Coro[Any]]
MaybeCoro = Union[T, Coro[T]]
MaybeAwaitable = Union[T, Awaitable[T]]
CogT = TypeVar('CogT', bound='Optional[Cog]')
Check = Callable[["ContextT"], MaybeCoro[bool]]
Hook = Union[Callable[["CogT", "ContextT"], Coro[Any]], Callable[["ContextT"], Coro[Any]]]
Error = Union[Callable[["CogT", "ContextT", "CommandError"], Coro[Any]], Callable[["ContextT", "CommandError"], Coro[Any]]]
ContextT = TypeVar('ContextT', bound='Context[Any]')
BotT = TypeVar('BotT', bound=_Bot, covariant=True)

class _BaseCommand: ...
