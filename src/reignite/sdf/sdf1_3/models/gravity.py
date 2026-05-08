from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_2.models.gravity import Gravity as _PrevGravity
from ....utils.vector3 import Vector3


class Gravity(_PrevGravity):
    def __init__(self, gravity: Vector3 = None):
        if gravity is None:
            gravity = Vector3.from_sdf("0 0 -9.8")
        super().__init__(gravity=gravity)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Gravity":
        _base = _PrevGravity.from_sdf(el)
        return cls(gravity=_base.gravity)
