from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from .normal_map import NormalMap


class Shader(Model):
    def __init__(self, type: str = "pixel", normal_map: "NormalMap" = None):
        self.type = type
        self.normal_map = normal_map

    def to_sdf(self) -> ET.Element:
        el = ET.Element("shader")
        if self.type is not None:
            el.set("type", self.type)
        if self.normal_map is not None:
            el.append(self.normal_map.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Shader":
        _type = el.get("type", "pixel")
        _c_normal_map = el.find("normal_map")
        _normal_map = NormalMap.from_sdf(_c_normal_map) if _c_normal_map is not None else None
        return cls(type=_type, normal_map=_normal_map)
