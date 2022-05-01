from .errors import DiscordException
from typing import Generator, IO, Tuple

class OggError(DiscordException): ...

class OggPage:
    flag: int
    gran_pos: int
    serial: int
    pagenum: int
    crc: int
    segnum: int
    segtable: bytes
    data: bytes
    def __init__(self, stream: IO[bytes]) -> None: ...
    def iter_packets(self) -> Generator[Tuple[bytes, bool], None, None]: ...

class OggStream:
    stream: IO[bytes]
    def __init__(self, stream: IO[bytes]) -> None: ...
    def iter_packets(self) -> Generator[bytes, None, None]: ...
