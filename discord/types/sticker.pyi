from .snowflake import Snowflake
from .user import User
from typing import List, Literal, Optional, TypedDict, Union
from typing_extensions import NotRequired

StickerFormatType = Literal[1, 2, 3]

class StickerItem(TypedDict):
    id: Snowflake
    name: str
    format_type: StickerFormatType

class BaseSticker(TypedDict):
    id: Snowflake
    name: str
    description: str
    tags: str
    format_type: StickerFormatType

class StandardSticker(BaseSticker):
    type: Literal[1]
    sort_value: int
    pack_id: Snowflake

class GuildSticker(BaseSticker):
    type: Literal[2]
    available: bool
    guild_id: Snowflake
    user: NotRequired[User]
Sticker = Union[StandardSticker, GuildSticker]

class StickerPack(TypedDict):
    id: Snowflake
    stickers: List[StandardSticker]
    name: str
    sku_id: Snowflake
    cover_sticker_id: Optional[Snowflake]
    description: str
    banner_asset_id: Optional[Snowflake]

class CreateGuildSticker(TypedDict):
    name: str
    tags: str
    description: NotRequired[str]

class ListPremiumStickerPacks(TypedDict):
    sticker_packs: List[StickerPack]
