### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

from ..utils.model import BaseModel
from ..utils.errors import SDFError

if typing.TYPE_CHECKING:
    from ..elements.noise import Noise


class Magnetometer(BaseModel):
    def __init__(self, sdf_version: str, x: "X" = None, y: "Y" = None, z: "Z" = None):
        self.__version__ = sdf_version
        self.x = x
        self.y = y
        self.z = z

    def to_version(self, target_version: str) -> "Magnetometer":
        kwargs = {"sdf_version": target_version}
        kwargs["x"] = self.x.to_version(target_version) if self.x is not None else None
        kwargs["y"] = self.y.to_version(target_version) if self.y is not None else None
        kwargs["z"] = self.z.to_version(target_version) if self.z is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("magnetometer")
        if self.x is not None:
            el.append(self.x.to_sdf(version))
        if self.y is not None:
            el.append(self.y.to_sdf(version))
        if self.z is not None:
            el.append(self.z.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_x = el.find("x")
        if _c_x is not None:
            _res = X._from_sdf(_c_x, version)
            if isinstance(_res, SDFError):
                return _res.extend("x")
            _x = _res
        else:
            _x = None
        _c_y = el.find("y")
        if _c_y is not None:
            _res = Y._from_sdf(_c_y, version)
            if isinstance(_res, SDFError):
                return _res.extend("y")
            _y = _res
        else:
            _y = None
        _c_z = el.find("z")
        if _c_z is not None:
            _res = Z._from_sdf(_c_z, version)
            if isinstance(_res, SDFError):
                return _res.extend("z")
            _z = _res
        else:
            _z = None
        return cls(sdf_version=version, x=_x, y=_y, z=_z)


class X(BaseModel):
    def __init__(self, sdf_version: str, noise: "Noise" = None):
        self.__version__ = sdf_version
        self.noise = noise

    def to_version(self, target_version: str) -> "X":
        from ..elements.noise import Noise
        kwargs = {"sdf_version": target_version}
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        from ..elements.noise import Noise
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("x")
        if self.noise is None:
            self.noise = Noise(sdf_version=version)
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
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


class Y(BaseModel):
    def __init__(self, sdf_version: str, noise: "Noise" = None):
        self.__version__ = sdf_version
        self.noise = noise

    def to_version(self, target_version: str) -> "Y":
        from ..elements.noise import Noise
        kwargs = {"sdf_version": target_version}
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        from ..elements.noise import Noise
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("y")
        if self.noise is None:
            self.noise = Noise(sdf_version=version)
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
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


class Z(BaseModel):
    def __init__(self, sdf_version: str, noise: "Noise" = None):
        self.__version__ = sdf_version
        self.noise = noise

    def to_version(self, target_version: str) -> "Z":
        from ..elements.noise import Noise
        kwargs = {"sdf_version": target_version}
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        from ..elements.noise import Noise
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("z")
        if self.noise is None:
            self.noise = Noise(sdf_version=version)
        if self.noise is not None:
            el.append(self.noise.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
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
