from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_11.models.roughness import Roughness as _PrevRoughness


class Roughness(_PrevRoughness):
    def __init__(self, roughness: str = "0.5"):
        super().__init__(roughness=roughness)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Roughness":
        _base = _PrevRoughness.from_sdf(el)
        return cls(roughness=_base.roughness)
