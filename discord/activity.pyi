import datetime
from .colour import Colour
from .enums import ActivityType
from .partial_emoji import PartialEmoji
from .types.activity import ActivityAssets, ActivityButton, ActivityParty, ActivityTimestamps
from typing import Any, Dict, List, Optional, Union, overload

class BaseActivity:
    @property
    def created_at(self) -> Optional[datetime.datetime]: ...

class Activity(BaseActivity):
    state: Optional[str]
    details: Optional[str]
    timestamps: ActivityTimestamps
    assets: ActivityAssets
    party: ActivityParty
    application_id: Optional[int]
    name: Optional[str]
    url: Optional[str]
    flags: int
    sync_id: Optional[str]
    session_id: Optional[str]
    buttons: List[ActivityButton]
    type: ActivityType
    emoji: Optional[PartialEmoji]
    def __init__(self, **kwargs: Any) -> None: ...
    def to_dict(self) -> Dict[str, Any]: ...
    @property
    def start(self) -> Optional[datetime.datetime]: ...
    @property
    def end(self) -> Optional[datetime.datetime]: ...
    @property
    def large_image_url(self) -> Optional[str]: ...
    @property
    def small_image_url(self) -> Optional[str]: ...
    @property
    def large_image_text(self) -> Optional[str]: ...
    @property
    def small_image_text(self) -> Optional[str]: ...

class Game(BaseActivity):
    name: Any
    def __init__(self, name: str, **extra: Any) -> None: ...
    @property
    def type(self) -> ActivityType: ...
    @property
    def start(self) -> Optional[datetime.datetime]: ...
    @property
    def end(self) -> Optional[datetime.datetime]: ...
    def to_dict(self) -> Dict[str, Any]: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...

class Streaming(BaseActivity):
    platform: Any
    name: Any
    game: Any
    url: Any
    details: Any
    assets: Any
    def __init__(self, name: Optional[str], url: str, **extra: Any) -> None: ...
    @property
    def type(self) -> ActivityType: ...
    @property
    def twitch_name(self) -> Optional[str]: ...
    def to_dict(self) -> Dict[str, Any]: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...

class Spotify:
    def __init__(self, **data: Any) -> None: ...
    @property
    def type(self) -> ActivityType: ...
    @property
    def created_at(self) -> Optional[datetime.datetime]: ...
    @property
    def colour(self) -> Colour: ...
    @property
    def color(self) -> Colour: ...
    def to_dict(self) -> Dict[str, Any]: ...
    @property
    def name(self) -> str: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    @property
    def title(self) -> str: ...
    @property
    def artists(self) -> List[str]: ...
    @property
    def artist(self) -> str: ...
    @property
    def album(self) -> str: ...
    @property
    def album_cover_url(self) -> str: ...
    @property
    def track_id(self) -> str: ...
    @property
    def track_url(self) -> str: ...
    @property
    def start(self) -> datetime.datetime: ...
    @property
    def end(self) -> datetime.datetime: ...
    @property
    def duration(self) -> datetime.timedelta: ...
    @property
    def party_id(self) -> str: ...

class CustomActivity(BaseActivity):
    name: Any
    state: Any
    emoji: Any
    def __init__(self, name: Optional[str], *, emoji: Optional[PartialEmoji] = ..., **extra: Any) -> None: ...
    @property
    def type(self) -> ActivityType: ...
    def to_dict(self) -> Dict[str, Any]: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
ActivityTypes = Union[Activity, Game, CustomActivity, Streaming, Spotify]