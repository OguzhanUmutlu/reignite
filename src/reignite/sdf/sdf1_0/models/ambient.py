from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ....utils.color import Color


class Ambient(Model):
    def __init__(self, rgba: Color = None):
        if rgba is None:
            rgba = Color.from_sdf("0 0 0 1")
        self.rgba = rgba

    def to_sdf(self) -> ET.Element:
        el = ET.Element("ambient")
        if self.rgba is not None:
            el.set("rgba", self.rgba.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Ambient":
        _rgba = Color.from_sdf(el.get("rgba", "0 0 0 1"))
        return cls(rgba=_rgba)
