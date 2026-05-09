from __future__ import annotations

from xml.etree import ElementTree as ET

from .x import X
from .y import Y
from .z import Z
from ...sdf1_11.models.linear_acceleration import LinearAcceleration as _PrevLinearAcceleration


class LinearAcceleration(_PrevLinearAcceleration):
    def __init__(self, x: "X" = None, y: "Y" = None, z: "Z" = None):
        super().__init__(x=x, y=y, z=z)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "LinearAcceleration":
        _base = _PrevLinearAcceleration.from_sdf(el)
        return cls(x=_base.x, y=_base.y, z=_base.z)
