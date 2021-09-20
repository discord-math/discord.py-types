from ..components import Button as ButtonComponent
from ..emoji import Emoji
from ..enums import ButtonStyle, ComponentType
from ..partial_emoji import PartialEmoji
from .item import Item, ItemCallbackType
from .view import View
from typing import Any, Callable, Optional, Tuple, TypeVar, Union

V = TypeVar('V', bound='View', covariant=True)

class Button(Item[V]):
    __item_repr_attributes__: Tuple[str, ...]
    row: Optional[int]
    def __init__(self, *, style: ButtonStyle = ..., label: Optional[str] = ..., disabled: bool = ..., custom_id: Optional[str] = ..., url: Optional[str] = ..., emoji: Optional[Union[str, Emoji, PartialEmoji]] = ..., row: Optional[int] = ...) -> None: ...
    @property
    def style(self) -> ButtonStyle: ...
    @style.setter
    def style(self, value: ButtonStyle) -> None: ...
    @property
    def custom_id(self) -> Optional[str]: ...
    @custom_id.setter
    def custom_id(self, value: Optional[str]) -> None: ...
    @property
    def url(self) -> Optional[str]: ...
    @url.setter
    def url(self, value: Optional[str]) -> None: ...
    @property
    def disabled(self) -> bool: ...
    @disabled.setter
    def disabled(self, value: bool) -> None: ...
    @property
    def label(self) -> Optional[str]: ...
    @label.setter
    def label(self, value: Optional[str]) -> None: ...
    @property
    def emoji(self) -> Optional[PartialEmoji]: ...
    @emoji.setter
    def emoji(self, value: Optional[Union[str, Emoji, PartialEmoji]]) -> None: ...
    @property
    def type(self) -> ComponentType: ...
    def is_dispatchable(self) -> bool: ...
    def is_persistent(self) -> bool: ...

def button(*, label: Optional[str] = ..., custom_id: Optional[str] = ..., disabled: bool = ..., style: ButtonStyle = ..., emoji: Optional[Union[str, Emoji, PartialEmoji]] = ..., row: Optional[int] = ...) -> Callable[[ItemCallbackType[Button[V]]], ItemCallbackType[Button[V]]]: ...
