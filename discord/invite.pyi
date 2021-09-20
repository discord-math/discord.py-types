import datetime
from .abc import GuildChannel
from .appinfo import PartialAppInfo
from .asset import Asset
from .enums import ChannelType, InviteTarget, VerificationLevel
from .guild import Guild
from .mixins import Hashable
from .object import Object
from .user import User
from typing import List, Optional, TypeVar, Union

InviteGuildType = Union[Guild, 'PartialInviteGuild', Object]
InviteChannelType = Union[GuildChannel, 'PartialInviteChannel', Object]

class PartialInviteChannel:
    id: int
    name: str
    type: ChannelType
    @property
    def mention(self) -> str: ...
    @property
    def created_at(self) -> datetime.datetime: ...

class PartialInviteGuild:
    id: int
    name: str
    features: List[str]
    verification_level: VerificationLevel
    description: Optional[str]
    @property
    def created_at(self) -> datetime.datetime: ...
    @property
    def icon(self) -> Optional[Asset]: ...
    @property
    def banner(self) -> Optional[Asset]: ...
    @property
    def splash(self) -> Optional[Asset]: ...

class Invite:
    BASE: str
    max_age: Optional[int]
    code: str
    guild: Optional[InviteGuildType]
    revoked: Optional[bool]
    created_at: Optional[datetime.datetime]
    temporary: Optional[bool]
    uses: Optional[int]
    max_uses: Optional[int]
    approximate_presence_count: Optional[int]
    approximate_member_count: Optional[int]
    expires_at: Optional[datetime.datetime]
    inviter: Optional[User]
    channel: Optional[InviteChannelType]
    target_user: Optional[User]
    target_type: InviteTarget
    target_application: Optional[PartialAppInfo]
    def __hash__(self) -> int: ...
    @property
    def id(self) -> str: ...
    @property
    def url(self) -> str: ...
    async def delete(self, *, reason: Optional[str] = ...) -> None: ...
