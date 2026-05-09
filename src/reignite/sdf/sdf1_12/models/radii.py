from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_11.models.radii import Radii as _PrevRadii
from ....utils.vector3 import Vector3


class Radii(_PrevRadii):
    def __init__(self, radii: Vector3 = None):
        if radii is None:
            radii = Vector3.from_sdf("1 1 1")
        super().__init__(radii=radii)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Radii":
        _base = _PrevRadii.from_sdf(el)
        return cls(radii=_base.radii)
