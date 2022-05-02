import discord.utils
from ._types import BotT, P
from .cog import Cog
from .core import Command
from .parameters import Parameter
from .view import StringView
from discord import Interaction, Message, User
from discord.abc import MessageableChannel
from discord.embeds import Embed
from discord.file import File
from discord.guild import Guild
from discord.member import Member
from discord.mentions import AllowedMentions
from discord.message import MessageReference, PartialMessage
from discord.sticker import GuildSticker, StickerItem
from discord.ui import View
from discord.user import ClientUser
from discord.voice_client import VoiceProtocol
from typing import Any, Dict, List, Generic, Optional, Sequence, Type, TypeVar, Union

T = TypeVar('T')
CogT = TypeVar('CogT', bound='Cog')
C = TypeVar('C', bound='Context[Any]')

class Context(discord.abc.Messageable, Generic[BotT]):
    message: Message
    bot: BotT
    args: List[Any]
    kwargs: Dict[str, Any]
    prefix: Optional[str]
    command: Optional[Command[Any, Any, ..., Any]]
    view: StringView
    invoked_with: Optional[str]
    invoked_parents: List[str]
    invoked_subcommand: Optional[Command[Any, Any, ..., Any]]
    subcommand_passed: Optional[str]
    command_failed: bool
    current_parameter: Optional[Parameter]
    current_argument: Optional[str]
    interaction: Optional[Interaction]
    def __init__(self: C, *, message: Message, bot: BotT, view: StringView, args: List[Any] = ..., kwargs: Dict[str, Any] = ..., prefix: Optional[str] = ..., command: Optional[Command[Any, C, ..., Any]] = ..., invoked_with: Optional[str] = ..., invoked_parents: List[str] = ..., invoked_subcommand: Optional[Command[Any, C, ..., Any]] = ..., subcommand_passed: Optional[str] = ..., command_failed: bool = ..., current_parameter: Optional[Parameter] = ..., current_argument: Optional[str] = ..., interaction: Optional[Interaction] = ...) -> None: ...
    @classmethod
    async def from_interaction(cls: Type[C], interaction: Interaction) -> C: ...
    async def invoke(self, command: Command[CogT, C, P, T], *args: P.args, **kwargs: P.kwargs) -> T: ...
    async def reinvoke(self, *, call_hooks: bool = ..., restart: bool = ...) -> None: ...
    @property
    def valid(self) -> bool: ...
    @property
    def clean_prefix(self) -> str: ...
    @property
    def cog(self) -> Optional[Cog]: ...
    @property
    def guild(self) -> Optional[Guild]: ...
    @property
    def channel(self) -> MessageableChannel: ...
    @property
    def author(self) -> Union[User, Member]: ...
    @property
    def me(self) -> Union[Member, ClientUser]: ...
    @property
    def voice_client(self) -> Optional[VoiceProtocol]: ...
    async def send_help(self, *args: Any) -> Any: ...
    async def reply(self, content: Optional[str] = ..., **kwargs: Any) -> Message: ...
    async def defer(self, *, ephemeral: bool = ...) -> None: ...
    async def send(self, content: Optional[str] = ..., *, tts: bool = ..., embed: Optional[Embed] = ..., embeds: Optional[Sequence[Embed]] = ..., file: Optional[File] = ..., files: Optional[Sequence[File]] = ..., stickers: Optional[Sequence[Union[GuildSticker, StickerItem]]] = ..., delete_after: Optional[float] = ..., nonce: Optional[Union[str, int]] = ..., allowed_mentions: Optional[AllowedMentions] = ..., reference: Optional[Union[Message, MessageReference, PartialMessage]] = ..., mention_author: Optional[bool] = ..., view: Optional[View] = ..., suppress_embeds: bool = ..., ephemeral: bool = ...) -> Message: ...
