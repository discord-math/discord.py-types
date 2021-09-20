from .abc import Snowflake
from typing import List, TypeVar, Union

A = TypeVar('A', bound='AllowedMentions')

class AllowedMentions:
    everyone: bool
    users: Union[bool, List[Snowflake]]
    roles: Union[bool, List[Snowflake]]
    replied_user: bool
    def __init__(self, *, everyone: bool = ..., users: Union[bool, List[Snowflake]] = ..., roles: Union[bool, List[Snowflake]] = ..., replied_user: bool = ...) -> None: ...
    @classmethod
    def all(cls) -> A: ...
    @classmethod
    def none(cls) -> A: ...
    def merge(self, other: AllowedMentions) -> AllowedMentions: ...
