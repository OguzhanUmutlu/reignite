from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class AmbientOcclusionMap(Model):
    def __init__(self, ambient_occlusion_map: str = ""):
        self.ambient_occlusion_map = ambient_occlusion_map

    def to_sdf(self) -> ET.Element:
        el = ET.Element("ambient_occlusion_map")
        if self.ambient_occlusion_map is not None:
            el.text = self.ambient_occlusion_map
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "AmbientOcclusionMap":
        _text = el.text or ""
        _ambient_occlusion_map = _text
        return cls(ambient_occlusion_map=_ambient_occlusion_map)
