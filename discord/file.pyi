import io
import os
from typing import Optional, Union

class File:
    fp: io.BufferedIOBase
    filename: Optional[str]
    spoiler: bool
    def __init__(self, fp: Union[str, bytes, os.PathLike[str], os.PathLike[bytes], io.BufferedIOBase], filename: Optional[str] = ..., *, spoiler: bool = ...) -> None: ...
    def reset(self, *, seek: Union[int, bool] = ...) -> None: ...
    def close(self) -> None: ...
