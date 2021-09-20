import aiohttp
import datetime
from ..abc import Snowflake
from ..asset import Asset
from ..channel import TextChannel
from ..embeds import Embed
from ..enums import WebhookType
from ..file import File
from ..guild import Guild
from ..mentions import AllowedMentions
from ..message import Message
from ..mixins import Hashable
from ..state import ConnectionState
from ..ui.view import View
from ..user import BaseUser, User
from typing import Any, Dict, List, Literal, NamedTuple, Optional, Union, overload

class PartialWebhookChannel(Hashable):
    id: int
    name: Any
    def __init__(self, data: Any) -> None: ...

class PartialWebhookGuild(Hashable):
    id: int
    name: Any
    def __init__(self, data: Any, state: ConnectionState) -> None: ...
    @property
    def icon(self) -> Optional[Asset]: ...

class WebhookMessage(Message):
    async def edit(self, content: Optional[str] = ..., embeds: List[Embed] = ..., embed: Optional[Embed] = ..., file: File = ..., files: List[File] = ..., view: Optional[View] = ..., allowed_mentions: Optional[AllowedMentions] = ...) -> WebhookMessage: ... # type: ignore
    async def delete(self, *, delay: Optional[float] = ...) -> None: ...

class BaseWebhook(Hashable):
    id: int
    type: WebhookType
    guild_id: int
    channel_id: int
    token: Optional[str]
    auth_token: Optional[str]
    user: Optional[Union[BaseUser, User]]
    name: Optional[str]
    source_guild: Optional[PartialWebhookGuild]
    source_channel: Optional[PartialWebhookChannel]
    def is_partial(self) -> bool: ...
    def is_authenticated(self) -> bool: ...
    @property
    def guild(self) -> Optional[Guild]: ...
    @property
    def channel(self) -> Optional[TextChannel]: ...
    @property
    def created_at(self) -> datetime.datetime: ...
    @property
    def avatar(self) -> Asset: ...

class Webhook(BaseWebhook):
    session: aiohttp.ClientSession
    @property
    def url(self) -> str: ...
    @classmethod
    def partial(cls, id: int, token: str, session: aiohttp.ClientSession, *, bot_token: Optional[str] = ...) -> Webhook: ...
    @classmethod
    def from_url(cls, url: str, session: aiohttp.ClientSession, *, bot_token: Optional[str] = ...) -> Webhook: ...
    async def fetch(self, *, prefer_auth: bool = ...) -> Webhook: ...
    async def delete(self, *, reason: Optional[str] = ..., prefer_auth: bool = ...) -> None: ...
    async def edit(self, *, reason: Optional[str] = ..., name: Optional[str] = ..., avatar: Optional[bytes] = ..., channel: Optional[Snowflake] = ..., prefer_auth: bool = ...) -> Webhook: ...
    @overload
    async def send(self, content: str = ..., *, username: str = ..., avatar_url: Any = ..., tts: bool = ..., ephemeral: bool = ..., file: File = ..., files: List[File] = ..., embed: Embed = ..., embeds: List[Embed] = ..., allowed_mentions: AllowedMentions = ..., view: View = ..., thread: Snowflake = ..., wait: Literal[True]) -> WebhookMessage: ...
    @overload
    async def send(self, content: str = ..., *, username: str = ..., avatar_url: Any = ..., tts: bool = ..., ephemeral: bool = ..., file: File = ..., files: List[File] = ..., embed: Embed = ..., embeds: List[Embed] = ..., allowed_mentions: AllowedMentions = ..., view: View = ..., thread: Snowflake = ..., wait: Literal[False] = ...) -> None: ...
    async def fetch_message(self, id: int) -> WebhookMessage: ...
    async def edit_message(self, message_id: int, *, content: Optional[str] = ..., embeds: List[Embed] = ..., embed: Optional[Embed] = ..., file: File = ..., files: List[File] = ..., view: Optional[View] = ..., allowed_mentions: Optional[AllowedMentions] = ...) -> WebhookMessage: ...
    async def delete_message(self, message_id: int) -> None: ...
