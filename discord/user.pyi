import discord.abc
from .asset import Asset
from .channel import DMChannel
from .colour import Colour
from .flags import PublicUserFlags
from .guild import Guild
from .message import Message
from .state import ConnectionState
from .types.user import PartialUser as PartialUserPayload, User as UserPayload
from datetime import datetime
from typing import List, Optional, Union

class _UserTag:
    id: int

class BaseUser(_UserTag):
    name: str
    id: int
    discriminator: str
    bot: bool
    system: bool
    def __init__(self, *, state: ConnectionState, data: Union[UserPayload, PartialUserPayload]) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    @property
    def public_flags(self) -> PublicUserFlags: ...
    @property
    def avatar(self) -> Optional[Asset]: ...
    @property
    def default_avatar(self) -> Asset: ...
    @property
    def display_avatar(self) -> Asset: ...
    @property
    def banner(self) -> Optional[Asset]: ...
    @property
    def accent_colour(self) -> Optional[Colour]: ...
    @property
    def accent_color(self) -> Optional[Colour]: ...
    @property
    def colour(self) -> Colour: ...
    @property
    def color(self) -> Colour: ...
    @property
    def mention(self) -> str: ...
    @property
    def created_at(self) -> datetime: ...
    @property
    def display_name(self) -> str: ...
    def mentioned_in(self, message: Message) -> bool: ...

class ClientUser(BaseUser):
    locale: Optional[str]
    verified: bool
    mfa_enabled: bool
    def __init__(self, *, state: ConnectionState, data: UserPayload) -> None: ...
    async def edit(self, *, username: str = ..., avatar: Optional[bytes] = ...) -> ClientUser: ...

class User(BaseUser, discord.abc.Messageable):
    @property
    def dm_channel(self) -> Optional[DMChannel]: ...
    @property
    def mutual_guilds(self) -> List[Guild]: ...
    async def create_dm(self) -> DMChannel: ...
