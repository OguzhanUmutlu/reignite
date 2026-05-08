from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_10.models.roughness_map import RoughnessMap as _PrevRoughnessMap


class RoughnessMap(_PrevRoughnessMap):
    def __init__(self, roughness_map: str = ""):
        super().__init__(roughness_map=roughness_map)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "RoughnessMap":
        _base = _PrevRoughnessMap.from_sdf(el)
        return cls(roughness_map=_base.roughness_map)
