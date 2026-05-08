from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_7.models.normal_map import NormalMap as _PrevNormalMap


class NormalMap(_PrevNormalMap):
    def __init__(self, normal_map: str = "__default__"):
        super().__init__(normal_map=normal_map)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "NormalMap":
        _base = _PrevNormalMap.from_sdf(el)
        return cls(normal_map=_base.normal_map)
