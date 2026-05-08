from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_10.models.radius import Radius as _PrevRadius
from .length import Length


import math
import sys

def _parse_int32(raw: str) -> int:
    v = int(raw)
    if not (-2147483648 <= v <= 2147483647):
        raise ValueError(f"int32 out of range: {v}")
    return v


def _parse_uint32(raw: str) -> int:
    v = int(raw)
    if not (0 <= v <= 4294967295):
        raise ValueError(f"uint32 out of range: {v}")
    return v


def _parse_double(raw: str) -> float:
    v = float(raw)
    if not math.isfinite(v) or abs(v) > 1.7976931348623157e+308:
        raise ValueError(f"double out of range: {raw}")
    return v



class Radius(_PrevRadius):
    def __init__(self, radius: float = 0.5):
        super().__init__(radius=radius)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Radius":
        _base = _PrevRadius.from_sdf(el)
        return cls(radius=_base.radius)


class Cone(Model):
    def __init__(self, radius: "Radius" = None, length: "Length" = None):
        self.radius = radius
        self.length = length

    def to_sdf(self) -> ET.Element:
        el = ET.Element("cone")
        if self.radius is not None:
            el.append(self.radius.to_sdf())
        if self.length is not None:
            el.append(self.length.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Cone":
        _c_radius = el.find("radius")
        _radius = Radius.from_sdf(_c_radius) if _c_radius is not None else None
        _c_length = el.find("length")
        _length = Length.from_sdf(_c_length) if _c_length is not None else None
        return cls(radius=_radius, length=_length)
