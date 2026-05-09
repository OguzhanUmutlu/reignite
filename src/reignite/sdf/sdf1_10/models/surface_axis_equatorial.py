from __future__ import annotations

import math
from xml.etree import ElementTree as ET

from ..model import Model


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


class SurfaceAxisEquatorial(Model):
    def __init__(self, surface_axis_equatorial: float = 0.0):
        self.surface_axis_equatorial = surface_axis_equatorial

    def to_sdf(self) -> ET.Element:
        el = ET.Element("surface_axis_equatorial")
        if self.surface_axis_equatorial is not None:
            el.text = str(self.surface_axis_equatorial)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "SurfaceAxisEquatorial":
        _text = el.text or 0.0
        _surface_axis_equatorial = _parse_double(_text)
        return cls(surface_axis_equatorial=_surface_axis_equatorial)
