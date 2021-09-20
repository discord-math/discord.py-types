from .snowflake import SnowflakeList as SnowflakeList
from .user import User as User
from typing import TypedDict

class Nickname(TypedDict):
    nick: str

class PartialMember(TypedDict):
    roles: SnowflakeList
    joined_at: str
    deaf: str
    mute: str

class Member(PartialMember):
    avatar: str
    user: User
    nick: str
    premium_since: str
    pending: bool
    permissions: str

class _OptionalMemberWithUser(PartialMember):
    avatar: str
    nick: str
    premium_since: str
    pending: bool
    permissions: str

class MemberWithUser(_OptionalMemberWithUser):
    user: User

class UserWithMember(User):
    member: _OptionalMemberWithUser
