import datetime
from .enums import ChannelType
from .member import Member
from .message import Message
from .partial_emoji import PartialEmoji
from .threads import Thread
from .types.gateway import GuildMemberRemoveEvent, IntegrationDeleteEvent, MessageDeleteBulkEvent as BulkMessageDeleteEvent, MessageDeleteEvent, MessageReactionAddEvent, MessageReactionRemoveAllEvent as ReactionClearEvent, MessageReactionRemoveEmojiEvent as ReactionClearEmojiEvent, MessageReactionRemoveEvent, MessageUpdateEvent, ThreadDeleteEvent, TypingStartEvent
from .user import User
from typing import List, Optional, Set, Union

ReactionActionEvent = Union[MessageReactionAddEvent, MessageReactionRemoveEvent]

class _RawReprMixin: ...

class RawMessageDeleteEvent(_RawReprMixin):
    message_id: int
    channel_id: int
    cached_message: Optional[Message]
    guild_id: Optional[int]
    def __init__(self, data: MessageDeleteEvent) -> None: ...

class RawBulkMessageDeleteEvent(_RawReprMixin):
    message_ids: Set[int]
    channel_id: int
    cached_messages: List[Message]
    guild_id: Optional[int]
    def __init__(self, data: BulkMessageDeleteEvent) -> None: ...

class RawMessageUpdateEvent(_RawReprMixin):
    message_id: int
    channel_id: int
    data: MessageUpdateEvent
    cached_message: Optional[Message]
    guild_id: Optional[int]
    def __init__(self, data: MessageUpdateEvent) -> None: ...

class RawReactionActionEvent(_RawReprMixin):
    message_id: int
    channel_id: int
    user_id: int
    emoji: PartialEmoji
    event_type: str
    member: Optional[Member]
    guild_id: Optional[int]
    def __init__(self, data: ReactionActionEvent, emoji: PartialEmoji, event_type: str) -> None: ...

class RawReactionClearEvent(_RawReprMixin):
    message_id: int
    channel_id: int
    guild_id: Optional[int]
    def __init__(self, data: ReactionClearEvent) -> None: ...

class RawReactionClearEmojiEvent(_RawReprMixin):
    emoji: PartialEmoji
    message_id: int
    channel_id: int
    guild_id: Optional[int]
    def __init__(self, data: ReactionClearEmojiEvent, emoji: PartialEmoji) -> None: ...

class RawIntegrationDeleteEvent(_RawReprMixin):
    integration_id: int
    guild_id: int
    application_id: Optional[int]
    def __init__(self, data: IntegrationDeleteEvent) -> None: ...

class RawThreadDeleteEvent(_RawReprMixin):
    thread_id: int
    thread_type: ChannelType
    guild_id: int
    parent_id: int
    thread: Optional[Thread]
    def __init__(self, data: ThreadDeleteEvent) -> None: ...

class RawTypingEvent(_RawReprMixin):
    channel_id: int
    user_id: int
    user: Optional[Union[User, Member]]
    timestamp: datetime.datetime
    guild_id: Optional[int]
    def __init__(self, data: TypingStartEvent) -> None: ...

class RawMemberRemoveEvent(_RawReprMixin):
    user: Union[User, Member]
    guild_id: int
    def __init__(self, data: GuildMemberRemoveEvent, user: User) -> None: ...
