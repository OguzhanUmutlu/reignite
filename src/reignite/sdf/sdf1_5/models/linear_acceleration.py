from __future__ import annotations

from xml.etree import ElementTree as ET

from .x import X
from .y import Y
from .z import Z
from ..model import Model


class LinearAcceleration(Model):
    def __init__(self, x: "X" = None, y: "Y" = None, z: "Z" = None):
        self.x = x
        self.y = y
        self.z = z

    def to_sdf(self) -> ET.Element:
        el = ET.Element("linear_acceleration")
        if self.x is not None:
            el.append(self.x.to_sdf())
        if self.y is not None:
            el.append(self.y.to_sdf())
        if self.z is not None:
            el.append(self.z.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "LinearAcceleration":
        _c_x = el.find("x")
        _x = X.from_sdf(_c_x) if _c_x is not None else None
        _c_y = el.find("y")
        _y = Y.from_sdf(_c_y) if _c_y is not None else None
        _c_z = el.find("z")
        _z = Z.from_sdf(_c_z) if _c_z is not None else None
        return cls(x=_x, y=_y, z=_z)
