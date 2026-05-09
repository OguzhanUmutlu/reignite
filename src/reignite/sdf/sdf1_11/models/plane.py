from __future__ import annotations

from xml.etree import ElementTree as ET

from .normal import Normal
from .size import Size
from ...sdf1_10.models.plane import Plane as _PrevPlane


class Plane(_PrevPlane):
    def __init__(self, normal: "Normal" = None, size: "Size" = None):
        super().__init__(normal=normal, size=size)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Plane":
        _base = _PrevPlane.from_sdf(el)
        return cls(normal=_base.normal, size=_base.size)
