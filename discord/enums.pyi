from enum import Enum as Enum
from typing import ClassVar, Optional, TypeVar

class ChannelType(Enum):
    text: int
    private: int
    voice: int
    group: int
    category: int
    news: int
    store: int
    news_thread: int
    public_thread: int
    private_thread: int
    stage_voice: int

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
    application_command: int
    thread_starter_message: int
    guild_invite_reminder: int

class VoiceRegion(Enum):
    us_west: str
    us_east: str
    us_south: str
    us_central: str
    eu_west: str
    eu_central: str
    singapore: str
    london: str
    sydney: str
    amsterdam: str
    frankfurt: str
    brazil: str
    hongkong: str
    russia: str
    japan: str
    southafrica: str
    south_korea: str
    india: str
    europe: str
    dubai: str
    vip_us_east: str
    vip_us_west: str
    vip_amsterdam: str

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

class InteractionResponseType(Enum):
    pong: int
    channel_message: int
    deferred_channel_message: int
    deferred_message_update: int
    message_update: int

class VideoQualityMode(Enum):
    auto: int
    full: int
    def __int__(self) -> int: ...

class ComponentType(Enum):
    action_row: int
    button: int
    select: int
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

class StagePrivacyLevel(Enum):
    public: int
    closed: int
    guild_only: int

class NSFWLevel(Enum):
    default: int
    explicit: int
    safe: int
    age_restricted: int
