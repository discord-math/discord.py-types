import ctypes.util
from .errors import DiscordException
from typing import Literal, TypeVar, TypedDict, overload

T = TypeVar('T')
BAND_CTL = Literal['narrow', 'medium', 'wide', 'superwide', 'full']
SIGNAL_CTL = Literal['auto', 'voice', 'music']

class BandCtl(TypedDict):
    narrow: int
    medium: int
    wide: int
    superwide: int
    full: int

class SignalCtl(TypedDict):
    auto: int
    voice: int
    music: int

class EncoderStruct(ctypes.Structure): ...
class DecoderStruct(ctypes.Structure): ...

class OpusError(DiscordException):
    code: int
    def __init__(self, code: int) -> None: ...

class OpusNotLoaded(DiscordException): ...

class _OpusStruct:
    SAMPLING_RATE: int
    CHANNELS: int
    FRAME_LENGTH: int
    SAMPLE_SIZE: int
    SAMPLES_PER_FRAME: int
    FRAME_SIZE: int
    @staticmethod
    def get_opus_version() -> str: ...

class Encoder(_OpusStruct):
    application: int
    def __init__(self, application: int = ...) -> None: ...
    def __del__(self) -> None: ...
    def set_bitrate(self, kbps: int) -> int: ...
    def set_bandwidth(self, req: BAND_CTL) -> None: ...
    def set_signal_type(self, req: SIGNAL_CTL) -> None: ...
    def set_fec(self, enabled: bool = ...) -> None: ...
    def set_expected_packet_loss_percent(self, percentage: float) -> None: ...
    def encode(self, pcm: bytes, frame_size: int) -> bytes: ...

class Decoder(_OpusStruct):
    def __init__(self) -> None: ...
    def __del__(self) -> None: ...
    @staticmethod
    def packet_get_nb_frames(data: bytes) -> int: ...
    @staticmethod
    def packet_get_nb_channels(data: bytes) -> int: ...
    @classmethod
    def packet_get_samples_per_frame(cls, data: bytes) -> int: ...
    def set_gain(self, dB: float) -> int: ...
    def set_volume(self, mult: float) -> int: ...
    @overload
    def decode(self, data: bytes, *, fec: bool) -> bytes: ...
    @overload
    def decode(self, data: Literal[None], *, fec: Literal[False]) -> bytes: ...
