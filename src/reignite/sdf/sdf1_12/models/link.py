from __future__ import annotations

from typing import List
from xml.etree import ElementTree as ET

from .audio_sink import AudioSink
from .audio_source import AudioSource
from .battery import Battery
from .collision import Collision
from .enable_wind import EnableWind
from .gravity import Gravity
from .inertial import Inertial
from .kinematic import Kinematic
from .light import Light
from .must_be_base_link import MustBeBaseLink
from .particle_emitter import ParticleEmitter
from .pose import Pose
from .projector import Projector
from .self_collide import SelfCollide
from .sensor import Sensor
from .velocity_decay import VelocityDecay
from .visual import Visual
from ...sdf1_11.models.link import Link as _PrevLink


class Link(_PrevLink):
    def __init__(
            self,
            name: str = "__default__",
            pose: "Pose" = None,
            inertial: "Inertial" = None,
            collision: List["Collision"] = None,
            visual: List["Visual"] = None,
            sensor: List["Sensor"] = None,
            projector: List["Projector"] = None,
            audio_sink: List["AudioSink"] = None,
            audio_source: List["AudioSource"] = None,
            battery: List["Battery"] = None,
            light: List["Light"] = None,
            particle_emitter: List["ParticleEmitter"] = None,
            gravity: "Gravity" = None,
            enable_wind: "EnableWind" = None,
            self_collide: "SelfCollide" = None,
            kinematic: "Kinematic" = None,
            must_be_base_link: "MustBeBaseLink" = None,
            velocity_decay: "VelocityDecay" = None
    ):
        super().__init__(name=name, pose=pose, inertial=inertial, collision=collision, visual=visual, sensor=sensor,
                         projector=projector, audio_sink=audio_sink, audio_source=audio_source, battery=battery,
                         light=light, particle_emitter=particle_emitter, gravity=gravity, enable_wind=enable_wind,
                         self_collide=self_collide, kinematic=kinematic, must_be_base_link=must_be_base_link,
                         velocity_decay=velocity_decay)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Link":
        _base = _PrevLink.from_sdf(el)
        return cls(name=_base.name, pose=_base.pose, inertial=_base.inertial, collision=_base.collision,
                   visual=_base.visual, sensor=_base.sensor, projector=_base.projector, audio_sink=_base.audio_sink,
                   audio_source=_base.audio_source, battery=_base.battery, light=_base.light,
                   particle_emitter=_base.particle_emitter, gravity=_base.gravity, enable_wind=_base.enable_wind,
                   self_collide=_base.self_collide, kinematic=_base.kinematic,
                   must_be_base_link=_base.must_be_base_link, velocity_decay=_base.velocity_decay)
