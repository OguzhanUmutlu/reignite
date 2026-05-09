from __future__ import annotations

import math
from xml.etree import ElementTree as ET

from ...sdf1_11.models.max_convex_hulls import MaxConvexHulls as _PrevMaxConvexHulls


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


class MaxConvexHulls(_PrevMaxConvexHulls):
    def __init__(self, max_convex_hulls: int = 16):
        super().__init__(max_convex_hulls=max_convex_hulls)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "MaxConvexHulls":
        _base = _PrevMaxConvexHulls.from_sdf(el)
        return cls(max_convex_hulls=_base.max_convex_hulls)
