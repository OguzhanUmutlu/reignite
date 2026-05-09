### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.model import BaseModel
from ..utils.errors import SDFError

from .noise import Noise


class AirSpeed(BaseModel):
    def __init__(self, sdf_version: str, pressure: "Pressure" = None):
        self.__version__ = sdf_version
        self.pressure = pressure

    def to_version(self, target_version: str) -> "AirSpeed":
        kwargs = {"sdf_version": target_version}
        kwargs["pressure"] = self.pressure.to_version(target_version) if self.pressure is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("air_speed")
        if self.pressure is not None:
            el.append(self.pressure.to_sdf(version))
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
        return cls(sdf_version=version, pressure=_pressure)


class Pressure(BaseModel):
    def __init__(self, sdf_version: str, noise: "Noise" = None):
        self.__version__ = sdf_version
        self.noise = noise

    def to_version(self, target_version: str) -> "Pressure":
        kwargs = {"sdf_version": target_version}
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("pressure")
        if self.noise is None:
            self.noise = Noise(sdf_version=version)
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_noise = el.find("noise")
        if _c_noise is not None:
            _res = Noise._from_sdf(_c_noise, version)
            if isinstance(_res, SDFError):
                return _res.extend("noise")
            _noise = _res
        else:
            _res = Noise._from_sdf(ET.Element("noise"), version)
            if isinstance(_res, SDFError):
                return _res.extend("noise")
            _noise = _res
        return cls(sdf_version=version, noise=_noise)
