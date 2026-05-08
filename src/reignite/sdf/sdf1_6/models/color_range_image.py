from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class ColorRangeImage(Model):
    def __init__(self, color_range_image: str = ""):
        self.color_range_image = color_range_image

    def to_sdf(self) -> ET.Element:
        el = ET.Element("color_range_image")
        if self.color_range_image is not None:
            el.text = self.color_range_image
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "ColorRangeImage":
        _text = el.text or ""
        _color_range_image = _text
        return cls(color_range_image=_color_range_image)
