from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_6.models.metalness import Metalness as _PrevMetalness


class Metalness(_PrevMetalness):
    def __init__(self, metalness: str = "0.5"):
        super().__init__(metalness=metalness)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Metalness":
        _base = _PrevMetalness.from_sdf(el)
        return cls(metalness=_base.metalness)
