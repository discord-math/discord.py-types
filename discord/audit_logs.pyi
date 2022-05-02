import datetime
from . import abc, enums, flags
from .emoji import Emoji
from .guild import Guild
from .invite import Invite
from .member import Member
from .mixins import Hashable
from .object import Object
from .role import Role
from .stage_instance import StageInstance
from .sticker import GuildSticker
from .threads import Thread
from .types.audit_log import AuditLogChange as AuditLogChangePayload, AuditLogEntry as AuditLogEntryPayload
from .user import User
from typing import Any, Callable, ClassVar, Dict, Generator, List, Optional, Tuple, TypeVar, Union

TargetType = Union[Guild, abc.GuildChannel, Member, User, Role, Invite, Emoji, StageInstance, GuildSticker, Thread, Object, None]

class AuditLogDiff:
    def __len__(self) -> int: ...
    def __iter__(self) -> Generator[Tuple[str, Any], None, None]: ...
    def __getattr__(self, item: str) -> Any: ...
    def __setattr__(self, key: str, value: Any) -> Any: ...

Transformer = Callable[['AuditLogEntry', Any], Any]

class AuditLogChanges:
    TRANSFORMERS: ClassVar[Dict[str, Tuple[Optional[str], Optional[Transformer]]]]
    before: AuditLogDiff
    after: AuditLogDiff
    def __init__(self, entry: AuditLogEntry, data: List[AuditLogChangePayload]) -> None: ...

class _AuditLogProxy:
    def __init__(self, **kwargs: Any) -> None: ...

class _AuditLogProxyMemberPrune(_AuditLogProxy):
    delete_member_days: int
    members_removed: int

class _AuditLogProxyMemberMoveOrMessageDelete(_AuditLogProxy):
    channel: Union[abc.GuildChannel, Thread]
    count: int

class _AuditLogProxyMemberDisconnect(_AuditLogProxy):
    count: int

class _AuditLogProxyPinAction(_AuditLogProxy):
    channel: Union[abc.GuildChannel, Thread]
    message_id: int

class _AuditLogProxyStageInstanceAction(_AuditLogProxy):
    channel: abc.GuildChannel

class AuditLogEntry(Hashable):
    guild: Guild
    action: enums.AuditLogAction
    id: int
    reason: Optional[str]
    extra: Union[_AuditLogProxyMemberPrune, _AuditLogProxyMemberMoveOrMessageDelete, _AuditLogProxyMemberDisconnect, _AuditLogProxyPinAction, _AuditLogProxyStageInstanceAction, Member, User, None, Role, Object]
    user: Optional[Union[User, Member]]
    def __init__(self, *, users: Dict[int, User], data: AuditLogEntryPayload, guild: Guild) -> None: ...
    @property
    def created_at(self) -> datetime.datetime: ...
    @property
    def target(self) -> TargetType: ...
    @property
    def category(self) -> Optional[enums.AuditLogActionCategory]: ...
    @property
    def changes(self) -> AuditLogChanges: ...
    @property
    def before(self) -> AuditLogDiff: ...
    @property
    def after(self) -> AuditLogDiff: ...
