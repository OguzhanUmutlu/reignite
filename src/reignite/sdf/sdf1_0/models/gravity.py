from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ....utils.vector3 import Vector3


class Gravity(Model):
    def __init__(self, xyz: Vector3 = None):
        if xyz is None:
            xyz = Vector3.from_sdf("0 0 -9.8")
        self.xyz = xyz

    def to_sdf(self) -> ET.Element:
        el = ET.Element("gravity")
        if self.xyz is not None:
            el.set("xyz", self.xyz.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Gravity":
        _xyz = Vector3.from_sdf(el.get("xyz", "0 0 -9.8"))
        return cls(xyz=_xyz)
