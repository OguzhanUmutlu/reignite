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


class Width(Model):
    def __init__(self, width: float = 1.0):
        self.width = width

    def to_sdf(self) -> ET.Element:
        el = ET.Element("width")
        if self.width is not None:
            el.text = str(self.width)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Width":
        _text = el.text or 1.0
        _width = _parse_double(_text)
        return cls(width=_width)
