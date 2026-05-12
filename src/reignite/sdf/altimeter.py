### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

from ..utils.model import BaseModel
from ..utils.errors import SDFError

if typing.TYPE_CHECKING:
    from ..elements.noise import Noise


class Altimeter(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        vertical_position: "VerticalPosition" = None,
        vertical_velocity: "VerticalVelocity" = None
    ):
        self.__version__ = sdf_version
        self.vertical_position = vertical_position
        self.vertical_velocity = vertical_velocity
        if self.vertical_position is not None:
            if getattr(self.vertical_position, '__version__', None) is None:
                self.vertical_position.__version__ = self.__version__
            elif getattr(self.vertical_position, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.vertical_position = self.vertical_position.to_version(self.__version__)
        if self.vertical_velocity is not None:
            if getattr(self.vertical_velocity, '__version__', None) is None:
                self.vertical_velocity.__version__ = self.__version__
            elif getattr(self.vertical_velocity, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.vertical_velocity = self.vertical_velocity.to_version(self.__version__)

    def to_version(self, target_version: str) -> "Altimeter":
        kwargs = {"sdf_version": target_version}
        kwargs["vertical_position"] = self.vertical_position.to_version(target_version) if self.vertical_position is not None else None
        kwargs["vertical_velocity"] = self.vertical_velocity.to_version(target_version) if self.vertical_velocity is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("altimeter")
        if self.vertical_position is not None:
            el.append(self.vertical_position.to_sdf(version))
        if self.vertical_velocity is not None:
            el.append(self.vertical_velocity.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_vertical_position = el.find("vertical_position")
        if _c_vertical_position is not None:
            _res = VerticalPosition._from_sdf(_c_vertical_position, version)
            if isinstance(_res, SDFError):
                return _res.extend("vertical_position")
            _vertical_position = _res
        else:
            _vertical_position = None
        _c_vertical_velocity = el.find("vertical_velocity")
        if _c_vertical_velocity is not None:
            _res = VerticalVelocity._from_sdf(_c_vertical_velocity, version)
            if isinstance(_res, SDFError):
                return _res.extend("vertical_velocity")
            _vertical_velocity = _res
        else:
            _vertical_velocity = None
        return cls(sdf_version=version, vertical_position=_vertical_position, vertical_velocity=_vertical_velocity)


class VerticalPosition(BaseModel):
    def __init__(self, sdf_version: str | None = None, noise: "Noise" = None):
        self.__version__ = sdf_version
        self.noise = noise
        if self.noise is not None:
            if getattr(self.noise, '__version__', None) is None:
                self.noise.__version__ = self.__version__
            elif getattr(self.noise, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.noise = self.noise.to_version(self.__version__)

    def to_version(self, target_version: str) -> "VerticalPosition":
        from ..elements.noise import Noise
        kwargs = {"sdf_version": target_version}
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        from ..elements.noise import Noise
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("vertical_position")
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


class VerticalVelocity(BaseModel):
    def __init__(self, sdf_version: str | None = None, noise: "Noise" = None):
        self.__version__ = sdf_version
        self.noise = noise
        if self.noise is not None:
            if getattr(self.noise, '__version__', None) is None:
                self.noise.__version__ = self.__version__
            elif getattr(self.noise, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.noise = self.noise.to_version(self.__version__)

    def to_version(self, target_version: str) -> "VerticalVelocity":
        from ..elements.noise import Noise
        kwargs = {"sdf_version": target_version}
        kwargs["noise"] = self.noise.to_version(target_version) if self.noise is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        from ..elements.noise import Noise
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("vertical_velocity")
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
