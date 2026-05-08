from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ....utils.vector3 import Vector3


class Plane(Model):
    def __init__(self, normal: Vector3 = None):
        if normal is None:
            normal = Vector3.from_sdf("0 0 1")
        self.normal = normal

    def to_sdf(self) -> ET.Element:
        el = ET.Element("plane")
        if self.normal is not None:
            el.set("normal", self.normal.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Plane":
        _normal = Vector3.from_sdf(el.get("normal", "0 0 1"))
        return cls(normal=_normal)
