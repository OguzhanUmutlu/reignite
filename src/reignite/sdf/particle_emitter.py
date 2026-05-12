### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.color import Color as _SDFColor
from ..utils.vector3 import Vector3 as _SDFVector3

if typing.TYPE_CHECKING:
    from ..elements.material import Material
    from ..elements.pose import Pose


import math

def _parse_int32(raw: str) -> int | SDFError:
    try:
        v = int(raw)
        if not (-2147483648 <= v <= 2147483647):
            return SDFError(f"int32 out of range: {v}")
        return v
    except ValueError:
        return SDFError(f"Invalid int32: {raw}")


def _parse_uint32(raw: str) -> int | SDFError:
    try:
        v = int(raw)
        if not (0 <= v <= 4294967295):
            return SDFError(f"uint32 out of range: {v}")
        return v
    except ValueError:
        return SDFError(f"Invalid uint32: {raw}")


def _parse_double(raw: str) -> float | SDFError:
    try:
        v = float(raw)
        if not math.isfinite(v) or abs(v) > math.inf:
            return SDFError(f"double out of range: {raw}")
        return v
    except ValueError:
        return SDFError(f"Invalid double: {raw}")



class ColorEnd(BaseModel):
    def __init__(self, sdf_version: str, color_end: _SDFColor = None):
        self.__version__ = sdf_version
        if color_end is None:
            color_end = _SDFColor.from_sdf("1 1 1 1")
        self.color_end = color_end

    def to_version(self, target_version: str) -> "ColorEnd":
        kwargs = {"sdf_version": target_version}
        kwargs["color_end"] = self.color_end
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("color_end")
        if self.color_end is not None:
            el.text = self.color_end.to_sdf()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "1 1 1 1"
        _color_end = _SDFColor._from_sdf(_text, version)
        if isinstance(_color_end, SDFError):
            return _color_end
        return cls(sdf_version=version, color_end=_color_end)


class ColorRangeImage(BaseModel):
    def __init__(self, sdf_version: str, color_range_image: str = ""):
        self.__version__ = sdf_version
        self.color_range_image = color_range_image

    def to_version(self, target_version: str) -> "ColorRangeImage":
        kwargs = {"sdf_version": target_version}
        kwargs["color_range_image"] = self.color_range_image
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("color_range_image")
        if self.color_range_image is not None:
            el.text = self.color_range_image
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or ""
        _color_range_image = _text
        if isinstance(_color_range_image, SDFError):
            return _color_range_image
        return cls(sdf_version=version, color_range_image=_color_range_image)


class ColorStart(BaseModel):
    def __init__(self, sdf_version: str, color_start: _SDFColor = None):
        self.__version__ = sdf_version
        if color_start is None:
            color_start = _SDFColor.from_sdf("1 1 1 1")
        self.color_start = color_start

    def to_version(self, target_version: str) -> "ColorStart":
        kwargs = {"sdf_version": target_version}
        kwargs["color_start"] = self.color_start
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("color_start")
        if self.color_start is not None:
            el.text = self.color_start.to_sdf()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "1 1 1 1"
        _color_start = _SDFColor._from_sdf(_text, version)
        if isinstance(_color_start, SDFError):
            return _color_start
        return cls(sdf_version=version, color_start=_color_start)


class Duration(BaseModel):
    def __init__(self, sdf_version: str, duration: float = 0):
        self.__version__ = sdf_version
        self.duration = duration

    def to_version(self, target_version: str) -> "Duration":
        kwargs = {"sdf_version": target_version}
        kwargs["duration"] = self.duration
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("duration")
        if self.duration is not None:
            el.text = str(self.duration)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _duration = _parse_double(_text)
        if isinstance(_duration, SDFError):
            return _duration
        return cls(sdf_version=version, duration=_duration)


