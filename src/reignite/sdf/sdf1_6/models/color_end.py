from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ....utils.color import Color


class ColorEnd(Model):
    def __init__(self, color_end: Color = None):
        if color_end is None:
            color_end = Color.from_sdf("1 1 1 1")
        self.color_end = color_end

    def to_sdf(self) -> ET.Element:
        el = ET.Element("color_end")
        if self.color_end is not None:
            el.text = self.color_end.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "ColorEnd":
        _text = el.text or "1 1 1 1"
        _color_end = Color.from_sdf(_text)
        return cls(color_end=_color_end)
