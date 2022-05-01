from .abc import Snowflake
from .types.message import AllowedMentions as AllowedMentionsPayload
from typing import List, Type, TypeVar, Union

AM = TypeVar('AM', bound='AllowedMentions')

class AllowedMentions:
    everyone: bool
    users: Union[bool, List[Snowflake]]
    roles: Union[bool, List[Snowflake]]
    replied_user: bool
    def __init__(self, *, everyone: bool = ..., users: Union[bool, List[Snowflake]] = ..., roles: Union[bool, List[Snowflake]] = ..., replied_user: bool = ...) -> None: ...
    @classmethod
    def all(cls: Type[AM]) -> AM: ...
    @classmethod
    def none(cls: Type[AM]) -> AM: ...
    def to_dict(self) -> AllowedMentionsPayload: ...
    def merge(self, other: AllowedMentions) -> AllowedMentions: ...
