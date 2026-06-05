### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

import typing
from ..utils.model import BaseModel
from ..utils.errors import SDFError

if typing.TYPE_CHECKING:
    from ..elements.noise import Noise


# noinspection PyUnusedImports
class AirSpeed(BaseModel):
    class Pressure(BaseModel):
        def __init__(self, sdf_version: str | None = None, noise: "Noise" = None):
            super().__init__(sdf_version)
            self.noise = noise
            if self.noise is not None and hasattr(self.noise, 'to_version'):
                if getattr(self.noise, 'sdfversion', None) is None:
                    self.noise.sdfversion = self.sdfversion
                elif getattr(self.noise, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.noise = self.noise.to_version(self.sdfversion)

        def to_version(self, target_version: str) -> "AirSpeed.Pressure":
            from ..elements.noise import Noise
            kwargs: dict = {"sdf_version": target_version, "noise": self.noise.to_version(target_version) if self.noise is not None and hasattr(self.noise, "to_version") else self.noise}
            return AirSpeed.Pressure(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            from ..elements.noise import Noise
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf(version)
            if version is None:
                version = self.sdfversion or "1.12"
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
        def _from_sdf(cls, el: ET.Element, version: str) -> "AirSpeed.Pressure | SDFError":
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

    def __init__(self, sdf_version: str | None = None, pressure: "AirSpeed.Pressure" = None):
        super().__init__(sdf_version)
        self.pressure = pressure
        if self.pressure is not None and hasattr(self.pressure, 'to_version'):
            if getattr(self.pressure, 'sdfversion', None) is None:
                self.pressure.sdfversion = self.sdfversion
            elif getattr(self.pressure, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.pressure = self.pressure.to_version(self.sdfversion)

    def to_version(self, target_version: str) -> "AirSpeed":
        kwargs: dict = {"sdf_version": target_version, "pressure": self.pressure.to_version(target_version) if self.pressure is not None and hasattr(self.pressure, "to_version") else self.pressure}
        return AirSpeed(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf(version)
        if version is None:
            version = self.sdfversion or "1.12"
        el = ET.Element("air_speed")
        if self.pressure is not None:
            _child_res = self.pressure.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('pressure')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "AirSpeed | SDFError":
        _c_pressure = el.find("pressure")
        if _c_pressure is not None:
            _res = cls.Pressure._from_sdf(_c_pressure, version)
            if isinstance(_res, SDFError):
                return _res.extend("pressure")
            _pressure = _res
        else:
            _pressure = None
        return cls(sdf_version=version, pressure=_pressure)
