from ..enums import AppCommandOptionType, AppCommandType
from ..errors import DiscordException
from ..types.snowflake import Snowflake, SnowflakeList
from .checks import Cooldown
from .commands import Command, ContextMenu, Group
from .transformers import Transformer
from typing import Any, List, Optional, Type, Union

class AppCommandError(DiscordException): ...

class CommandInvokeError(AppCommandError):
    original: Exception
    command: Union[Command[Any, ..., Any], ContextMenu]
    def __init__(self, command: Union[Command[Any, ..., Any], ContextMenu], e: Exception) -> None: ...

class TransformerError(AppCommandError):
    value: Any
    type: AppCommandOptionType
    transformer: Type[Transformer]
    def __init__(self, value: Any, opt_type: AppCommandOptionType, transformer: Type[Transformer]) -> None: ...

class CheckFailure(AppCommandError): ...

class NoPrivateMessage(CheckFailure):
    def __init__(self, message: Optional[str] = ...) -> None: ...

class MissingRole(CheckFailure):
    missing_role: Snowflake
    def __init__(self, missing_role: Snowflake) -> None: ...

class MissingAnyRole(CheckFailure):
    missing_roles: SnowflakeList
    def __init__(self, missing_roles: SnowflakeList) -> None: ...

class MissingPermissions(CheckFailure):
    missing_permissions: List[str]
    def __init__(self, missing_permissions: List[str], *args: Any) -> None: ...

class BotMissingPermissions(CheckFailure):
    missing_permissions: List[str]
    def __init__(self, missing_permissions: List[str], *args: Any) -> None: ...

class CommandOnCooldown(CheckFailure):
    cooldown: Cooldown
    retry_after: float
    def __init__(self, cooldown: Cooldown, retry_after: float) -> None: ...

class CommandAlreadyRegistered(AppCommandError):
    name: str
    guild_id: Optional[int]
    def __init__(self, name: str, guild_id: Optional[int]) -> None: ...

class CommandNotFound(AppCommandError):
    name: str
    parents: List[str]
    type: AppCommandType
    def __init__(self, name: str, parents: List[str], type: AppCommandType = ...) -> None: ...

class CommandLimitReached(AppCommandError):
    guild_id: Optional[int]
    limit: int
    type: AppCommandType
    def __init__(self, guild_id: Optional[int], limit: int, type: AppCommandType = ...) -> None: ...

class CommandSignatureMismatch(AppCommandError):
    command: Union[Command[Any, ..., Any], ContextMenu, Group]
    def __init__(self, command: Union[Command[Any, ..., Any], ContextMenu, Group]) -> None: ...
