from __future__ import annotations

import math
from xml.etree import ElementTree as ET

from ...sdf1_7.models.k2 import K2 as _PrevK2


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


class K2(_PrevK2):
    def __init__(self, k2: float = 0.0):
        super().__init__(k2=k2)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "K2":
        _base = _PrevK2.from_sdf(el)
        return cls(k2=_base.k2)
