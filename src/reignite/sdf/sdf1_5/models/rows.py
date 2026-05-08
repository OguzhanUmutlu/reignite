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



class Rows(Model):
    def __init__(self, rows: int = 1):
        self.rows = rows

    def to_sdf(self) -> ET.Element:
        el = ET.Element("rows")
        if self.rows is not None:
            el.text = str(self.rows)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Rows":
        _text = el.text or 1
        _rows = _parse_int32(_text)
        return cls(rows=_rows)
