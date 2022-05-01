from .errors import *
import discord
import inspect
from .context import Context
from typing import Any, Generic, List, Optional, Tuple, TypeVar, Union

T = TypeVar('T')
T_co = TypeVar('T_co', covariant=True)
CT = TypeVar('CT', bound=discord.abc.GuildChannel)
TT = TypeVar('TT', bound=discord.Thread)

class Converter(Generic[T_co]):
    async def convert(self, ctx: Context, argument: str) -> T_co: ...

class IDConverter(Converter[T_co]): ...

class ObjectConverter(IDConverter[discord.Object]):
    async def convert(self, ctx: Context, argument: str) -> discord.Object: ...

class MemberConverter(IDConverter[discord.Member]):
    async def convert(self, ctx: Context, argument: str) -> discord.Member: ...

class UserConverter(IDConverter[discord.User]):
    async def convert(self, ctx: Context, argument: str) -> discord.User: ...

class PartialMessageConverter(Converter[discord.PartialMessage]):
    async def convert(self, ctx: Context, argument: str) -> discord.PartialMessage: ...

class MessageConverter(IDConverter[discord.Message]):
    async def convert(self, ctx: Context, argument: str) -> discord.Message: ...

class GuildChannelConverter(IDConverter[discord.abc.GuildChannel]):
    async def convert(self, ctx: Context, argument: str) -> discord.abc.GuildChannel: ...

class TextChannelConverter(IDConverter[discord.TextChannel]):
    async def convert(self, ctx: Context, argument: str) -> discord.TextChannel: ...

class VoiceChannelConverter(IDConverter[discord.VoiceChannel]):
    async def convert(self, ctx: Context, argument: str) -> discord.VoiceChannel: ...

class StageChannelConverter(IDConverter[discord.StageChannel]):
    async def convert(self, ctx: Context, argument: str) -> discord.StageChannel: ...

class CategoryChannelConverter(IDConverter[discord.CategoryChannel]):
    async def convert(self, ctx: Context, argument: str) -> discord.CategoryChannel: ...

class ThreadConverter(IDConverter[discord.Thread]):
    async def convert(self, ctx: Context, argument: str) -> discord.Thread: ...

class ColourConverter(Converter[discord.Colour]):
    async def convert(self, ctx: Context, argument: str) -> discord.Colour: ...
ColorConverter = ColourConverter

class RoleConverter(IDConverter[discord.Role]):
    async def convert(self, ctx: Context, argument: str) -> discord.Role: ...

class GameConverter(Converter[discord.Game]):
    async def convert(self, ctx: Context, argument: str) -> discord.Game: ...

class InviteConverter(Converter[discord.Invite]):
    async def convert(self, ctx: Context, argument: str) -> discord.Invite: ...

class GuildConverter(IDConverter[discord.Guild]):
    async def convert(self, ctx: Context, argument: str) -> discord.Guild: ...

class EmojiConverter(IDConverter[discord.Emoji]):
    async def convert(self, ctx: Context, argument: str) -> discord.Emoji: ...

class PartialEmojiConverter(Converter[discord.PartialEmoji]):
    async def convert(self, ctx: Context, argument: str) -> discord.PartialEmoji: ...

class GuildStickerConverter(IDConverter[discord.GuildSticker]):
    async def convert(self, ctx: Context, argument: str) -> discord.GuildSticker: ...

class clean_content(Converter[str]):
    fix_channel_mentions: bool
    use_nicknames: bool
    escape_markdown: bool
    remove_markdown: bool
    def __init__(self, *, fix_channel_mentions: bool = ..., use_nicknames: bool = ..., escape_markdown: bool = ..., remove_markdown: bool = ...) -> None: ...
    async def convert(self, ctx: Context, argument: str) -> str: ...

class Greedy(List[T]):
    converter: Any
    def __init__(self, converter: T) -> None: ...
    def __class_getitem__(cls, params: Union[Tuple[T], T]) -> Greedy[T]: ... # type: ignore

async def run_converters(ctx: Context, converter: Any, argument: str, param: inspect.Parameter) -> Any: ...
