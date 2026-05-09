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


class MaxForce(Model):
    def __init__(self, max_force: float = 0):
        self.max_force = max_force

    def to_sdf(self) -> ET.Element:
        el = ET.Element("max_force")
        if self.max_force is not None:
            el.text = str(self.max_force)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "MaxForce":
        _text = el.text or 0
        _max_force = _parse_double(_text)
        return cls(max_force=_max_force)
