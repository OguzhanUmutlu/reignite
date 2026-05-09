from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_3.models.color import Color as _PrevColor
from ....utils.color import Color


class Color(_PrevColor):
    def __init__(self, color: Color = None):
        if color is None:
            color = Color.from_sdf("1 1 1 1")
        super().__init__(color=color)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Color":
        _base = _PrevColor.from_sdf(el)
        return cls(color=_base.color)
