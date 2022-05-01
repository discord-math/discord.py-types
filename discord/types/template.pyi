from .guild import Guild
from .snowflake import Snowflake
from .user import User
from typing import Optional, TypedDict

class CreateTemplate(TypedDict):
    name: str
    icon: Optional[bytes]

class Template(TypedDict):
    code: str
    name: str
    description: Optional[str]
    usage_count: int
    creator_id: Snowflake
    creator: User
    created_at: str
    updated_at: str
    source_guild_id: Snowflake
    serialized_source_guild: Guild
    is_dirty: Optional[bool]
