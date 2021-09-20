import datetime
from .mixins import Hashable
from typing import Any, SupportsInt, Union

SupportsIntCast = Union[SupportsInt, str, bytes, bytearray]

class Object(Hashable):
    id: Any
    def __init__(self, id: SupportsIntCast) -> None: ...
    @property
    def created_at(self) -> datetime.datetime: ...
