from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class BoxType(Model):
    def __init__(self, box_type: str = "2d"):
        self.box_type = box_type

    def to_sdf(self) -> ET.Element:
        el = ET.Element("box_type")
        if self.box_type is not None:
            el.text = self.box_type
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "BoxType":
        _text = el.text or "2d"
        _box_type = _text
        return cls(box_type=_box_type)
