from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class EmissiveMap(Model):
    def __init__(self, emissive_map: str = ""):
        self.emissive_map = emissive_map

    def to_sdf(self) -> ET.Element:
        el = ET.Element("emissive_map")
        if self.emissive_map is not None:
            el.text = self.emissive_map
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "EmissiveMap":
        _text = el.text or ""
        _emissive_map = _text
        return cls(emissive_map=_emissive_map)
