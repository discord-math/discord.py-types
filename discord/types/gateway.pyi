from .activity import PartialPresenceUpdate
from .appinfo import GatewayAppInfo, PartialAppInfo
from .channel import ChannelType, StageInstance
from .emoji import Emoji, PartialEmoji
from .guild import Guild, UnavailableGuild
from .integration import BaseIntegration, IntegrationApplication
from .interactions import Interaction
from .invite import InviteTargetType
from .member import MemberWithUser
from .message import Message
from .role import Role
from .scheduled_event import GuildScheduledEvent
from .snowflake import Snowflake
from .sticker import GuildSticker
from .threads import Thread, ThreadMember
from .user import User
from .voice import GuildVoiceState
from typing import List, Literal, Optional, TypedDict
from typing_extensions import NotRequired, Required

class SessionStartLimit(TypedDict):
    total: int
    remaining: int
    reset_after: int
    max_concurrency: int

class Gateway(TypedDict):
    url: str

class GatewayBot(Gateway):
    shards: int
    session_start_limit: SessionStartLimit

class ReadyEvent(TypedDict):
    v: int
    user: User
    guilds: List[UnavailableGuild]
    session_id: str
    shard: List[int]
    application: GatewayAppInfo
ResumedEvent = Literal[None]
MessageCreateEvent = Message

class MessageDeleteEvent(TypedDict):
    id: Snowflake
    channel_id: Snowflake
    guild_id: NotRequired[Snowflake]

class MessageDeleteBulkEvent(TypedDict):
    ids: List[Snowflake]
    channel_id: Snowflake
    guild_id: NotRequired[Snowflake]

class MessageUpdateEvent(Message):
    channel_id: Snowflake # type: ignore

class MessageReactionAddEvent(TypedDict):
    user_id: Snowflake
    channel_id: Snowflake
    message_id: Snowflake
    emoji: PartialEmoji
    member: NotRequired[MemberWithUser]
    guild_id: NotRequired[Snowflake]

class MessageReactionRemoveEvent(TypedDict):
    user_id: Snowflake
    channel_id: Snowflake
    message_id: Snowflake
    emoji: PartialEmoji
    guild_id: NotRequired[Snowflake]

class MessageReactionRemoveAllEvent(TypedDict):
    message_id: Snowflake
    channel_id: Snowflake
    guild_id: NotRequired[Snowflake]

class MessageReactionRemoveEmojiEvent(TypedDict):
    emoji: PartialEmoji
    message_id: Snowflake
    channel_id: Snowflake
    guild_id: NotRequired[Snowflake]
InteractionCreateEvent = Interaction
PresenceUpdateEvent = PartialPresenceUpdate
UserUpdateEvent = User

class InviteCreateEvent(TypedDict):
    channel_id: Snowflake
    code: str
    created_at: str
    max_age: int
    max_uses: int
    temporary: bool
    uses: Literal[0]
    guild_id: NotRequired[Snowflake]
    inviter: NotRequired[User]
    target_type: NotRequired[InviteTargetType]
    target_user: NotRequired[User]
    target_application: NotRequired[PartialAppInfo]

class InviteDeleteEvent(TypedDict):
    channel_id: Snowflake
    code: str
    guild_id: NotRequired[Snowflake]

class _ChannelEvent(TypedDict):
    id: Snowflake
    type: ChannelType

ChannelCreateEvent = _ChannelEvent
ChannelUpdateEvent = _ChannelEvent
ChannelDeleteEvent = _ChannelEvent

class ChannelPinsUpdateEvent(TypedDict):
    channel_id: Snowflake
    guild_id: NotRequired[Snowflake]
    last_pin_timestamp: NotRequired[Optional[str]]

class ThreadCreateEvent(Thread, total=False):
    newly_created: bool # type: ignore
    members: List[ThreadMember]
ThreadUpdateEvent = Thread

class ThreadDeleteEvent(TypedDict):
    id: Snowflake
    guild_id: Snowflake
    parent_id: Snowflake
    type: ChannelType

