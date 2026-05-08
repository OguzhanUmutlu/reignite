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



class Iterations(Model):
    def __init__(self, iterations: int = 0):
        self.iterations = iterations

    def to_sdf(self) -> ET.Element:
        el = ET.Element("iterations")
        if self.iterations is not None:
            el.text = str(self.iterations)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Iterations":
        _text = el.text or 0
        _iterations = _parse_uint32(_text)
        return cls(iterations=_iterations)
