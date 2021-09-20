from .cog import Cog
from .context import Context
from .errors import CommandError
from typing import Any, Callable, Coroutine, TypeVar, Union

T = TypeVar('T')
Coro = Coroutine[Any, Any, T]
MaybeCoro = Union[T, Coro[T]]
CoroFunc = Callable[..., Coro[Any]]
Check = Union[Callable[["Cog", "Context"], MaybeCoro[bool]], Callable[["Context"], MaybeCoro[bool]]]
Hook = Union[Callable[["Cog", "Context"], Coro[Any]], Callable[["Context"], Coro[Any]]]
Error = Union[Callable[["Cog", "Context", "CommandError"], Coro[Any]], Callable[["Context", "CommandError"], Coro[Any]]]

class _BaseCommand: ...
