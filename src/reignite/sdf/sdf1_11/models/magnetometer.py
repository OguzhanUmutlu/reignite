from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_10.models.magnetometer import Magnetometer as _PrevMagnetometer
from .x import X
from .y import Y
from .z import Z


class Magnetometer(_PrevMagnetometer):
    def __init__(self, x: "X" = None, y: "Y" = None, z: "Z" = None):
        super().__init__(x=x, y=y, z=z)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Magnetometer":
        _base = _PrevMagnetometer.from_sdf(el)
        return cls(x=_base.x, y=_base.y, z=_base.z)
