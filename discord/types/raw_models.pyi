from .snowflake import Snowflake
from typing import TypedDict

class _MessageEventOptional(TypedDict):
    guild_id: Snowflake

class MessageUpdateEvent(_MessageEventOptional):
    id: Snowflake
    channel_id: Snowflake
