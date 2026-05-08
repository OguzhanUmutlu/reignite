from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_6.models.direction import Direction as _PrevDirection
from ....utils.vector3 import Vector3


class Direction(_PrevDirection):
    def __init__(self, direction: Vector3 = None):
        if direction is None:
            direction = Vector3.from_sdf("0 0 -1")
        super().__init__(direction=direction)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Direction":
        _base = _PrevDirection.from_sdf(el)
        return cls(direction=_base.direction)
