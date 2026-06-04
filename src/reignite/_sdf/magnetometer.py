### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

import typing
from ..utils.model import BaseModel
from ..utils.errors import SDFError

if typing.TYPE_CHECKING:
    from ..elements.noise import Noise


# noinspection PyUnusedImports
class Magnetometer(BaseModel):
    class X(BaseModel):
        def __init__(self, sdf_version: str | None = None, noise: "Noise" = None):
            super().__init__(sdf_version)
            self.noise = noise
            if self.noise is not None and hasattr(self.noise, 'to_version'):
                if getattr(self.noise, 'sdfversion', None) is None:
                    self.noise.sdfversion = self.sdfversion
                elif getattr(self.noise, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.noise = self.noise.to_version(self.sdfversion)

        def to_version(self, target_version: str) -> "Magnetometer.X":
            from ..elements.noise import Noise
            kwargs: dict = {"sdf_version": target_version, "noise": self.noise.to_version(target_version) if self.noise is not None and hasattr(self.noise, "to_version") else self.noise}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            from ..elements.noise import Noise
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf(version)
            if version is None:
                version = self.sdfversion or "1.12"
            el = ET.Element("x")
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
        def _from_sdf(cls, el: ET.Element, version: str) -> "Magnetometer.X | SDFError":
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

    class Y(BaseModel):
        def __init__(self, sdf_version: str | None = None, noise: "Noise" = None):
            super().__init__(sdf_version)
            self.noise = noise
            if self.noise is not None and hasattr(self.noise, 'to_version'):
                if getattr(self.noise, 'sdfversion', None) is None:
                    self.noise.sdfversion = self.sdfversion
                elif getattr(self.noise, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.noise = self.noise.to_version(self.sdfversion)

        def to_version(self, target_version: str) -> "Magnetometer.Y":
            from ..elements.noise import Noise
            kwargs: dict = {"sdf_version": target_version, "noise": self.noise.to_version(target_version) if self.noise is not None and hasattr(self.noise, "to_version") else self.noise}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            from ..elements.noise import Noise
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf(version)
            if version is None:
                version = self.sdfversion or "1.12"
            el = ET.Element("y")
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
        def _from_sdf(cls, el: ET.Element, version: str) -> "Magnetometer.Y | SDFError":
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

    class Z(BaseModel):
        def __init__(self, sdf_version: str | None = None, noise: "Noise" = None):
            super().__init__(sdf_version)
            self.noise = noise
            if self.noise is not None and hasattr(self.noise, 'to_version'):
                if getattr(self.noise, 'sdfversion', None) is None:
                    self.noise.sdfversion = self.sdfversion
                elif getattr(self.noise, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                    self.noise = self.noise.to_version(self.sdfversion)

        def to_version(self, target_version: str) -> "Magnetometer.Z":
            from ..elements.noise import Noise
            kwargs: dict = {"sdf_version": target_version, "noise": self.noise.to_version(target_version) if self.noise is not None and hasattr(self.noise, "to_version") else self.noise}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            from ..elements.noise import Noise
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf(version)
            if version is None:
                version = self.sdfversion or "1.12"
            el = ET.Element("z")
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
        def _from_sdf(cls, el: ET.Element, version: str) -> "Magnetometer.Z | SDFError":
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
        x: "Magnetometer.X" = None,
        y: "Magnetometer.Y" = None,
        z: "Magnetometer.Z" = None
    ):
        super().__init__(sdf_version)
        self.x = x
        self.y = y
        self.z = z
        if self.x is not None and hasattr(self.x, 'to_version'):
            if getattr(self.x, 'sdfversion', None) is None:
                self.x.sdfversion = self.sdfversion
            elif getattr(self.x, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.x = self.x.to_version(self.sdfversion)
        if self.y is not None and hasattr(self.y, 'to_version'):
            if getattr(self.y, 'sdfversion', None) is None:
                self.y.sdfversion = self.sdfversion
            elif getattr(self.y, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.y = self.y.to_version(self.sdfversion)
        if self.z is not None and hasattr(self.z, 'to_version'):
            if getattr(self.z, 'sdfversion', None) is None:
                self.z.sdfversion = self.sdfversion
            elif getattr(self.z, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.z = self.z.to_version(self.sdfversion)

    def to_version(self, target_version: str) -> "Magnetometer":
        kwargs: dict = {"sdf_version": target_version, "x": self.x.to_version(target_version) if self.x is not None and hasattr(self.x, "to_version") else self.x, "y": self.y.to_version(target_version) if self.y is not None and hasattr(self.y, "to_version") else self.y, "z": self.z.to_version(target_version) if self.z is not None and hasattr(self.z, "to_version") else self.z}
        return self.__class__(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf(version)
        if version is None:
            version = self.sdfversion or "1.12"
        el = ET.Element("magnetometer")
        if self.x is not None:
            _child_res = self.x.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('x')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.y is not None:
            _child_res = self.y.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('y')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.z is not None:
            _child_res = self.z.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('z')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Magnetometer | SDFError":
        _c_x = el.find("x")
        if _c_x is not None:
            _res = cls.X._from_sdf(_c_x, version)
            if isinstance(_res, SDFError):
                return _res.extend("x")
            _x = _res
        else:
            _x = None
        _c_y = el.find("y")
        if _c_y is not None:
            _res = cls.Y._from_sdf(_c_y, version)
            if isinstance(_res, SDFError):
                return _res.extend("y")
            _y = _res
        else:
            _y = None
        _c_z = el.find("z")
        if _c_z is not None:
            _res = cls.Z._from_sdf(_c_z, version)
            if isinstance(_res, SDFError):
                return _res.extend("z")
            _z = _res
        else:
            _z = None
        return cls(sdf_version=version, x=_x, y=_y, z=_z)
