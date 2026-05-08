from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ....utils.vector3 import Vector3


class Box(Model):
    def __init__(self, size: Vector3 = None):
        if size is None:
            size = Vector3.from_sdf("1 1 1")
        self.size = size

    def to_sdf(self) -> ET.Element:
        el = ET.Element("box")
        if self.size is not None:
            el.set("size", self.size.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Box":
        _size = Vector3.from_sdf(el.get("size", "1 1 1"))
        return cls(size=_size)
