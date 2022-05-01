from .snowflake import Snowflake
from typing import Optional, TypedDict
from typing_extensions import NotRequired

class Role(TypedDict):
    id: Snowflake
    name: str
    color: int
    hoist: bool
    position: int
    permissions: str
    managed: bool
    mentionable: bool
    icon: NotRequired[Optional[str]]
    unicode_emoji: NotRequired[Optional[str]]
    tags: NotRequired[RoleTags]

class RoleTags(TypedDict, total=False):
    bot_id: Snowflake
    integration_id: Snowflake
    premium_subscriber: None
