from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_5.models.size import Size as _PrevSize
from ....utils.vector3 import Vector3


class Size(_PrevSize):
    def __init__(self, size: Vector3 = None):
        if size is None:
            size = Vector3.from_sdf("1 1 1")
        super().__init__(size=size)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Size":
        _base = _PrevSize.from_sdf(el)
        return cls(size=_base.size)
