from .emoji import Emoji
from .enums import ComponentType, ButtonStyle
from .partial_emoji import PartialEmoji
from typing import Any, ClassVar, Dict, List, Optional, Tuple, TypeVar, Union

C = TypeVar('C', bound='Component')

class Component:
    __repr_info__: ClassVar[Tuple[str, ...]]
    type: ComponentType
    def to_dict(self) -> Dict[str, Any]: ...

class ActionRow(Component):
    __repr_info__: ClassVar[Tuple[str, ...]]
    type: ComponentType
    children: List[Component]

class Button(Component):
    __repr_info__: ClassVar[Tuple[str, ...]]
    type: ComponentType
    style: ButtonStyle
    custom_id: Optional[str]
    url: Optional[str]
    disabled: bool
    label: Optional[str]
    emoji: Optional[PartialEmoji]

class SelectMenu(Component):
    __repr_info__: ClassVar[Tuple[str, ...]]
    type: ComponentType
    custom_id: str
    placeholder: Optional[str]
    min_values: int
    max_values: int
    options: List[SelectOption]
    disabled: bool

class SelectOption:
    label: str
    value: str
    description: Optional[str]
    emoji: Optional[Union[str, Emoji, PartialEmoji]]
    default: bool
    def __init__(self, label: str, *, value: str = ..., description: Optional[str] = ..., emoji: Optional[Union[str, Emoji, PartialEmoji]] = ..., default: bool = ...) -> None: ...
