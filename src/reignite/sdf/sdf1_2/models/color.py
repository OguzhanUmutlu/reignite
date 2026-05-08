from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ....utils.color import Color


class Color(Model):
    def __init__(self, color: Color = None):
        if color is None:
            color = Color.from_sdf("1 1 1 1")
        self.color = color

    def to_sdf(self) -> ET.Element:
        el = ET.Element("color")
        if self.color is not None:
            el.text = self.color.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Color":
        _text = el.text or "1 1 1 1"
        _color = Color.from_sdf(_text)
        return cls(color=_color)
