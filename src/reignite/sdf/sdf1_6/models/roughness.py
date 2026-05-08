from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class Roughness(Model):
    def __init__(self, roughness: str = "0.5"):
        self.roughness = roughness

    def to_sdf(self) -> ET.Element:
        el = ET.Element("roughness")
        if self.roughness is not None:
            el.text = self.roughness
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Roughness":
        _text = el.text or "0.5"
        _roughness = _text
        return cls(roughness=_roughness)
