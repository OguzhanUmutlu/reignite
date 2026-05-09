### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.model import BaseModel
from ..utils.errors import SDFError


class Ode(BaseModel):
    def __init__(self, sdf_version: str, type: str = "__default__"):
        self.__version__ = sdf_version
        self.type = type

    def to_version(self, target_version: str) -> "Ode":
        kwargs = {"sdf_version": target_version}
        kwargs["type"] = self.type
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("ode")
        if self.type is not None:
            el.set("type", self.type)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _type = el.get("type", "__default__")
        if isinstance(_type, SDFError):
            return _type.extend("@type")
        return cls(sdf_version=version, type=_type)


class Bullet(BaseModel):
    def __init__(self, sdf_version: str, type: str = "__default__"):
        self.__version__ = sdf_version
        self.type = type

    def to_version(self, target_version: str) -> "Bullet":
        kwargs = {"sdf_version": target_version}
        kwargs["type"] = self.type
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("bullet")
        if self.type is not None:
            el.set("type", self.type)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _type = el.get("type", "__default__")
        if isinstance(_type, SDFError):
            return _type.extend("@type")
        return cls(sdf_version=version, type=_type)


class CollisionEngine(BaseModel):
    def __init__(self, sdf_version: str, ode: "Ode" = None, bullet: "Bullet" = None):
        self.__version__ = sdf_version
        self.ode = ode
        self.bullet = bullet

    def to_version(self, target_version: str) -> "CollisionEngine":
        kwargs = {"sdf_version": target_version}
        kwargs["ode"] = self.ode.to_version(target_version) if self.ode is not None else None
        kwargs["bullet"] = self.bullet.to_version(target_version) if self.bullet is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("collision_engine")
        if self.ode is not None:
            el.append(self.ode.to_sdf(version))
        if self.bullet is not None:
            el.append(self.bullet.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_ode = el.find("ode")
        if _c_ode is not None:
            _res = Ode._from_sdf(_c_ode, version)
            if isinstance(_res, SDFError):
                return _res.extend("ode")
            _ode = _res
        else:
            _ode = None
        _c_bullet = el.find("bullet")
        if _c_bullet is not None:
            _res = Bullet._from_sdf(_c_bullet, version)
            if isinstance(_res, SDFError):
                return _res.extend("bullet")
            _bullet = _res
        else:
            _bullet = None
        return cls(sdf_version=version, ode=_ode, bullet=_bullet)
