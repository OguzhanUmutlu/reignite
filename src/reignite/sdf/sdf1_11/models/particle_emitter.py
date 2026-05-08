from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_10.models.particle_emitter import ParticleEmitter as _PrevParticleEmitter
from .pose import Pose
from .material import Material
from .emitting import Emitting
from .duration import Duration
from .size import Size
from .particle_size import ParticleSize
from .lifetime import Lifetime
from .rate import Rate
from .min_velocity import MinVelocity
from .max_velocity import MaxVelocity
from .scale_rate import ScaleRate
from .color_start import ColorStart
from .color_end import ColorEnd
from .color_range_image import ColorRangeImage
from .topic import Topic
from .particle_scatter_ratio import ParticleScatterRatio


class ParticleEmitter(_PrevParticleEmitter):
    def __init__(
        self,
        name: str = "__default__",
        type: str = "point",
        pose: "Pose" = None,
        material: "Material" = None,
        emitting: "Emitting" = None,
        duration: "Duration" = None,
        size: "Size" = None,
        particle_size: "ParticleSize" = None,
        lifetime: "Lifetime" = None,
        rate: "Rate" = None,
        min_velocity: "MinVelocity" = None,
        max_velocity: "MaxVelocity" = None,
        scale_rate: "ScaleRate" = None,
        color_start: "ColorStart" = None,
        color_end: "ColorEnd" = None,
        color_range_image: "ColorRangeImage" = None,
        topic: "Topic" = None,
        particle_scatter_ratio: "ParticleScatterRatio" = None
    ):
        super().__init__(name=name, type=type, pose=pose, material=material, emitting=emitting, duration=duration, size=size, particle_size=particle_size, lifetime=lifetime, rate=rate, min_velocity=min_velocity, max_velocity=max_velocity, scale_rate=scale_rate, color_start=color_start, color_end=color_end, color_range_image=color_range_image, topic=topic, particle_scatter_ratio=particle_scatter_ratio)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "ParticleEmitter":
        _base = _PrevParticleEmitter.from_sdf(el)
        return cls(name=_base.name, type=_base.type, pose=_base.pose, material=_base.material, emitting=_base.emitting, duration=_base.duration, size=_base.size, particle_size=_base.particle_size, lifetime=_base.lifetime, rate=_base.rate, min_velocity=_base.min_velocity, max_velocity=_base.max_velocity, scale_rate=_base.scale_rate, color_start=_base.color_start, color_end=_base.color_end, color_range_image=_base.color_range_image, topic=_base.topic, particle_scatter_ratio=_base.particle_scatter_ratio)
