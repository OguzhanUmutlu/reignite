from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_10.models.metalness_map import MetalnessMap as _PrevMetalnessMap


class MetalnessMap(_PrevMetalnessMap):
    def __init__(self, metalness_map: str = ""):
        super().__init__(metalness_map=metalness_map)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "MetalnessMap":
        _base = _PrevMetalnessMap.from_sdf(el)
        return cls(metalness_map=_base.metalness_map)
