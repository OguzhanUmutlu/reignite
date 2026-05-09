from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_0.models.diffuse import Diffuse as _PrevDiffuse


class Diffuse(_PrevDiffuse):
    def __init__(self, diffuse: str = "__default__"):
        super().__init__()
        self.diffuse = diffuse

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.diffuse is not None:
            el.text = self.diffuse
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Diffuse":
        _text = el.text or "__default__"
        _diffuse = _text
        return cls(diffuse=_diffuse)
