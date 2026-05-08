from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class NormalMap(Model):
    def __init__(self, normal_map: str = "__default__"):
        self.normal_map = normal_map

    def to_sdf(self) -> ET.Element:
        el = ET.Element("normal_map")
        if self.normal_map is not None:
            el.text = self.normal_map
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "NormalMap":
        _text = el.text or "__default__"
        _normal_map = _text
        return cls(normal_map=_normal_map)
