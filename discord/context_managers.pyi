import asyncio
from .abc import Messageable
from types import TracebackType
from typing import Optional, Type, TypeVar

BE = TypeVar('BE', bound=BaseException)

class Typing:
    loop: asyncio.AbstractEventLoop
    messageable: Messageable
    def __init__(self, messageable: Messageable) -> None: ...
    async def do_typing(self) -> None: ...
    task: asyncio.Task[None]
    async def __aenter__(self) -> None: ...
    async def __aexit__(self, exc_type: Optional[Type[BE]], exc: Optional[BE], traceback: Optional[TracebackType]) -> None: ...
