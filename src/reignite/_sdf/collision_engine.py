### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.model import BaseModel
from ..utils.errors import SDFError


# noinspection PyUnusedImports
class CollisionEngine(BaseModel):
    class Bullet(BaseModel):
        def __init__(self, sdf_version: str | None = None, type: str | None = None):
            super().__init__(sdf_version)
            self.type = type

        def to_version(self, target_version: str) -> "CollisionEngine.Bullet":
            kwargs: dict = {"sdf_version": target_version, "type": self.type}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf()
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
        def __init__(self, sdf_version: str | None = None, type: str | None = None):
            super().__init__(sdf_version)
            self.type = type

        def to_version(self, target_version: str) -> "CollisionEngine.Ode":
            kwargs: dict = {"sdf_version": target_version, "type": self.type}
            return self.__class__(**kwargs)

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.sdfversion is None and version is not None:
                self.sdfversion = version
            elif version is not None and version != self.sdfversion:
                return self.to_version(str(version)).to_sdf()
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
        if self.bullet is not None and hasattr(self.bullet, 'to_version'):
            if getattr(self.bullet, 'sdfversion', None) is None:
                self.bullet.sdfversion = self.sdfversion
            elif getattr(self.bullet, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.bullet = self.bullet.to_version(self.sdfversion)
        if self.ode is not None and hasattr(self.ode, 'to_version'):
            if getattr(self.ode, 'sdfversion', None) is None:
                self.ode.sdfversion = self.sdfversion
            elif getattr(self.ode, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.ode = self.ode.to_version(self.sdfversion)

    def to_version(self, target_version: str) -> "CollisionEngine":
        kwargs: dict = {"sdf_version": target_version, "bullet": self.bullet.to_version(target_version) if self.bullet is not None and hasattr(self.bullet, "to_version") else self.bullet, "ode": self.ode.to_version(target_version) if self.ode is not None and hasattr(self.ode, "to_version") else self.ode}
        return self.__class__(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf()
        el = ET.Element("collision_engine")
        if self.bullet is not None:
            _child_res = self.bullet.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('bullet')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.ode is not None:
            _child_res = self.ode.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('ode')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
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
