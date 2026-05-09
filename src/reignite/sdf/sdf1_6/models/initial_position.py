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


class InitialPosition(Model):
    def __init__(self, initial_position: float = 0):
        self.initial_position = initial_position

    def to_sdf(self) -> ET.Element:
        el = ET.Element("initial_position")
        if self.initial_position is not None:
            el.text = str(self.initial_position)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "InitialPosition":
        _text = el.text or 0
        _initial_position = _parse_double(_text)
        return cls(initial_position=_initial_position)
