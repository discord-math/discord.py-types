from .asset import Asset
from .flags import ApplicationFlags
from .guild import Guild
from .state import ConnectionState
from .team import Team
from .types.appinfo import AppInfo as AppInfoPayload, PartialAppInfo as PartialAppInfoPayload
from .user import User
from typing import List, Optional

class AppInfo:
    description: str
    id: int
    name: str
    rpc_origins: List[str]
    bot_public: bool
    bot_require_code_grant: bool
    owner: User
    verify_key: str
    team: Optional[Team]
    guild_id: Optional[int]
    primary_sku_id: Optional[int]
    slug: Optional[str]
    terms_of_service_url: Optional[str]
    privacy_policy_url: Optional[str]
    def __init__(self, state: ConnectionState, data: AppInfoPayload) -> None: ...
    @property
    def icon(self) -> Optional[Asset]: ...
    @property
    def cover_image(self) -> Optional[Asset]: ...
    @property
    def guild(self) -> Optional[Guild]: ...
    @property
    def flags(self) -> ApplicationFlags: ...

class PartialAppInfo:
    id: int
    name: str
    description: str
    rpc_origins: Optional[List[str]]
    verify_key: str
    terms_of_service_url: Optional[str]
    privacy_policy_url: Optional[str]
    def __init__(self, *, state: ConnectionState, data: PartialAppInfoPayload) -> None: ...
    @property
    def icon(self) -> Optional[Asset]: ...
    @property
    def flags(self) -> ApplicationFlags: ...
