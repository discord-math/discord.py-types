import datetime
import io
from .abc import GuildChannel, MessageableChannel as MessageableChannel, Snowflake
from .embeds import Embed
from .emoji import Emoji
from .enums import InteractionType, MessageType, ChannelType
from .components import Component
from .file import File
from .flags import MessageFlags
from .guild import Guild
from .member import Member
from .mentions import AllowedMentions
from .mixins import Hashable
from .partial_emoji import PartialEmoji
from .reaction import Reaction
from .role import Role
from .state import ConnectionState
from .sticker import StickerItem
from .threads import Thread
from .types.interactions import MessageInteraction as MessageInteractionPayload
from .types.message import Attachment as AttachmentPayload, Message as MessagePayload, MessageActivity as MessageActivityPayload, MessageApplication as MessageApplicationPayload, MessageReference as MessageReferencePayload
from .types.threads import ThreadArchiveDuration
from .ui.view import View
from .user import User
from os import PathLike
from typing import Any, List, Optional, Sequence, Type, TypeVar, Union, overload

EmojiInputType = Union[Emoji, PartialEmoji, str]

class Attachment(Hashable):
    id: int
    size: int
    height: Optional[int]
    width: Optional[int]
    filename: str
    url: str
    proxy_url: str
    content_type: Optional[str]
    description: Optional[str]
    ephemeral: bool
    def __init__(self, *, data: AttachmentPayload, state: ConnectionState) -> None: ...
    def is_spoiler(self) -> bool: ...
    async def save(self, fp: Union[io.BufferedIOBase, PathLike[Any]], *, seek_begin: bool = ..., use_cached: bool = ...) -> int: ...
    async def read(self, *, use_cached: bool = ...) -> bytes: ...
    async def to_file(self, *, filename: Optional[str] = ..., description: Optional[str] = ..., use_cached: bool = ..., spoiler: bool = ...) -> File: ...
    def to_dict(self) -> AttachmentPayload: ...

class DeletedReferencedMessage:
    def __init__(self, parent: MessageReference) -> None: ...
    @property
    def id(self) -> int: ...
    @property
    def channel_id(self) -> int: ...
    @property
    def guild_id(self) -> Optional[int]: ...

MR = TypeVar('MR', bound='MessageReference')

class MessageReference:
    message_id: Optional[int]
    channel_id: int
    guild_id: Optional[int]
    fail_if_not_exists: bool
    resolved: Optional[Union[Message, DeletedReferencedMessage]]
    def __init__(self, *, message_id: int, channel_id: int, guild_id: Optional[int] = ..., fail_if_not_exists: bool = ...) -> None: ...
    @classmethod
    def with_state(cls: Type[MR], state: ConnectionState, data: MessageReferencePayload) -> MR: ...
    @classmethod
    def from_message(cls: Type[MR], message: PartialMessage, *, fail_if_not_exists: bool = ...) -> MR: ...
    @property
    def cached_message(self) -> Optional[Message]: ...
    @property
    def jump_url(self) -> str: ...
    def to_dict(self) -> MessageReferencePayload: ...
    def to_message_reference_dict(self) -> MessageReferencePayload: ...

class MessageInteraction(Hashable):
    id: int
    type: InteractionType
    name: str
    user: Union[User, Member]
    def __init__(self, *, state: ConnectionState, guild: Optional[Guild], data: MessageInteractionPayload) -> None: ...
    @property
    def created_at(self) -> datetime.datetime: ...

class PartialMessage(Hashable):
    channel: MessageableChannel
    id: int
    guild: Optional[Guild]
    def __init__(self, *, channel: MessageableChannel, id: int) -> None: ...
    pinned: Any
    @property
    def created_at(self) -> datetime.datetime: ...
    @property
    def jump_url(self) -> str: ...
    async def fetch(self) -> Message: ...
    async def delete(self, *, delay: Optional[float] = ...) -> None: ...
    @overload
    async def edit(self, *, content: Optional[str] = ..., embed: Optional[Embed] = ..., attachments: Sequence[Union[Attachment, File]] = ..., delete_after: Optional[float] = ..., allowed_mentions: Optional[AllowedMentions] = ..., view: Optional[View] = ...) -> Message: ...
    @overload
    async def edit(self, *, content: Optional[str] = ..., embeds: Sequence[Embed] = ..., attachments: Sequence[Union[Attachment, File]] = ..., delete_after: Optional[float] = ..., allowed_mentions: Optional[AllowedMentions] = ..., view: Optional[View] = ...) -> Message: ...
    async def publish(self) -> None: ...
    async def pin(self, *, reason: Optional[str] = ...) -> None: ...
    async def unpin(self, *, reason: Optional[str] = ...) -> None: ...
    async def add_reaction(self, emoji: EmojiInputType) -> None: ...
    async def remove_reaction(self, emoji: Union[EmojiInputType, Reaction], member: Snowflake) -> None: ...
    async def clear_reaction(self, emoji: Union[EmojiInputType, Reaction]) -> None: ...
    async def clear_reactions(self) -> None: ...
    async def create_thread(self, *, name: str, auto_archive_duration: ThreadArchiveDuration = ..., slowmode_delay: Optional[int] = ..., reason: Optional[str] = ...) -> Thread: ...
    async def reply(self, content: Optional[str] = ..., **kwargs: Any) -> Message: ...
    def to_reference(self, *, fail_if_not_exists: bool = ...) -> MessageReference: ...
    def to_message_reference_dict(self) -> MessageReferencePayload: ...

class Message(PartialMessage, Hashable):
    tts: bool
    content: str
    channel: MessageableChannel
    webhook_id: Optional[int]
    mention_everyone: bool
    embeds: List[Embed]
    mentions: List[Union[User, Member]]
    author: Union[User, Member]
    attachments: List[Attachment]
    nonce: Optional[Union[int, str]]
    pinned: bool
    role_mentions: List[Role]
    type: MessageType
    flags: MessageFlags
    reactions: List[Reaction]
    reference: Optional[MessageReference]
    application: Optional[MessageApplicationPayload]
    activity: Optional[MessageActivityPayload]
    stickers: List[StickerItem]
    components: List[Component]
    interaction: Optional[MessageInteraction]
    def __init__(self, *, state: ConnectionState, channel: MessageableChannel, data: MessagePayload) -> None: ...
    def raw_mentions(self) -> List[int]: ...
    def raw_channel_mentions(self) -> List[int]: ...
    def raw_role_mentions(self) -> List[int]: ...
    def channel_mentions(self) -> List[Union[GuildChannel, Thread]]: ...
    def clean_content(self) -> str: ...
    @property
    def created_at(self) -> datetime.datetime: ...
    @property
    def edited_at(self) -> Optional[datetime.datetime]: ...
    def is_system(self) -> bool: ...
    def system_content(self) -> Optional[str]: ...
    @overload
    async def edit(self, *, content: Optional[str] = ..., embed: Optional[Embed] = ..., attachments: Sequence[Union[Attachment, File]] = ..., suppress: bool = ..., delete_after: Optional[float] = ..., allowed_mentions: Optional[AllowedMentions] = ..., view: Optional[View] = ...) -> Message: ...
    @overload
    async def edit(self, *, content: Optional[str] = ..., embeds: Sequence[Embed] = ..., attachments: Sequence[Union[Attachment, File]] = ..., suppress: bool = ..., delete_after: Optional[float] = ..., allowed_mentions: Optional[AllowedMentions] = ..., view: Optional[View] = ...) -> Message: ...
    async def add_files(self, *files: File) -> Message: ...
    async def remove_attachments(self, *attachments: Attachment) -> Message: ...
