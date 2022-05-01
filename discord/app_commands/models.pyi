from ..channel import TextChannel
from ..enums import AppCommandOptionType, AppCommandType, ChannelType
from ..guild import Guild, GuildChannel
from ..mixins import Hashable
from ..permissions import Permissions
from ..state import ConnectionState
from ..threads import Thread
from ..types.command import ApplicationCommand as ApplicationCommandPayload, ApplicationCommandOption, ApplicationCommandOptionChoice
from ..types.interactions import PartialChannel, PartialThread
from ..types.threads import ThreadArchiveDuration
from datetime import datetime
from typing import List, Generic, Optional, TypeVar, Union

ChoiceT = TypeVar('ChoiceT', str, int, float, Union[str, int, float])
ApplicationCommandParent = Union['AppCommand', 'AppCommandGroup']

class AppCommand(Hashable):
    id: int
    type: AppCommandType
    application_id: int
    name: str
    description: str
    options: List[Union[Argument, AppCommandGroup]]
    default_member_permissions: Optional[Permissions]
    dm_permissions: bool
    def __init__(self, *, data: ApplicationCommandPayload, state: Optional[ConnectionState] = ...) -> None: ...
    def to_dict(self) -> ApplicationCommandPayload: ...

class Choice(Generic[ChoiceT]):
    name: str
    value: ChoiceT
    def __init__(self, *, name: str, value: ChoiceT) -> None: ...
    def __eq__(self, o: object) -> bool: ...
    def __hash__(self) -> int: ...
    def to_dict(self) -> ApplicationCommandOptionChoice: ...

class AppCommandChannel(Hashable):
    guild_id: int
    id: int
    type: ChannelType
    name: str
    permissions: Permissions
    def __init__(self, *, state: ConnectionState, data: PartialChannel, guild_id: int) -> None: ...
    @property
    def guild(self) -> Optional[Guild]: ...
    def resolve(self) -> Optional[GuildChannel]: ...
    async def fetch(self) -> GuildChannel: ...
    @property
    def mention(self) -> str: ...
    @property
    def created_at(self) -> datetime: ...

class AppCommandThread(Hashable):
    id: int
    type: ChannelType
    name: str
    permissions: ChannelType
    guild_id: int
    parent_id: int
    archived: bool
    archiver_id: Optional[int]
    auto_archive_duration: ThreadArchiveDuration
    archive_timestamp: datetime
    locked: bool
    invitable: bool
    def __init__(self, *, state: ConnectionState, data: PartialThread, guild_id: int) -> None: ...
    @property
    def guild(self) -> Optional[Guild]: ...
    @property
    def parent(self) -> Optional[TextChannel]: ...
    @property
    def mention(self) -> str: ...
    @property
    def created_at(self) -> Optional[datetime]: ...
    def resolve(self) -> Optional[Thread]: ...
    async def fetch(self) -> Thread: ...

class Argument:
    type: AppCommandOptionType
    name: str
    description: str
    required: bool
    choices: List[Choice[Union[int, float, str]]]
    parent: ApplicationCommandParent
    def __init__(self, *, parent: ApplicationCommandParent, data: ApplicationCommandOption, state: Optional[ConnectionState] = ...) -> None: ...
    def to_dict(self) -> ApplicationCommandOption: ...

class AppCommandGroup:
    type: AppCommandOptionType
    name: str
    description: str
    required: bool
    choices: List[Choice[Union[int, float, str]]]
    arguments: List[Argument]
    parent: ApplicationCommandParent
    def __init__(self, *, parent: ApplicationCommandParent, data: ApplicationCommandOption, state: Optional[ConnectionState] = ...) -> None: ...
    def to_dict(self) -> ApplicationCommandOption: ...
