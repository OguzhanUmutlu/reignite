from __future__ import annotations

import math
from xml.etree import ElementTree as ET

from ...sdf1_7.models.min_step_size import MinStepSize as _PrevMinStepSize


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


class MinStepSize(_PrevMinStepSize):
    def __init__(self, min_step_size: float = 0.0001):
        super().__init__(min_step_size=min_step_size)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "MinStepSize":
        _base = _PrevMinStepSize.from_sdf(el)
        return cls(min_step_size=_base.min_step_size)
