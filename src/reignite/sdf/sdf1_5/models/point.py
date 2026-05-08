from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ....utils.vector2d import Vector2d


class Point(Model):
    def __init__(self, point: Vector2d = None):
        if point is None:
            point = Vector2d.from_sdf("0 0")
        self.point = point

    def to_sdf(self) -> ET.Element:
        el = ET.Element("point")
        if self.point is not None:
            el.text = self.point.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Point":
        _text = el.text or "0 0"
        _point = Vector2d.from_sdf(_text)
        return cls(point=_point)
