from .snowflake import SnowflakeList
from .user import User
from typing import Optional, TypedDict

class Nickname(TypedDict):
    nick: str

class PartialMember(TypedDict):
    roles: SnowflakeList
    joined_at: str
    deaf: str
    mute: str

class Member(PartialMember, total=False):
    avatar: str
    user: User
    nick: str
    premium_since: Optional[str]
    pending: bool
    permissions: str
    communication_disabled_until: str

class _OptionalMemberWithUser(PartialMember, total=False):
    avatar: str
    nick: str
    premium_since: Optional[str]
    pending: bool
    permissions: str
    communication_disabled_until: str

class MemberWithUser(_OptionalMemberWithUser):
    user: User

class UserWithMember(User, total=False):
    member: _OptionalMemberWithUser
