from __future__ import annotations

from typing import List
from xml.etree import ElementTree as ET

from .collision import Collision
from .inertial import Inertial
from .kinematic import Kinematic
from .pose import Pose
from .projector import Projector
from .self_collide import SelfCollide
from .sensor import Sensor
from .velocity_decay import VelocityDecay
from .visual import Visual
from ...sdf1_2.models.gravity import Gravity as _PrevGravity
from ...sdf1_2.models.link import Link as _PrevLink


class Gravity(_PrevGravity):
    def __init__(self, gravity: bool = True):
        super().__init__(gravity=gravity)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Gravity":
        _base = _PrevGravity.from_sdf(el)
        return cls(gravity=_base.gravity)


class Link(_PrevLink):
    def __init__(
            self,
            name: str = "__default__",
            inertial: "Inertial" = None,
            collision: List["Collision"] = None,
            visual: List["Visual"] = None,
            sensor: List["Sensor"] = None,
            projector: List["Projector"] = None,
            gravity: "Gravity" = None,
            self_collide: "SelfCollide" = None,
            kinematic: "Kinematic" = None,
            pose: "Pose" = None,
            velocity_decay: "VelocityDecay" = None
    ):
        super().__init__(name=name, inertial=inertial, collision=collision, visual=visual, sensor=sensor,
                         projector=projector, gravity=gravity, self_collide=self_collide, kinematic=kinematic,
                         pose=pose, velocity_decay=velocity_decay)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Link":
        _base = _PrevLink.from_sdf(el)
        return cls(name=_base.name, inertial=_base.inertial, collision=_base.collision, visual=_base.visual,
                   sensor=_base.sensor, projector=_base.projector, gravity=_base.gravity,
                   self_collide=_base.self_collide, kinematic=_base.kinematic, pose=_base.pose,
                   velocity_decay=_base.velocity_decay)
