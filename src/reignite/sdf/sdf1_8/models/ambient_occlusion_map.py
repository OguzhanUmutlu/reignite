from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_7.models.ambient_occlusion_map import AmbientOcclusionMap as _PrevAmbientOcclusionMap


class AmbientOcclusionMap(_PrevAmbientOcclusionMap):
    def __init__(self, ambient_occlusion_map: str = ""):
        super().__init__(ambient_occlusion_map=ambient_occlusion_map)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "AmbientOcclusionMap":
        _base = _PrevAmbientOcclusionMap.from_sdf(el)
        return cls(ambient_occlusion_map=_base.ambient_occlusion_map)
