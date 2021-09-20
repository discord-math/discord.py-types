from typing import Any, Optional, Tuple, TypeVar, Union

CT = TypeVar('CT', bound='Colour')

class Colour:
    value: Any
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __int__(self) -> int: ...
    def __hash__(self) -> int: ...
    @property
    def r(self) -> int: ...
    @property
    def g(self) -> int: ...
    @property
    def b(self) -> int: ...
    def to_rgb(self) -> Tuple[int, int, int]: ...
    @classmethod
    def from_rgb(cls, r: int, g: int, b: int) -> CT: ...
    @classmethod
    def from_hsv(cls, h: float, s: float, v: float) -> CT: ...
    @classmethod
    def default(cls) -> CT: ...
    @classmethod
    def random(cls, *, seed: Optional[Union[int, str, float, bytes, bytearray]] = ...) -> CT: ...
    @classmethod
    def teal(cls) -> CT: ...
    @classmethod
    def dark_teal(cls) -> CT: ...
    @classmethod
    def brand_green(cls) -> CT: ...
    @classmethod
    def green(cls) -> CT: ...
    @classmethod
    def dark_green(cls) -> CT: ...
    @classmethod
    def blue(cls) -> CT: ...
    @classmethod
    def dark_blue(cls) -> CT: ...
    @classmethod
    def purple(cls) -> CT: ...
    @classmethod
    def dark_purple(cls) -> CT: ...
    @classmethod
    def magenta(cls) -> CT: ...
    @classmethod
    def dark_magenta(cls) -> CT: ...
    @classmethod
    def gold(cls) -> CT: ...
    @classmethod
    def dark_gold(cls) -> CT: ...
    @classmethod
    def orange(cls) -> CT: ...
    @classmethod
    def dark_orange(cls) -> CT: ...
    @classmethod
    def brand_red(cls) -> CT: ...
    @classmethod
    def red(cls) -> CT: ...
    @classmethod
    def dark_red(cls) -> CT: ...
    @classmethod
    def lighter_grey(cls) -> CT: ...
    @classmethod
    def lighter_gray(cls) -> CT: ...
    @classmethod
    def dark_grey(cls) -> CT: ...
    @classmethod
    def dark_gray(cls) -> CT: ...
    @classmethod
    def light_grey(cls) -> CT: ...
    @classmethod
    def light_gray(cls) -> CT: ...
    @classmethod
    def darker_grey(cls) -> CT: ...
    @classmethod
    def darker_gray(cls) -> CT: ...
    @classmethod
    def og_blurple(cls) -> CT: ...
    @classmethod
    def blurple(cls) -> CT: ...
    @classmethod
    def greyple(cls) -> CT: ...
    @classmethod
    def dark_theme(cls) -> CT: ...
    @classmethod
    def fuchsia(cls) -> CT: ...
    @classmethod
    def yellow(cls) -> CT: ...
Color = Colour