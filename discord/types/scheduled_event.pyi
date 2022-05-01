from .channel import PrivacyLevel
from .member import Member
from .snowflake import Snowflake
from .user import User
from typing import List, Literal, Optional, TypedDict, Union
from typing_extensions import NotRequired

EventStatus = Literal[1, 2, 3, 4]
EntityType = Literal[1, 2, 3]

class _BaseGuildScheduledEvent(TypedDict):
    id: Snowflake
    guild_id: Snowflake
    entity_id: Optional[Snowflake]
    name: str
    scheduled_start_time: str
    privacy_level: PrivacyLevel
    status: EventStatus
    creator_id: NotRequired[Optional[Snowflake]]
    description: NotRequired[Optional[str]]
    creator: NotRequired[User]
    user_count: NotRequired[int]
    image: NotRequired[Optional[str]]

class _VoiceChannelScheduledEvent(_BaseGuildScheduledEvent):
    channel_id: Snowflake
    entity_metadata: Literal[None]
    scheduled_end_time: NotRequired[Optional[str]]

class StageInstanceScheduledEvent(_VoiceChannelScheduledEvent):
    entity_type: Literal[1]

class VoiceScheduledEvent(_VoiceChannelScheduledEvent):
    entity_type: Literal[2]

class EntityMetadata(TypedDict):
    location: str

class ExternalScheduledEvent(_BaseGuildScheduledEvent):
    channel_id: Literal[None]
    entity_metadata: EntityMetadata
    scheduled_end_time: str
    entity_type: Literal[3]
GuildScheduledEvent = Union[StageInstanceScheduledEvent, VoiceScheduledEvent, ExternalScheduledEvent]

class _WithUserCount(TypedDict):
    user_count: int

class _StageInstanceScheduledEventWithUserCount(StageInstanceScheduledEvent, _WithUserCount): ... # type: ignore
class _VoiceScheduledEventWithUserCount(VoiceScheduledEvent, _WithUserCount): ... # type: ignore
class _ExternalScheduledEventWithUserCount(ExternalScheduledEvent, _WithUserCount): ... # type: ignore

GuildScheduledEventWithUserCount = Union[_StageInstanceScheduledEventWithUserCount, _VoiceScheduledEventWithUserCount, _ExternalScheduledEventWithUserCount]

class ScheduledEventUser(TypedDict):
    guild_scheduled_event_id: Snowflake
    user: User

class ScheduledEventUserWithMember(ScheduledEventUser):
    member: Member
ScheduledEventUsers = List[ScheduledEventUser]
ScheduledEventUsersWithMember = List[ScheduledEventUserWithMember]
