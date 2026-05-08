from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_11.models.surface_axis_equatorial import SurfaceAxisEquatorial as _PrevSurfaceAxisEquatorial


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



class SurfaceAxisEquatorial(_PrevSurfaceAxisEquatorial):
    def __init__(self, surface_axis_equatorial: float = 0.0):
        super().__init__(surface_axis_equatorial=surface_axis_equatorial)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "SurfaceAxisEquatorial":
        _base = _PrevSurfaceAxisEquatorial.from_sdf(el)
        return cls(surface_axis_equatorial=_base.surface_axis_equatorial)
