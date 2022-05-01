from ..components import SelectMenu, SelectOption
from ..emoji import Emoji
from ..enums import ComponentType
from ..partial_emoji import PartialEmoji
from ..types.components import SelectMenu as SelectMenuPayload
from .item import Item, ItemCallbackType
from .view import View
from typing import Any, Callable, List, Literal, Optional, Tuple, Type, TypeVar, Union

V = TypeVar('V', bound='View', covariant=True)
S = TypeVar('S', bound='Select[Any]')

class Select(Item[V]):
    __item_repr_attributes__: Tuple[str, ...]
    row: Optional[int]
    def __init__(self, *, custom_id: str = ..., placeholder: Optional[str] = ..., min_values: int = ..., max_values: int = ..., options: List[SelectOption] = ..., disabled: bool = ..., row: Optional[int] = ...) -> None: ...
    @property
    def custom_id(self) -> str: ...
    @custom_id.setter
    def custom_id(self, value: str) -> None: ...
    @property
    def placeholder(self) -> Optional[str]: ...
    @placeholder.setter
    def placeholder(self, value: Optional[str]) -> None: ...
    @property
    def min_values(self) -> int: ...
    @min_values.setter
    def min_values(self, value: int) -> None: ...
    @property
    def max_values(self) -> int: ...
    @max_values.setter
    def max_values(self, value: int) -> None: ...
    @property
    def options(self) -> List[SelectOption]: ...
    @options.setter
    def options(self, value: List[SelectOption]) -> None: ...
    def add_option(self, *, label: str, value: str = ..., description: Optional[str] = ..., emoji: Optional[Union[str, Emoji, PartialEmoji]] = ..., default: bool = ...) -> None: ...
    def append_option(self, option: SelectOption) -> None: ...
    @property
    def disabled(self) -> bool: ...
    @disabled.setter
    def disabled(self, value: bool) -> None: ...
    @property
    def values(self) -> List[str]: ...
    @property
    def width(self) -> int: ...
    def to_component_dict(self) -> SelectMenuPayload: ... # type: ignore
    @classmethod
    def from_component(cls: Type[S], component: SelectMenu) -> S: ... # type: ignore
    @property
    def type(self) -> Literal[ComponentType.select]: ...
    def is_dispatchable(self) -> bool: ...

def select(*, placeholder: Optional[str] = ..., custom_id: str = ..., min_values: int = ..., max_values: int = ..., options: List[SelectOption] = ..., disabled: bool = ..., row: Optional[int] = ...) -> Callable[[ItemCallbackType[V, Select[V]]], Select[V]]: ...
