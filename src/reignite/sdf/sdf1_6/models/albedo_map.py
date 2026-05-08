from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class AlbedoMap(Model):
    def __init__(self, albedo_map: str = ""):
        self.albedo_map = albedo_map

    def to_sdf(self) -> ET.Element:
        el = ET.Element("albedo_map")
        if self.albedo_map is not None:
            el.text = self.albedo_map
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "AlbedoMap":
        _text = el.text or ""
        _albedo_map = _text
        return cls(albedo_map=_albedo_map)
