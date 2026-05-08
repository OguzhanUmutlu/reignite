from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_10.models.dynamic_bias_correlation_time import DynamicBiasCorrelationTime as _PrevDynamicBiasCorrelationTime


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



class DynamicBiasCorrelationTime(_PrevDynamicBiasCorrelationTime):
    def __init__(self, dynamic_bias_correlation_time: float = 0.0):
        super().__init__(dynamic_bias_correlation_time=dynamic_bias_correlation_time)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "DynamicBiasCorrelationTime":
        _base = _PrevDynamicBiasCorrelationTime.from_sdf(el)
        return cls(dynamic_bias_correlation_time=_base.dynamic_bias_correlation_time)
