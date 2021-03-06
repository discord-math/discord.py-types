from ._types import BotT
from .context import Context
from typing import Any, Dict, Iterator, List, Pattern, Tuple, Type, TypeVar

class Flag:
    name: str
    aliases: List[str]
    attribute: str
    annotation: Any
    default: Any
    max_args: int
    override: bool
    cast_to_dict: bool
    @property
    def required(self) -> bool: ...

def flag(*, name: str = ..., aliases: List[str] = ..., default: Any = ..., max_args: int = ..., override: bool = ..., converter: Any = ...) -> Any: ...

FM = TypeVar('FM', bound='FlagsMeta')

class FlagsMeta(type):
    __commands_is_flag__: bool
    __commands_flags__: Dict[str, Flag]
    __commands_flag_aliases__: Dict[str, str]
    __commands_flag_regex__: Pattern[str]
    __commands_flag_case_insensitive__: bool
    __commands_flag_delimiter__: str
    __commands_flag_prefix__: str
    def __new__(cls: Type[FM], name: str, bases: Tuple[type, ...], attrs: Dict[str, Any], *, case_insensitive: bool = ..., delimiter: str = ..., prefix: str = ...) -> FM: ...

FC = TypeVar('FC', bound='FlagConverter')

class FlagConverter(metaclass=FlagsMeta):
    @classmethod
    def get_flags(cls) -> Dict[str, Flag]: ...
    def __iter__(self) -> Iterator[Tuple[str, Any]]: ...
    @classmethod
    def parse_flags(cls, argument: str) -> Dict[str, List[str]]: ...
    @classmethod
    async def convert(cls: Type[FC], ctx: Context[BotT], argument: str) -> FC: ...