class Emitting(BaseModel):
    def __init__(self, sdf_version: str, emitting: bool = True):
        self.__version__ = sdf_version
        self.emitting = emitting

    def to_version(self, target_version: str) -> "Emitting":
        kwargs = {"sdf_version": target_version}
        kwargs["emitting"] = self.emitting
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("emitting")
        if self.emitting is not None:
            el.text = str(self.emitting).lower()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or True
        _emitting = str(_text).strip().lower() == 'true'
        if isinstance(_emitting, SDFError):
            return _emitting
        return cls(sdf_version=version, emitting=_emitting)


class Lifetime(BaseModel):
    def __init__(self, sdf_version: str, lifetime: float = 5):
        self.__version__ = sdf_version
        self.lifetime = lifetime

    def to_version(self, target_version: str) -> "Lifetime":
        kwargs = {"sdf_version": target_version}
        kwargs["lifetime"] = self.lifetime
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("lifetime")
        if self.lifetime is not None:
            el.text = str(self.lifetime)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 5
        _lifetime = _parse_double(_text)
        if isinstance(_lifetime, SDFError):
            return _lifetime
        return cls(sdf_version=version, lifetime=_lifetime)


class MaxVelocity(BaseModel):
    def __init__(self, sdf_version: str, max_velocity: float = 1):
        self.__version__ = sdf_version
        self.max_velocity = max_velocity

    def to_version(self, target_version: str) -> "MaxVelocity":
        kwargs = {"sdf_version": target_version}
        kwargs["max_velocity"] = self.max_velocity
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("max_velocity")
        if self.max_velocity is not None:
            el.text = str(self.max_velocity)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _max_velocity = _parse_double(_text)
        if isinstance(_max_velocity, SDFError):
            return _max_velocity
        return cls(sdf_version=version, max_velocity=_max_velocity)


class MinVelocity(BaseModel):
    def __init__(self, sdf_version: str, min_velocity: float = 1):
        self.__version__ = sdf_version
        self.min_velocity = min_velocity

    def to_version(self, target_version: str) -> "MinVelocity":
        kwargs = {"sdf_version": target_version}
        kwargs["min_velocity"] = self.min_velocity
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("min_velocity")
        if self.min_velocity is not None:
            el.text = str(self.min_velocity)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _min_velocity = _parse_double(_text)
        if isinstance(_min_velocity, SDFError):
            return _min_velocity
        return cls(sdf_version=version, min_velocity=_min_velocity)


