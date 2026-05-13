### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

from ..utils.model import BaseModel
from ..utils.errors import SDFError

if typing.TYPE_CHECKING:
    from ..elements.noise import Noise


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



class AirPressure(BaseModel):
    class Pressure(BaseModel):
        def __init__(self, sdf_version: str | None = None, noise: "Noise" = None):
            super().__init__(sdf_version)
            self.noise = noise
            if self.noise is not None and hasattr(self.noise, 'to_version'):
                if getattr(self.noise, '__version__', None) is None:
                    self.noise.__version__ = self.__version__
                elif getattr(self.noise, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.noise = self.noise.to_version(self.__version__)

        def to_version(self, target_version: str) -> "AirPressure.Pressure":
            from ..elements.noise import Noise
            kwargs = {"sdf_version": target_version}
            kwargs["noise"] = self.noise.to_version(target_version) if hasattr(self.noise, "to_version") else self.noise
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            from ..elements.noise import Noise
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("pressure")
            if self.noise is None:
                self.noise = Noise(sdf_version=version)
            if self.noise is not None:
                if hasattr(self.noise, 'to_sdf'):
                    _child_res = self.noise.to_sdf(version)
                else:
                    _child_res = str(self.noise)
                if isinstance(_child_res, str):
                    _item_el = ET.Element('noise')
                    _item_el.text = _child_res
                else:
                    _item_el = _child_res
                el.append(_item_el)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "AirPressure.Pressure | SDFError":
            from ..elements.noise import Noise
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

    def __init__(
        self,
        sdf_version: str | None = None,
        pressure: "AirPressure.Pressure" = None,
        reference_altitude: float = 0.0
    ):
        super().__init__(sdf_version)
        self.pressure = pressure
        self.reference_altitude = reference_altitude
        if self.pressure is not None and hasattr(self.pressure, 'to_version'):
            if getattr(self.pressure, '__version__', None) is None:
                self.pressure.__version__ = self.__version__
            elif getattr(self.pressure, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.pressure = self.pressure.to_version(self.__version__)

    def to_version(self, target_version: str) -> "AirPressure":
        kwargs = {"sdf_version": target_version}
        kwargs["pressure"] = self.pressure.to_version(target_version) if hasattr(self.pressure, "to_version") else self.pressure
        kwargs["reference_altitude"] = self.reference_altitude
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("air_pressure")
        if self.pressure is not None:
            if hasattr(self.pressure, 'to_sdf'):
                _child_res = self.pressure.to_sdf(version)
            else:
                _child_res = str(self.pressure)
            if isinstance(_child_res, str):
                _item_el = ET.Element('pressure')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.reference_altitude is not None:
            _c_tmp = ET.Element("reference_altitude")
            _c_tmp.text = str(self.reference_altitude)
            el.append(_c_tmp)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "AirPressure | SDFError":
        _c_pressure = el.find("pressure")
        if _c_pressure is not None:
            _res = cls.Pressure._from_sdf(_c_pressure, version)
            if isinstance(_res, SDFError):
                return _res.extend("pressure")
            _pressure = _res
        else:
            _pressure = None
        _c_tmp = el.find("reference_altitude")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 0.0
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("reference_altitude")
            _reference_altitude = _val
        else:
            _reference_altitude = None
        return cls(sdf_version=version, pressure=_pressure, reference_altitude=_reference_altitude)
