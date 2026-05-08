from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
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


class ParticleEmitter(Model):
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
        self.name = name
        self.type = type
        self.pose = pose
        self.material = material
        self.emitting = emitting
        self.duration = duration
        self.size = size
        self.particle_size = particle_size
        self.lifetime = lifetime
        self.rate = rate
        self.min_velocity = min_velocity
        self.max_velocity = max_velocity
        self.scale_rate = scale_rate
        self.color_start = color_start
        self.color_end = color_end
        self.color_range_image = color_range_image
        self.topic = topic
        self.particle_scatter_ratio = particle_scatter_ratio

    def to_sdf(self) -> ET.Element:
        el = ET.Element("particle_emitter")
        if self.name is not None:
            el.set("name", self.name)
        if self.type is not None:
            el.set("type", self.type)
        if self.pose is not None:
            el.append(self.pose.to_sdf())
        if self.material is not None:
            el.append(self.material.to_sdf())
        if self.emitting is not None:
            el.append(self.emitting.to_sdf())
        if self.duration is not None:
            el.append(self.duration.to_sdf())
        if self.size is not None:
            el.append(self.size.to_sdf())
        if self.particle_size is not None:
            el.append(self.particle_size.to_sdf())
        if self.lifetime is not None:
            el.append(self.lifetime.to_sdf())
        if self.rate is not None:
            el.append(self.rate.to_sdf())
        if self.min_velocity is not None:
            el.append(self.min_velocity.to_sdf())
        if self.max_velocity is not None:
            el.append(self.max_velocity.to_sdf())
        if self.scale_rate is not None:
            el.append(self.scale_rate.to_sdf())
        if self.color_start is not None:
            el.append(self.color_start.to_sdf())
        if self.color_end is not None:
            el.append(self.color_end.to_sdf())
        if self.color_range_image is not None:
            el.append(self.color_range_image.to_sdf())
        if self.topic is not None:
            el.append(self.topic.to_sdf())
        if self.particle_scatter_ratio is not None:
            el.append(self.particle_scatter_ratio.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "ParticleEmitter":
        _name = el.get("name", "__default__")
        _type = el.get("type", "point")
        _c_pose = el.find("pose")
        _pose = Pose.from_sdf(_c_pose) if _c_pose is not None else None
        _c_material = el.find("material")
        _material = Material.from_sdf(_c_material) if _c_material is not None else None
        _c_emitting = el.find("emitting")
        _emitting = Emitting.from_sdf(_c_emitting) if _c_emitting is not None else None
        _c_duration = el.find("duration")
        _duration = Duration.from_sdf(_c_duration) if _c_duration is not None else None
        _c_size = el.find("size")
        _size = Size.from_sdf(_c_size) if _c_size is not None else None
        _c_particle_size = el.find("particle_size")
        _particle_size = ParticleSize.from_sdf(_c_particle_size) if _c_particle_size is not None else None
        _c_lifetime = el.find("lifetime")
        _lifetime = Lifetime.from_sdf(_c_lifetime) if _c_lifetime is not None else None
        _c_rate = el.find("rate")
        _rate = Rate.from_sdf(_c_rate) if _c_rate is not None else None
        _c_min_velocity = el.find("min_velocity")
        _min_velocity = MinVelocity.from_sdf(_c_min_velocity) if _c_min_velocity is not None else None
        _c_max_velocity = el.find("max_velocity")
        _max_velocity = MaxVelocity.from_sdf(_c_max_velocity) if _c_max_velocity is not None else None
        _c_scale_rate = el.find("scale_rate")
        _scale_rate = ScaleRate.from_sdf(_c_scale_rate) if _c_scale_rate is not None else None
        _c_color_start = el.find("color_start")
        _color_start = ColorStart.from_sdf(_c_color_start) if _c_color_start is not None else None
        _c_color_end = el.find("color_end")
        _color_end = ColorEnd.from_sdf(_c_color_end) if _c_color_end is not None else None
        _c_color_range_image = el.find("color_range_image")
        _color_range_image = ColorRangeImage.from_sdf(_c_color_range_image) if _c_color_range_image is not None else None
        _c_topic = el.find("topic")
        _topic = Topic.from_sdf(_c_topic) if _c_topic is not None else None
        _c_particle_scatter_ratio = el.find("particle_scatter_ratio")
        _particle_scatter_ratio = ParticleScatterRatio.from_sdf(_c_particle_scatter_ratio) if _c_particle_scatter_ratio is not None else None
        return cls(name=_name, type=_type, pose=_pose, material=_material, emitting=_emitting, duration=_duration, size=_size, particle_size=_particle_size, lifetime=_lifetime, rate=_rate, min_velocity=_min_velocity, max_velocity=_max_velocity, scale_rate=_scale_rate, color_start=_color_start, color_end=_color_end, color_range_image=_color_range_image, topic=_topic, particle_scatter_ratio=_particle_scatter_ratio)
