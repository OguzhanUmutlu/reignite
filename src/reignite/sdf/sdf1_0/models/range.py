from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


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



class Range(Model):
    def __init__(self, min: float = 0, max: float = 0, resolution: float = 0):
        self.min = min
        self.max = max
        self.resolution = resolution

    def to_sdf(self) -> ET.Element:
        el = ET.Element("range")
        if self.min is not None:
            el.set("min", str(self.min))
        if self.max is not None:
            el.set("max", str(self.max))
        if self.resolution is not None:
            el.set("resolution", str(self.resolution))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Range":
        _min = _parse_double(el.get("min", 0))
        _max = _parse_double(el.get("max", 0))
        _resolution = _parse_double(el.get("resolution", 0))
        return cls(min=_min, max=_max, resolution=_resolution)
