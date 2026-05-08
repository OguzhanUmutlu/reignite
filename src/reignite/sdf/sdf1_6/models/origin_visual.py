from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_5.models.origin_visual import OriginVisual as _PrevOriginVisual


class OriginVisual(_PrevOriginVisual):
    def __init__(self, origin_visual: bool = True):
        super().__init__(origin_visual=origin_visual)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "OriginVisual":
        _base = _PrevOriginVisual.from_sdf(el)
        return cls(origin_visual=_base.origin_visual)
