from __future__ import annotations

from xml.etree import ElementTree as ET

from .bounce import Bounce
from .friction import Friction
from .soft_contact import SoftContact
from ...sdf1_6.models.bullet import Bullet as _PrevBullet
from ...sdf1_6.models.contact import Contact as _PrevContact
from ...sdf1_6.models.ode import Ode as _PrevOde
from ...sdf1_6.models.surface import Surface as _PrevSurface


class Ode(_PrevOde):
    def __init__(self, slip: "Slip" = None):
        super().__init__()
        self.slip = slip

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.slip is not None:
            el.append(self.slip.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Ode":
        _c_slip = el.find("slip")
        _slip = Slip.from_sdf(_c_slip) if _c_slip is not None else None
        return cls(slip=_slip)


class Bullet(_PrevBullet):
    def __init__(
            self,
            friction: "Friction" = None,
            friction2: "Friction2" = None,
            fdir1: "Fdir1" = None,
            rolling_friction: "RollingFriction" = None
    ):
        super().__init__()
        self.friction = friction
        self.friction2 = friction2
        self.fdir1 = fdir1
        self.rolling_friction = rolling_friction

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.friction is not None:
            el.append(self.friction.to_sdf())
        if self.friction2 is not None:
            el.append(self.friction2.to_sdf())
        if self.fdir1 is not None:
            el.append(self.fdir1.to_sdf())
        if self.rolling_friction is not None:
            el.append(self.rolling_friction.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Bullet":
        _c_friction = el.find("friction")
        _friction = Friction.from_sdf(_c_friction) if _c_friction is not None else None
        _c_friction2 = el.find("friction2")
        _friction2 = Friction2.from_sdf(_c_friction2) if _c_friction2 is not None else None
        _c_fdir1 = el.find("fdir1")
        _fdir1 = Fdir1.from_sdf(_c_fdir1) if _c_fdir1 is not None else None
        _c_rolling_friction = el.find("rolling_friction")
        _rolling_friction = RollingFriction.from_sdf(_c_rolling_friction) if _c_rolling_friction is not None else None
        return cls(friction=_friction, friction2=_friction2, fdir1=_fdir1, rolling_friction=_rolling_friction)


class Contact(_PrevContact):
    def __init__(
            self,
            collide_without_contact: "CollideWithoutContact" = None,
            collide_without_contact_bitmask: "CollideWithoutContactBitmask" = None,
            collide_bitmask: "CollideBitmask" = None,
            category_bitmask: "CategoryBitmask" = None,
            poissons_ratio: "PoissonsRatio" = None,
            elastic_modulus: "ElasticModulus" = None,
            ode: "Ode" = None,
            bullet: "Bullet" = None
    ):
        super().__init__()
        self.collide_without_contact = collide_without_contact
        self.collide_without_contact_bitmask = collide_without_contact_bitmask
        self.collide_bitmask = collide_bitmask
        self.category_bitmask = category_bitmask
        self.poissons_ratio = poissons_ratio
        self.elastic_modulus = elastic_modulus
        self.ode = ode
        self.bullet = bullet

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.collide_without_contact is not None:
            el.append(self.collide_without_contact.to_sdf())
        if self.collide_without_contact_bitmask is not None:
            el.append(self.collide_without_contact_bitmask.to_sdf())
        if self.collide_bitmask is not None:
            el.append(self.collide_bitmask.to_sdf())
        if self.category_bitmask is not None:
            el.append(self.category_bitmask.to_sdf())
        if self.poissons_ratio is not None:
            el.append(self.poissons_ratio.to_sdf())
        if self.elastic_modulus is not None:
            el.append(self.elastic_modulus.to_sdf())
        if self.ode is not None:
            el.append(self.ode.to_sdf())
        if self.bullet is not None:
            el.append(self.bullet.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Contact":
        _c_collide_without_contact = el.find("collide_without_contact")
        _collide_without_contact = CollideWithoutContact.from_sdf(
            _c_collide_without_contact) if _c_collide_without_contact is not None else None
        _c_collide_without_contact_bitmask = el.find("collide_without_contact_bitmask")
        _collide_without_contact_bitmask = CollideWithoutContactBitmask.from_sdf(
            _c_collide_without_contact_bitmask) if _c_collide_without_contact_bitmask is not None else None
        _c_collide_bitmask = el.find("collide_bitmask")
        _collide_bitmask = CollideBitmask.from_sdf(_c_collide_bitmask) if _c_collide_bitmask is not None else None
        _c_category_bitmask = el.find("category_bitmask")
        _category_bitmask = CategoryBitmask.from_sdf(_c_category_bitmask) if _c_category_bitmask is not None else None
        _c_poissons_ratio = el.find("poissons_ratio")
        _poissons_ratio = PoissonsRatio.from_sdf(_c_poissons_ratio) if _c_poissons_ratio is not None else None
        _c_elastic_modulus = el.find("elastic_modulus")
        _elastic_modulus = ElasticModulus.from_sdf(_c_elastic_modulus) if _c_elastic_modulus is not None else None
        _c_ode = el.find("ode")
        _ode = Ode.from_sdf(_c_ode) if _c_ode is not None else None
        _c_bullet = el.find("bullet")
        _bullet = Bullet.from_sdf(_c_bullet) if _c_bullet is not None else None
        return cls(collide_without_contact=_collide_without_contact,
                   collide_without_contact_bitmask=_collide_without_contact_bitmask, collide_bitmask=_collide_bitmask,
                   category_bitmask=_category_bitmask, poissons_ratio=_poissons_ratio, elastic_modulus=_elastic_modulus,
                   ode=_ode, bullet=_bullet)


class Surface(_PrevSurface):
    def __init__(
            self,
            bounce: "Bounce" = None,
            friction: "Friction" = None,
            contact: "Contact" = None,
            soft_contact: "SoftContact" = None
    ):
        super().__init__(bounce=bounce, friction=friction, contact=contact, soft_contact=soft_contact)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Surface":
        _base = _PrevSurface.from_sdf(el)
        return cls(bounce=_base.bounce, friction=_base.friction, contact=_base.contact, soft_contact=_base.soft_contact)
