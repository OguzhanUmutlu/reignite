from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_0.models.emissive import Emissive as _PrevEmissive
from ....utils.color import Color


class Emissive(_PrevEmissive):
    def __init__(self, emissive: Color = None):
        if emissive is None:
            emissive = Color.from_sdf("0 0 0 1")
        super().__init__()
        self.emissive = emissive

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.emissive is not None:
            el.text = self.emissive.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Emissive":
        _text = el.text or "0 0 0 1"
        _emissive = Color.from_sdf(_text)
        return cls(emissive=_emissive)
