from __future__ import annotations

import math
from xml.etree import ElementTree as ET

from .geometry import Geometry
from .mass import Mass
from .origin import Origin
from .surface import Surface
from ..model import Model


def _parse_int32(raw: str) -> int:
    v = int(raw)
    if not (-2147483648 <= v <= 2147483647):
        raise ValueError(f"int32 out of range: {v}")
    return v


def _parse_uint32(raw: str) -> int:
    v = int(raw)
    if not (0 <= v <= 4294967295):
        raise ValueError(f"uint32 out of range: {v}")
    return v


def _parse_double(raw: str) -> float:
    v = float(raw)
    if not math.isfinite(v) or abs(v) > 1.7976931348623157e+308:
        raise ValueError(f"double out of range: {raw}")
    return v


class MaxContacts(Model):
    def __init__(self, max_contacts: int = 10):
        self.max_contacts = max_contacts

    def to_sdf(self) -> ET.Element:
        el = ET.Element("max_contacts")
        if self.max_contacts is not None:
            el.text = str(self.max_contacts)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "MaxContacts":
        _text = el.text or 10
        _max_contacts = _parse_int32(_text)
        return cls(max_contacts=_max_contacts)


class Collision(Model):
    def __init__(
            self,
            name: str = "__default__",
            laser_retro: float = 0,
            geometry: "Geometry" = None,
            surface: "Surface" = None,
            max_contacts: "MaxContacts" = None,
            mass: "Mass" = None,
            origin: "Origin" = None
    ):
        self.name = name
        self.laser_retro = laser_retro
        self.geometry = geometry
        self.surface = surface
        self.max_contacts = max_contacts
        self.mass = mass
        self.origin = origin

    def to_sdf(self) -> ET.Element:
        el = ET.Element("collision")
        if self.name is not None:
            el.set("name", self.name)
        if self.laser_retro is not None:
            el.set("laser_retro", str(self.laser_retro))
        if self.geometry is not None:
            el.append(self.geometry.to_sdf())
        if self.surface is not None:
            el.append(self.surface.to_sdf())
        if self.max_contacts is not None:
            el.append(self.max_contacts.to_sdf())
        if self.mass is not None:
            el.append(self.mass.to_sdf())
        if self.origin is not None:
            el.append(self.origin.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Collision":
        _name = el.get("name", "__default__")
        _laser_retro = _parse_double(el.get("laser_retro", 0))
        _c_geometry = el.find("geometry")
        _geometry = Geometry.from_sdf(_c_geometry) if _c_geometry is not None else None
        _c_surface = el.find("surface")
        _surface = Surface.from_sdf(_c_surface) if _c_surface is not None else None
        _c_max_contacts = el.find("max_contacts")
        _max_contacts = MaxContacts.from_sdf(_c_max_contacts) if _c_max_contacts is not None else None
        _c_mass = el.find("mass")
        _mass = Mass.from_sdf(_c_mass) if _c_mass is not None else None
        _c_origin = el.find("origin")
        _origin = Origin.from_sdf(_c_origin) if _c_origin is not None else None
        return cls(name=_name, laser_retro=_laser_retro, geometry=_geometry, surface=_surface,
                   max_contacts=_max_contacts, mass=_mass, origin=_origin)
