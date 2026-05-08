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



class Spot(Model):
    def __init__(self, inner_angle: float = 0, outer_angle: float = 0, falloff: float = 0):
        self.inner_angle = inner_angle
        self.outer_angle = outer_angle
        self.falloff = falloff

    def to_sdf(self) -> ET.Element:
        el = ET.Element("spot")
        if self.inner_angle is not None:
            el.set("inner_angle", str(self.inner_angle))
        if self.outer_angle is not None:
            el.set("outer_angle", str(self.outer_angle))
        if self.falloff is not None:
            el.set("falloff", str(self.falloff))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Spot":
        _inner_angle = _parse_double(el.get("inner_angle", 0))
        _outer_angle = _parse_double(el.get("outer_angle", 0))
        _falloff = _parse_double(el.get("falloff", 0))
        return cls(inner_angle=_inner_angle, outer_angle=_outer_angle, falloff=_falloff)
