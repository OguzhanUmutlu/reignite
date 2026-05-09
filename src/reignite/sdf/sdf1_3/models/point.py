from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_2.models.point import Point as _PrevPoint
from ....utils.vector3 import Vector3


class Point(_PrevPoint):
    def __init__(self, point: Vector3 = None):
        if point is None:
            point = Vector3.from_sdf("0 0 0")
        super().__init__(point=point)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Point":
        _base = _PrevPoint.from_sdf(el)
        return cls(point=_base.point)
