from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class Type(Model):
    def __init__(self, type: str = "quick"):
        self.type = type

    def to_sdf(self) -> ET.Element:
        el = ET.Element("type")
        if self.type is not None:
            el.text = self.type
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Type":
        _text = el.text or "quick"
        _type = _text
        return cls(type=_type)
