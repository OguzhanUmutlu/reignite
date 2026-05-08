from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_5.models.use_parent_model_frame import UseParentModelFrame as _PrevUseParentModelFrame


class UseParentModelFrame(_PrevUseParentModelFrame):
    def __init__(self, use_parent_model_frame: bool = False):
        super().__init__(use_parent_model_frame=use_parent_model_frame)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "UseParentModelFrame":
        _base = _PrevUseParentModelFrame.from_sdf(el)
        return cls(use_parent_model_frame=_base.use_parent_model_frame)
