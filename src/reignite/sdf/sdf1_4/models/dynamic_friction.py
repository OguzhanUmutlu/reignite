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


class DynamicFriction(Model):
    def __init__(self, dynamic_friction: float = 0.9):
        self.dynamic_friction = dynamic_friction

    def to_sdf(self) -> ET.Element:
        el = ET.Element("dynamic_friction")
        if self.dynamic_friction is not None:
            el.text = str(self.dynamic_friction)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "DynamicFriction":
        _text = el.text or 0.9
        _dynamic_friction = _parse_double(_text)
        return cls(dynamic_friction=_dynamic_friction)
