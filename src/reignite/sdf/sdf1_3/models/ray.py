from __future__ import annotations

from xml.etree import ElementTree as ET

from .range import Range
from .scan import Scan
from ...sdf1_2.models.ray import Ray as _PrevRay


class Ray(_PrevRay):
    def __init__(self, scan: "Scan" = None, range: "Range" = None):
        super().__init__(scan=scan, range=range)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Ray":
        _base = _PrevRay.from_sdf(el)
        return cls(scan=_base.scan, range=_base.range)
