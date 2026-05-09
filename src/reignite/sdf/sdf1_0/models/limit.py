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


class Limit(Model):
    def __init__(
            self,
            lower: float = -1e16,
            upper: float = 1e16,
            effort: float = 0,
            velocity: float = 0
    ):
        self.lower = lower
        self.upper = upper
        self.effort = effort
        self.velocity = velocity

    def to_sdf(self) -> ET.Element:
        el = ET.Element("limit")
        if self.lower is not None:
            el.set("lower", str(self.lower))
        if self.upper is not None:
            el.set("upper", str(self.upper))
        if self.effort is not None:
            el.set("effort", str(self.effort))
        if self.velocity is not None:
            el.set("velocity", str(self.velocity))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Limit":
        _lower = _parse_double(el.get("lower", -1e16))
        _upper = _parse_double(el.get("upper", 1e16))
        _effort = _parse_double(el.get("effort", 0))
        _velocity = _parse_double(el.get("velocity", 0))
        return cls(lower=_lower, upper=_upper, effort=_effort, velocity=_velocity)
