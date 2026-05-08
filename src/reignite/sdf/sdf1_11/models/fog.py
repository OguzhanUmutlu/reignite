from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_10.models.type import Type as _PrevType
from ...sdf1_10.models.density import Density as _PrevDensity
from ...sdf1_10.models.fog import Fog as _PrevFog
from .color import Color
from .start import Start
from .end import End


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



class Type(_PrevType):
    def __init__(self, type: str = "none"):
        super().__init__(type=type)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Type":
        _base = _PrevType.from_sdf(el)
        return cls(type=_base.type)


class Density(_PrevDensity):
    def __init__(self, density: float = 1.0):
        super().__init__(density=density)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Density":
        _base = _PrevDensity.from_sdf(el)
        return cls(density=_base.density)


class Fog(_PrevFog):
    def __init__(
        self,
        color: "Color" = None,
        type: "Type" = None,
        start: "Start" = None,
        end: "End" = None,
        density: "Density" = None
    ):
        super().__init__(color=color, type=type, start=start, end=end, density=density)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Fog":
        _base = _PrevFog.from_sdf(el)
        return cls(color=_base.color, type=_base.type, start=_base.start, end=_base.end, density=_base.density)