class ParticleEmitter(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        color_end: "ColorEnd" = None,
        color_range_image: "ColorRangeImage" = None,
        color_start: "ColorStart" = None,
        duration: "Duration" = None,
        emitting: "Emitting" = None,
        lifetime: "Lifetime" = None,
        material: "Material" = None,
        max_velocity: "MaxVelocity" = None,
        min_velocity: "MinVelocity" = None,
        name: str = "__default__",
        particle_scatter_ratio: "ParticleScatterRatio" = None,
        particle_size: "ParticleSize" = None,
        pose: "Pose" = None,
        rate: "Rate" = None,
        scale_rate: "ScaleRate" = None,
        size: "Size" = None,
        topic: "Topic" = None,
        type: str = "point"
    ):
        self.__version__ = sdf_version
        self.color_end = color_end
        self.color_range_image = color_range_image
        self.color_start = color_start
        self.duration = duration
        self.emitting = emitting
        self.lifetime = lifetime
        self.material = material
        self.max_velocity = max_velocity
        self.min_velocity = min_velocity
        self.name = name
        self.particle_scatter_ratio = particle_scatter_ratio
        self.particle_size = particle_size
        self.pose = pose
        self.rate = rate
        self.scale_rate = scale_rate
        self.size = size
        self.topic = topic
        self.type = type

    def to_version(self, target_version: str) -> "ParticleEmitter":
        from ..elements.material import Material
        from ..elements.pose import Pose
        kwargs = {"sdf_version": target_version}
        kwargs["color_end"] = self.color_end.to_version(target_version) if self.color_end is not None else None
        kwargs["color_range_image"] = self.color_range_image.to_version(target_version) if self.color_range_image is not None else None
        kwargs["color_start"] = self.color_start.to_version(target_version) if self.color_start is not None else None
        kwargs["duration"] = self.duration.to_version(target_version) if self.duration is not None else None
        kwargs["emitting"] = self.emitting.to_version(target_version) if self.emitting is not None else None
        kwargs["lifetime"] = self.lifetime.to_version(target_version) if self.lifetime is not None else None
        kwargs["material"] = self.material.to_version(target_version) if self.material is not None else None
        kwargs["max_velocity"] = self.max_velocity.to_version(target_version) if self.max_velocity is not None else None
        kwargs["min_velocity"] = self.min_velocity.to_version(target_version) if self.min_velocity is not None else None
        kwargs["name"] = self.name
        kwargs["particle_scatter_ratio"] = self.particle_scatter_ratio.to_version(target_version) if self.particle_scatter_ratio is not None else None
        kwargs["particle_size"] = self.particle_size.to_version(target_version) if self.particle_size is not None else None
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["rate"] = self.rate.to_version(target_version) if self.rate is not None else None
        kwargs["scale_rate"] = self.scale_rate.to_version(target_version) if self.scale_rate is not None else None
        kwargs["size"] = self.size.to_version(target_version) if self.size is not None else None
        kwargs["topic"] = self.topic.to_version(target_version) if self.topic is not None else None
        kwargs["type"] = self.type
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        from ..elements.material import Material
        from ..elements.pose import Pose
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("particle_emitter")
        if self.color_end is not None:
            el.append(self.color_end.to_sdf(version))
        if self.color_range_image is not None:
            el.append(self.color_range_image.to_sdf(version))
        if self.color_start is not None:
            el.append(self.color_start.to_sdf(version))
        if self.duration is not None:
            el.append(self.duration.to_sdf(version))
        if self.emitting is not None:
            el.append(self.emitting.to_sdf(version))
        if self.lifetime is not None:
            el.append(self.lifetime.to_sdf(version))
        if self.material is not None:
            el.append(self.material.to_sdf(version))
        if self.max_velocity is not None:
            el.append(self.max_velocity.to_sdf(version))
        if self.min_velocity is not None:
            el.append(self.min_velocity.to_sdf(version))
        if self.name is not None:
            el.set("name", self.name)
        if self.particle_scatter_ratio is not None:
            el.append(self.particle_scatter_ratio.to_sdf(version))
        if self.particle_size is not None:
            el.append(self.particle_size.to_sdf(version))
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        if self.rate is not None:
            el.append(self.rate.to_sdf(version))
        if self.scale_rate is not None:
            el.append(self.scale_rate.to_sdf(version))
        if self.size is not None:
            el.append(self.size.to_sdf(version))
        if self.topic is not None:
            el.append(self.topic.to_sdf(version))
        if self.type is not None:
            el.set("type", self.type)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        from ..elements.material import Material
        from ..elements.pose import Pose
        _c_color_end = el.find("color_end")
        if _c_color_end is not None:
            _res = ColorEnd._from_sdf(_c_color_end, version)
            if isinstance(_res, SDFError):
                return _res.extend("color_end")
            _color_end = _res
        else:
            _color_end = None
        _c_color_range_image = el.find("color_range_image")
        if _c_color_range_image is not None:
            _res = ColorRangeImage._from_sdf(_c_color_range_image, version)
            if isinstance(_res, SDFError):
                return _res.extend("color_range_image")
            _color_range_image = _res
        else:
            _color_range_image = None
        _c_color_start = el.find("color_start")
        if _c_color_start is not None:
            _res = ColorStart._from_sdf(_c_color_start, version)
            if isinstance(_res, SDFError):
                return _res.extend("color_start")
            _color_start = _res
        else:
            _color_start = None
        _c_duration = el.find("duration")
        if _c_duration is not None:
            _res = Duration._from_sdf(_c_duration, version)
            if isinstance(_res, SDFError):
                return _res.extend("duration")
            _duration = _res
        else:
            _duration = None
        _c_emitting = el.find("emitting")
        if _c_emitting is not None:
            _res = Emitting._from_sdf(_c_emitting, version)
            if isinstance(_res, SDFError):
                return _res.extend("emitting")
            _emitting = _res
        else:
            _emitting = None
        _c_lifetime = el.find("lifetime")
        if _c_lifetime is not None:
            _res = Lifetime._from_sdf(_c_lifetime, version)
            if isinstance(_res, SDFError):
                return _res.extend("lifetime")
            _lifetime = _res
        else:
            _lifetime = None
        _c_material = el.find("material")
        if _c_material is not None:
            _res = Material._from_sdf(_c_material, version)
            if isinstance(_res, SDFError):
                return _res.extend("material")
            _material = _res
        else:
            _material = None
        _c_max_velocity = el.find("max_velocity")
        if _c_max_velocity is not None:
            _res = MaxVelocity._from_sdf(_c_max_velocity, version)
            if isinstance(_res, SDFError):
                return _res.extend("max_velocity")
            _max_velocity = _res
        else:
            _max_velocity = None
        _c_min_velocity = el.find("min_velocity")
        if _c_min_velocity is not None:
            _res = MinVelocity._from_sdf(_c_min_velocity, version)
            if isinstance(_res, SDFError):
                return _res.extend("min_velocity")
            _min_velocity = _res
        else:
            _min_velocity = None
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        _c_particle_scatter_ratio = el.find("particle_scatter_ratio")
        if _c_particle_scatter_ratio is not None:
            _res = ParticleScatterRatio._from_sdf(_c_particle_scatter_ratio, version)
            if isinstance(_res, SDFError):
                return _res.extend("particle_scatter_ratio")
            _particle_scatter_ratio = _res
        else:
            _particle_scatter_ratio = None
        _c_particle_size = el.find("particle_size")
        if _c_particle_size is not None:
            _res = ParticleSize._from_sdf(_c_particle_size, version)
            if isinstance(_res, SDFError):
                return _res.extend("particle_size")
            _particle_size = _res
        else:
            _particle_size = None
        _c_pose = el.find("pose")
        if _c_pose is not None:
            _res = Pose._from_sdf(_c_pose, version)
            if isinstance(_res, SDFError):
                return _res.extend("pose")
            _pose = _res
        else:
            _pose = None
        _c_rate = el.find("rate")
        if _c_rate is not None:
            _res = Rate._from_sdf(_c_rate, version)
            if isinstance(_res, SDFError):
                return _res.extend("rate")
            _rate = _res
        else:
            _rate = None
        _c_scale_rate = el.find("scale_rate")
        if _c_scale_rate is not None:
            _res = ScaleRate._from_sdf(_c_scale_rate, version)
            if isinstance(_res, SDFError):
                return _res.extend("scale_rate")
            _scale_rate = _res
        else:
            _scale_rate = None
        _c_size = el.find("size")
        if _c_size is not None:
            _res = Size._from_sdf(_c_size, version)
            if isinstance(_res, SDFError):
                return _res.extend("size")
            _size = _res
        else:
            _size = None
        _c_topic = el.find("topic")
        if _c_topic is not None:
            _res = Topic._from_sdf(_c_topic, version)
            if isinstance(_res, SDFError):
                return _res.extend("topic")
            _topic = _res
        else:
            _topic = None
        _type = el.get("type", "point")
        if isinstance(_type, SDFError):
            return _type.extend("@type")
        return cls(sdf_version=version, color_end=_color_end, color_range_image=_color_range_image, color_start=_color_start, duration=_duration, emitting=_emitting, lifetime=_lifetime, material=_material, max_velocity=_max_velocity, min_velocity=_min_velocity, name=_name, particle_scatter_ratio=_particle_scatter_ratio, particle_size=_particle_size, pose=_pose, rate=_rate, scale_rate=_scale_rate, size=_size, topic=_topic, type=_type)


