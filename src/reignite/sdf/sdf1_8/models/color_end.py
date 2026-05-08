from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_7.models.color_end import ColorEnd as _PrevColorEnd
from ....utils.color import Color


class ColorEnd(_PrevColorEnd):
    def __init__(self, color_end: Color = None):
        if color_end is None:
            color_end = Color.from_sdf("1 1 1 1")
        super().__init__(color_end=color_end)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "ColorEnd":
        _base = _PrevColorEnd.from_sdf(el)
        return cls(color_end=_base.color_end)
