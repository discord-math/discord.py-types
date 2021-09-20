from .snowflake import Snowflake as Snowflake
from typing import Literal, Optional, TypedDict

MessageActivityType = Literal[1, 2, 3, 5]

class MessageActivity(TypedDict):
    type: MessageActivityType
    party_id: str

class _MessageApplicationOptional(TypedDict):
    cover_image: str

class MessageApplication(_MessageApplicationOptional):
    id: Snowflake
    description: str
    icon: Optional[str]
    name: str