class ParticleScatterRatio(BaseModel):
    def __init__(self, sdf_version: str, particle_scatter_ratio: float = 0.65):
        self.__version__ = sdf_version
        self.particle_scatter_ratio = particle_scatter_ratio

    def to_version(self, target_version: str) -> "ParticleScatterRatio":
        kwargs = {"sdf_version": target_version}
        kwargs["particle_scatter_ratio"] = self.particle_scatter_ratio
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("particle_scatter_ratio")
        if self.particle_scatter_ratio is not None:
            el.text = str(self.particle_scatter_ratio)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.65
        _particle_scatter_ratio = _parse_double(_text)
        if isinstance(_particle_scatter_ratio, SDFError):
            return _particle_scatter_ratio
        return cls(sdf_version=version, particle_scatter_ratio=_particle_scatter_ratio)


class ParticleSize(BaseModel):
    def __init__(self, sdf_version: str, particle_size: _SDFVector3 = None):
        self.__version__ = sdf_version
        if particle_size is None:
            particle_size = _SDFVector3.from_sdf("1 1 1")
        self.particle_size = particle_size

    def to_version(self, target_version: str) -> "ParticleSize":
        kwargs = {"sdf_version": target_version}
        kwargs["particle_size"] = self.particle_size
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("particle_size")
        if self.particle_size is not None:
            el.text = self.particle_size.to_sdf()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "1 1 1"
        _particle_size = _SDFVector3._from_sdf(_text, version)
        if isinstance(_particle_size, SDFError):
            return _particle_size
        return cls(sdf_version=version, particle_size=_particle_size)


