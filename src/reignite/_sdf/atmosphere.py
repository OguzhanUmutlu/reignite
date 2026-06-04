### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.utils import _parse_double
from ..utils.model import BaseModel
from ..utils.errors import SDFError


# noinspection PyUnusedImports
class Atmosphere(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        pressure: float | None = None,
        temperature: float | None = None,
        temperature_gradient: float | None = None,
        type: str | None = "adiabatic"
    ):
        super().__init__(sdf_version)
        self.pressure = pressure
        self.temperature = temperature
        self.temperature_gradient = temperature_gradient
        self.type = type

    def to_version(self, target_version: str) -> "Atmosphere":
        kwargs: dict = {"sdf_version": target_version, "pressure": self.pressure, "temperature": self.temperature, "temperature_gradient": self.temperature_gradient, "type": self.type}
        return self.__class__(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf()
        el = ET.Element("atmosphere")
        if self.pressure is not None:
            _c_tmp = ET.Element("pressure")
            _c_tmp.text = str(self.pressure)
            el.append(_c_tmp)
        if self.temperature is not None:
            _c_tmp = ET.Element("temperature")
            _c_tmp.text = str(self.temperature)
            el.append(_c_tmp)
        if self.temperature_gradient is not None:
            _c_tmp = ET.Element("temperature_gradient")
            _c_tmp.text = str(self.temperature_gradient)
            el.append(_c_tmp)
        if self.type is not None:
            el.set("type", self.type)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Atmosphere | SDFError":
        _c_tmp = el.find("pressure")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 101325
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("pressure")
            _pressure = _val
        else:
            _pressure = None
        _c_tmp = el.find("temperature")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 288.15
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("temperature")
            _temperature = _val
        else:
            _temperature = None
        _c_tmp = el.find("temperature_gradient")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else -0.0065
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("temperature_gradient")
            _temperature_gradient = _val
        else:
            _temperature_gradient = None
        _type = el.get("type", "adiabatic")
        if isinstance(_type, SDFError):
            return _type.extend("@type")
        return cls(sdf_version=version, pressure=_pressure, temperature=_temperature, temperature_gradient=_temperature_gradient, type=_type)
