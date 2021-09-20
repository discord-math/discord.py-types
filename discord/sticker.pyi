import datetime
from .asset import Asset, AssetMixin
from .enums import StickerFormatType
from .guild import Guild
from .mixins import Hashable
from typing import Optional, Union

class StickerPack(Hashable):
    @property
    def banner(self) -> Asset: ...

class _StickerTag(Hashable, AssetMixin):
    id: int
    format: StickerFormatType
    async def read(self) -> bytes: ...

class StickerItem(_StickerTag):
    name: str
    id: int
    format: StickerFormatType
    url: str
    async def fetch(self) -> Union[Sticker, StandardSticker, GuildSticker]: ...

class Sticker(_StickerTag):
    @property
    def created_at(self) -> datetime.datetime: ...

class StandardSticker(Sticker):
    async def pack(self) -> StickerPack: ...

class GuildSticker(Sticker):
    @property
    def guild(self) -> Optional[Guild]: ...
    async def edit(self, *, name: str = ..., description: str = ..., emoji: str = ..., reason: Optional[str] = ...) -> GuildSticker: ...
    async def delete(self, *, reason: Optional[str] = ...) -> None: ...
