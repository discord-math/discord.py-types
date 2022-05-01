from enum import Enum as Enum
from typing import Any, Optional, Type, TypeVar

class ChannelType(Enum):
    text: int
    private: int
    voice: int
    group: int
    category: int
    news: int
    news_thread: int
    public_thread: int
    private_thread: int
    stage_voice: int
    forum: int

class MessageType(Enum):
    default: int
    recipient_add: int
    recipient_remove: int
    call: int
    channel_name_change: int
    channel_icon_change: int
    pins_add: int
    new_member: int
    premium_guild_subscription: int
    premium_guild_tier_1: int
    premium_guild_tier_2: int
    premium_guild_tier_3: int
    channel_follow_add: int
    guild_stream: int
    guild_discovery_disqualified: int
    guild_discovery_requalified: int
    guild_discovery_grace_period_initial_warning: int
    guild_discovery_grace_period_final_warning: int
    thread_created: int
    reply: int
    chat_input_command: int
    thread_starter_message: int
    guild_invite_reminder: int
    context_menu_command: int

class SpeakingState(Enum):
    none: int
    voice: int
    soundshare: int
    priority: int
    def __int__(self) -> int: ...

class VerificationLevel(Enum):
    none: int
    low: int
    medium: int
    high: int
    highest: int

class ContentFilter(Enum):
    disabled: int
    no_role: int
    all_members: int

class Status(Enum):
    online: str
    offline: str
    idle: str
    dnd: str
    do_not_disturb: str
    invisible: str

class DefaultAvatar(Enum):
    blurple: int
    grey: int
    gray: int
    green: int
    orange: int
    red: int

class NotificationLevel(Enum):
    all_messages: int
    only_mentions: int

class AuditLogActionCategory(Enum):
    create: int
    delete: int
    update: int

class AuditLogAction(Enum):
    guild_update: int
    channel_create: int
    channel_update: int
    channel_delete: int
    overwrite_create: int
    overwrite_update: int
    overwrite_delete: int
    kick: int
    member_prune: int
    ban: int
    unban: int
    member_update: int
    member_role_update: int
    member_move: int
    member_disconnect: int
    bot_add: int
    role_create: int
    role_update: int
    role_delete: int
    invite_create: int
    invite_update: int
    invite_delete: int
    webhook_create: int
    webhook_update: int
    webhook_delete: int
    emoji_create: int
    emoji_update: int
    emoji_delete: int
    message_delete: int
    message_bulk_delete: int
    message_pin: int
    message_unpin: int
    integration_create: int
    integration_update: int
    integration_delete: int
    stage_instance_create: int
    stage_instance_update: int
    stage_instance_delete: int
    sticker_create: int
    sticker_update: int
    sticker_delete: int
    scheduled_event_create: int
    scheduled_event_update: int
    scheduled_event_delete: int
    thread_create: int
    thread_update: int
    thread_delete: int
    @property
    def category(self) -> Optional[AuditLogActionCategory]: ...
    @property
    def target_type(self) -> Optional[str]: ...

class UserFlags(Enum):
    staff: int
    partner: int
    hypesquad: int
    bug_hunter: int
    mfa_sms: int
    premium_promo_dismissed: int
    hypesquad_bravery: int
    hypesquad_brilliance: int
    hypesquad_balance: int
    early_supporter: int
    team_user: int
    system: int
    has_unread_urgent_messages: int
    bug_hunter_level_2: int
    verified_bot: int
    verified_bot_developer: int
    discord_certified_moderator: int
    bot_http_interactions: int
    spammer: int

class ActivityType(Enum):
    unknown: int
    playing: int
    streaming: int
    listening: int
    watching: int
    custom: int
    competing: int
    def __int__(self) -> int: ...

class TeamMembershipState(Enum):
    invited: int
    accepted: int

class WebhookType(Enum):
    incoming: int
    channel_follower: int
    application: int

class ExpireBehaviour(Enum):
    remove_role: int
    kick: int
ExpireBehavior = ExpireBehaviour

class StickerType(Enum):
    standard: int
    guild: int

class StickerFormatType(Enum):
    png: int
    apng: int
    lottie: int
    @property
    def file_extension(self) -> str: ...

class InviteTarget(Enum):
    unknown: int
    stream: int
    embedded_application: int

class InteractionType(Enum):
    ping: int
    application_command: int
    component: int
    autocomplete: int
    modal_submit: int

class InteractionResponseType(Enum):
    pong: int
    channel_message: int
    deferred_channel_message: int
    deferred_message_update: int
    message_update: int
    autocomplete_result: int
    modal: int

class VideoQualityMode(Enum):
    auto: int
    full: int
    def __int__(self) -> int: ...

class ComponentType(Enum):
    action_row: int
    button: int
    select: int
    text_input: int
    def __int__(self) -> int: ...

class ButtonStyle(Enum):
    primary: int
    secondary: int
    success: int
    danger: int
    link: int
    blurple: int
    grey: int
    gray: int
    green: int
    red: int
    url: int
    def __int__(self) -> int: ...

class TextStyle(Enum):
    short: int
    paragraph: int
    long: int
    def __int__(self) -> int: ...

class PrivacyLevel(Enum):
    guild_only: int

class NSFWLevel(Enum):
    default: int
    explicit: int
    safe: int
    age_restricted: int

class MFALevel(Enum):
    disabled: int
    require_2fa: int

class Locale(Enum):
    american_english: str
    british_english: str
    bulgarian: str
    chinese: str
    taiwan_chinese: str
    croatian: str
    czech: str
    danish: str
    dutch: str
    finnish: str
    french: str
    german: str
    greek: str
    hindi: str
    hungarian: str
    italian: str
    japanese: str
    korean: str
    lithuanian: str
    norwegian: str
    polish: str
    brazil_portuguese: str
    romanian: str
    russian: str
    spain_spanish: str
    swedish: str
    thai: str
    turkish: str
    ukrainian: str
    vietnamese: str
E = TypeVar('E', bound='Enum')

class EntityType(Enum):
    stage_instance: int
    voice: int
    external: int

class EventStatus(Enum):
    scheduled: int
    active: int
    completed: int
    canceled: int
    ended: int
    cancelled: int

class AppCommandOptionType(Enum):
    subcommand: int
    subcommand_group: int
    string: int
    integer: int
    boolean: int
    user: int
    channel: int
    role: int
    mentionable: int
    number: int
    attachment: int

class AppCommandType(Enum):
    chat_input: int
    user: int
    message: int

def create_unknown_value(cls: Type[E], val: Any) -> E: ...

def try_enum(cls: Type[E], val: Any) -> E: ...
