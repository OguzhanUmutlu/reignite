### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

from ..utils.model import BaseModel
from ..utils.errors import SDFError


class CollisionEngine(BaseModel):
    class Bullet(BaseModel):
        def __init__(self, sdf_version: str | None = None, type: str = "__default__"):
            super().__init__(sdf_version)
            self.type = type

        def to_version(self, target_version: str) -> "CollisionEngine.Bullet":
            kwargs = {"sdf_version": target_version}
            kwargs["type"] = self.type
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("bullet")
            if self.type is not None:
                el.set("type", self.type)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "CollisionEngine.Bullet | SDFError":
            _type = el.get("type", "__default__")
            if isinstance(_type, SDFError):
                return _type.extend("@type")
            return cls(sdf_version=version, type=_type)

    class Ode(BaseModel):
        def __init__(self, sdf_version: str | None = None, type: str = "__default__"):
            super().__init__(sdf_version)
            self.type = type

        def to_version(self, target_version: str) -> "CollisionEngine.Ode":
            kwargs = {"sdf_version": target_version}
            kwargs["type"] = self.type
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("ode")
            if self.type is not None:
                el.set("type", self.type)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "CollisionEngine.Ode | SDFError":
            _type = el.get("type", "__default__")
            if isinstance(_type, SDFError):
                return _type.extend("@type")
            return cls(sdf_version=version, type=_type)

    def __init__(
        self,
        sdf_version: str | None = None,
        bullet: "CollisionEngine.Bullet" = None,
        ode: "CollisionEngine.Ode" = None
    ):
        super().__init__(sdf_version)
        self.bullet = bullet
        self.ode = ode
        if self.bullet is not None:
            if getattr(self.bullet, '__version__', None) is None:
                self.bullet.__version__ = self.__version__
            elif getattr(self.bullet, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.bullet = self.bullet.to_version(self.__version__)
        if self.ode is not None:
            if getattr(self.ode, '__version__', None) is None:
                self.ode.__version__ = self.__version__
            elif getattr(self.ode, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.ode = self.ode.to_version(self.__version__)

    def to_version(self, target_version: str) -> "CollisionEngine":
        kwargs = {"sdf_version": target_version}
        kwargs["bullet"] = self.bullet.to_version(target_version) if self.bullet is not None else None
        kwargs["ode"] = self.ode.to_version(target_version) if self.ode is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("collision_engine")
        if self.bullet is not None:
            el.append(self.bullet.to_sdf(version))
        if self.ode is not None:
            el.append(self.ode.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "CollisionEngine | SDFError":
        _c_bullet = el.find("bullet")
        if _c_bullet is not None:
            _res = cls.Bullet._from_sdf(_c_bullet, version)
            if isinstance(_res, SDFError):
                return _res.extend("bullet")
            _bullet = _res
        else:
            _bullet = None
        _c_ode = el.find("ode")
        if _c_ode is not None:
            _res = cls.Ode._from_sdf(_c_ode, version)
            if isinstance(_res, SDFError):
                return _res.extend("ode")
            _ode = _res
        else:
            _ode = None
        return cls(sdf_version=version, bullet=_bullet, ode=_ode)
