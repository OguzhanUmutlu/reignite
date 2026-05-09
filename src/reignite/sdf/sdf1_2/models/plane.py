from __future__ import annotations

from xml.etree import ElementTree as ET

from .normal import Normal
from .size import Size
from ...sdf1_0.models.plane import Plane as _PrevPlane


class Plane(_PrevPlane):
    def __init__(self, normal: "Normal" = None, size: "Size" = None):
        super().__init__(normal=normal)
        self.size = size

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.size is not None:
            el.append(self.size.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Plane":
        _base = _PrevPlane.from_sdf(el)
        _c_size = el.find("size")
        _size = Size.from_sdf(_c_size) if _c_size is not None else None
        return cls(normal=_base.normal, size=_size)
