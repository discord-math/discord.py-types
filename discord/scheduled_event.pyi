from .abc import Snowflake
from .asset import Asset
from .channel import StageChannel, VoiceChannel
from .enums import EntityType, EventStatus, PrivacyLevel
from .guild import Guild
from .mixins import Hashable
from .state import ConnectionState
from .types.scheduled_event import GuildScheduledEvent as GuildScheduledEventPayload, GuildScheduledEventWithUserCount as GuildScheduledEventWithUserCountPayload
from .user import User
from datetime import datetime
from typing import AsyncIterator, Optional, Union

_GuildScheduledEventPayload = Union[GuildScheduledEventPayload, GuildScheduledEventWithUserCountPayload]

class ScheduledEvent(Hashable):
    id: int
    guild_id: int
    name: str
    description: Optional[str]
    entity_type: EntityType
    entity_id: Optional[int]
    start_time: datetime
    end_time: Optional[datetime]
    privacy_level: PrivacyLevel
    status: EventStatus
    user_count: int
    creator: Optional[User]
    channel_id: Optional[int]
    location: Optional[str]
    def __init__(self, *, state: ConnectionState, data: _GuildScheduledEventPayload) -> None: ...
    @classmethod
    def from_creation(cls, *, state: ConnectionState, data: _GuildScheduledEventPayload) -> None: ...
    @property
    def cover_image(self) -> Optional[Asset]: ...
    @property
    def guild(self) -> Optional[Guild]: ...
    @property
    def channel(self) -> Optional[Union[VoiceChannel, StageChannel]]: ...
    @property
    def url(self) -> str: ...
    async def start(self, *, reason: Optional[str] = ...) -> ScheduledEvent: ...
    async def end(self, *, reason: Optional[str] = ...) -> ScheduledEvent: ...
    async def cancel(self, *, reason: Optional[str] = ...) -> ScheduledEvent: ...
    async def edit(self, *, name: str = ..., description: str = ..., channel: Optional[Snowflake] = ..., start_time: datetime = ..., end_time: Optional[datetime] = ..., privacy_level: PrivacyLevel = ..., entity_type: EntityType = ..., status: EventStatus = ..., image: bytes = ..., location: str = ..., reason: Optional[str] = ...) -> ScheduledEvent: ...
    async def delete(self, *, reason: Optional[str] = ...) -> None: ...
    async def users(self, *, limit: Optional[int] = ..., before: Optional[Snowflake] = ..., after: Optional[Snowflake] = ..., oldest_first: bool = ...) -> AsyncIterator[User]: ...
