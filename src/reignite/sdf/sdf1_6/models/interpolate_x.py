from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_5.models.interpolate_x import InterpolateX as _PrevInterpolateX


class InterpolateX(_PrevInterpolateX):
    def __init__(self, interpolate_x: bool = False):
        super().__init__(interpolate_x=interpolate_x)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "InterpolateX":
        _base = _PrevInterpolateX.from_sdf(el)
        return cls(interpolate_x=_base.interpolate_x)
