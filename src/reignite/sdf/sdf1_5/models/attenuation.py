from __future__ import annotations

import math
from xml.etree import ElementTree as ET

from .constant import Constant
from .quadratic import Quadratic
from ...sdf1_4.models.attenuation import Attenuation as _PrevAttenuation
from ...sdf1_4.models.linear import Linear as _PrevLinear
from ...sdf1_4.models.range import Range as _PrevRange


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


class Range(_PrevRange):
    def __init__(self, range: float = 10):
        super().__init__(range=range)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Range":
        _base = _PrevRange.from_sdf(el)
        return cls(range=_base.range)


class Linear(_PrevLinear):
    def __init__(self, linear: float = 1):
        super().__init__(linear=linear)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Linear":
        _base = _PrevLinear.from_sdf(el)
        return cls(linear=_base.linear)


class Attenuation(_PrevAttenuation):
    def __init__(
            self,
            range: "Range" = None,
            linear: "Linear" = None,
            constant: "Constant" = None,
            quadratic: "Quadratic" = None
    ):
        super().__init__(range=range, linear=linear, constant=constant, quadratic=quadratic)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Attenuation":
        _base = _PrevAttenuation.from_sdf(el)
        return cls(range=_base.range, linear=_base.linear, constant=_base.constant, quadratic=_base.quadratic)
