from __future__ import annotations

import math
from xml.etree import ElementTree as ET

from .constant import Constant
from .quadratic import Quadratic
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


class Range(Model):
    def __init__(self, range: float = 10):
        self.range = range

    def to_sdf(self) -> ET.Element:
        el = ET.Element("range")
        if self.range is not None:
            el.text = str(self.range)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Range":
        _text = el.text or 10
        _range = _parse_double(_text)
        return cls(range=_range)


class Linear(Model):
    def __init__(self, linear: float = 1):
        self.linear = linear

    def to_sdf(self) -> ET.Element:
        el = ET.Element("linear")
        if self.linear is not None:
            el.text = str(self.linear)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Linear":
        _text = el.text or 1
        _linear = _parse_double(_text)
        return cls(linear=_linear)


class Attenuation(Model):
    def __init__(
            self,
            range: "Range" = None,
            linear: "Linear" = None,
            constant: "Constant" = None,
            quadratic: "Quadratic" = None
    ):
        self.range = range
        self.linear = linear
        self.constant = constant
        self.quadratic = quadratic

    def to_sdf(self) -> ET.Element:
        el = ET.Element("attenuation")
        if self.range is not None:
            el.append(self.range.to_sdf())
        if self.linear is not None:
            el.append(self.linear.to_sdf())
        if self.constant is not None:
            el.append(self.constant.to_sdf())
        if self.quadratic is not None:
            el.append(self.quadratic.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Attenuation":
        _c_range = el.find("range")
        _range = Range.from_sdf(_c_range) if _c_range is not None else None
        _c_linear = el.find("linear")
        _linear = Linear.from_sdf(_c_linear) if _c_linear is not None else None
        _c_constant = el.find("constant")
        _constant = Constant.from_sdf(_c_constant) if _c_constant is not None else None
        _c_quadratic = el.find("quadratic")
        _quadratic = Quadratic.from_sdf(_c_quadratic) if _c_quadratic is not None else None
        return cls(range=_range, linear=_linear, constant=_constant, quadratic=_quadratic)
