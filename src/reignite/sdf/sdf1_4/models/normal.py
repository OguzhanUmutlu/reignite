from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class Normal(Model):
    def __init__(self, normal: str = "__default__"):
        self.normal = normal

    def to_sdf(self) -> ET.Element:
        el = ET.Element("normal")
        if self.normal is not None:
            el.text = self.normal
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Normal":
        _text = el.text or "__default__"
        _normal = _text
        return cls(normal=_normal)
