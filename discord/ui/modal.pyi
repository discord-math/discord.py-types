from ..interactions import Interaction
from .item import Item
from .view import View
from typing import Any, ClassVar, Dict, Optional

class Modal(View):
    title: str
    __discord_ui_modal__ = True
    __modal_children_items__: ClassVar[Dict[str, Item[Modal]]]
    def __init_subclass__(cls, *, title: str = ...) -> None: ...
    custom_id: str
    def __init__(self, *, title: str = ..., timeout: Optional[float] = ..., custom_id: str = ...) -> None: ...
    async def on_submit(self, interaction: Interaction) -> None: ...
    async def on_error(self, error: Exception, interaction: Interaction) -> None: ... # type: ignore
    def to_dict(self) -> Dict[str, Any]: ...
