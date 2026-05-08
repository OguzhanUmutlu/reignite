from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class Format(Model):
    def __init__(self, format: str = "R8G8B8"):
        self.format = format

    def to_sdf(self) -> ET.Element:
        el = ET.Element("format")
        if self.format is not None:
            el.text = self.format
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Format":
        _text = el.text or "R8G8B8"
        _format = _text
        return cls(format=_format)
