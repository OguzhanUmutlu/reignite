from __future__ import annotations

import math
from xml.etree import ElementTree as ET

from ...sdf1_10.models.yr import Yr as _PrevYr


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


class Yr(_PrevYr):
    def __init__(self, yr: float = 0.0):
        super().__init__(yr=yr)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Yr":
        _base = _PrevYr.from_sdf(el)
        return cls(yr=_base.yr)
