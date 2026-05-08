from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_7.models.pressure import Pressure as _PrevPressure
from ...sdf1_7.models.atmosphere import Atmosphere as _PrevAtmosphere
from .temperature import Temperature
from .temperature_gradient import TemperatureGradient


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



class Pressure(_PrevPressure):
    def __init__(self, pressure: float = 101325):
        super().__init__()
        self.pressure = pressure

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.pressure is not None:
            el.text = str(self.pressure)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Pressure":
        _text = el.text or 101325
        _pressure = _parse_double(_text)
        return cls(pressure=_pressure)


class Atmosphere(_PrevAtmosphere):
    def __init__(
        self,
        type: str = "adiabatic",
        temperature: "Temperature" = None,
        pressure: "Pressure" = None,
        temperature_gradient: "TemperatureGradient" = None
    ):
        super().__init__(type=type, temperature=temperature, pressure=pressure, temperature_gradient=temperature_gradient)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Atmosphere":
        _base = _PrevAtmosphere.from_sdf(el)
        return cls(type=_base.type, temperature=_base.temperature, pressure=_base.pressure, temperature_gradient=_base.temperature_gradient)
