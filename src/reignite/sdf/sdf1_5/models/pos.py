from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_4.models.pos import Pos as _PrevPos
from ....utils.vector3 import Vector3


class Pos(_PrevPos):
    def __init__(self, pos: Vector3 = None):
        if pos is None:
            pos = Vector3.from_sdf("0 0 0")
        super().__init__(pos=pos)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Pos":
        _base = _PrevPos.from_sdf(el)
        return cls(pos=_base.pos)
