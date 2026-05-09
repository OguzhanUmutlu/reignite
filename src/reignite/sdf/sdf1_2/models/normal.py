from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_0.models.normal import Normal as _PrevNormal
from ....utils.vector3 import Vector3


class Normal(_PrevNormal):
    def __init__(self, normal: Vector3 = None):
        if normal is None:
            normal = Vector3.from_sdf("0 0 1")
        super().__init__(normal=normal)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Normal":
        _base = _PrevNormal.from_sdf(el)
        return cls(normal=_base.normal)
