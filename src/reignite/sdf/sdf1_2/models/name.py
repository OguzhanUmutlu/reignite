from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class Name(Model):
    def __init__(self, name: str = "__default__"):
        self.name = name

    def to_sdf(self) -> ET.Element:
        el = ET.Element("name")
        if self.name is not None:
            el.text = self.name
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Name":
        _text = el.text or "__default__"
        _name = _text
        return cls(name=_name)
