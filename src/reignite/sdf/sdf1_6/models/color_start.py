from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ....utils.color import Color


class ColorStart(Model):
    def __init__(self, color_start: Color = None):
        if color_start is None:
            color_start = Color.from_sdf("1 1 1 1")
        self.color_start = color_start

    def to_sdf(self) -> ET.Element:
        el = ET.Element("color_start")
        if self.color_start is not None:
            el.text = self.color_start.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "ColorStart":
        _text = el.text or "1 1 1 1"
        _color_start = Color.from_sdf(_text)
        return cls(color_start=_color_start)
