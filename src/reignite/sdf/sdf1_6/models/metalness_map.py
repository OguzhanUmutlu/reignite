from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class MetalnessMap(Model):
    def __init__(self, metalness_map: str = ""):
        self.metalness_map = metalness_map

    def to_sdf(self) -> ET.Element:
        el = ET.Element("metalness_map")
        if self.metalness_map is not None:
            el.text = self.metalness_map
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "MetalnessMap":
        _text = el.text or ""
        _metalness_map = _text
        return cls(metalness_map=_metalness_map)