class ThreadListSyncEvent(TypedDict):
    guild_id: Snowflake
    threads: List[Thread]
    members: List[ThreadMember]
    channel_ids: NotRequired[List[Snowflake]]

class ThreadMemberUpdate(ThreadMember):
    guild_id: Snowflake

class ThreadMembersUpdate(TypedDict):
    id: Snowflake
    guild_id: Snowflake
    member_count: int
    added_members: NotRequired[List[ThreadMember]]
    removed_member_ids: NotRequired[List[Snowflake]]

class GuildMemberAddEvent(MemberWithUser):
    guild_id: Snowflake

class GuildMemberRemoveEvent(TypedDict):
    guild_id: Snowflake
    user: User

class GuildMemberUpdateEvent(TypedDict):
    guild_id: Snowflake
    roles: List[Snowflake]
    user: User
    avatar: Optional[str]
    joined_at: Optional[str]
    nick: NotRequired[str]
    premium_since: NotRequired[Optional[str]]
    deaf: NotRequired[bool]
    mute: NotRequired[bool]
    pending: NotRequired[bool]
    communication_disabled_until: NotRequired[str]

class GuildEmojisUpdateEvent(TypedDict):
    guild_id: Snowflake
    emojis: List[Emoji]

class GuildStickersUpdateEvent(TypedDict):
    guild_id: Snowflake
    stickers: List[GuildSticker]
GuildCreateEvent = Guild
GuildUpdateEvent = Guild
GuildDeleteEvent = UnavailableGuild

class _GuildBanEvent(TypedDict):
    guild_id: Snowflake
    user: User

GuildBanAddEvent = _GuildBanEvent
GuildBanRemoveEvent = _GuildBanEvent

class _GuildRoleEvent(TypedDict):
    guild_id: Snowflake
    role: Role

class GuildRoleDeleteEvent(TypedDict):
    guild_id: Snowflake
    role_id: Snowflake

GuildRoleCreateEvent = _GuildRoleEvent
GuildRoleUpdateEvent = _GuildRoleEvent

class GuildMembersChunkEvent(TypedDict):
    guild_id: Snowflake
    members: List[MemberWithUser]
    chunk_index: int
    chunk_count: int
    not_found: NotRequired[List[Snowflake]]
    presences: NotRequired[List[PresenceUpdateEvent]]
    nonce: NotRequired[str]

class GuildIntegrationsUpdateEvent(TypedDict):
    guild_id: Snowflake

class _IntegrationEvent(BaseIntegration, total=False):
    guild_id: Required[Snowflake]
    role_id: Optional[Snowflake]
    enable_emoticons: bool
    subscriber_count: int
    revoked: bool
    application: IntegrationApplication

IntegrationCreateEvent = _IntegrationEvent
IntegrationUpdateEvent = _IntegrationEvent

class IntegrationDeleteEvent(TypedDict):
    id: Snowflake
    guild_id: Snowflake
    application_id: NotRequired[Snowflake]

class WebhooksUpdateEvent(TypedDict):
    guild_id: Snowflake
    channel_id: Snowflake
StageInstanceCreateEvent = StageInstance
StageInstanceUpdateEvent = StageInstance
StageInstanceDeleteEvent = StageInstance
GuildScheduledEventCreateEvent = GuildScheduledEvent
GuildScheduledEventUpdateEvent = GuildScheduledEvent
GuildScheduledEventDeleteEvent = GuildScheduledEvent

class _GuildScheduledEventUsersEvent(TypedDict):
    guild_scheduled_event_id: Snowflake
    user_id: Snowflake
    guild_id: Snowflake

GuildScheduledEventUserAdd = _GuildScheduledEventUsersEvent
GuildScheduledEventUserRemove = _GuildScheduledEventUsersEvent
VoiceStateUpdateEvent = GuildVoiceState

class VoiceServerUpdateEvent(TypedDict):
    token: str
    guild_id: Snowflake
    endpoint: Optional[str]

class TypingStartEvent(TypedDict):
    channel_id: Snowflake
    user_id: Snowflake
    timestamp: int
    guild_id: NotRequired[Snowflake]
    member: NotRequired[MemberWithUser]
