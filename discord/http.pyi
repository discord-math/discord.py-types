import aiohttp
import asyncio
from . import utils
from .embeds import Embed
from .enums import AuditLogAction
from .errors import DiscordServerError, Forbidden, GatewayNotFound as GatewayNotFound, HTTPException as HTTPException, LoginFailure as LoginFailure, NotFound as NotFound
from .file import File
from .flags import MessageFlags
from .gateway import DiscordClientWebSocketResponse
from .mentions import AllowedMentions
from .message import Attachment
from .types import appinfo, audit_log, channel, command, emoji, guild, integration, invite, member, message, role, scheduled_event, sticker, template, threads, user, webhook, widget
from .types.snowflake import Snowflake, SnowflakeList
from .ui.view import View
from .utils import MISSING
from types import TracebackType
from typing import Any, ClassVar, Coroutine, Dict, Iterable, List, Literal, NamedTuple, Optional, Sequence, Tuple, Type, TypeVar, Union, overload

T = TypeVar('T')
BE = TypeVar('BE', bound=BaseException)
Response = Coroutine[Any, Any, T]

async def json_or_text(response: aiohttp.ClientResponse) -> Union[Dict[str, Any], str]: ...

MP = TypeVar('MP', bound='MultipartParameters')

class MultipartParameters(NamedTuple):
    payload: Optional[Dict[str, Any]]
    multipart: Optional[List[Dict[str, Any]]]
    files: Optional[Sequence[File]]
    def __enter__(self: MP) -> MP: ...
    def __exit__(self, exc_type: Optional[Type[BE]], exc: Optional[BE], traceback: Optional[TracebackType]) -> None: ...

def handle_message_parameters(content: Optional[str] = ..., *, username: str = ..., avatar_url: Any = ..., tts: bool = ..., nonce: Optional[Union[int, str]] = ..., flags: MessageFlags = ..., file: File = ..., files: Sequence[File] = ..., embed: Optional[Embed] = ..., embeds: Sequence[Embed] = ..., attachments: Sequence[Union[Attachment, File]] = ..., view: Optional[View] = ..., allowed_mentions: Optional[AllowedMentions] = ..., message_reference: Optional[message.MessageReference] = ..., stickers: Optional[SnowflakeList] = ..., previous_allowed_mentions: Optional[AllowedMentions] = ..., mention_author: Optional[bool] = ..., channel_payload: Dict[str, Any] = ...) -> MultipartParameters: ...

INTERNAL_API_VERSION: int

class Route:
    BASE: ClassVar[str]
    path: str
    method: str
    url: str
    channel_id: Optional[Snowflake]
    guild_id: Optional[Snowflake]
    webhook_id: Optional[Snowflake]
    webhook_token: Optional[str]
    def __init__(self, method: str, path: str, **parameters: Any) -> None: ...
    @property
    def bucket(self) -> str: ...

MU = TypeVar('MU', bound='MaybeUnlock')

class MaybeUnlock:
    lock: asyncio.Lock
    def __init__(self, lock: asyncio.Lock) -> None: ...
    def __enter__(self: MU) -> MU: ...
    def defer(self) -> None: ...
    def __exit__(self, exc_type: Optional[Type[BE]], exc: Optional[BE], traceback: Optional[TracebackType]) -> None: ...

