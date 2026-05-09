from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_10.models.normal import Normal as _PrevNormal


class Normal(_PrevNormal):
    def __init__(self, normal: str = "__default__"):
        super().__init__(normal=normal)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Normal":
        _base = _PrevNormal.from_sdf(el)
        return cls(normal=_base.normal)
