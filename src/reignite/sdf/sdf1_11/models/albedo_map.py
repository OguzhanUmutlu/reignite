from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_10.models.albedo_map import AlbedoMap as _PrevAlbedoMap


class AlbedoMap(_PrevAlbedoMap):
    def __init__(self, albedo_map: str = ""):
        super().__init__(albedo_map=albedo_map)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "AlbedoMap":
        _base = _PrevAlbedoMap.from_sdf(el)
        return cls(albedo_map=_base.albedo_map)
