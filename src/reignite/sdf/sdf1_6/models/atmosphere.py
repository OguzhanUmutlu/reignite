from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
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



class Pressure(Model):
    def __init__(self, pressure: float = 101325):
        self.pressure = pressure

    def to_sdf(self) -> ET.Element:
        el = ET.Element("pressure")
        if self.pressure is not None:
            el.text = str(self.pressure)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Pressure":
        _text = el.text or 101325
        _pressure = _parse_double(_text)
        return cls(pressure=_pressure)


class Atmosphere(Model):
    def __init__(
        self,
        type: str = "adiabatic",
        temperature: "Temperature" = None,
        pressure: "Pressure" = None,
        temperature_gradient: "TemperatureGradient" = None
    ):
        self.type = type
        self.temperature = temperature
        self.pressure = pressure
        self.temperature_gradient = temperature_gradient

    def to_sdf(self) -> ET.Element:
        el = ET.Element("atmosphere")
        if self.type is not None:
            el.set("type", self.type)
        if self.temperature is not None:
            el.append(self.temperature.to_sdf())
        if self.pressure is not None:
            el.append(self.pressure.to_sdf())
        if self.temperature_gradient is not None:
            el.append(self.temperature_gradient.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Atmosphere":
        _type = el.get("type", "adiabatic")
        _c_temperature = el.find("temperature")
        _temperature = Temperature.from_sdf(_c_temperature) if _c_temperature is not None else None
        _c_pressure = el.find("pressure")
        _pressure = Pressure.from_sdf(_c_pressure) if _c_pressure is not None else None
        _c_temperature_gradient = el.find("temperature_gradient")
        _temperature_gradient = TemperatureGradient.from_sdf(_c_temperature_gradient) if _c_temperature_gradient is not None else None
        return cls(type=_type, temperature=_temperature, pressure=_pressure, temperature_gradient=_temperature_gradient)
