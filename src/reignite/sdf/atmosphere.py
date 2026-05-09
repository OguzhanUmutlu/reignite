### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.model import BaseModel
from ..utils.errors import SDFError


import math

def _parse_int32(raw: str) -> int | SDFError:
    try:
        v = int(raw)
        if not (-2147483648 <= v <= 2147483647):
            return SDFError(f"int32 out of range: {v}")
        return v
    except ValueError:
        return SDFError(f"Invalid int32: {raw}")


def _parse_uint32(raw: str) -> int | SDFError:
    try:
        v = int(raw)
        if not (0 <= v <= 4294967295):
            return SDFError(f"uint32 out of range: {v}")
        return v
    except ValueError:
        return SDFError(f"Invalid uint32: {raw}")


def _parse_double(raw: str) -> float | SDFError:
    try:
        v = float(raw)
        if not math.isfinite(v) or abs(v) > math.inf:
            return SDFError(f"double out of range: {raw}")
        return v
    except ValueError:
        return SDFError(f"Invalid double: {raw}")



class Atmosphere(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        pressure: "Pressure" = None,
        temperature: "Temperature" = None,
        temperature_gradient: "TemperatureGradient" = None,
        type: str = "adiabatic"
    ):
        self.__version__ = sdf_version
        self.pressure = pressure
        self.temperature = temperature
        self.temperature_gradient = temperature_gradient
        self.type = type

    def to_version(self, target_version: str) -> "Atmosphere":
        kwargs = {"sdf_version": target_version}
        kwargs["pressure"] = self.pressure.to_version(target_version) if self.pressure is not None else None
        kwargs["temperature"] = self.temperature.to_version(target_version) if self.temperature is not None else None
        kwargs["temperature_gradient"] = self.temperature_gradient.to_version(target_version) if self.temperature_gradient is not None else None
        kwargs["type"] = self.type
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("atmosphere")
        if self.pressure is not None:
            el.append(self.pressure.to_sdf(version))
        if self.temperature is not None:
            el.append(self.temperature.to_sdf(version))
        if self.temperature_gradient is not None:
            el.append(self.temperature_gradient.to_sdf(version))
        if self.type is not None:
            el.set("type", self.type)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_pressure = el.find("pressure")
        if _c_pressure is not None:
            _res = Pressure._from_sdf(_c_pressure, version)
            if isinstance(_res, SDFError):
                return _res.extend("pressure")
            _pressure = _res
        else:
            _pressure = None
        _c_temperature = el.find("temperature")
        if _c_temperature is not None:
            _res = Temperature._from_sdf(_c_temperature, version)
            if isinstance(_res, SDFError):
                return _res.extend("temperature")
            _temperature = _res
        else:
            _temperature = None
        _c_temperature_gradient = el.find("temperature_gradient")
        if _c_temperature_gradient is not None:
            _res = TemperatureGradient._from_sdf(_c_temperature_gradient, version)
            if isinstance(_res, SDFError):
                return _res.extend("temperature_gradient")
            _temperature_gradient = _res
        else:
            _temperature_gradient = None
        _type = el.get("type", "adiabatic")
        if isinstance(_type, SDFError):
            return _type.extend("@type")
        return cls(sdf_version=version, pressure=_pressure, temperature=_temperature, temperature_gradient=_temperature_gradient, type=_type)


class Pressure(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 101325
        _pressure = _parse_double(_text)
        if isinstance(_pressure, SDFError):
            return _pressure
        return cls(sdf_version=version, pressure=_pressure)


class Temperature(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 288.15
        _temperature = _parse_double(_text)
        if isinstance(_temperature, SDFError):
            return _temperature
        return cls(sdf_version=version, temperature=_temperature)


class TemperatureGradient(BaseModel):
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
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or -0.0065
        _temperature_gradient = _parse_double(_text)
        if isinstance(_temperature_gradient, SDFError):
            return _temperature_gradient
        return cls(sdf_version=version, temperature_gradient=_temperature_gradient)
