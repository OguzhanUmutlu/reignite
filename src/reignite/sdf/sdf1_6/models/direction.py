from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ....utils.vector3 import Vector3


class Direction(Model):
    def __init__(self, direction: Vector3 = None):
        if direction is None:
            direction = Vector3.from_sdf("0 0 -1")
        self.direction = direction

    def to_sdf(self) -> ET.Element:
        el = ET.Element("direction")
        if self.direction is not None:
            el.text = self.direction.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Direction":
        _text = el.text or "0 0 -1"
        _direction = Vector3.from_sdf(_text)
        return cls(direction=_direction)
