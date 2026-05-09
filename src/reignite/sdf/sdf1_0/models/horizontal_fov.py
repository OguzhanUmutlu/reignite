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


class HorizontalFov(Model):
    def __init__(self, angle: float = 1.047):
        self.angle = angle

    def to_sdf(self) -> ET.Element:
        el = ET.Element("horizontal_fov")
        if self.angle is not None:
            el.set("angle", str(self.angle))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "HorizontalFov":
        _angle = _parse_double(el.get("angle", 1.047))
        return cls(angle=_angle)
