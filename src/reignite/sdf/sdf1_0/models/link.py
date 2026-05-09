from __future__ import annotations

from typing import List
from xml.etree import ElementTree as ET

from .collision import Collision
from .damping import Damping
from .inertial import Inertial
from .origin import Origin
from .projector import Projector
from .sensor import Sensor
from .visual import Visual
from ..model import Model


class Link(Model):
    def __init__(
            self,
            name: str = "__default__",
            gravity: bool = True,
            self_collide: bool = False,
            kinematic: bool = False,
            inertial: "Inertial" = None,
            collision: List["Collision"] = None,
            visual: List["Visual"] = None,
            sensor: List["Sensor"] = None,
            projector: List["Projector"] = None,
            origin: "Origin" = None,
            damping: "Damping" = None
    ):
        self.name = name
        self.gravity = gravity
        self.self_collide = self_collide
        self.kinematic = kinematic
        self.inertial = inertial
        self.collision = collision or []
        self.visual = visual or []
        self.sensor = sensor or []
        self.projector = projector or []
        self.origin = origin
        self.damping = damping

    def to_sdf(self) -> ET.Element:
        el = ET.Element("link")
        if self.name is not None:
            el.set("name", self.name)
        if self.gravity is not None:
            el.set("gravity", str(self.gravity).lower())
        if self.self_collide is not None:
            el.set("self_collide", str(self.self_collide).lower())
        if self.kinematic is not None:
            el.set("kinematic", str(self.kinematic).lower())
        if self.inertial is not None:
            el.append(self.inertial.to_sdf())
        for item in (self.collision or []):
            el.append(item.to_sdf())
        for item in (self.visual or []):
            el.append(item.to_sdf())
        for item in (self.sensor or []):
            el.append(item.to_sdf())
        for item in (self.projector or []):
            el.append(item.to_sdf())
        if self.origin is not None:
            el.append(self.origin.to_sdf())
        if self.damping is not None:
            el.append(self.damping.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Link":
        _name = el.get("name", "__default__")
        _gravity = el.get("gravity", True).strip().lower() == 'true'
        _self_collide = el.get("self_collide", False).strip().lower() == 'true'
        _kinematic = el.get("kinematic", False).strip().lower() == 'true'
        _c_inertial = el.find("inertial")
        _inertial = Inertial.from_sdf(_c_inertial) if _c_inertial is not None else None
        _collision = [Collision.from_sdf(c) for c in el.findall("collision")]
        _visual = [Visual.from_sdf(c) for c in el.findall("visual")]
        _sensor = [Sensor.from_sdf(c) for c in el.findall("sensor")]
        _projector = [Projector.from_sdf(c) for c in el.findall("projector")]
        _c_origin = el.find("origin")
        _origin = Origin.from_sdf(_c_origin) if _c_origin is not None else None
        _c_damping = el.find("damping")
        _damping = Damping.from_sdf(_c_damping) if _c_damping is not None else None
        return cls(name=_name, gravity=_gravity, self_collide=_self_collide, kinematic=_kinematic, inertial=_inertial,
                   collision=_collision, visual=_visual, sensor=_sensor, projector=_projector, origin=_origin,
                   damping=_damping)
