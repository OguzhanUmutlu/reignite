### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.utils import _parse_double
import typing
from ..utils.model import BaseModel
from ..utils.errors import SDFError

if typing.TYPE_CHECKING:
    from ..elements.noise import Noise


# noinspection PyUnusedImports
class AirPressure(BaseModel):
    class Pressure(BaseModel):
        def __init__(self, sdf_version: str | None = None, noise: "Noise" = None):
            super().__init__(sdf_version)
            self.noise = noise
            if self.noise is not None and hasattr(self.noise, 'to_version'):
                if getattr(self.noise, 'sdfversion', None) is None:
                    self.noise.sdfversion = self.sdfversion
                elif getattr(self.noise, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.noise = self.noise.to_version(self.sdfversion)

        def to_version(self, target_version: str) -> "AirPressure.Pressure":
            from ..elements.noise import Noise
            kwargs: dict = {"sdf_version": target_version, "noise": self.noise.to_version(target_version) if self.noise is not None and hasattr(self.noise, "to_version") else self.noise}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            from ..elements.noise import Noise
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf()
            el = ET.Element("pressure")
            if self.noise is not None:
                _child_res = self.noise.to_sdf(version)
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
                _noise = None
            return cls(sdf_version=version, noise=_noise)

    def __init__(
        self,
        sdf_version: str | None = None,
        pressure: "AirPressure.Pressure" = None,
        reference_altitude: float | None = 0.0
    ):
        super().__init__(sdf_version)
        self.pressure = pressure
        self.reference_altitude = reference_altitude if reference_altitude is not None else 0.0
        if self.pressure is not None and hasattr(self.pressure, 'to_version'):
            if getattr(self.pressure, 'sdfversion', None) is None:
                self.pressure.sdfversion = self.sdfversion
            elif getattr(self.pressure, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.pressure = self.pressure.to_version(self.sdfversion)

    def to_version(self, target_version: str) -> "AirPressure":
        kwargs: dict = {"sdf_version": target_version, "pressure": self.pressure.to_version(target_version) if self.pressure is not None and hasattr(self.pressure, "to_version") else self.pressure, "reference_altitude": self.reference_altitude}
        return self.__class__(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf()
        el = ET.Element("air_pressure")
        if self.pressure is not None:
            _child_res = self.pressure.to_sdf(version)
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
