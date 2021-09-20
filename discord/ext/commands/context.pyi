import discord.utils
import inspect
from .bot import AutoShardedBot, Bot
from .cog import Cog
from .core import Command
from .view import StringView
from discord.abc import MessageableChannel
from discord.guild import Guild
from discord.member import Member
from discord.message import Message
from discord.user import ClientUser, User
from discord.voice_client import VoiceProtocol
from typing import Any, Dict, Generic, List, Optional, Union

class Context(discord.abc.Messageable):
    message: Message
    bot: Union[AutoShardedBot, Bot]
    args: List[Any]
    kwargs: Dict[str, Any]
    prefix: Optional[str]
    command: Optional[Command]
    view: StringView
    invoked_with: Optional[str]
    invoked_parents: List[str]
    invoked_subcommand: Optional[Command]
    subcommand_passed: Optional[str]
    command_failed: bool
    current_parameter: Optional[inspect.Parameter]
    def __init__(self, message: Message, bot: Union[AutoShardedBot, Bot], view: StringView, *, args: List[Any] = ..., kwargs: Dict[str, Any] = ..., prefix: Optional[str] = ..., command: Optional[Command] = ..., invoked_with: Optional[str] = ..., invoked_parents: List[str] = ..., invoked_subcommand: Optional[Command] = ..., subcommand_passed: Optional[str] = ..., command_failed: bool = ..., current_parameter: Optional[inspect.Parameter] = ...) -> None: ...
    async def invoke(self, command: Command, *args: Any, **kwargs: Any) -> Any: ...
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
