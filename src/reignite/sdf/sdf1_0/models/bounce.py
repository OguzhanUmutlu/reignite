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


class Bounce(Model):
    def __init__(self, restitution_coefficient: float = 0, threshold: float = 100000):
        self.restitution_coefficient = restitution_coefficient
        self.threshold = threshold

    def to_sdf(self) -> ET.Element:
        el = ET.Element("bounce")
        if self.restitution_coefficient is not None:
            el.set("restitution_coefficient", str(self.restitution_coefficient))
        if self.threshold is not None:
            el.set("threshold", str(self.threshold))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Bounce":
        _restitution_coefficient = _parse_double(el.get("restitution_coefficient", 0))
        _threshold = _parse_double(el.get("threshold", 100000))
        return cls(restitution_coefficient=_restitution_coefficient, threshold=_threshold)
