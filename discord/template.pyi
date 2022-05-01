import datetime
from .guild import Guild
from .state import ConnectionState
from .types.template import Template as TemplatePayload
from .user import User
from typing import Any, Optional

class Template:
    code: str
    uses: int
    name: str
    description: Optional[str]
    creator: Optional[User]
    created_at: Optional[datetime.datetime]
    updated_at: Optional[datetime.datetime]
    source_guild: Guild
    is_dirty: Optional[bool]
    def __init__(self, *, state: ConnectionState, data: TemplatePayload) -> None: ...
    async def create_guild(self, name: str, icon: bytes = ...) -> Guild: ...
    async def sync(self) -> Template: ...
    async def edit(self, *, name: str = ..., description: Optional[str] = ...) -> Template: ...
    async def delete(self) -> None: ...
    @property
    def url(self) -> str: ...
