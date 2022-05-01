import inspect
from discord import DMChannel, Guild, Member, TextChannel, Thread, User, VoiceChannel
from .context import Context
from typing import Any, Literal, Optional, OrderedDict, Protocol, Union, TypeVar

ParamKinds = Literal[inspect._ParameterKind.POSITIONAL_ONLY, inspect._ParameterKind.POSITIONAL_OR_KEYWORD, inspect._ParameterKind.VAR_POSITIONAL, inspect._ParameterKind.KEYWORD_ONLY, inspect._ParameterKind.VAR_KEYWORD]
P = TypeVar('P', bound='Parameter')

class Parameter(inspect.Parameter):
    def __init__(self, name: str, kind: ParamKinds, default: Any = ..., annotation: Any = ..., displayed_default: str = ...) -> None: ...
    def replace(self: P, *, name: str = ..., kind: ParamKinds = ..., default: Any = ..., annotation: Any = ..., displayed_default: Any = ...) -> P: ... # type: ignore
    @property
    def required(self) -> bool: ...
    @property
    def converter(self) -> Any: ...
    @property
    def displayed_default(self) -> Optional[str]: ...
    async def get_default(self, ctx: Context[Any]) -> Any: ...

def parameter(*, converter: Any = ..., default: Any = ..., displayed_default: str = ...) -> Any: ...

class ParameterAlias(Protocol):
    def __call__(self, *, converter: Any = ..., default: Any = ..., displayed_default: str = ...) -> Any: ...

param: ParameterAlias
Author = Union[Member, User]
CurrentChannel = Union[TextChannel, DMChannel, Thread, VoiceChannel]
CurrentGuild = Guild

class Signature(inspect.Signature):
    parameters: OrderedDict[str, Parameter] # type: ignore
