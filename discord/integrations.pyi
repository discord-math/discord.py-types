import datetime
from .enums import ExpireBehaviour
from .guild import Guild
from .role import Role
from .state import ConnectionState
from .types.integration import Integration as IntegrationPayload, IntegrationAccount as IntegrationAccountPayload, IntegrationApplication as IntegrationApplicationPayload, IntegrationType
from .user import User
from typing import Optional

class IntegrationAccount:
    id: str
    name: str
    def __init__(self, data: IntegrationAccountPayload) -> None: ...

class Integration:
    guild: Guild
    id : int
    type: IntegrationType
    name: str
    account: IntegrationAccount
    user: Optional[User]
    enabled: bool
    def __init__(self, *, data: IntegrationPayload, guild: Guild) -> None: ...
    async def delete(self, *, reason: Optional[str] = ...) -> None: ...

class StreamIntegration(Integration):
    revoked: bool
    expire_behaviour: ExpireBehaviour
    expire_grace_period: int
    synced_at: datetime.datetime
    syncing: bool
    enable_emoticons: bool
    subscriber_count: int
    @property
    def expire_behavior(self) -> ExpireBehaviour: ...
    @property
    def role(self) -> Optional[Role]: ...
    async def edit(self, *, expire_behaviour: ExpireBehaviour = ..., expire_grace_period: int = ..., enable_emoticons: bool = ...) -> None: ...
    async def sync(self) -> None: ...

class IntegrationApplication:
    id: int
    name: str
    icon: Optional[str]
    description: str
    summary: str
    user: Optional[User]
    def __init__(self, *, data: IntegrationApplicationPayload, state: ConnectionState) -> None: ...

class BotIntegration(Integration):
    application: IntegrationApplication
