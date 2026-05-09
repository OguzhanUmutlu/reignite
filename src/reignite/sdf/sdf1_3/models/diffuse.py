from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_2.models.diffuse import Diffuse as _PrevDiffuse


class Diffuse(_PrevDiffuse):
    def __init__(self, diffuse: str = "__default__"):
        super().__init__(diffuse=diffuse)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Diffuse":
        _base = _PrevDiffuse.from_sdf(el)
        return cls(diffuse=_base.diffuse)
