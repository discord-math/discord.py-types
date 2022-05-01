import datetime
from .activity import BaseActivity, Spotify
from .enums import Status
from .invite import Invite
from .state import ConnectionState
from .types.widget import Widget as WidgetPayload, WidgetMember as WidgetMemberPayload
from .user import BaseUser
from typing import List, Optional, Union

class WidgetChannel:
    id: int
    name: str
    position: int
    def __init__(self, id: int, name: str, position: int) -> None: ...
    @property
    def mention(self) -> str: ...
    @property
    def created_at(self) -> datetime.datetime: ...

class WidgetMember(BaseUser):
    name: str
    status: Status
    nick: Optional[str]
    avatar: Optional[str] # type: ignore
    discriminator: str
    id: int
    bot: bool
    activity: Optional[Union[BaseActivity, Spotify]]
    deafened: Optional[bool]
    suppress: Optional[bool]
    muted: Optional[bool]
    connected_channel: Optional[WidgetChannel]
    def __init__(self, *, state: ConnectionState, data: WidgetMemberPayload, connected_channel: Optional[WidgetChannel] = ...) -> None: ...
    @property
    def display_name(self) -> str: ...

class Widget:
    name: str
    id: int
    channels: List[WidgetChannel]
    members: List[WidgetMember]
    presence_count: int
    def __init__(self, *, state: ConnectionState, data: WidgetPayload) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    @property
    def created_at(self) -> datetime.datetime: ...
    @property
    def json_url(self) -> str: ...
    @property
    def invite_url(self) -> Optional[str]: ...
    async def fetch_invite(self, *, with_counts: bool = ...) -> Optional[Invite]: ...
