from .appinfo import PartialAppInfo
from .channel import PartialChannel
from .guild import InviteGuild as InviteGuild, _GuildPreviewUnique
from .scheduled_event import GuildScheduledEvent
from .snowflake import Snowflake
from .user import PartialUser
from typing import Literal, Optional, TypedDict, Union
from typing_extensions import NotRequired

InviteTargetType = Literal[1, 2]

class _InviteMetadata(TypedDict, total=False):
    uses: int
    max_uses: int
    max_age: int
    temporary: bool
    created_at: str
    expires_at: Optional[str]

class VanityInvite(_InviteMetadata):
    code: Optional[str]
    revoked: NotRequired[bool]

class IncompleteInvite(_InviteMetadata):
    code: str
    channel: PartialChannel

class Invite(IncompleteInvite, total=False):
    guild: InviteGuild
    inviter: PartialUser
    target_user: PartialUser
    target_type: InviteTargetType
    target_application: PartialAppInfo
    guild_scheduled_event: GuildScheduledEvent

class InviteWithCounts(Invite, _GuildPreviewUnique): ...

class GatewayInviteCreate(TypedDict):
    channel_id: Snowflake
    code: str
    created_at: str
    max_age: int
    max_uses: int
    temporary: bool
    uses: bool
    guild_id: Snowflake
    inviter: NotRequired[PartialUser]
    target_type: NotRequired[InviteTargetType]
    target_user: NotRequired[PartialUser]
    target_application: NotRequired[PartialAppInfo]

class GatewayInviteDelete(TypedDict):
    channel_id: Snowflake
    code: str
    guild_id: NotRequired[Snowflake]
GatewayInvite = Union[GatewayInviteCreate, GatewayInviteDelete]
