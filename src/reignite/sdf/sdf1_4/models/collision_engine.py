from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class Ode(Model):
    def __init__(self, type: str = "__default__"):
        self.type = type

    def to_sdf(self) -> ET.Element:
        el = ET.Element("ode")
        if self.type is not None:
            el.set("type", self.type)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Ode":
        _type = el.get("type", "__default__")
        return cls(type=_type)


class Bullet(Model):
    def __init__(self, type: str = "__default__"):
        self.type = type

    def to_sdf(self) -> ET.Element:
        el = ET.Element("bullet")
        if self.type is not None:
            el.set("type", self.type)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Bullet":
        _type = el.get("type", "__default__")
        return cls(type=_type)


class CollisionEngine(Model):
    def __init__(self, ode: "Ode" = None, bullet: "Bullet" = None):
        self.ode = ode
        self.bullet = bullet

    def to_sdf(self) -> ET.Element:
        el = ET.Element("collision_engine")
        if self.ode is not None:
            el.append(self.ode.to_sdf())
        if self.bullet is not None:
            el.append(self.bullet.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "CollisionEngine":
        _c_ode = el.find("ode")
        _ode = Ode.from_sdf(_c_ode) if _c_ode is not None else None
        _c_bullet = el.find("bullet")
        _bullet = Bullet.from_sdf(_c_bullet) if _c_bullet is not None else None
        return cls(ode=_ode, bullet=_bullet)
