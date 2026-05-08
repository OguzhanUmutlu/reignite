from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class Diffuse(Model):
    def __init__(self, diffuse: str = "__default__"):
        self.diffuse = diffuse

    def to_sdf(self) -> ET.Element:
        el = ET.Element("diffuse")
        if self.diffuse is not None:
            el.text = self.diffuse
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Diffuse":
        _text = el.text or "__default__"
        _diffuse = _text
        return cls(diffuse=_diffuse)
