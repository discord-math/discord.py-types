import abc
import array
import collections.abc
import datetime
from .abc import Snowflake
from .permissions import Permissions
from typing import Any, AsyncIterator, Callable, Iterable, Iterator, List, Literal, Optional, TypeVar, Union, overload

DISCORD_EPOCH: int
MISSING: Any

TimestampStyle = Literal['f', 'F', 'd', 'D', 't', 'T', 'R']

T = TypeVar('T')

def oauth_url(client_id: Union[int, str], *, permissions: Permissions = ..., guild: Snowflake = ..., redirect_uri: str = ..., scopes: Iterable[str] = ..., disable_guild_select: bool = ...) -> str: ...
def snowflake_time(id: int) -> datetime.datetime: ...
def time_snowflake(dt: datetime.datetime, high: bool = ...) -> int: ...
def find(predicate: Callable[[T], Any], seq: Iterable[T]) -> Optional[T]: ...
def get(iterable: Iterable[T], **attrs: Any) -> Optional[T]: ...
async def sleep_until(when: datetime.datetime, result: Optional[T] = ...) -> Optional[T]: ...
def utcnow() -> datetime.datetime: ...

class SnowflakeList(array.array[int]):
    def __init__(self, data: Iterable[int], *, is_sorted: bool = ...) -> None: ...
    def add(self, element: int) -> None: ...
    def get(self, element: int) -> Optional[int]: ...
    def has(self, element: int) -> bool: ...

def remove_markdown(text: str, *, ignore_links: bool = ...) -> str: ...
def escape_markdown(text: str, *, as_needed: bool = ..., ignore_links: bool = ...) -> str: ...
def escape_mentions(text: str) -> str: ...
@overload
def as_chunks(iterator: Iterator[T], max_size: int) -> Iterator[List[T]]: ...
@overload
def as_chunks(iterator: AsyncIterator[T], max_size: int) -> AsyncIterator[List[T]]: ...
def format_dt(dt: datetime.datetime, style: Optional[TimestampStyle] = ...) -> str: ...