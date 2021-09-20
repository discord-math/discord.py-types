from .channel import StageChannel
from .enums import StagePrivacyLevel
from .guild import Guild
from .mixins import Hashable
from .state import ConnectionState
from typing import Optional

class StageInstance(Hashable):
    guild: Guild
    @property
    def channel(self) -> Optional[StageChannel]: ...
    def is_public(self) -> bool: ...
    async def edit(self, *, topic: str = ..., privacy_level: StagePrivacyLevel = ..., reason: Optional[str] = ...) -> None: ...
    async def delete(self, *, reason: Optional[str] = ...) -> None: ...
