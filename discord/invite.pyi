import datetime
from .abc import GuildChannel, Snowflake
from .asset import Asset
from .enums import ChannelType, InviteTarget, NSFWLevel, VerificationLevel
from .guild import Guild
from .mixins import Hashable
from .object import Object
from .scheduled_event import ScheduledEvent
from .state import ConnectionState
from .types.channel import PartialChannel as InviteChannelPayload
from .types.invite import GatewayInvite as GatewayInvitePayload, Invite as InvitePayload, InviteGuild as InviteGuildPayload
from .user import User
from typing import List, Optional, Type, TypeVar, Union

InviteGuildType = Union[Guild, 'PartialInviteGuild', Object]
InviteChannelType = Union[GuildChannel, 'PartialInviteChannel', Object]

class PartialInviteChannel:
    id: int
    name: str
    type: ChannelType
    def __init__(self, data: InviteChannelPayload) -> None: ...
    @property
    def mention(self) -> str: ...
    @property
    def created_at(self) -> datetime.datetime: ...

class PartialInviteGuild:
    features: List[str]
    id: int
    name: str
    verification_level: VerificationLevel
    description: Optional[str]
    vanity_url_code: Optional[str]
    nsfw_level: NSFWLevel
    premium_subscription_count: int
    def __init__(self, state: ConnectionState, data: InviteGuildPayload, id: int) -> None: ...
    @property
    def created_at(self) -> datetime.datetime: ...
    @property
    def vanity_url(self) -> Optional[str]: ...
    @property
    def icon(self) -> Optional[Asset]: ...
    @property
    def banner(self) -> Optional[Asset]: ...
    @property
    def splash(self) -> Optional[Asset]: ...

I = TypeVar('I', bound='Invite')

class Invite(Hashable):
    BASE: str
    max_age: Optional[int]
    code: str
    guild: Optional[InviteGuildType]
    revoked: Optional[bool]
    created_at: Optional[datetime.datetime]
    uses: Optional[int]
    temporary: Optional[bool]
    max_uses: Optional[int]
    inviter: Optional[User]
    channel: Optional[InviteChannelType]
    target_user: Optional[User]
    target_type: InviteTarget
    approximate_member_count: Optional[int]
    approximate_presence_count: Optional[int]
    target_application:Optional[int]
    expires_at: Optional[datetime.datetime]
    scheduled_event: Optional[ScheduledEvent]
    scheduled_event_id: Optional[int]
    def __init__(self, *, state: ConnectionState, data: InvitePayload, guild: Optional[Union[PartialInviteGuild, Guild]] = ..., channel: Optional[Union[PartialInviteChannel, GuildChannel]] = ...) -> None: ...
    @classmethod
    def from_incomplete(cls: Type[I], *, state: ConnectionState, data: InvitePayload) -> I: ...
    @classmethod
    def from_gateway(cls: Type[I], *, state: ConnectionState, data: GatewayInvitePayload) -> I: ...
    def __hash__(self) -> int: ...
    @property
    def id(self) -> str: ... # type: ignore
    @property
    def url(self) -> str: ...
    def set_scheduled_event(self: I, scheduled_event: Snowflake) -> I: ...
    async def delete(self, *, reason: Optional[str] = ...) -> None: ...
