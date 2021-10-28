from datetime import datetime
from .abc import Snowflake
from .asset import AssetMixin
from .guild import Guild
from .partial_emoji import _EmojiTag
from .role import Role
from .user import User
from typing import Any, Iterator, List, Optional, Tuple

class Emoji(_EmojiTag, AssetMixin):
    require_colons: bool
    animated: bool
    managed: bool
    id: int
    name: str
    guild_id: int
    user: Optional[User]
    available: bool
    def __iter__(self) -> Iterator[Tuple[str, Any]]: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    @property
    def created_at(self) -> datetime: ...
    @property
    def url(self) -> str: ...
    @property
    def roles(self) -> List[Role]: ...
    @property
    def guild(self) -> Guild: ...
    def is_usable(self) -> bool: ...
    async def delete(self, *, reason: Optional[str] = ...) -> None: ...
    async def edit(self, *, name: str = ..., roles: List[Snowflake] = ..., reason: Optional[str] = ...) -> Emoji: ...
