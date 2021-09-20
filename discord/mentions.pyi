from .abc import Snowflake
from typing import List, Type, TypeVar, Union

A = TypeVar('A', bound='AllowedMentions')

class AllowedMentions:
    everyone: bool
    users: Union[bool, List[Snowflake]]
    roles: Union[bool, List[Snowflake]]
    replied_user: bool
    def __init__(self, *, everyone: bool = ..., users: Union[bool, List[Snowflake]] = ..., roles: Union[bool, List[Snowflake]] = ..., replied_user: bool = ...) -> None: ...
    @classmethod
    def all(cls: Type[A]) -> A: ...
    @classmethod
    def none(cls: Type[A]) -> A: ...
    def merge(self, other: AllowedMentions) -> AllowedMentions: ...
