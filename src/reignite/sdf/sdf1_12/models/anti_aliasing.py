from __future__ import annotations

import math
from xml.etree import ElementTree as ET

from ...sdf1_11.models.anti_aliasing import AntiAliasing as _PrevAntiAliasing


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


class AntiAliasing(_PrevAntiAliasing):
    def __init__(self, anti_aliasing: int = 4):
        super().__init__(anti_aliasing=anti_aliasing)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "AntiAliasing":
        _base = _PrevAntiAliasing.from_sdf(el)
        return cls(anti_aliasing=_base.anti_aliasing)