class Rate(BaseModel):
    def __init__(self, sdf_version: str, rate: float = 10):
        self.__version__ = sdf_version
        self.rate = rate

    def to_version(self, target_version: str) -> "Rate":
        kwargs = {"sdf_version": target_version}
        kwargs["rate"] = self.rate
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("rate")
        if self.rate is not None:
            el.text = str(self.rate)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 10
        _rate = _parse_double(_text)
        if isinstance(_rate, SDFError):
            return _rate
        return cls(sdf_version=version, rate=_rate)


class ScaleRate(BaseModel):
    def __init__(self, sdf_version: str, scale_rate: float = 0):
        self.__version__ = sdf_version
        self.scale_rate = scale_rate

    def to_version(self, target_version: str) -> "ScaleRate":
        kwargs = {"sdf_version": target_version}
        kwargs["scale_rate"] = self.scale_rate
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("scale_rate")
        if self.scale_rate is not None:
            el.text = str(self.scale_rate)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _scale_rate = _parse_double(_text)
        if isinstance(_scale_rate, SDFError):
            return _scale_rate
        return cls(sdf_version=version, scale_rate=_scale_rate)


class Size(BaseModel):
    def __init__(self, sdf_version: str, size: _SDFVector3 = None):
        self.__version__ = sdf_version
        if size is None:
            size = _SDFVector3.from_sdf("1 1 1")
        self.size = size

    def to_version(self, target_version: str) -> "Size":
        kwargs = {"sdf_version": target_version}
        kwargs["size"] = self.size
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("size")
        if self.size is not None:
            el.text = self.size.to_sdf()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "1 1 1"
        _size = _SDFVector3._from_sdf(_text, version)
        if isinstance(_size, SDFError):
            return _size
        return cls(sdf_version=version, size=_size)


class Topic(BaseModel):
    def __init__(self, sdf_version: str, topic: str = ""):
        self.__version__ = sdf_version
        self.topic = topic

    def to_version(self, target_version: str) -> "Topic":
        kwargs = {"sdf_version": target_version}
        kwargs["topic"] = self.topic
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("topic")
        if self.topic is not None:
            el.text = self.topic
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or ""
        _topic = _text
        if isinstance(_topic, SDFError):
            return _topic
        return cls(sdf_version=version, topic=_topic)
