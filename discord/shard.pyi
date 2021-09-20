import asyncio
from .activity import BaseActivity
from .client import Client
from .enums import Status
from typing import Any, Dict, List, Optional, Tuple

class ShardInfo:
    id: int
    shard_count: Optional[int]
    def is_closed(self) -> bool: ...
    async def disconnect(self) -> None: ...
    async def reconnect(self) -> None: ...
    async def connect(self) -> None: ...
    @property
    def latency(self) -> float: ...
    def is_ws_ratelimited(self) -> bool: ...

class AutoShardedClient(Client):
    shard_ids: Optional[List[int]]
    def __init__(self, *args: Any, loop: Optional[asyncio.AbstractEventLoop] = ..., **kwargs: Any): ...
    @property
    def latency(self) -> float: ...
    @property
    def latencies(self) -> List[Tuple[int, float]]: ...
    def get_shard(self, shard_id: int) -> Optional[ShardInfo]: ...
    @property
    def shards(self) -> Dict[int, ShardInfo]: ...
    async def launch_shard(self, gateway: str, shard_id: int, *, initial: bool = ...) -> None: ...
    async def launch_shards(self) -> None: ...
    async def connect(self, *, reconnect: bool = ...) -> None: ...
    async def close(self) -> None: ...
    async def change_presence(self, *, activity: Optional[BaseActivity] = ..., status: Optional[Status] = ..., shard_id: int = ...) -> None: ...
    def is_ws_ratelimited(self) -> bool: ...