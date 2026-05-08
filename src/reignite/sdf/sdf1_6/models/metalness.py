from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class Metalness(Model):
    def __init__(self, metalness: str = "0.5"):
        self.metalness = metalness

    def to_sdf(self) -> ET.Element:
        el = ET.Element("metalness")
        if self.metalness is not None:
            el.text = self.metalness
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Metalness":
        _text = el.text or "0.5"
        _metalness = _text
        return cls(metalness=_metalness)
