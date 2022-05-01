from .flags import BaseFlags, alias_flag_value, flag_value
from typing import ClassVar, Iterator, Optional, Set, Tuple, Type, TypeVar

class permission_alias(alias_flag_value):
    alias: str

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
    def elevated(cls: Type[P]) -> P: ...
    @classmethod
    def advanced(cls: Type[P]) -> P: ...
    def update(self, **kwargs: bool) -> None: ...
    def handle_overwrite(self, allow: int, deny: int) -> None: ...
    create_instant_invite: flag_value
    kick_members: flag_value
    ban_members: flag_value
    administrator: flag_value
    manage_channels: flag_value
    manage_guild: flag_value
    add_reactions: flag_value
    view_audit_log: flag_value
    priority_speaker: flag_value
    stream: flag_value
    read_messages: flag_value
    view_channel: flag_value
    send_messages: flag_value
    send_tts_messages: flag_value
    manage_messages: flag_value
    embed_links: flag_value
    attach_files: flag_value
    read_message_history: flag_value
    mention_everyone: flag_value
    external_emojis: flag_value
    use_external_emojis: flag_value
    view_guild_insights: flag_value
    connect: flag_value
    speak: flag_value
    mute_members: flag_value
    deafen_members: flag_value
    move_members: flag_value
    use_voice_activation: flag_value
    change_nickname: flag_value
    manage_nicknames: flag_value
    manage_roles: flag_value
    manage_permissions: flag_value
    manage_webhooks: flag_value
    manage_emojis: flag_value
    manage_emojis_and_stickers: flag_value
    use_application_commands: flag_value
    request_to_speak: flag_value
    manage_events: flag_value
    manage_threads: flag_value
    create_public_threads: flag_value
    create_private_threads: flag_value
    external_stickers: flag_value
    use_external_stickers: flag_value
    send_messages_in_threads: flag_value
    use_embedded_activities: flag_value
    moderate_members: flag_value

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
    use_application_commands: Optional[bool]
    request_to_speak: Optional[bool]
    manage_events: Optional[bool]
    manage_threads: Optional[bool]
    create_public_threads: Optional[bool]
    create_private_threads: Optional[bool]
    send_messages_in_threads: Optional[bool]
    external_stickers: Optional[bool]
    use_external_stickers: Optional[bool]
    use_embedded_activities: Optional[bool]
    moderate_members: Optional[bool]
    def __init__(self, **kwargs: Optional[bool]) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def pair(self) -> Tuple[Permissions, Permissions]: ...
    @classmethod
    def from_pair(cls: Type[PO], allow: Permissions, deny: Permissions) -> PO: ...
    def is_empty(self) -> bool: ...
    def update(self, **kwargs: Optional[bool]) -> None: ...
    def __iter__(self) -> Iterator[Tuple[str, Optional[bool]]]: ...
