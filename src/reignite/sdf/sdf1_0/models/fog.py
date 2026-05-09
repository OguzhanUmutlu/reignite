from __future__ import annotations

import math
from xml.etree import ElementTree as ET

from ..model import Model
from ....utils.color import Color


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


class Fog(Model):
    def __init__(
            self,
            rgba: Color = None,
            type: str = "linear",
            start: float = 1.0,
            end: float = 100.0,
            density: float = 1.0
    ):
        if rgba is None:
            rgba = Color.from_sdf("1 1 1 1")
        self.rgba = rgba
        self.type = type
        self.start = start
        self.end = end
        self.density = density

    def to_sdf(self) -> ET.Element:
        el = ET.Element("fog")
        if self.rgba is not None:
            el.set("rgba", self.rgba.to_sdf())
        if self.type is not None:
            el.set("type", self.type)
        if self.start is not None:
            el.set("start", str(self.start))
        if self.end is not None:
            el.set("end", str(self.end))
        if self.density is not None:
            el.set("density", str(self.density))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Fog":
        _rgba = Color.from_sdf(el.get("rgba", "1 1 1 1"))
        _type = el.get("type", "linear")
        _start = _parse_double(el.get("start", 1.0))
        _end = _parse_double(el.get("end", 100.0))
        _density = _parse_double(el.get("density", 1.0))
        return cls(rgba=_rgba, type=_type, start=_start, end=_end, density=_density)
