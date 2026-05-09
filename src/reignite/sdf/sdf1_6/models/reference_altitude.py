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


class ReferenceAltitude(Model):
    def __init__(self, reference_altitude: float = 0.0):
        self.reference_altitude = reference_altitude

    def to_sdf(self) -> ET.Element:
        el = ET.Element("reference_altitude")
        if self.reference_altitude is not None:
            el.text = str(self.reference_altitude)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "ReferenceAltitude":
        _text = el.text or 0.0
        _reference_altitude = _parse_double(_text)
        return cls(reference_altitude=_reference_altitude)
