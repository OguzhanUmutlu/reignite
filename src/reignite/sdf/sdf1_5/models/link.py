from __future__ import annotations

from typing import List
from xml.etree import ElementTree as ET

from .audio_sink import AudioSink
from .audio_source import AudioSource
from .battery import Battery
from .collision import Collision
from .frame import Frame
from .inertial import Inertial
from .kinematic import Kinematic
from .must_be_base_link import MustBeBaseLink
from .pose import Pose
from .projector import Projector
from .self_collide import SelfCollide
from .sensor import Sensor
from .velocity_decay import VelocityDecay
from .visual import Visual
from ...sdf1_4.models.gravity import Gravity as _PrevGravity
from ...sdf1_4.models.link import Link as _PrevLink


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
            frame: List["Frame"] = None,
            pose: "Pose" = None,
            inertial: "Inertial" = None,
            collision: List["Collision"] = None,
            visual: List["Visual"] = None,
            sensor: List["Sensor"] = None,
            projector: List["Projector"] = None,
            audio_sink: List["AudioSink"] = None,
            audio_source: List["AudioSource"] = None,
            battery: List["Battery"] = None,
            gravity: "Gravity" = None,
            self_collide: "SelfCollide" = None,
            kinematic: "Kinematic" = None,
            must_be_base_link: "MustBeBaseLink" = None,
            velocity_decay: "VelocityDecay" = None
    ):
        super().__init__(name=name, pose=pose, inertial=inertial, collision=collision, visual=visual, sensor=sensor,
                         projector=projector, audio_sink=audio_sink, audio_source=audio_source, gravity=gravity,
                         self_collide=self_collide, kinematic=kinematic, must_be_base_link=must_be_base_link,
                         velocity_decay=velocity_decay)
        self.frame = frame or []
        self.battery = battery or []

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        for item in (self.frame or []):
            el.append(item.to_sdf())
        for item in (self.battery or []):
            el.append(item.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Link":
        _base = _PrevLink.from_sdf(el)
        _frame = [Frame.from_sdf(c) for c in el.findall("frame")]
        _battery = [Battery.from_sdf(c) for c in el.findall("battery")]
        return cls(name=_base.name, frame=_frame, pose=_base.pose, inertial=_base.inertial, collision=_base.collision,
                   visual=_base.visual, sensor=_base.sensor, projector=_base.projector, audio_sink=_base.audio_sink,
                   audio_source=_base.audio_source, battery=_battery, gravity=_base.gravity,
                   self_collide=_base.self_collide, kinematic=_base.kinematic,
                   must_be_base_link=_base.must_be_base_link, velocity_decay=_base.velocity_decay)
