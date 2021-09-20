from .asset import Asset
from .guild import Guild
from .user import User
from .types.team import Team as TeamPayload
from typing import Any, List, Optional

class AppInfo:
    id: int
    name: str
    description: str
    rpc_origins: List[str]
    bot_public: bool
    bot_require_code_grant: bool
    owner: User
    team: Optional[TeamPayload]
    summary: str
    verify_key: str
    guild_id: Optional[int]
    primary_sku_id: Optional[int]
    slug: Optional[str]
    terms_of_service_url: Optional[str]
    privacy_policy_url: Optional[str]
    @property
    def icon(self) -> Optional[Asset]: ...
    @property
    def cover_image(self) -> Optional[Asset]: ...
    @property
    def guild(self) -> Optional[Guild]: ...

class PartialAppInfo:
    id: int
    name: str
    description: str
    rpc_origins: Optional[List[str]]
    summary: str
    verify_key: str
    terms_of_service_url: Optional[str]
    privacy_policy_url: Optional[str]
    @property
    def icon(self) -> Optional[Asset]: ...
