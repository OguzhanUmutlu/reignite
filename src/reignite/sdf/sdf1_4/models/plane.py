from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_3.models.normal import Normal as _PrevNormal
from ...sdf1_3.models.plane import Plane as _PrevPlane
from ...sdf1_3.models.size import Size as _PrevSize
from ....utils.vector3 import Vector3


class Normal(_PrevNormal):
    def __init__(self, normal: str = "__default__"):
        super().__init__(normal=normal)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Normal":
        _base = _PrevNormal.from_sdf(el)
        return cls(normal=_base.normal)


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
