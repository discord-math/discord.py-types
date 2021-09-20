from datetime import datetime
from .asset import AssetMixin
from .state import ConnectionState
from typing import Any, Dict, Optional, TypeVar, Union

class _EmojiTag:
    id: Optional[int]
PE = TypeVar('PE', bound='PartialEmoji')

class PartialEmoji(_EmojiTag, AssetMixin):
    id: Optional[int]
    animated: bool
    name: str
    def __init__(self, name: str, *, animated: bool = ..., id: Optional[int] = ...) -> None: ...
    @classmethod
    def from_str(cls, value: str) -> PE: ...
    def to_dict(self) -> Dict[str, Any]: ...
    @classmethod
    def with_state(cls, state: ConnectionState, name: str, *, animated: bool = ..., id: Optional[int] = ...) -> PE: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    def is_custom_emoji(self) -> bool: ...
    def is_unicode_emoji(self) -> bool: ...
    @property
    def created_at(self) -> Optional[datetime]: ...
    @property
    def url(self) -> str: ...
    async def read(self) -> bytes: ...
