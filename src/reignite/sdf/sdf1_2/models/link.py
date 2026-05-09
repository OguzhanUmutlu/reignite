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
from ..model import Model
from ...sdf1_0.models.link import Link as _PrevLink


class Gravity(Model):
    def __init__(self, gravity: bool = True):
        self.gravity = gravity

    def to_sdf(self) -> ET.Element:
        el = ET.Element("gravity")
        if self.gravity is not None:
            el.text = str(self.gravity).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Gravity":
        _text = el.text or True
        _gravity = _text.strip().lower() == 'true'
        return cls(gravity=_gravity)


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
                         projector=projector, gravity=gravity, self_collide=self_collide, kinematic=kinematic)
        self.pose = pose
        self.velocity_decay = velocity_decay

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.pose is not None:
            el.append(self.pose.to_sdf())
        if self.velocity_decay is not None:
            el.append(self.velocity_decay.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Link":
        _base = _PrevLink.from_sdf(el)
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose) if _c_pose is not None else None
        _c_velocity_decay = el.find("velocity_decay")
        _velocity_decay = VelocityDecay.from_sdf(_c_velocity_decay) if _c_velocity_decay is not None else None
        return cls(name=_base.name, inertial=_base.inertial, collision=_base.collision, visual=_base.visual,
                   sensor=_base.sensor, projector=_base.projector, gravity=_base.gravity,
                   self_collide=_base.self_collide, kinematic=_base.kinematic, pose=_pose,
                   velocity_decay=_velocity_decay)
