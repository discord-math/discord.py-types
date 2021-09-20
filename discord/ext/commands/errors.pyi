from .context import Context
from .converter import Converter as Converter
from .cooldowns import BucketType, Cooldown
from .flags import Flag
from discord.abc import GuildChannel
from discord.errors import ClientException, DiscordException
from discord.threads import Thread
from discord.types.snowflake import Snowflake, SnowflakeList
from inspect import Parameter
from typing import Any, Callable, List, Optional, Tuple, Type, Union

class CommandError(DiscordException):
    def __init__(self, message: Optional[str] = ..., *args: Any) -> None: ...

class ConversionError(CommandError):
    converter: Converter[Any]
    original: Exception
    def __init__(self, converter: Converter[Any], original: Exception) -> None: ...

class UserInputError(CommandError): ...
class CommandNotFound(CommandError): ...

class MissingRequiredArgument(UserInputError):
    param: Parameter
    def __init__(self, param: Parameter) -> None: ...

class TooManyArguments(UserInputError): ...
class BadArgument(UserInputError): ...
class CheckFailure(CommandError): ...

class CheckAnyFailure(CheckFailure):
    checks: List[CheckFailure]
    errors: List[Callable[[Context], bool]]
    def __init__(self, checks: List[CheckFailure], errors: List[Callable[[Context], bool]]) -> None: ...

class PrivateMessageOnly(CheckFailure):
    def __init__(self, message: Optional[str] = ...) -> None: ...

class NoPrivateMessage(CheckFailure):
    def __init__(self, message: Optional[str] = ...) -> None: ...

class NotOwner(CheckFailure): ...

class ObjectNotFound(BadArgument):
    argument: str
    def __init__(self, argument: str) -> None: ...

class MemberNotFound(BadArgument):
    argument: str
    def __init__(self, argument: str) -> None: ...

class GuildNotFound(BadArgument):
    argument: str
    def __init__(self, argument: str) -> None: ...

class UserNotFound(BadArgument):
    argument: str
    def __init__(self, argument: str) -> None: ...

class MessageNotFound(BadArgument):
    argument: str
    def __init__(self, argument: str) -> None: ...

class ChannelNotReadable(BadArgument):
    argument: str
    def __init__(self, argument: Union[GuildChannel, Thread]) -> None: ...

class ChannelNotFound(BadArgument):
    argument: str
    def __init__(self, argument: str) -> None: ...

class ThreadNotFound(BadArgument):
    argument: str
    def __init__(self, argument: str) -> None: ...

class BadColourArgument(BadArgument):
    argument: str
    def __init__(self, argument: str) -> None: ...
BadColorArgument = BadColourArgument

class RoleNotFound(BadArgument):
    argument: str
    def __init__(self, argument: str) -> None: ...

class BadInviteArgument(BadArgument):
    argument: str
    def __init__(self, argument: str) -> None: ...

class EmojiNotFound(BadArgument):
    argument: str
    def __init__(self, argument: str) -> None: ...

class PartialEmojiConversionFailure(BadArgument):
    argument: str
    def __init__(self, argument: str) -> None: ...

class GuildStickerNotFound(BadArgument):
    argument: str
    def __init__(self, argument: str) -> None: ...

class BadBoolArgument(BadArgument):
    argument: str
    def __init__(self, argument: str) -> None: ...

class DisabledCommand(CommandError): ...

class CommandInvokeError(CommandError):
    original: Exception
    def __init__(self, e: Exception) -> None: ...

class CommandOnCooldown(CommandError):
    cooldown: Cooldown
    retry_after: float
    type: BucketType
    def __init__(self, cooldown: Cooldown, retry_after: float, type: BucketType) -> None: ...

class MaxConcurrencyReached(CommandError):
    number: int
    per: BucketType
    def __init__(self, number: int, per: BucketType) -> None: ...

class MissingRole(CheckFailure):
    missing_role: Snowflake
    def __init__(self, missing_role: Snowflake) -> None: ...

class BotMissingRole(CheckFailure):
    missing_role: Snowflake
    def __init__(self, missing_role: Snowflake) -> None: ...

class MissingAnyRole(CheckFailure):
    missing_roles: SnowflakeList
    def __init__(self, missing_roles: SnowflakeList) -> None: ...

class BotMissingAnyRole(CheckFailure):
    missing_roles: SnowflakeList
    def __init__(self, missing_roles: SnowflakeList) -> None: ...

class NSFWChannelRequired(CheckFailure):
    channel: Union[GuildChannel, Thread]
    def __init__(self, channel: Union[GuildChannel, Thread]) -> None: ...

class MissingPermissions(CheckFailure):
    missing_permissions: Any
    def __init__(self, missing_permissions: List[str], *args: Any) -> None: ...

class BotMissingPermissions(CheckFailure):
    missing_permissions: Any
    def __init__(self, missing_permissions: List[str], *args: Any) -> None: ...

class BadUnionArgument(UserInputError):
    param: Parameter
    converters: Tuple[Type[Any], ...]
    errors: List[CommandError]
    def __init__(self, param: Parameter, converters: Tuple[Type[Any], ...], errors: List[CommandError]): ...

class BadLiteralArgument(UserInputError):
    param: Parameter
    literals: Tuple[Any, ...]
    errors: List[CommandError]
    def __init__(self, param: Parameter, literals: Tuple[Any, ...], errors: List[CommandError]) -> None: ...

class ArgumentParsingError(UserInputError): ...

class UnexpectedQuoteError(ArgumentParsingError):
    quote: str
    def __init__(self, quote: str) -> None: ...

class InvalidEndOfQuotedStringError(ArgumentParsingError):
    char: str
    def __init__(self, char: str) -> None: ...

class ExpectedClosingQuoteError(ArgumentParsingError):
    close_quote: str
    def __init__(self, close_quote: str) -> None: ...

class ExtensionError(DiscordException):
    name: str
    def __init__(self, message: Optional[str] = ..., *args: Any, name: str) -> None: ...

class ExtensionAlreadyLoaded(ExtensionError):
    def __init__(self, name: str) -> None: ...

class ExtensionNotLoaded(ExtensionError):
    def __init__(self, name: str) -> None: ...

class NoEntryPointError(ExtensionError):
    def __init__(self, name: str) -> None: ...

class ExtensionFailed(ExtensionError):
    original: Exception
    def __init__(self, name: str, original: Exception) -> None: ...

class ExtensionNotFound(ExtensionError):
    def __init__(self, name: str) -> None: ...

class CommandRegistrationError(ClientException):
    name: str
    alias_conflict: bool
    def __init__(self, name: str, *, alias_conflict: bool = ...) -> None: ...

class FlagError(BadArgument): ...

class TooManyFlags(FlagError):
    flag: Flag
    values: List[str]
    def __init__(self, flag: Flag, values: List[str]) -> None: ...

class BadFlagArgument(FlagError):
    flag: Flag
    def __init__(self, flag: Flag) -> None: ...

class MissingRequiredFlag(FlagError):
    flag: Flag
    def __init__(self, flag: Flag) -> None: ...

class MissingFlagArgument(FlagError):
    flag: Flag
    def __init__(self, flag: Flag) -> None: ...
