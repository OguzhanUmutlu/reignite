from __future__ import annotations

import math
from xml.etree import ElementTree as ET

from ...sdf1_7.models.radius import Radius as _PrevRadius
from ...sdf1_7.models.sphere import Sphere as _PrevSphere


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


class Sphere(_PrevSphere):
    def __init__(self, radius: "Radius" = None):
        super().__init__(radius=radius)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Sphere":
        _base = _PrevSphere.from_sdf(el)
        return cls(radius=_base.radius)
