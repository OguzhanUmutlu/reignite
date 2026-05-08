from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ....utils.vector3 import Vector3


class Point(Model):
    def __init__(self, point: Vector3 = None):
        if point is None:
            point = Vector3.from_sdf("0 0 0")
        self.point = point

    def to_sdf(self) -> ET.Element:
        el = ET.Element("point")
        if self.point is not None:
            el.text = self.point.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Point":
        _text = el.text or "0 0 0"
        _point = Vector3.from_sdf(_text)
        return cls(point=_point)
