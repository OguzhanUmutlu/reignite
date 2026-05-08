from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_0.models.pos import Pos as _PrevPos
from ...sdf1_0.models.wrench import Wrench as _PrevWrench
from ....utils.vector3 import Vector3
from .mag import Mag


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


class Wrench(_PrevWrench):
    def __init__(self, pos: "Pos" = None, mag: "Mag" = None):
        super().__init__(pos=pos, mag=mag)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Wrench":
        _base = _PrevWrench.from_sdf(el)
        return cls(pos=_base.pos, mag=_base.mag)
