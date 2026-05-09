from __future__ import annotations

import math
from xml.etree import ElementTree as ET

from .max import Max
from .min import Min
from ..model import Model
from ...sdf1_3.models.radius import Radius as _PrevRadius


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
    def __init__(self, radius: float = 1):
        super().__init__(radius=radius)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Radius":
        _base = _PrevRadius.from_sdf(el)
        return cls(radius=_base.radius)


class Sonar(Model):
    def __init__(self, min: "Min" = None, max: "Max" = None, radius: "Radius" = None):
        self.min = min
        self.max = max
        self.radius = radius

    def to_sdf(self) -> ET.Element:
        el = ET.Element("sonar")
        if self.min is not None:
            el.append(self.min.to_sdf())
        if self.max is not None:
            el.append(self.max.to_sdf())
        if self.radius is not None:
            el.append(self.radius.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Sonar":
        _c_min = el.find("min")
        _min = Min.from_sdf(_c_min) if _c_min is not None else None
        _c_max = el.find("max")
        _max = Max.from_sdf(_c_max) if _c_max is not None else None
        _c_radius = el.find("radius")
        _radius = Radius.from_sdf(_c_radius) if _c_radius is not None else None
        return cls(min=_min, max=_max, radius=_radius)
