from . import (
    abc as abc,
    app_commands as app_commands,
    opus as opus,
    ui as ui,
    utils as utils,
)
from discord.activity import (
    Activity as Activity,
    BaseActivity as BaseActivity,
    CustomActivity as CustomActivity,
    Game as Game,
    Spotify as Spotify,
    Streaming as Streaming,
)
from discord.appinfo import (
    AppInfo as AppInfo,
    PartialAppInfo as PartialAppInfo,
)
from discord.asset import (
    Asset as Asset,
)
from discord.audit_logs import (
    AuditLogChanges as AuditLogChanges,
    AuditLogDiff as AuditLogDiff,
    AuditLogEntry as AuditLogEntry,
)
from discord.channel import (
    CategoryChannel as CategoryChannel,
    DMChannel as DMChannel,
    ForumChannel as ForumChannel,
    GroupChannel as GroupChannel,
    PartialMessageable as PartialMessageable,
    StageChannel as StageChannel,
    TextChannel as TextChannel,
    VoiceChannel as VoiceChannel,
)
from discord.client import (
    Client as Client,
)
from discord.colour import (
    Color as Color,
    Colour as Colour,
)
from discord.components import (
    ActionRow as ActionRow,
    Button as Button,
    Component as Component,
    SelectMenu as SelectMenu,
    SelectOption as SelectOption,
    TextInput as TextInput,
)
from discord.embeds import (
    Embed as Embed,
)
from discord.emoji import (
    Emoji as Emoji,
)
from discord.enums import (
    ActivityType as ActivityType,
    AppCommandOptionType as AppCommandOptionType,
    AppCommandType as AppCommandType,
    AuditLogAction as AuditLogAction,
    AuditLogActionCategory as AuditLogActionCategory,
    ButtonStyle as ButtonStyle,
    ChannelType as ChannelType,
    ComponentType as ComponentType,
    ContentFilter as ContentFilter,
    DefaultAvatar as DefaultAvatar,
    EntityType as EntityType,
    Enum as Enum,
    EventStatus as EventStatus,
    ExpireBehavior as ExpireBehavior,
    ExpireBehaviour as ExpireBehaviour,
    InteractionResponseType as InteractionResponseType,
    InteractionType as InteractionType,
    InviteTarget as InviteTarget,
    Locale as Locale,
    MFALevel as MFALevel,
    MessageType as MessageType,
    NSFWLevel as NSFWLevel,
    NotificationLevel as NotificationLevel,
    PrivacyLevel as PrivacyLevel,
    SpeakingState as SpeakingState,
    Status as Status,
    StickerFormatType as StickerFormatType,
    StickerType as StickerType,
    TeamMembershipState as TeamMembershipState,
    TextStyle as TextStyle,
    UserFlags as UserFlags,
    VerificationLevel as VerificationLevel,
    VideoQualityMode as VideoQualityMode,
    WebhookType as WebhookType,
)
from discord.errors import (
    ClientException as ClientException,
    ConnectionClosed as ConnectionClosed,
    DiscordException as DiscordException,
    DiscordServerError as DiscordServerError,
    Forbidden as Forbidden,
    GatewayNotFound as GatewayNotFound,
    HTTPException as HTTPException,
    InteractionResponded as InteractionResponded,
    InvalidData as InvalidData,
    LoginFailure as LoginFailure,
    NotFound as NotFound,
    PrivilegedIntentsRequired as PrivilegedIntentsRequired,
)
from discord.file import (
    File as File,
)
from discord.flags import (
    ApplicationFlags as ApplicationFlags,
    ChannelFlags as ChannelFlags,
    Intents as Intents,
    MemberCacheFlags as MemberCacheFlags,
    MessageFlags as MessageFlags,
    PublicUserFlags as PublicUserFlags,
    SystemChannelFlags as SystemChannelFlags,
)
from discord.guild import (
    BanEntry as BanEntry,
    Guild as Guild,
)
from discord.integrations import (
    BotIntegration as BotIntegration,
    Integration as Integration,
    IntegrationAccount as IntegrationAccount,
    IntegrationApplication as IntegrationApplication,
    StreamIntegration as StreamIntegration,
)
from discord.interactions import (
    Interaction as Interaction,
    InteractionMessage as InteractionMessage,
    InteractionResponse as InteractionResponse,
)
from discord.invite import (
    Invite as Invite,
    PartialInviteChannel as PartialInviteChannel,
    PartialInviteGuild as PartialInviteGuild,
)
from discord.member import (
    Member as Member,
    VoiceState as VoiceState,
)
from discord.mentions import (
    AllowedMentions as AllowedMentions,
)
from discord.message import (
    Attachment as Attachment,
    DeletedReferencedMessage as DeletedReferencedMessage,
    Message as Message,
    MessageInteraction as MessageInteraction,
    MessageReference as MessageReference,
    PartialMessage as PartialMessage,
)
from discord.object import (
    Object as Object,
)
from discord.partial_emoji import (
    PartialEmoji as PartialEmoji,
)
from discord.permissions import (
    PermissionOverwrite as PermissionOverwrite,
    Permissions as Permissions,
)
from discord.player import (
    AudioSource as AudioSource,
    FFmpegAudio as FFmpegAudio,
    FFmpegOpusAudio as FFmpegOpusAudio,
    FFmpegPCMAudio as FFmpegPCMAudio,
    PCMAudio as PCMAudio,
    PCMVolumeTransformer as PCMVolumeTransformer,
)
from discord.raw_models import (
    RawBulkMessageDeleteEvent as RawBulkMessageDeleteEvent,
    RawIntegrationDeleteEvent as RawIntegrationDeleteEvent,
    RawMemberRemoveEvent as RawMemberRemoveEvent,
    RawMessageDeleteEvent as RawMessageDeleteEvent,
    RawMessageUpdateEvent as RawMessageUpdateEvent,
    RawReactionActionEvent as RawReactionActionEvent,
    RawReactionClearEmojiEvent as RawReactionClearEmojiEvent,
    RawReactionClearEvent as RawReactionClearEvent,
    RawThreadDeleteEvent as RawThreadDeleteEvent,
    RawTypingEvent as RawTypingEvent,
)
from discord.reaction import (
    Reaction as Reaction,
)
from discord.role import (
    Role as Role,
    RoleTags as RoleTags,
)
from discord.scheduled_event import (
    ScheduledEvent as ScheduledEvent,
)
from discord.shard import (
    AutoShardedClient as AutoShardedClient,
    ShardInfo as ShardInfo,
)
from discord.stage_instance import (
    StageInstance as StageInstance,
)
from discord.sticker import (
    GuildSticker as GuildSticker,
    StandardSticker as StandardSticker,
    Sticker as Sticker,
    StickerItem as StickerItem,
    StickerPack as StickerPack,
)
from discord.team import (
    Team as Team,
    TeamMember as TeamMember,
)
from discord.template import (
    Template as Template,
)
from discord.threads import (
    Thread as Thread,
    ThreadMember as ThreadMember,
)
from discord.user import (
    ClientUser as ClientUser,
    User as User,
)
from discord.voice_client import (
    VoiceClient as VoiceClient,
    VoiceProtocol as VoiceProtocol,
)
from discord.webhook import (
    Webhook as Webhook,
    WebhookMessage as WebhookMessage,
    PartialWebhookChannel as PartialWebhookChannel,
    PartialWebhookGuild as PartialWebhookGuild,
    SyncWebhook as SyncWebhook,
    SyncWebhookMessage as SyncWebhookMessage,
)
from discord.widget import (
    Widget as Widget,
    WidgetChannel as WidgetChannel,
    WidgetMember as WidgetMember,
)
from typing import Literal, NamedTuple

class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: Literal["alpha", "beta", "candidate", "final"]
    serial: int

version_info: VersionInfo
