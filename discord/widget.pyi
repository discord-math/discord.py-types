import datetime
from .activity import BaseActivity, Spotify
from .enums import Status
from .invite import Invite
from .user import BaseUser
from typing import Any, List, Optional, Union

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
    activity: Optional[Union[BaseActivity, Spotify]]
    nick: int
    status: Status
    deafened: Optional[bool]
    muted: Optional[bool]
    suppress: Optional[bool]
    connected_channel: Optional[WidgetChannel]
    @property
    def display_name(self) -> str: ...

class Widget:
    name: str
    id: int
    channels: List[WidgetChannel]
    members: List[WidgetMember]
    def __eq__(self, other: Any) -> bool: ...
    @property
    def created_at(self) -> datetime.datetime: ...
    @property
    def json_url(self) -> str: ...
    @property
    def invite_url(self) -> str: ...
    async def fetch_invite(self, *, with_counts: bool = ...) -> Invite: ...
