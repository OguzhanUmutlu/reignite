from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..model import Model
from ...sdf1_3.models.gravity import Gravity as _PrevGravity
from ...sdf1_3.models.link import Link as _PrevLink
from .inertial import Inertial
from .collision import Collision
from .visual import Visual
from .sensor import Sensor
from .projector import Projector
from .audio_sink import AudioSink
from .audio_source import AudioSource
from .self_collide import SelfCollide
from .kinematic import Kinematic
from .pose import Pose
from .must_be_base_link import MustBeBaseLink
from .velocity_decay import VelocityDecay


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
        audio_sink: List["AudioSink"] = None,
        audio_source: List["AudioSource"] = None,
        gravity: "Gravity" = None,
        self_collide: "SelfCollide" = None,
        kinematic: "Kinematic" = None,
        pose: "Pose" = None,
        must_be_base_link: "MustBeBaseLink" = None,
        velocity_decay: "VelocityDecay" = None
    ):
        super().__init__(name=name, inertial=inertial, collision=collision, visual=visual, sensor=sensor, projector=projector, gravity=gravity, self_collide=self_collide, kinematic=kinematic, pose=pose, velocity_decay=velocity_decay)
        self.audio_sink = audio_sink or []
        self.audio_source = audio_source or []
        self.must_be_base_link = must_be_base_link

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        for item in (self.audio_sink or []):
            el.append(item.to_sdf())
        for item in (self.audio_source or []):
            el.append(item.to_sdf())
        if self.must_be_base_link is not None:
            el.append(self.must_be_base_link.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Link":
        _base = _PrevLink.from_sdf(el)
        _audio_sink = [AudioSink.from_sdf(c) for c in el.findall("audio_sink")]
        _audio_source = [AudioSource.from_sdf(c) for c in el.findall("audio_source")]
        _c_must_be_base_link = el.find("must_be_base_link")
        _must_be_base_link = MustBeBaseLink.from_sdf(_c_must_be_base_link) if _c_must_be_base_link is not None else None
        return cls(name=_base.name, inertial=_base.inertial, collision=_base.collision, visual=_base.visual, sensor=_base.sensor, projector=_base.projector, audio_sink=_audio_sink, audio_source=_audio_source, gravity=_base.gravity, self_collide=_base.self_collide, kinematic=_base.kinematic, pose=_base.pose, must_be_base_link=_must_be_base_link, velocity_decay=_base.velocity_decay)
