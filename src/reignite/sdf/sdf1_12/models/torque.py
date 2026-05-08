from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_11.models.torque import Torque as _PrevTorque
from .x import X
from .y import Y
from .z import Z


class Torque(_PrevTorque):
    def __init__(self, x: "X" = None, y: "Y" = None, z: "Z" = None):
        super().__init__(x=x, y=y, z=z)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Torque":
        _base = _PrevTorque.from_sdf(el)
        return cls(x=_base.x, y=_base.y, z=_base.z)
