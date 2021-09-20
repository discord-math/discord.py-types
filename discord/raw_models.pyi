from .partial_emoji import PartialEmoji
from .member import Member
from .message import Message
from .types.raw_models import MessageUpdateEvent
from typing import List, Optional, Set

class _RawReprMixin:
    pass

class RawMessageDeleteEvent(_RawReprMixin):
    message_id: int
    channel_id: int
    cached_message: Optional[Message]
    guild_id: Optional[int]

class RawBulkMessageDeleteEvent(_RawReprMixin):
    message_ids: Set[int]
    channel_id: int
    cached_messages: List[Message]
    guild_id: Optional[int]

class RawMessageUpdateEvent(_RawReprMixin):
    message_id: int
    channel_id: int
    data: MessageUpdateEvent
    cached_message: Optional[Message]
    guild_id: Optional[int]

class RawReactionActionEvent(_RawReprMixin):
    message_id: int
    channel_id: int
    user_id: int
    emoji: PartialEmoji
    event_type: str
    member: Optional[Member]
    guild_id: Optional[int]

class RawReactionClearEvent(_RawReprMixin):
    message_id: int
    channel_id: int
    guild_id: int

class RawReactionClearEmojiEvent(_RawReprMixin):
    emoji: PartialEmoji
    message_id: int
    channel_id: int
    guild_id: int

class RawIntegrationDeleteEvent(_RawReprMixin):
    integration_id: int
    guild_id: int
    application_id: Optional[int]
