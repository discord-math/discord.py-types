from .emoji import Emoji
from .enums import ButtonStyle, ComponentType, TextStyle
from .partial_emoji import PartialEmoji
from .types.components import ActionRow as ActionRowPayload, ButtonComponent as ButtonComponentPayload, Component as ComponentPayload, SelectMenu as SelectMenuPayload, SelectOption as SelectOptionPayload, TextInput as TextInputPayload
from typing import Any, ClassVar, Dict, List, Literal, Optional, Tuple, Union

class Component:
    __repr_info__: ClassVar[Tuple[str, ...]]
    type: ComponentType
    def to_dict(self) -> ComponentPayload: ...

class ActionRow(Component):
    __repr_info__: ClassVar[Tuple[str, ...]]
    type: Literal[ComponentType.action_row]
    children: List[Component]
    def __init__(self, data: ComponentPayload) -> None: ...
    def to_dict(self) -> ActionRowPayload: ...

class Button(Component):
    __repr_info__: ClassVar[Tuple[str, ...]]
    type: Literal[ComponentType.button]
    style: ButtonStyle
    custom_id: Optional[str]
    url: Optional[str]
    disabled: bool
    label: Optional[str]
    emoji: Optional[PartialEmoji]
    def __init__(self, data: ButtonComponentPayload) -> None: ...
    def to_dict(self) -> ButtonComponentPayload: ...

class SelectMenu(Component):
    __repr_info__: ClassVar[Tuple[str, ...]]
    type: Literal[ComponentType.select]
    custom_id: str
    placeholder: Optional[str]
    min_values: int
    max_values: int
    options: List[SelectOption]
    disabled: bool
    def __init__(self, data: SelectMenuPayload) -> None: ...
    def to_dict(self) -> SelectMenuPayload: ...

class SelectOption:
    label: str
    value: str
    description: Optional[str]
    emoji: Optional[Union[str, Emoji, PartialEmoji]]
    default: bool
    def __init__(self, *, label: str, value: str = ..., description: Optional[str] = ..., emoji: Optional[Union[str, Emoji, PartialEmoji]] = ..., default: bool = ...) -> None: ...
    @classmethod
    def from_dict(cls, data: SelectOptionPayload) -> SelectOption: ...
    def to_dict(self) -> SelectOptionPayload: ...

class TextInput(Component):
    __repr_info__: ClassVar[Tuple[str, ...]]
    type: Literal[ComponentType.text_input]
    style: TextStyle
    label: str
    custom_id: str
    placeholder: Optional[str]
    value: Optional[str]
    required: bool
    min_length: Optional[int]
    max_length: Optional[int]
    def __init__(self, data: TextInputPayload) -> None: ...
    def to_dict(self) -> TextInputPayload: ...
    @property
    def default(self) -> Optional[str]: ...
