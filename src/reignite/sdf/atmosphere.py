### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.model import Model


import math

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
    if not math.isfinite(v) or abs(v) > math.inf:
        raise ValueError(f"double out of range: {raw}")
    return v



class Temperature(Model):
    def __init__(self, sdf_version: str, temperature: float = 288.15):
        self.__version__ = sdf_version
        self.temperature = temperature

    def to_version(self, target_version: str) -> "Temperature":
        kwargs = {"sdf_version": target_version}
        kwargs["temperature"] = self.temperature
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("temperature")
        if self.temperature is not None:
            el.text = str(self.temperature)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Temperature":
        _text = el.text or 288.15
        _temperature = _parse_double(_text)
        return cls(sdf_version=version, temperature=_temperature)


class Pressure(Model):
    def __init__(self, sdf_version: str, pressure: float = 101325):
        self.__version__ = sdf_version
        self.pressure = pressure

    def to_version(self, target_version: str) -> "Pressure":
        kwargs = {"sdf_version": target_version}
        kwargs["pressure"] = self.pressure
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("pressure")
        if self.pressure is not None:
            el.text = str(self.pressure)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Pressure":
        _text = el.text or 101325
        _pressure = _parse_double(_text)
        return cls(sdf_version=version, pressure=_pressure)


class TemperatureGradient(Model):
    def __init__(self, sdf_version: str, temperature_gradient: float = -0.0065):
        self.__version__ = sdf_version
        self.temperature_gradient = temperature_gradient

    def to_version(self, target_version: str) -> "TemperatureGradient":
        kwargs = {"sdf_version": target_version}
        kwargs["temperature_gradient"] = self.temperature_gradient
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("temperature_gradient")
        if self.temperature_gradient is not None:
            el.text = str(self.temperature_gradient)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "TemperatureGradient":
        _text = el.text or -0.0065
        _temperature_gradient = _parse_double(_text)
        return cls(sdf_version=version, temperature_gradient=_temperature_gradient)


class Atmosphere(Model):
    def __init__(
        self,
        sdf_version: str,
        type: str = "adiabatic",
        temperature: "Temperature" = None,
        pressure: "Pressure" = None,
        temperature_gradient: "TemperatureGradient" = None
    ):
        self.__version__ = sdf_version
        self.type = type
        self.temperature = temperature
        self.pressure = pressure
        self.temperature_gradient = temperature_gradient

    def to_version(self, target_version: str) -> "Atmosphere":
        kwargs = {"sdf_version": target_version}
        kwargs["type"] = self.type
        kwargs["temperature"] = self.temperature.to_version(target_version) if self.temperature is not None else None
        kwargs["pressure"] = self.pressure.to_version(target_version) if self.pressure is not None else None
        kwargs["temperature_gradient"] = self.temperature_gradient.to_version(target_version) if self.temperature_gradient is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("atmosphere")
        if self.type is not None:
            el.set("type", self.type)
        if self.temperature is not None:
            el.append(self.temperature.to_sdf(version))
        if self.pressure is not None:
            el.append(self.pressure.to_sdf(version))
        if self.temperature_gradient is not None:
            el.append(self.temperature_gradient.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Atmosphere":
        _type = el.get("type", "adiabatic")
        _c_temperature = el.find("temperature")
        _temperature = Temperature.from_sdf(_c_temperature, version) if _c_temperature is not None else None
        _c_pressure = el.find("pressure")
        _pressure = Pressure.from_sdf(_c_pressure, version) if _c_pressure is not None else None
        _c_temperature_gradient = el.find("temperature_gradient")
        _temperature_gradient = TemperatureGradient.from_sdf(_c_temperature_gradient, version) if _c_temperature_gradient is not None else None
        return cls(sdf_version=version, type=_type, temperature=_temperature, pressure=_pressure, temperature_gradient=_temperature_gradient)
