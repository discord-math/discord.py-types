from .snowflake import Snowflake
from typing import List, Optional, TypedDict

class WelcomeScreen(TypedDict):
    description: str
    welcome_channels: List[WelcomeScreenChannel]

class WelcomeScreenChannel(TypedDict):
    channel_id: Snowflake
    description: str
    emoji_id: Optional[Snowflake]
    emoji_name: Optional[str]