class HTTPClient:
    loop: asyncio.AbstractEventLoop
    connector: aiohttp.BaseConnector
    token: Optional[str]
    bot_token: bool
    proxy: Optional[str]
    proxy_auth: Optional[aiohttp.BasicAuth]
    http_trace: Optional[aiohttp.TraceConfig]
    use_clock: bool
    user_agent: str
    def __init__(self, loop: asyncio.AbstractEventLoop, connector: Optional[aiohttp.BaseConnector] = ..., *, proxy: Optional[str] = ..., proxy_auth: Optional[aiohttp.BasicAuth] = ..., unsync_clock: bool = ..., http_trace: Optional[aiohttp.TraceConfig] = ...) -> None: ...
    def recreate(self) -> None: ...
    async def ws_connect(self, url: str, *, compress: int = ...) -> aiohttp.ClientWebSocketResponse: ...
    async def request(self, route: Route, *, files: Optional[Sequence[File]] = ..., form: Optional[Iterable[Dict[str, Any]]] = ..., **kwargs: Any) -> Any: ...
    async def get_from_cdn(self, url: str) -> bytes: ...
    async def close(self) -> None: ...
    async def static_login(self, token: str) -> user.User: ...
    def logout(self) -> Response[None]: ...
    def start_group(self, user_id: Snowflake, recipients: List[int]) -> Response[channel.GroupDMChannel]: ...
    def leave_group(self, channel_id: Snowflake) -> Response[None]: ...
    def start_private_message(self, user_id: Snowflake) -> Response[channel.DMChannel]: ...
    def send_message(self, channel_id: Snowflake, *, params: MultipartParameters) -> Response[message.Message]: ...
    def send_typing(self, channel_id: Snowflake) -> Response[None]: ...
    def delete_message(self, channel_id: Snowflake, message_id: Snowflake, *, reason: Optional[str] = ...) -> Response[None]: ...
    def delete_messages(self, channel_id: Snowflake, message_ids: SnowflakeList, *, reason: Optional[str] = ...) -> Response[None]: ...
    def edit_message(self, channel_id: Snowflake, message_id: Snowflake, *, params: MultipartParameters) -> Response[message.Message]: ...
    def add_reaction(self, channel_id: Snowflake, message_id: Snowflake, emoji: str) -> Response[None]: ...
    def remove_reaction(self, channel_id: Snowflake, message_id: Snowflake, emoji: str, member_id: Snowflake) -> Response[None]: ...
    def remove_own_reaction(self, channel_id: Snowflake, message_id: Snowflake, emoji: str) -> Response[None]: ...
    def get_reaction_users(self, channel_id: Snowflake, message_id: Snowflake, emoji: str, limit: int, after: Optional[Snowflake] = ...) -> Response[List[user.User]]: ...
    def clear_reactions(self, channel_id: Snowflake, message_id: Snowflake) -> Response[None]: ...
    def clear_single_reaction(self, channel_id: Snowflake, message_id: Snowflake, emoji: str) -> Response[None]: ...
    def get_message(self, channel_id: Snowflake, message_id: Snowflake) -> Response[message.Message]: ...
    def get_channel(self, channel_id: Snowflake) -> Response[channel.Channel]: ...
    def logs_from(self, channel_id: Snowflake, limit: int, before: Optional[Snowflake] = ..., after: Optional[Snowflake] = ..., around: Optional[Snowflake] = ...) -> Response[List[message.Message]]: ...
    def publish_message(self, channel_id: Snowflake, message_id: Snowflake) -> Response[message.Message]: ...
    def pin_message(self, channel_id: Snowflake, message_id: Snowflake, reason: Optional[str] = ...) -> Response[None]: ...
    def unpin_message(self, channel_id: Snowflake, message_id: Snowflake, reason: Optional[str] = ...) -> Response[None]: ...
    def pins_from(self, channel_id: Snowflake) -> Response[List[message.Message]]: ...
    def kick(self, user_id: Snowflake, guild_id: Snowflake, reason: Optional[str] = ...) -> Response[None]: ...
    def ban(self, user_id: Snowflake, guild_id: Snowflake, delete_message_days: int = ..., reason: Optional[str] = ...) -> Response[None]: ...
    def unban(self, user_id: Snowflake, guild_id: Snowflake, *, reason: Optional[str] = ...) -> Response[None]: ...
    def guild_voice_state(self, user_id: Snowflake, guild_id: Snowflake, *, mute: Optional[bool] = ..., deafen: Optional[bool] = ..., reason: Optional[str] = ...) -> Response[member.Member]: ...
    def edit_profile(self, payload: Dict[str, Any]) -> Response[user.User]: ...
    def change_my_nickname(self, guild_id: Snowflake, nickname: str, *, reason: Optional[str] = ...) -> Response[member.Nickname]: ...
    def change_nickname(self, guild_id: Snowflake, user_id: Snowflake, nickname: str, *, reason: Optional[str] = ...) -> Response[member.Member]: ...
    def edit_my_voice_state(self, guild_id: Snowflake, payload: Dict[str, Any]) -> Response[None]: ...
    def edit_voice_state(self, guild_id: Snowflake, user_id: Snowflake, payload: Dict[str, Any]) -> Response[None]: ...
    def edit_member(self, guild_id: Snowflake, user_id: Snowflake, *, reason: Optional[str] = ..., **fields: Any) -> Response[member.MemberWithUser]: ...
    def edit_channel(self, channel_id: Snowflake, *, reason: Optional[str] = ..., **options: Any) -> Response[channel.Channel]: ...
    def bulk_channel_update(self, guild_id: Snowflake, data: List[guild.ChannelPositionUpdate], *, reason: Optional[str] = ...) -> Response[None]: ...
    def create_channel(self, guild_id: Snowflake, channel_type: channel.ChannelType, *, reason: Optional[str] = ..., **options: Any) -> Response[channel.GuildChannel]: ...
    def delete_channel(self, channel_id: Snowflake, *, reason: Optional[str] = ...) -> Response[None]: ...
    def start_thread_with_message(self, channel_id: Snowflake, message_id: Snowflake, *, name: str, auto_archive_duration: threads.ThreadArchiveDuration, rate_limit_per_user: Optional[int] = ..., reason: Optional[str] = ...) -> Response[threads.Thread]: ...
    def start_thread_without_message(self, channel_id: Snowflake, *, name: str, auto_archive_duration: threads.ThreadArchiveDuration, type: threads.ThreadType, invitable: bool = ..., rate_limit_per_user: Optional[int] = ..., reason: Optional[str] = ...) -> Response[threads.Thread]: ...
    def start_thread_in_forum(self, channel_id: Snowflake, *, params: MultipartParameters, reason: Optional[str] = ...) -> Response[threads.Thread]: ...
    def join_thread(self, channel_id: Snowflake) -> Response[None]: ...
    def add_user_to_thread(self, channel_id: Snowflake, user_id: Snowflake) -> Response[None]: ...
    def leave_thread(self, channel_id: Snowflake) -> Response[None]: ...
    def remove_user_from_thread(self, channel_id: Snowflake, user_id: Snowflake) -> Response[None]: ...
    def get_public_archived_threads(self, channel_id: Snowflake, before: Optional[Snowflake] = ..., limit: int = ...) -> Response[threads.ThreadPaginationPayload]: ...
    def get_private_archived_threads(self, channel_id: Snowflake, before: Optional[Snowflake] = ..., limit: int = ...) -> Response[threads.ThreadPaginationPayload]: ...
    def get_joined_private_archived_threads(self, channel_id: Snowflake, before: Optional[Snowflake] = ..., limit: int = ...) -> Response[threads.ThreadPaginationPayload]: ...
    def get_active_threads(self, guild_id: Snowflake) -> Response[threads.ThreadPaginationPayload]: ...
    def get_thread_member(self, channel_id: Snowflake, user_id: Snowflake) -> Response[threads.ThreadMember]: ...
    def get_thread_members(self, channel_id: Snowflake) -> Response[List[threads.ThreadMember]]: ...
    def create_webhook(self, channel_id: Snowflake, *, name: str, avatar: Optional[bytes] = ..., reason: Optional[str] = ...) -> Response[webhook.Webhook]: ...
    def channel_webhooks(self, channel_id: Snowflake) -> Response[List[webhook.Webhook]]: ...
    def guild_webhooks(self, guild_id: Snowflake) -> Response[List[webhook.Webhook]]: ...
    def get_webhook(self, webhook_id: Snowflake) -> Response[webhook.Webhook]: ...
    def follow_webhook(self, channel_id: Snowflake, webhook_channel_id: Snowflake, reason: Optional[str] = ...) -> Response[None]: ...
    def get_guilds(self, limit: int, before: Optional[Snowflake] = ..., after: Optional[Snowflake] = ...) -> Response[List[guild.Guild]]: ...
    def leave_guild(self, guild_id: Snowflake) -> Response[None]: ...
    def get_guild(self, guild_id: Snowflake, *, with_counts: bool = ...) -> Response[guild.Guild]: ...
    def delete_guild(self, guild_id: Snowflake) -> Response[None]: ...
    def create_guild(self, name: str, icon: Optional[str]) -> Response[guild.Guild]: ...
    def edit_guild(self, guild_id: Snowflake, *, reason: Optional[str] = ..., **fields: Any) -> Response[guild.Guild]: ...
    def get_template(self, code: str) -> Response[template.Template]: ...
    def guild_templates(self, guild_id: Snowflake) -> Response[List[template.Template]]: ...
    def create_template(self, guild_id: Snowflake, payload: Dict[str, Any]) -> Response[template.Template]: ...
    def sync_template(self, guild_id: Snowflake, code: str) -> Response[template.Template]: ...
    def edit_template(self, guild_id: Snowflake, code: str, payload: Dict[str, Any]) -> Response[template.Template]: ...
    def delete_template(self, guild_id: Snowflake, code: str) -> Response[None]: ...
    def create_from_template(self, code: str, name: str, icon: Optional[str]) -> Response[guild.Guild]: ...
    def get_bans(self, guild_id: Snowflake, limit: int, before: Optional[Snowflake] = ..., after: Optional[Snowflake] = ...) -> Response[List[guild.Ban]]: ...
    def get_ban(self, user_id: Snowflake, guild_id: Snowflake) -> Response[guild.Ban]: ...
    def get_vanity_code(self, guild_id: Snowflake) -> Response[invite.VanityInvite]: ...
    def change_vanity_code(self, guild_id: Snowflake, code: str, *, reason: Optional[str] = ...) -> Response[None]: ...
    def get_all_guild_channels(self, guild_id: Snowflake) -> Response[List[guild.GuildChannel]]: ...
    def get_members(self, guild_id: Snowflake, limit: int, after: Optional[Snowflake]) -> Response[List[member.MemberWithUser]]: ...
    def get_member(self, guild_id: Snowflake, member_id: Snowflake) -> Response[member.MemberWithUser]: ...
    def prune_members(self, guild_id: Snowflake, days: int, compute_prune_count: bool, roles: Iterable[str], *, reason: Optional[str] = ...) -> Response[guild.GuildPrune]: ...
    def estimate_pruned_members(self, guild_id: Snowflake, days: int, roles: Iterable[str]) -> Response[guild.GuildPrune]: ...
    def get_sticker(self, sticker_id: Snowflake) -> Response[sticker.Sticker]: ...
    def list_premium_sticker_packs(self) -> Response[sticker.ListPremiumStickerPacks]: ...
    def get_all_guild_stickers(self, guild_id: Snowflake) -> Response[List[sticker.GuildSticker]]: ...
    def get_guild_sticker(self, guild_id: Snowflake, sticker_id: Snowflake) -> Response[sticker.GuildSticker]: ...
    def create_guild_sticker(self, guild_id: Snowflake, payload: Dict[str, Any], file: File, reason: Optional[str]) -> Response[sticker.GuildSticker]: ...
    def modify_guild_sticker(self, guild_id: Snowflake, sticker_id: Snowflake, payload: Dict[str, Any], reason: Optional[str]) -> Response[sticker.GuildSticker]: ...
    def delete_guild_sticker(self, guild_id: Snowflake, sticker_id: Snowflake, reason: Optional[str]) -> Response[None]: ...
    def get_all_custom_emojis(self, guild_id: Snowflake) -> Response[List[emoji.Emoji]]: ...
    def get_custom_emoji(self, guild_id: Snowflake, emoji_id: Snowflake) -> Response[emoji.Emoji]: ...
    def create_custom_emoji(self, guild_id: Snowflake, name: str, image: str, *, roles: Optional[SnowflakeList] = ..., reason: Optional[str] = ...) -> Response[emoji.Emoji]: ...
    def delete_custom_emoji(self, guild_id: Snowflake, emoji_id: Snowflake, *, reason: Optional[str] = ...) -> Response[None]: ...
    def edit_custom_emoji(self, guild_id: Snowflake, emoji_id: Snowflake, *, payload: Dict[str, Any], reason: Optional[str] = ...) -> Response[emoji.Emoji]: ...
    def get_all_integrations(self, guild_id: Snowflake) -> Response[List[integration.Integration]]: ...
    def create_integration(self, guild_id: Snowflake, type: integration.IntegrationType, id: int) -> Response[None]: ...
    def edit_integration(self, guild_id: Snowflake, integration_id: Snowflake, **payload: Any) -> Response[None]: ...
    def sync_integration(self, guild_id: Snowflake, integration_id: Snowflake) -> Response[None]: ...
    def delete_integration(self, guild_id: Snowflake, integration_id: Snowflake, *, reason: Optional[str] = ...) -> Response[None]: ...
    def get_audit_logs(self, guild_id: Snowflake, limit: int = ..., before: Optional[Snowflake] = ..., after: Optional[Snowflake] = ..., user_id: Optional[Snowflake] = ..., action_type: Optional[AuditLogAction] = ...) -> Response[audit_log.AuditLog]: ...
    def get_widget(self, guild_id: Snowflake) -> Response[widget.Widget]: ...
    def edit_widget(self, guild_id: Snowflake, payload: widget.EditWidgetSettings, reason: Optional[str] = ...) -> Response[widget.WidgetSettings]: ...
    def create_invite(self, channel_id: Snowflake, *, reason: Optional[str] = ..., max_age: int = ..., max_uses: int = ..., temporary: bool = ..., unique: bool = ..., target_type: Optional[invite.InviteTargetType] = ..., target_user_id: Optional[Snowflake] = ..., target_application_id: Optional[Snowflake] = ...) -> Response[invite.Invite]: ...
    def get_invite(self, invite_id: str, *, with_counts: bool = ..., with_expiration: bool = ..., guild_scheduled_event_id: Optional[Snowflake] = ...) -> Response[invite.Invite]: ...
    def invites_from(self, guild_id: Snowflake) -> Response[List[invite.Invite]]: ...
    def invites_from_channel(self, channel_id: Snowflake) -> Response[List[invite.Invite]]: ...
    def delete_invite(self, invite_id: str, *, reason: Optional[str] = ...) -> Response[None]: ...
    def get_roles(self, guild_id: Snowflake) -> Response[List[role.Role]]: ...
    def edit_role(self, guild_id: Snowflake, role_id: Snowflake, *, reason: Optional[str] = ..., **fields: Any) -> Response[role.Role]: ...
    def delete_role(self, guild_id: Snowflake, role_id: Snowflake, *, reason: Optional[str] = ...) -> Response[None]: ...
    def replace_roles(self, user_id: Snowflake, guild_id: Snowflake, role_ids: List[int], *, reason: Optional[str] = ...) -> Response[member.MemberWithUser]: ...
    def create_role(self, guild_id: Snowflake, *, reason: Optional[str] = ..., **fields: Any) -> Response[role.Role]: ...
    def move_role_position(self, guild_id: Snowflake, positions: List[guild.RolePositionUpdate], *, reason: Optional[str] = ...) -> Response[List[role.Role]]: ...
    def add_role(self, guild_id: Snowflake, user_id: Snowflake, role_id: Snowflake, *, reason: Optional[str] = ...) -> Response[None]: ...
    def remove_role(self, guild_id: Snowflake, user_id: Snowflake, role_id: Snowflake, *, reason: Optional[str] = ...) -> Response[None]: ...
    def edit_channel_permissions(self, channel_id: Snowflake, target: Snowflake, allow: str, deny: str, type: channel.OverwriteType, *, reason: Optional[str] = ...) -> Response[None]: ...
    def delete_channel_permissions(self, channel_id: Snowflake, target: Snowflake, *, reason: Optional[str] = ...) -> Response[None]: ...
    def move_member(self, user_id: Snowflake, guild_id: Snowflake, channel_id: Snowflake, *, reason: Optional[str] = ...) -> Response[member.MemberWithUser]: ...
    def get_stage_instance(self, channel_id: Snowflake) -> Response[channel.StageInstance]: ...
    def create_stage_instance(self, *, reason: Optional[str], **payload: Any) -> Response[channel.StageInstance]: ...
    def edit_stage_instance(self, channel_id: Snowflake, *, reason: Optional[str] = ..., **payload: Any) -> Response[None]: ...
    def delete_stage_instance(self, channel_id: Snowflake, *, reason: Optional[str] = ...) -> Response[None]: ...
    @overload
    def get_scheduled_events(self, guild_id: Snowflake, with_user_count: Literal[True]) -> Response[List[scheduled_event.GuildScheduledEventWithUserCount]]: ...
    @overload
    def get_scheduled_events(self, guild_id: Snowflake, with_user_count: Literal[False]) -> Response[List[scheduled_event.GuildScheduledEvent]]: ...
    @overload
    def get_scheduled_events(self, guild_id: Snowflake, with_user_count: bool) -> Union[Response[List[scheduled_event.GuildScheduledEventWithUserCount]], Response[List[scheduled_event.GuildScheduledEvent]]]: ...
    def create_guild_scheduled_event(self, guild_id: Snowflake, *, reason: Optional[str] = ..., **payload: Any) -> Response[scheduled_event.GuildScheduledEvent]: ...
    @overload
    def get_scheduled_event(self, guild_id: Snowflake, guild_scheduled_event_id: Snowflake, with_user_count: Literal[True]) -> Response[scheduled_event.GuildScheduledEventWithUserCount]: ...
    @overload
    def get_scheduled_event(self, guild_id: Snowflake, guild_scheduled_event_id: Snowflake, with_user_count: Literal[False]) -> Response[scheduled_event.GuildScheduledEvent]: ...
    @overload
    def get_scheduled_event(self, guild_id: Snowflake, guild_scheduled_event_id: Snowflake, with_user_count: bool) -> Union[Response[scheduled_event.GuildScheduledEventWithUserCount], Response[scheduled_event.GuildScheduledEvent]]: ...
    def edit_scheduled_event(self, guild_id: Snowflake, guild_scheduled_event_id: Snowflake, *, reason: Optional[str] = ..., **payload: Any) -> Response[scheduled_event.GuildScheduledEvent]: ...
    def delete_scheduled_event(self, guild_id: Snowflake, guild_scheduled_event_id: Snowflake, *, reason: Optional[str] = ...) -> Response[None]: ...
    @overload
    def get_scheduled_event_users(self, guild_id: Snowflake, guild_scheduled_event_id: Snowflake, limit: int, with_member: Literal[True], before: Optional[Snowflake] = ..., after: Optional[Snowflake] = ...) -> Response[scheduled_event.ScheduledEventUsersWithMember]: ...
    @overload
    def get_scheduled_event_users(self, guild_id: Snowflake, guild_scheduled_event_id: Snowflake, limit: int, with_member: Literal[False], before: Optional[Snowflake] = ..., after: Optional[Snowflake] = ...) -> Response[scheduled_event.ScheduledEventUsers]: ...
    @overload
    def get_scheduled_event_users(self, guild_id: Snowflake, guild_scheduled_event_id: Snowflake, limit: int, with_member: bool, before: Optional[Snowflake] = ..., after: Optional[Snowflake] = ...) -> Union[Response[scheduled_event.ScheduledEventUsersWithMember], Response[scheduled_event.ScheduledEventUsers]]: ...
    def get_global_commands(self, application_id: Snowflake) -> Response[List[command.ApplicationCommand]]: ...
    def get_global_command(self, application_id: Snowflake, command_id: Snowflake) -> Response[command.ApplicationCommand]: ...
    def upsert_global_command(self, application_id: Snowflake, payload: command.ApplicationCommand) -> Response[command.ApplicationCommand]: ...
    def edit_global_command(self, application_id: Snowflake, command_id: Snowflake, payload: Dict[str, Any]) -> Response[command.ApplicationCommand]: ...
    def delete_global_command(self, application_id: Snowflake, command_id: Snowflake) -> Response[None]: ...
    def bulk_upsert_global_commands(self, application_id: Snowflake, payload: List[Dict[str, Any]]) -> Response[List[command.ApplicationCommand]]: ...
    def get_guild_commands(self, application_id: Snowflake, guild_id: Snowflake) -> Response[List[command.ApplicationCommand]]: ...
    def get_guild_command(self, application_id: Snowflake, guild_id: Snowflake, command_id: Snowflake) -> Response[command.ApplicationCommand]: ...
    def upsert_guild_command(self, application_id: Snowflake, guild_id: Snowflake, payload: Dict[str, Any]) -> Response[command.ApplicationCommand]: ...
    def edit_guild_command(self, application_id: Snowflake, guild_id: Snowflake, command_id: Snowflake, payload: Dict[str, Any]) -> Response[command.ApplicationCommand]: ...
    def delete_guild_command(self, application_id: Snowflake, guild_id: Snowflake, command_id: Snowflake) -> Response[None]: ...
    def bulk_upsert_guild_commands(self, application_id: Snowflake, guild_id: Snowflake, payload: List[Dict[str, Any]]) -> Response[List[command.ApplicationCommand]]: ...
    def get_guild_application_command_permissions(self, application_id: Snowflake, guild_id: Snowflake) -> Response[List[command.GuildApplicationCommandPermissions]]: ...
    def get_application_command_permissions(self, application_id: Snowflake, guild_id: Snowflake, command_id: Snowflake) -> Response[command.GuildApplicationCommandPermissions]: ...
    def edit_application_command_permissions(self, application_id: Snowflake, guild_id: Snowflake, command_id: Snowflake, payload: Dict[str, Any]) -> Response[None]: ...
    def bulk_edit_guild_application_command_permissions(self, application_id: Snowflake, guild_id: Snowflake, payload: List[Dict[str, Any]]) -> Response[None]: ...
    def application_info(self) -> Response[appinfo.AppInfo]: ...
    async def get_gateway(self, *, encoding: str = ..., zlib: bool = ...) -> str: ...
    async def get_bot_gateway(self, *, encoding: str = ..., zlib: bool = ...) -> Tuple[int, str]: ...
    def get_user(self, user_id: Snowflake) -> Response[user.User]: ...
