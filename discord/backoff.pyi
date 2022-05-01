from typing import Generic, Literal, TypeVar, Union, overload

T = TypeVar('T', bool, Literal[True], Literal[False])

class ExponentialBackoff(Generic[T]):
    def __init__(self, base: int = ..., *, integral: T = ...) -> None: ...
    @overload
    def delay(self: ExponentialBackoff[Literal[False]]) -> float: ...
    @overload
    def delay(self: ExponentialBackoff[Literal[True]]) -> int: ... # type: ignore
    @overload
    def delay(self) -> Union[int, float]: ...
