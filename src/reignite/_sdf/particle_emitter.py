### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.utils import _parse_double
import typing
from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.color import _ColorT, _color
from ..utils.vector3 import _Vector3T, _vector3

if typing.TYPE_CHECKING:
    from ..elements.material import Material
    from ..elements.pose import Pose

def _parse_color(raw: str) -> _ColorT | SDFError:
    try:
        return _color(raw)
    except ValueError as e:
        return SDFError(str(e))

def _parse_vector3(raw: str) -> _Vector3T | SDFError:
    try:
        return _vector3(raw)
    except ValueError as e:
        return SDFError(str(e))


# noinspection PyUnusedImports
class ParticleEmitter(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        color_end: _ColorT | None = None,
        color_range_image: str | None = None,
        color_start: _ColorT | None = None,
        duration: float | None = None,
        emitting: bool | None = None,
        lifetime: float | None = None,
        material: "Material" = None,
        max_velocity: float | None = None,
        min_velocity: float | None = None,
        name: str | None = None,
        particle_scatter_ratio: float | None = None,
        particle_size: _Vector3T | None = None,
        pose: "Pose" = None,
        rate: float | None = None,
        scale_rate: float | None = None,
        size: _Vector3T | None = None,
        topic: str | None = None,
        type: str | None = None
    ):
        super().__init__(sdf_version)
        self.color_end = _color(color_end) if color_end is not None else None
        self.color_range_image = color_range_image
        self.color_start = _color(color_start) if color_start is not None else None
        self.duration = duration
        self.emitting = emitting
        self.lifetime = lifetime
        self.material = material
        self.max_velocity = max_velocity
        self.min_velocity = min_velocity
        self.name = name
        self.particle_scatter_ratio = particle_scatter_ratio
        self.particle_size = _vector3(particle_size) if particle_size is not None else None
        self.pose = pose
        self.rate = rate
        self.scale_rate = scale_rate
        self.size = _vector3(size) if size is not None else None
        self.topic = topic
        self.type = type
        if self.material is not None and hasattr(self.material, 'to_version'):
            if getattr(self.material, 'sdfversion', None) is None:
                self.material.sdfversion = self.sdfversion
            elif getattr(self.material, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.material = self.material.to_version(self.sdfversion)
        if self.pose is not None and hasattr(self.pose, 'to_version'):
            if getattr(self.pose, 'sdfversion', None) is None:
                self.pose.sdfversion = self.sdfversion
            elif getattr(self.pose, 'sdfversion', None) != self.sdfversion and self.sdfversion is not None:
                self.pose = self.pose.to_version(self.sdfversion)

    def to_version(self, target_version: str) -> "ParticleEmitter":
        from ..elements.material import Material
        from ..elements.pose import Pose
        kwargs: dict = {"sdf_version": target_version, "color_end": self.color_end, "color_range_image": self.color_range_image, "color_start": self.color_start, "duration": self.duration, "emitting": self.emitting, "lifetime": self.lifetime, "material": self.material.to_version(target_version) if self.material is not None and hasattr(self.material, "to_version") else self.material, "max_velocity": self.max_velocity, "min_velocity": self.min_velocity, "name": self.name, "particle_scatter_ratio": self.particle_scatter_ratio, "particle_size": self.particle_size, "pose": self.pose.to_version(target_version) if self.pose is not None and hasattr(self.pose, "to_version") else self.pose, "rate": self.rate, "scale_rate": self.scale_rate, "size": self.size, "topic": self.topic, "type": self.type}
        return self.__class__(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        from ..elements.material import Material
        from ..elements.pose import Pose
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf(version)
        if version is None:
            version = self.sdfversion or "1.12"
        el = ET.Element("particle_emitter")
        if self.color_end is not None:
            _c_tmp = ET.Element("color_end")
            _c_tmp.text = str(self.color_end)
            el.append(_c_tmp)
        if self.color_range_image is not None:
            _c_tmp = ET.Element("color_range_image")
            _c_tmp.text = self.color_range_image
            el.append(_c_tmp)
        if self.color_start is not None:
            _c_tmp = ET.Element("color_start")
            _c_tmp.text = str(self.color_start)
            el.append(_c_tmp)
        if self.duration is not None:
            _c_tmp = ET.Element("duration")
            _c_tmp.text = str(self.duration)
            el.append(_c_tmp)
        if self.emitting is not None:
            _c_tmp = ET.Element("emitting")
            _c_tmp.text = str(self.emitting).lower()
            el.append(_c_tmp)
        if self.lifetime is not None:
            _c_tmp = ET.Element("lifetime")
            _c_tmp.text = str(self.lifetime)
            el.append(_c_tmp)
        if self.material is not None:
            _child_res = self.material.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('material')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.max_velocity is not None:
            _c_tmp = ET.Element("max_velocity")
            _c_tmp.text = str(self.max_velocity)
            el.append(_c_tmp)
        if self.min_velocity is not None:
            _c_tmp = ET.Element("min_velocity")
            _c_tmp.text = str(self.min_velocity)
            el.append(_c_tmp)
        if self.name is not None:
            el.set("name", self.name)
        if self.particle_scatter_ratio is not None:
            _c_tmp = ET.Element("particle_scatter_ratio")
            _c_tmp.text = str(self.particle_scatter_ratio)
            el.append(_c_tmp)
        if self.particle_size is not None:
            _c_tmp = ET.Element("particle_size")
            _c_tmp.text = str(self.particle_size)
            el.append(_c_tmp)
        if self.pose is not None:
            _child_res = self.pose.to_sdf(version)
            if isinstance(_child_res, str):
                _item_el = ET.Element('pose')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.rate is not None:
            _c_tmp = ET.Element("rate")
            _c_tmp.text = str(self.rate)
            el.append(_c_tmp)
        if self.scale_rate is not None:
            _c_tmp = ET.Element("scale_rate")
            _c_tmp.text = str(self.scale_rate)
            el.append(_c_tmp)
        if self.size is not None:
            _c_tmp = ET.Element("size")
            _c_tmp.text = str(self.size)
            el.append(_c_tmp)
        if self.topic is not None:
            _c_tmp = ET.Element("topic")
            _c_tmp.text = self.topic
            el.append(_c_tmp)
        if self.type is not None:
            el.set("type", self.type)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "ParticleEmitter | SDFError":
        from ..elements.material import Material
        from ..elements.pose import Pose
        _c_tmp = el.find("color_end")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "1 1 1 1"
            _val = _parse_color(_text)
            if isinstance(_val, SDFError):
                return _val.extend("color_end")
            _color_end = _val
        else:
            _color_end = None
        _c_tmp = el.find("color_range_image")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else None
            _val = _text
            if isinstance(_val, SDFError):
                return _val.extend("color_range_image")
            _color_range_image = _val
        else:
            _color_range_image = None
        _c_tmp = el.find("color_start")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "1 1 1 1"
            _val = _parse_color(_text)
            if isinstance(_val, SDFError):
                return _val.extend("color_start")
            _color_start = _val
        else:
            _color_start = None
        _c_tmp = el.find("duration")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 0
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("duration")
            _duration = _val
        else:
            _duration = None
        _c_tmp = el.find("emitting")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else True
            _val = str(_text).strip().lower() == 'true'
            if isinstance(_val, SDFError):
                return _val.extend("emitting")
            _emitting = _val
        else:
            _emitting = None
        _c_tmp = el.find("lifetime")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 5
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("lifetime")
            _lifetime = _val
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
        _c_tmp = el.find("max_velocity")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 1
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("max_velocity")
            _max_velocity = _val
        else:
            _max_velocity = None
        _c_tmp = el.find("min_velocity")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 1
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("min_velocity")
            _min_velocity = _val
        else:
            _min_velocity = None
        _raw_name = el.get("name")
        if _raw_name is not None:
            _name = _raw_name
            if isinstance(_name, SDFError):
                return _name.extend("@name")
        else:
            _name = None
        _c_tmp = el.find("particle_scatter_ratio")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 0.65
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("particle_scatter_ratio")
            _particle_scatter_ratio = _val
        else:
            _particle_scatter_ratio = None
        _c_tmp = el.find("particle_size")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "1 1 1"
            _val = _parse_vector3(_text)
            if isinstance(_val, SDFError):
                return _val.extend("particle_size")
            _particle_size = _val
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
        _c_tmp = el.find("rate")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 10
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("rate")
            _rate = _val
        else:
            _rate = None
        _c_tmp = el.find("scale_rate")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else 0
            _val = _parse_double(_text)
            if isinstance(_val, SDFError):
                return _val.extend("scale_rate")
            _scale_rate = _val
        else:
            _scale_rate = None
        _c_tmp = el.find("size")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "1 1 1"
            _val = _parse_vector3(_text)
            if isinstance(_val, SDFError):
                return _val.extend("size")
            _size = _val
        else:
            _size = None
        _c_tmp = el.find("topic")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else None
            _val = _text
            if isinstance(_val, SDFError):
                return _val.extend("topic")
            _topic = _val
        else:
            _topic = None
        _raw_type = el.get("type")
        if _raw_type is not None:
            _type = _raw_type
            if isinstance(_type, SDFError):
                return _type.extend("@type")
        else:
            _type = None
        return cls(sdf_version=version, color_end=_color_end, color_range_image=_color_range_image, color_start=_color_start, duration=_duration, emitting=_emitting, lifetime=_lifetime, material=_material, max_velocity=_max_velocity, min_velocity=_min_velocity, name=_name, particle_scatter_ratio=_particle_scatter_ratio, particle_size=_particle_size, pose=_pose, rate=_rate, scale_rate=_scale_rate, size=_size, topic=_topic, type=_type)
