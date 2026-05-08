from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ....utils.color import Color


class Background(Model):
    def __init__(self, background: Color = None):
        if background is None:
            background = Color.from_sdf(".7 .7 .7 1")
        self.background = background

    def to_sdf(self) -> ET.Element:
        el = ET.Element("background")
        if self.background is not None:
            el.text = self.background.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Background":
        _text = el.text or ".7 .7 .7 1"
        _background = Color.from_sdf(_text)
        return cls(background=_background)
