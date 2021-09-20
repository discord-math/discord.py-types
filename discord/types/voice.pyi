from .member import MemberWithUser as MemberWithUser
from .snowflake import Snowflake as Snowflake
from typing import Any, List, Optional, TypedDict

SupportedModes: Any

class _PartialVoiceStateOptional(TypedDict):
    member: MemberWithUser
    self_stream: bool

class _VoiceState(_PartialVoiceStateOptional):
    user_id: Snowflake
    session_id: str
    deaf: bool
    mute: bool
    self_deaf: bool
    self_mute: bool
    self_video: bool
    suppress: bool

class GuildVoiceState(_VoiceState):
    channel_id: Snowflake

class VoiceState(_VoiceState):
    channel_id: Optional[Snowflake]
    guild_id: Snowflake

class VoiceRegion(TypedDict):
    id: str
    name: str
    vip: bool
    optimal: bool
    deprecated: bool
    custom: bool

class VoiceServerUpdate(TypedDict):
    token: str
    guild_id: Snowflake
    endpoint: Optional[str]

class VoiceIdentify(TypedDict):
    server_id: Snowflake
    user_id: Snowflake
    session_id: str
    token: str

class VoiceReady(TypedDict):
    ssrc: int
    ip: str
    port: int
    modes: List[SupportedModes]
    heartbeat_interval: int