from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_5.models.shadows import Shadows as _PrevShadows


class Shadows(_PrevShadows):
    def __init__(self, shadows: bool = True):
        super().__init__(shadows=shadows)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Shadows":
        _base = _PrevShadows.from_sdf(el)
        return cls(shadows=_base.shadows)
