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



class Attenuation(Model):
    def __init__(
        self,
        range: float = 10,
        linear: float = 1,
        constant: float = 1,
        quadratic: float = 0
    ):
        self.range = range
        self.linear = linear
        self.constant = constant
        self.quadratic = quadratic

    def to_sdf(self) -> ET.Element:
        el = ET.Element("attenuation")
        if self.range is not None:
            el.set("range", str(self.range))
        if self.linear is not None:
            el.set("linear", str(self.linear))
        if self.constant is not None:
            el.set("constant", str(self.constant))
        if self.quadratic is not None:
            el.set("quadratic", str(self.quadratic))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Attenuation":
        _range = _parse_double(el.get("range", 10))
        _linear = _parse_double(el.get("linear", 1))
        _constant = _parse_double(el.get("constant", 1))
        _quadratic = _parse_double(el.get("quadratic", 0))
        return cls(range=_range, linear=_linear, constant=_constant, quadratic=_quadratic)
