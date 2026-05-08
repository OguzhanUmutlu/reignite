from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_5.models.direction import Direction as _PrevDirection
from ...sdf1_5.models.ambient import Ambient as _PrevAmbient
from ...sdf1_5.models.clouds import Clouds as _PrevClouds
from ....utils.color import Color
from .speed import Speed
from .humidity import Humidity
from .mean_size import MeanSize


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



class Direction(_PrevDirection):
    def __init__(self, direction: float = 0.0):
        super().__init__(direction=direction)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Direction":
        _base = _PrevDirection.from_sdf(el)
        return cls(direction=_base.direction)


class Ambient(_PrevAmbient):
    def __init__(self, ambient: Color = None):
        if ambient is None:
            ambient = Color.from_sdf("0.4 0.4 0.4 1.0")
        super().__init__(ambient=ambient)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Ambient":
        _base = _PrevAmbient.from_sdf(el)
        return cls(ambient=_base.ambient)


class Clouds(_PrevClouds):
    def __init__(
        self,
        speed: "Speed" = None,
        direction: "Direction" = None,
        humidity: "Humidity" = None,
        mean_size: "MeanSize" = None,
        ambient: "Ambient" = None
    ):
        super().__init__(speed=speed, direction=direction, humidity=humidity, mean_size=mean_size, ambient=ambient)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Clouds":
        _base = _PrevClouds.from_sdf(el)
        return cls(speed=_base.speed, direction=_base.direction, humidity=_base.humidity, mean_size=_base.mean_size, ambient=_base.ambient)
