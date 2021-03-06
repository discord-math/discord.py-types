from typing import Optional, Tuple, Type, TypeVar, Union

C = TypeVar('C', bound='Colour')

class Colour:
    value: int
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
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
    def from_rgb(cls: Type[C], r: int, g: int, b: int) -> C: ...
    @classmethod
    def from_hsv(cls: Type[C], h: float, s: float, v: float) -> C: ...
    @classmethod
    def from_str(cls: Type[C], value: str) -> C: ...
    @classmethod
    def default(cls: Type[C]) -> C: ...
    @classmethod
    def random(cls: Type[C], *, seed: Optional[Union[int, str, float, bytes, bytearray]] = ...) -> C: ...
    @classmethod
    def teal(cls: Type[C]) -> C: ...
    @classmethod
    def dark_teal(cls: Type[C]) -> C: ...
    @classmethod
    def brand_green(cls: Type[C]) -> C: ...
    @classmethod
    def green(cls: Type[C]) -> C: ...
    @classmethod
    def dark_green(cls: Type[C]) -> C: ...
    @classmethod
    def blue(cls: Type[C]) -> C: ...
    @classmethod
    def dark_blue(cls: Type[C]) -> C: ...
    @classmethod
    def purple(cls: Type[C]) -> C: ...
    @classmethod
    def dark_purple(cls: Type[C]) -> C: ...
    @classmethod
    def magenta(cls: Type[C]) -> C: ...
    @classmethod
    def dark_magenta(cls: Type[C]) -> C: ...
    @classmethod
    def gold(cls: Type[C]) -> C: ...
    @classmethod
    def dark_gold(cls: Type[C]) -> C: ...
    @classmethod
    def orange(cls: Type[C]) -> C: ...
    @classmethod
    def dark_orange(cls: Type[C]) -> C: ...
    @classmethod
    def brand_red(cls: Type[C]) -> C: ...
    @classmethod
    def red(cls: Type[C]) -> C: ...
    @classmethod
    def dark_red(cls: Type[C]) -> C: ...
    @classmethod
    def lighter_grey(cls: Type[C]) -> C: ...
    @classmethod
    def lighter_gray(cls: Type[C]) -> C: ...
    @classmethod
    def dark_grey(cls: Type[C]) -> C: ...
    @classmethod
    def dark_gray(cls: Type[C]) -> C: ...
    @classmethod
    def light_grey(cls: Type[C]) -> C: ...
    @classmethod
    def light_gray(cls: Type[C]) -> C: ...
    @classmethod
    def darker_grey(cls: Type[C]) -> C: ...
    @classmethod
    def darker_gray(cls: Type[C]) -> C: ...
    @classmethod
    def og_blurple(cls: Type[C]) -> C: ...
    @classmethod
    def blurple(cls: Type[C]) -> C: ...
    @classmethod
    def greyple(cls: Type[C]) -> C: ...
    @classmethod
    def dark_theme(cls: Type[C]) -> C: ...
    @classmethod
    def fuchsia(cls: Type[C]) -> C: ...
    @classmethod
    def yellow(cls: Type[C]) -> C: ...
Color = Colour
