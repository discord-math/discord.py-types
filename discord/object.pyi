import datetime
from .mixins import Hashable
from typing import SupportsInt, Union

SupportsIntCast = Union[SupportsInt, str, bytes, bytearray]

class Object(Hashable):
    id: int
    def __init__(self, id: SupportsIntCast) -> None: ...
    @property
    def created_at(self) -> datetime.datetime: ...
