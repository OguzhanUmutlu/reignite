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



class ParticleEmitter(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        color_end: _SDFColor = None,
        color_range_image: str = "",
        color_start: _SDFColor = None,
        duration: float = 0,
        emitting: bool = True,
        lifetime: float = 5,
        material: "Material" = None,
        max_velocity: float = 1,
        min_velocity: float = 1,
        name: str = "__default__",
        particle_scatter_ratio: float = 0.65,
        particle_size: _SDFVector3 = None,
        pose: "Pose" = None,
        rate: float = 10,
        scale_rate: float = 0,
        size: _SDFVector3 = None,
        topic: str = "",
        type: str = "point"
    ):
        super().__init__(sdf_version)
        if color_end is None:
            color_end = _SDFColor.from_sdf("1 1 1 1", version=sdf_version)
        if color_start is None:
            color_start = _SDFColor.from_sdf("1 1 1 1", version=sdf_version)
        if particle_size is None:
            particle_size = _SDFVector3.from_sdf("1 1 1", version=sdf_version)
        if size is None:
            size = _SDFVector3.from_sdf("1 1 1", version=sdf_version)
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
        if self.material is not None and hasattr(self.material, 'to_version'):
            if getattr(self.material, '__version__', None) is None:
                self.material.__version__ = self.__version__
            elif getattr(self.material, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.material = self.material.to_version(self.__version__)
        if self.pose is not None and hasattr(self.pose, 'to_version'):
            if getattr(self.pose, '__version__', None) is None:
                self.pose.__version__ = self.__version__
            elif getattr(self.pose, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.pose = self.pose.to_version(self.__version__)

    def to_version(self, target_version: str) -> "ParticleEmitter":
        from ..elements.material import Material
        from ..elements.pose import Pose
        kwargs = {"sdf_version": target_version}
        kwargs["color_end"] = self.color_end
        kwargs["color_range_image"] = self.color_range_image
        kwargs["color_start"] = self.color_start
        kwargs["duration"] = self.duration
        kwargs["emitting"] = self.emitting
        kwargs["lifetime"] = self.lifetime
        kwargs["material"] = self.material.to_version(target_version) if hasattr(self.material, "to_version") else self.material
        kwargs["max_velocity"] = self.max_velocity
        kwargs["min_velocity"] = self.min_velocity
        kwargs["name"] = self.name
        kwargs["particle_scatter_ratio"] = self.particle_scatter_ratio
        kwargs["particle_size"] = self.particle_size
        kwargs["pose"] = self.pose.to_version(target_version) if hasattr(self.pose, "to_version") else self.pose
        kwargs["rate"] = self.rate
        kwargs["scale_rate"] = self.scale_rate
        kwargs["size"] = self.size
        kwargs["topic"] = self.topic
        kwargs["type"] = self.type
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        from ..elements.material import Material
        from ..elements.pose import Pose
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("particle_emitter")
        if self.color_end is not None:
            _c_tmp = ET.Element("color_end")
            _c_tmp.text = self.color_end.to_sdf(version)
            el.append(_c_tmp)
        if self.color_range_image is not None:
            _c_tmp = ET.Element("color_range_image")
            _c_tmp.text = self.color_range_image
            el.append(_c_tmp)
        if self.color_start is not None:
            _c_tmp = ET.Element("color_start")
            _c_tmp.text = self.color_start.to_sdf(version)
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
            if hasattr(self.material, 'to_sdf'):
                _child_res = self.material.to_sdf(version)
            else:
                _child_res = str(self.material)
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
            _c_tmp.text = self.particle_size.to_sdf(version)
            el.append(_c_tmp)
        if self.pose is not None:
            if hasattr(self.pose, 'to_sdf'):
                _child_res = self.pose.to_sdf(version)
            else:
                _child_res = str(self.pose)
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
            _c_tmp.text = self.size.to_sdf(version)
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
            _val = _SDFColor._from_sdf(_text, version)
            if isinstance(_val, SDFError):
                return _val.extend("color_end")
            _color_end = _val
        else:
            _color_end = None
        _c_tmp = el.find("color_range_image")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else ""
            _val = _text
            if isinstance(_val, SDFError):
                return _val.extend("color_range_image")
            _color_range_image = _val
        else:
            _color_range_image = None
        _c_tmp = el.find("color_start")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "1 1 1 1"
            _val = _SDFColor._from_sdf(_text, version)
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
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
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
            _val = _SDFVector3._from_sdf(_text, version)
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
            _val = _SDFVector3._from_sdf(_text, version)
            if isinstance(_val, SDFError):
                return _val.extend("size")
            _size = _val
        else:
            _size = None
        _c_tmp = el.find("topic")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else ""
            _val = _text
            if isinstance(_val, SDFError):
                return _val.extend("topic")
            _topic = _val
        else:
            _topic = None
        _type = el.get("type", "point")
        if isinstance(_type, SDFError):
            return _type.extend("@type")
        return cls(sdf_version=version, color_end=_color_end, color_range_image=_color_range_image, color_start=_color_start, duration=_duration, emitting=_emitting, lifetime=_lifetime, material=_material, max_velocity=_max_velocity, min_velocity=_min_velocity, name=_name, particle_scatter_ratio=_particle_scatter_ratio, particle_size=_particle_size, pose=_pose, rate=_rate, scale_rate=_scale_rate, size=_size, topic=_topic, type=_type)
