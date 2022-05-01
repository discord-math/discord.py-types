import datetime
from .asset import Asset, AssetMixin
from .enums import StickerFormatType, StickerType
from .guild import Guild
from .mixins import Hashable
from .state import ConnectionState
from .types.sticker import Sticker as StickerPayload, StickerItem as StickerItemPayload, StickerPack as StickerPackPayload
from .user import User
from typing import List, Optional, Union

class StickerPack(Hashable):
    id: int
    stickers: List[StandardSticker]
    name: str
    sku_id: int
    cover_sticker_id: Optional[int]
    cover_sticker: Optional[StandardSticker]
    description: str
    def __init__(self, *, state: ConnectionState, data: StickerPackPayload) -> None: ...
    @property
    def banner(self) -> Optional[Asset]: ...

class _StickerTag(Hashable, AssetMixin):
    id: int
    format: StickerFormatType
    async def read(self) -> bytes: ...

class StickerItem(_StickerTag):
    name: str
    id: int
    format: StickerFormatType
    url: str
    def __init__(self, *, state: ConnectionState, data: StickerItemPayload) -> None: ...
    async def fetch(self) -> Union[Sticker, StandardSticker, GuildSticker]: ...

class Sticker(_StickerTag):
    id: int
    name: str
    description: str
    format: StickerFormatType
    url: str
    def __init__(self, *, state: ConnectionState, data: StickerPayload) -> None: ...
    @property
    def created_at(self) -> datetime.datetime: ...

class StandardSticker(Sticker):
    sort_value: int
    pack_id: int
    type: StickerType
    tags: List[str]
    async def pack(self) -> StickerPack: ...

class GuildSticker(Sticker):
    available: bool
    guild_id: int
    user: Optional[User]
    emoji: str
    type: StickerType
    def guild(self) -> Optional[Guild]: ...
    async def edit(self, *, name: str = ..., description: str = ..., emoji: str = ..., reason: Optional[str] = ...) -> GuildSticker: ...
    async def delete(self, *, reason: Optional[str] = ...) -> None: ...
