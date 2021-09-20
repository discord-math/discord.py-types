from .flags import BaseFlags
from typing import Any, ClassVar, Iterator, Optional, Set, Tuple, Type, TypeVar

P = TypeVar('P', bound='Permissions')

class Permissions(BaseFlags):
    value: int
    def __init__(self, permissions: int = ..., **kwargs: bool) -> None: ...
    def is_subset(self, other: Permissions) -> bool: ...
    def is_superset(self, other: Permissions) -> bool: ...
    def is_strict_subset(self, other: Permissions) -> bool: ...
    def is_strict_superset(self, other: Permissions) -> bool: ...
    def __le__(self, other: Permissions) -> bool: ...
    def __ge__(self, other: Permissions) -> bool: ...
    def __lt__(self, other: Permissions) -> bool: ...
    def __gt__(self, other: Permissions) -> bool: ...
    @classmethod
    def none(cls: Type[P]) -> P: ...
    @classmethod
    def all(cls: Type[P]) -> P: ...
    @classmethod
    def all_channel(cls: Type[P]) -> P: ...
    @classmethod
    def general(cls: Type[P]) -> P: ...
    @classmethod
    def membership(cls: Type[P]) -> P: ...
    @classmethod
    def text(cls: Type[P]) -> P: ...
    @classmethod
    def voice(cls: Type[P]) -> P: ...
    @classmethod
    def stage(cls: Type[P]) -> P: ...
    @classmethod
    def stage_moderator(cls: Type[P]) -> P: ...
    @classmethod
    def advanced(cls: Type[P]) -> P: ...
    def update(self, **kwargs: bool) -> None: ...
    def handle_overwrite(self, allow: int, deny: int) -> None: ...
    create_instant_invite: bool
    kick_members: bool
    ban_members: bool
    administrator: bool
    manage_channels: bool
    manage_guild: bool
    add_reactions: bool
    view_audit_log: bool
    priority_speaker: bool
    stream: bool
    read_messages: bool
    view_channel: bool
    send_messages: bool
    send_tts_messages: bool
    manage_messages: bool
    embed_links: bool
    attach_files: bool
    read_message_history: bool
    mention_everyone: bool
    external_emojis: bool
    use_external_emojis: bool
    view_guild_insights: bool
    connect: bool
    speak: bool
    mute_members: bool
    deafen_members: bool
    move_members: bool
    use_voice_activation: bool
    change_nickname: bool
    manage_nicknames: bool
    manage_roles: bool
    manage_permissions: bool
    manage_webhooks: bool
    manage_emojis: bool
    manage_emojis_and_stickers: bool
    use_slash_commands: bool
    request_to_speak: bool
    manage_events: bool
    manage_threads: bool
    create_public_threads: bool
    create_private_threads: bool
    external_stickers: bool
    use_external_stickers: bool
    send_messages_in_threads: bool

PO = TypeVar('PO', bound='PermissionOverwrite')

class PermissionOverwrite:
    VALID_NAMES: ClassVar[Set[str]]
    PURE_FLAGS: ClassVar[Set[str]]
    create_instant_invite: Optional[bool]
    kick_members: Optional[bool]
    ban_members: Optional[bool]
    administrator: Optional[bool]
    manage_channels: Optional[bool]
    manage_guild: Optional[bool]
    add_reactions: Optional[bool]
    view_audit_log: Optional[bool]
    priority_speaker: Optional[bool]
    stream: Optional[bool]
    read_messages: Optional[bool]
    view_channel: Optional[bool]
    send_messages: Optional[bool]
    send_tts_messages: Optional[bool]
    manage_messages: Optional[bool]
    embed_links: Optional[bool]
    attach_files: Optional[bool]
    read_message_history: Optional[bool]
    mention_everyone: Optional[bool]
    external_emojis: Optional[bool]
    use_external_emojis: Optional[bool]
    view_guild_insights: Optional[bool]
    connect: Optional[bool]
    speak: Optional[bool]
    mute_members: Optional[bool]
    deafen_members: Optional[bool]
    move_members: Optional[bool]
    use_voice_activation: Optional[bool]
    change_nickname: Optional[bool]
    manage_nicknames: Optional[bool]
    manage_roles: Optional[bool]
    manage_permissions: Optional[bool]
    manage_webhooks: Optional[bool]
    manage_emojis: Optional[bool]
    manage_emojis_and_stickers: Optional[bool]
    use_slash_commands: Optional[bool]
    request_to_speak: Optional[bool]
    manage_events: Optional[bool]
    manage_threads: Optional[bool]
    create_public_threads: Optional[bool]
    create_private_threads: Optional[bool]
    send_messages_in_threads: Optional[bool]
    external_stickers: Optional[bool]
    use_external_stickers: Optional[bool]
    def __init__(self, **kwargs: Optional[bool]) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    def pair(self) -> Tuple[Permissions, Permissions]: ...
    @classmethod
    def from_pair(cls: Type[PO], allow: Permissions, deny: Permissions) -> PO: ...
    def is_empty(self) -> bool: ...
    def update(self, **kwargs: bool) -> None: ...
    def __iter__(self) -> Iterator[Tuple[str, Optional[bool]]]: ...
