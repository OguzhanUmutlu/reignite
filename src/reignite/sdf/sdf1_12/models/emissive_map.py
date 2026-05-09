from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_11.models.emissive_map import EmissiveMap as _PrevEmissiveMap


class EmissiveMap(_PrevEmissiveMap):
    def __init__(self, emissive_map: str = ""):
        super().__init__(emissive_map=emissive_map)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "EmissiveMap":
        _base = _PrevEmissiveMap.from_sdf(el)
        return cls(emissive_map=_base.emissive_map)
