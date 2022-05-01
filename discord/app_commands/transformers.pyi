from ..enums import AppCommandOptionType, ChannelType
from ..interactions import Interaction
from ..member import Member
from .models import Choice
from typing import Any, Callable, ClassVar, Coroutine, Dict, List, Optional, Type, TypeVar, Union
from typing_extensions import Annotated

Range = Annotated
Transform = Annotated
T = TypeVar('T')
FuncT = TypeVar('FuncT', bound=Callable[..., Any])
ChoiceT = TypeVar('ChoiceT', str, int, float, Union[str, int, float])

class CommandParameter:
    name: str
    description: str
    required: bool
    default: Any
    choices: List[Choice[Union[str, int, float]]]
    type: AppCommandOptionType
    channel_types: List[ChannelType]
    min_value: Optional[Union[int, float]]
    max_value: Optional[Union[int, float]]
    autocomplete: Optional[Callable[..., Coroutine[Any, Any, Any]]]
    def to_dict(self) -> Dict[str, Any]: ...
    def is_choice_annotation(self) -> bool: ...
    async def transform(self, interaction: Interaction, value: Any) -> Any: ...
    @property
    def display_name(self) -> str: ...

class Transformer:
    __discord_app_commands_transformer__: ClassVar[bool]
    __discord_app_commands_is_choice__: ClassVar[bool]
    @classmethod
    def type(cls) -> AppCommandOptionType: ...
    @classmethod
    def channel_types(cls) -> List[ChannelType]: ...
    @classmethod
    def min_value(cls) -> Optional[Union[int, float]]: ...
    @classmethod
    def max_value(cls) -> Optional[Union[int, float]]: ...
    @classmethod
    async def transform(cls, interaction: Interaction, value: Any) -> Any: ...
    @classmethod
    async def autocomplete(cls, interaction: Interaction, value: Union[int, float, str]) -> List[Choice[Union[int, float, str]]]: ...

class _TransformMetadata:
    __discord_app_commands_transform__: ClassVar[bool]
    metadata: Type[Transformer]
    def __init__(self, metadata: Type[Transformer]) -> None: ...
    def __call__(self) -> None: ...

class MemberTransformer(Transformer):
    @classmethod
    def type(cls) -> AppCommandOptionType: ...
    @classmethod
    async def transform(cls, interaction: Interaction, value: Any) -> Member: ...
