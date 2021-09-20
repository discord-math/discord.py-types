from .enums import UserFlags
from typing import Any, Callable, ClassVar, Dict, Iterator, List, Tuple, Type, TypeVar, overload

class BaseFlags:
    VALID_FLAGS: ClassVar[Dict[str, int]]
    DEFAULT_VALUE: ClassVar[int]
    value: int
    def __init__(self, **kwargs: bool): ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    def __iter__(self) -> Iterator[Tuple[str, bool]]: ...
    def _has_flag(self, o: int) -> bool: ...
    def _set_flag(self, o: int, toggle: bool) -> None: ...

class SystemChannelFlags(BaseFlags):
    join_notifications: bool
    premium_subscriptions: bool
    guild_reminder_notifications: bool

class MessageFlags(BaseFlags):
    crossposted: bool
    is_crossposted: bool
    suppress_embeds: bool
    source_message_deleted: bool
    urgent: bool
    has_thread: bool
    ephemeral: bool

class PublicUserFlags(BaseFlags):
    staff: bool
    partner: bool
    hypesquad: bool
    bug_hunter: bool
    hypesquad_bravery: bool
    hypesquad_brilliance: bool
    hypesquad_balance: bool
    early_supporter: bool
    team_user: bool
    system: bool
    bug_hunter_level_2: bool
    verified_bot: bool
    verified_bot_developer: bool
    early_verified_bot_developer: bool
    discord_certified_moderator: bool
    def all(self) -> List[UserFlags]: ...

class Intents(BaseFlags):
    value: Any
    def __init__(self, **kwargs: bool) -> None: ...
    @classmethod
    def all(cls) -> Intents: ...
    @classmethod
    def none(cls) -> Intents: ...
    @classmethod
    def default(cls) -> Intents: ...
    guilds: bool
    members: bool
    bans: bool
    emojis: bool
    emojis_and_stickers: bool
    integrations: bool
    webhooks: bool
    invites: bool
    voice_states: bool
    presences: bool
    messages: bool
    guild_messages: bool
    dm_messages: bool
    reactions: bool
    guild_reactions: bool
    dm_reactions: bool
    typing: bool
    guild_typing: bool
    dm_typing: bool

class MemberCacheFlags(BaseFlags):
    value: Any
    def __init__(self, **kwargs: bool) -> None: ...
    @classmethod
    def all(cls) -> MemberCacheFlags: ...
    @classmethod
    def none(cls) -> MemberCacheFlags: ...
    voice: bool
    joined: bool
    @classmethod
    def from_intents(cls, intents: Intents) -> MemberCacheFlags: ...

class ApplicationFlags(BaseFlags):
    gateway_presence: bool
    gateway_presence_limited: bool
    gateway_guild_members: bool
    gateway_guild_members_limited: bool
    verification_pending_guild_limit: bool
    embedded: bool
