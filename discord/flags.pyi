from .enums import UserFlags
from typing import Any, Callable, ClassVar, Dict, Iterator, List, Tuple, Type, TypeVar, Optional, overload

FV = TypeVar('FV', bound='flag_value')
BF = TypeVar('BF', bound='BaseFlags')

class flag_value:
    flag: int
    __doc__: Optional[str]
    def __init__(self, func: Callable[[Any], int]) -> None: ...
    @overload
    def __get__(self: FV, instance: None, owner: Type[BF]) -> FV: ...
    @overload
    def __get__(self, instance: BF, owner: Type[BF]) -> bool: ...
    def __set__(self, instance: BaseFlags, value: bool) -> None: ...

class alias_flag_value(flag_value): ...

class BaseFlags:
    VALID_FLAGS: ClassVar[Dict[str, int]]
    DEFAULT_VALUE: ClassVar[int]
    value: int
    def __init__(self, **kwargs: bool) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __iter__(self) -> Iterator[Tuple[str, bool]]: ...

class SystemChannelFlags(BaseFlags):
    join_notifications: flag_value
    premium_subscriptions: flag_value
    guild_reminder_notifications: flag_value
    join_notification_replies: flag_value

class MessageFlags(BaseFlags):
    crossposted: flag_value
    is_crossposted: flag_value
    suppress_embeds: flag_value
    source_message_deleted: flag_value
    urgent: flag_value
    has_thread: flag_value
    ephemeral: flag_value
    loading: flag_value
    failed_to_mention_some_roles_in_thread: flag_value

class PublicUserFlags(BaseFlags):
    staff: flag_value
    partner: flag_value
    hypesquad: flag_value
    bug_hunter: flag_value
    hypesquad_bravery: flag_value
    hypesquad_brilliance: flag_value
    hypesquad_balance: flag_value
    early_supporter: flag_value
    team_user: flag_value
    system: flag_value
    bug_hunter_level_2: flag_value
    verified_bot: flag_value
    verified_bot_developer: flag_value
    early_verified_bot_developer: flag_value
    discord_certified_moderator: flag_value
    bot_http_interactions: flag_value
    spammer: flag_value
    def all(self) -> List[UserFlags]: ...

class Intents(BaseFlags):
    value: int
    def __init__(self, value: int = ..., **kwargs: bool) -> None: ...
    @classmethod
    def all(cls) -> Intents: ...
    @classmethod
    def none(cls) -> Intents: ...
    @classmethod
    def default(cls) -> Intents: ...
    guilds: flag_value
    members: flag_value
    bans: flag_value
    emojis: flag_value
    emojis_and_stickers: flag_value
    integrations: flag_value
    webhooks: flag_value
    invites: flag_value
    voice_states: flag_value
    presences: flag_value
    messages: flag_value
    guild_messages: flag_value
    dm_messages: flag_value
    reactions: flag_value
    guild_reactions: flag_value
    dm_reactions: flag_value
    typing: flag_value
    guild_typing: flag_value
    dm_typing: flag_value
    message_content: flag_value
    guild_scheduled_events: flag_value

class MemberCacheFlags(BaseFlags):
    value: int
    def __init__(self, **kwargs: bool) -> None: ...
    @classmethod
    def all(cls) -> MemberCacheFlags: ...
    @classmethod
    def none(cls) -> MemberCacheFlags: ...
    voice: flag_value
    joined: flag_value
    @classmethod
    def from_intents(cls, intents: Intents) -> MemberCacheFlags: ...

class ApplicationFlags(BaseFlags):
    gateway_presence: flag_value
    gateway_presence_limited: flag_value
    gateway_guild_members: flag_value
    gateway_guild_members_limited: flag_value
    verification_pending_guild_limit: flag_value
    embedded: flag_value
    gateway_message_content: flag_value
    gateway_message_content_limited: flag_value

class ChannelFlags(BaseFlags):
    pinned: flag_value
