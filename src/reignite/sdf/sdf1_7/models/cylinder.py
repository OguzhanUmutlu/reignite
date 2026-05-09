from __future__ import annotations

from xml.etree import ElementTree as ET

from .length import Length
from .radius import Radius
from ...sdf1_6.models.cylinder import Cylinder as _PrevCylinder


class Cylinder(_PrevCylinder):
    def __init__(self, radius: "Radius" = None, length: "Length" = None):
        super().__init__(radius=radius, length=length)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Cylinder":
        _base = _PrevCylinder.from_sdf(el)
        return cls(radius=_base.radius, length=_base.length)
