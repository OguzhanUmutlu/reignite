from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ....utils.vector3 import Vector3


class Size(Model):
    def __init__(self, size: Vector3 = None):
        if size is None:
            size = Vector3.from_sdf("1 1 1")
        self.size = size

    def to_sdf(self) -> ET.Element:
        el = ET.Element("size")
        if self.size is not None:
            el.text = self.size.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Size":
        _text = el.text or "1 1 1"
        _size = Vector3.from_sdf(_text)
        return cls(size=_size)
