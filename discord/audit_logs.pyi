import datetime
from .abc import GuildChannel
from .emoji import Emoji
from .enums import AuditLogAction, AuditLogActionCategory
from .guild import Guild
from .invite import Invite
from .member import Member
from .mixins import Hashable
from .object import Object
from .role import Role
from .stage_instance import StageInstance
from .sticker import GuildSticker
from .threads import Thread
from .user import User
from typing import Any, ClassVar, Dict, Generator, List, Optional, Tuple, Union

class AuditLogDiff:
    def __len__(self) -> int: ...
    def __iter__(self) -> Generator[Tuple[str, Any], None, None]: ...
    def __getattr__(self, item: str) -> Any: ...
    def __setattr__(self, key: str, value: Any) -> Any: ...

class AuditLogChanges:
    before: AuditLogDiff
    after: AuditLogDiff

class _AuditLogProxyMemberPrune:
    delete_member_days: int
    members_removed: int

class _AuditLogProxyMemberMoveOrMessageDelete:
    channel: GuildChannel
    count: int

class _AuditLogProxyMemberDisconnect:
    count: int

class _AuditLogProxyPinAction:
    channel: GuildChannel
    message_id: int

class _AuditLogProxyStageInstanceAction:
    channel: GuildChannel

class AuditLogEntry(Hashable):
    guild: Guild
    action: AuditLogAction
    id: int
    reason: Optional[str]
    extra: Any
    user: Union[Member, User, None]
    @property
    def created_at(self) -> datetime.datetime: ...
    @property
    def target(self) -> Union[Guild, GuildChannel, Member, User, Role, Invite, Emoji, StageInstance, GuildSticker, Thread, Object, None]: ...
    @property
    def category(self) -> AuditLogActionCategory: ...
    @property
    def changes(self) -> AuditLogChanges: ...
    @property
    def before(self) -> AuditLogDiff: ...
    @property
    def after(self) -> AuditLogDiff: ...
