from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_11.models.emissive import Emissive as _PrevEmissive
from ....utils.color import Color


class Emissive(_PrevEmissive):
    def __init__(self, emissive: Color = None):
        if emissive is None:
            emissive = Color.from_sdf("0 0 0 1")
        super().__init__(emissive=emissive)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Emissive":
        _base = _PrevEmissive.from_sdf(el)
        return cls(emissive=_base.emissive)
