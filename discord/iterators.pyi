import datetime
from .abc import Snowflake
from .audit_logs import AuditLogEntry
from .guild import Guild
from .member import Member
from .message import Message
from .threads import Thread
from .user import User
from typing import Any, AsyncIterator, Awaitable, Callable, List, Optional, TypeVar, Union

T = TypeVar('T')
OT = TypeVar('OT')
_Func = Callable[[T], Union[OT, Awaitable[OT]]]

class _AsyncIterator(AsyncIterator[T]):
    async def next(self) -> T: ...
    def get(self, **attrs: Any) -> Awaitable[Optional[T]]: ...
    async def find(self, predicate: _Func[T, bool]) -> Optional[T]: ...
    def chunk(self, max_size: int) -> _ChunkedAsyncIterator[T]: ...
    def map(self, func: _Func[T, OT]) -> _MappedAsyncIterator[OT]: ...
    def filter(self, predicate: _Func[T, bool]) -> _FilteredAsyncIterator[T]: ...
    async def flatten(self) -> List[T]: ...
    async def __anext__(self) -> T: ...

class _ChunkedAsyncIterator(_AsyncIterator[List[T]]):
    async def next(self) -> List[T]: ...

class _MappedAsyncIterator(_AsyncIterator[T]):
    async def next(self) -> T: ...

class _FilteredAsyncIterator(_AsyncIterator[T]):
    async def next(self) -> T: ...

class ReactionIterator(_AsyncIterator[Union['User', 'Member']]):
    async def next(self) -> Union[User, Member]: ...
    async def fill_users(self) -> None: ...

class HistoryIterator(_AsyncIterator['Message']):
    async def next(self) -> Message: ...
    async def fill_messages(self) -> None: ...

class AuditLogIterator(_AsyncIterator['AuditLogEntry']):
    async def next(self) -> AuditLogEntry: ...

class GuildIterator(_AsyncIterator['Guild']):
    async def next(self) -> Guild: ...
    async def fill_guilds(self) -> None: ...

class MemberIterator(_AsyncIterator['Member']):
    async def next(self) -> Member: ...
    async def fill_members(self) -> None: ...

class ArchivedThreadIterator(_AsyncIterator['Thread']):
    has_more: bool
    async def next(self) -> Thread: ...
    async def fill_queue(self) -> None: ...