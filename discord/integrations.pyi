from .enums import ExpireBehaviour
from .guild import Guild
from .role import Role
from typing import Any, Optional

class IntegrationAccount:
    id: Any
    name: Any

class Integration:
    guild: Any
    async def delete(self, *, reason: Optional[str] = ...) -> None: ...

class StreamIntegration(Integration):
    @property
    def expire_behavior(self) -> ExpireBehaviour: ...
    @property
    def role(self) -> Optional[Role]: ...
    async def edit(self, *, expire_behaviour: ExpireBehaviour = ..., expire_grace_period: int = ..., enable_emoticons: bool = ...) -> None: ...
    synced_at: Any
    async def sync(self) -> None: ...

class IntegrationApplication:
    id: Any
    name: Any
    icon: Any
    description: Any
    summary: Any
    user: Any

class BotIntegration(Integration): ...
