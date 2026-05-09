from __future__ import annotations

import math
from xml.etree import ElementTree as ET

from ...sdf1_7.models.split_impulse_penetration_threshold import \
    SplitImpulsePenetrationThreshold as _PrevSplitImpulsePenetrationThreshold


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


class SplitImpulsePenetrationThreshold(_PrevSplitImpulsePenetrationThreshold):
    def __init__(self, split_impulse_penetration_threshold: float = -0.01):
        super().__init__(split_impulse_penetration_threshold=split_impulse_penetration_threshold)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "SplitImpulsePenetrationThreshold":
        _base = _PrevSplitImpulsePenetrationThreshold.from_sdf(el)
        return cls(split_impulse_penetration_threshold=_base.split_impulse_penetration_threshold)
