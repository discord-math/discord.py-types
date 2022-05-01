from .channel import StageChannel
from .enums import PrivacyLevel
from .guild import Guild
from .mixins import Hashable
from .scheduled_event import ScheduledEvent
from .state import ConnectionState
from .types.channel import StageInstance as StageInstancePayload
from typing import Optional

class StageInstance(Hashable):
    id: int
    guild: Guild
    channel_id: int
    topic: str
    privacy_level: PrivacyLevel
    discoverable_disabled: bool
    scheduled_event_id: Optional[int]
    def __init__(self, *, state: ConnectionState, guild: Guild, data: StageInstancePayload) -> None: ...
    def channel(self) -> Optional[StageChannel]: ...
    def scheduled_event(self) -> Optional[ScheduledEvent]: ...
    async def edit(self, *, topic: str = ..., privacy_level: PrivacyLevel = ..., reason: Optional[str] = ...) -> None: ...
    async def delete(self, *, reason: Optional[str] = ...) -> None: ...
