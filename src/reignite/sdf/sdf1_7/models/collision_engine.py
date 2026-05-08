from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_6.models.ode import Ode as _PrevOde
from ...sdf1_6.models.bullet import Bullet as _PrevBullet
from ...sdf1_6.models.collision_engine import CollisionEngine as _PrevCollisionEngine


class Ode(_PrevOde):
    def __init__(self, type: str = "__default__"):
        super().__init__(type=type)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Ode":
        _base = _PrevOde.from_sdf(el)
        return cls(type=_base.type)


class Bullet(_PrevBullet):
    def __init__(self, type: str = "__default__"):
        super().__init__(type=type)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Bullet":
        _base = _PrevBullet.from_sdf(el)
        return cls(type=_base.type)


class CollisionEngine(_PrevCollisionEngine):
    def __init__(self, ode: "Ode" = None, bullet: "Bullet" = None):
        super().__init__(ode=ode, bullet=bullet)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "CollisionEngine":
        _base = _PrevCollisionEngine.from_sdf(el)
        return cls(ode=_base.ode, bullet=_base.bullet)
