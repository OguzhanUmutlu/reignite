from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_11.models.scale_rate import ScaleRate as _PrevScaleRate


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



class ScaleRate(_PrevScaleRate):
    def __init__(self, scale_rate: float = 0):
        super().__init__(scale_rate=scale_rate)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "ScaleRate":
        _base = _PrevScaleRate.from_sdf(el)
        return cls(scale_rate=_base.scale_rate)
