from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class RoughnessMap(Model):
    def __init__(self, roughness_map: str = ""):
        self.roughness_map = roughness_map

    def to_sdf(self) -> ET.Element:
        el = ET.Element("roughness_map")
        if self.roughness_map is not None:
            el.text = self.roughness_map
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "RoughnessMap":
        _text = el.text or ""
        _roughness_map = _text
        return cls(roughness_map=_roughness_map)
