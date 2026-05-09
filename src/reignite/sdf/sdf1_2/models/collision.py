from __future__ import annotations

import math
from xml.etree import ElementTree as ET

from .geometry import Geometry
from .laser_retro import LaserRetro
from .pose import Pose
from .surface import Surface
from ...sdf1_0.models.collision import Collision as _PrevCollision
from ...sdf1_0.models.max_contacts import MaxContacts as _PrevMaxContacts


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


class MaxContacts(_PrevMaxContacts):
    def __init__(self, max_contacts: int = 10):
        super().__init__(max_contacts=max_contacts)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "MaxContacts":
        _base = _PrevMaxContacts.from_sdf(el)
        return cls(max_contacts=_base.max_contacts)


class Collision(_PrevCollision):
    def __init__(
            self,
            name: str = "__default__",
            geometry: "Geometry" = None,
            surface: "Surface" = None,
            laser_retro: "LaserRetro" = None,
            max_contacts: "MaxContacts" = None,
            pose: "Pose" = None
    ):
        super().__init__(name=name)
        self.geometry = geometry
        self.surface = surface
        self.laser_retro = laser_retro
        self.max_contacts = max_contacts
        self.pose = pose

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.geometry is not None:
            el.append(self.geometry.to_sdf())
        if self.surface is not None:
            el.append(self.surface.to_sdf())
        if self.laser_retro is not None:
            el.append(self.laser_retro.to_sdf())
        if self.max_contacts is not None:
            el.append(self.max_contacts.to_sdf())
        if self.pose is not None:
            el.append(self.pose.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Collision":
        _base = _PrevCollision.from_sdf(el)
        _c_geometry = el.find("geometry")
        _geometry = Geometry.from_sdf(_c_geometry) if _c_geometry is not None else None
        _c_surface = el.find("surface")
        _surface = Surface.from_sdf(_c_surface) if _c_surface is not None else None
        _c_laser_retro = el.find("laser_retro")
        _laser_retro = LaserRetro.from_sdf(_c_laser_retro) if _c_laser_retro is not None else None
        _c_max_contacts = el.find("max_contacts")
        _max_contacts = MaxContacts.from_sdf(_c_max_contacts) if _c_max_contacts is not None else None
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose) if _c_pose is not None else None
        return cls(name=_base.name, geometry=_geometry, surface=_surface, laser_retro=_laser_retro,
                   max_contacts=_max_contacts, pose=_pose)
