from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


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



class MinContactCount(Model):
    def __init__(self, min_contact_count: int = 2):
        self.min_contact_count = min_contact_count

    def to_sdf(self) -> ET.Element:
        el = ET.Element("min_contact_count")
        if self.min_contact_count is not None:
            el.text = str(self.min_contact_count)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "MinContactCount":
        _text = el.text or 2
        _min_contact_count = _parse_uint32(_text)
        return cls(min_contact_count=_min_contact_count)
