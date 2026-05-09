### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.color import Color as _SDFColor
from ..utils.pose import Pose as _SDFPose
from ..utils.vector3 import Vector3 as _SDFVector3
from ..utils.version import cmp_version
from ..utils.migration import apply_migrations


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



class Pose(BaseModel):
    _MIGRATIONS = [{"version": "1.7", "ops": [{"type": "move", "from": "frame", "to": "relative_to"}]}]

    def __init__(
        self,
        sdf_version: str,
        degrees: bool = False,
        frame: str = "",
        pose: _SDFPose = None,
        relative_to: str = "",
        rotation_format: str = "euler_rpy"
    ):
        self.__version__ = sdf_version
        if pose is None:
            pose = _SDFPose.from_sdf("0 0 0 0 0 0")
        self.degrees = degrees
        self.frame = frame
        self.pose = pose
        self.relative_to = relative_to
        self.rotation_format = rotation_format

    def to_version(self, target_version: str) -> "Pose":
        if self.degrees is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'degrees' is not supported in SDF version {target_version} (added in 1.9)")
        if self.frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.relative_to is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'relative_to' is not supported in SDF version {target_version} (added in 1.7)")
        if self.rotation_format is not None and cmp_version(target_version, "1.9") < 0:
            raise ValueError(f"'rotation_format' is not supported in SDF version {target_version} (added in 1.9)")
        kwargs = {"sdf_version": target_version}
        kwargs["degrees"] = self.degrees
        kwargs["frame"] = self.frame
        kwargs["pose"] = self.pose
        kwargs["relative_to"] = self.relative_to
        kwargs["rotation_format"] = self.rotation_format
        new_obj = self.__class__(**kwargs)
        apply_migrations(new_obj, target_version)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("pose")
        if self.degrees is not None:
            el.set("degrees", str(self.degrees).lower())
        if self.frame is not None:
            el.set("frame", self.frame)
        if self.pose is not None:
            el.text = self.pose.to_sdf()
        if self.relative_to is not None:
            el.set("relative_to", self.relative_to)
        if self.rotation_format is not None:
            el.set("rotation_format", self.rotation_format)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _degrees = str(el.get("degrees", False)).strip().lower() == 'true'
        if isinstance(_degrees, SDFError):
            return _degrees.extend("@degrees")
        if _degrees is not None and cmp_version(version, "1.9") < 0:
            if _degrees != False:
                return SDFError(f"'degrees' is not supported in SDF version {version} (added in 1.9)")
        _frame = el.get("frame", "")
        if isinstance(_frame, SDFError):
            return _frame.extend("@frame")
        _text = el.text or "0 0 0 0 0 0"
        _pose = _SDFPose._from_sdf(_text, version)
        if isinstance(_pose, SDFError):
            return _pose
        _relative_to = el.get("relative_to", "")
        if isinstance(_relative_to, SDFError):
            return _relative_to.extend("@relative_to")
        if _relative_to is not None and cmp_version(version, "1.7") < 0:
            if _relative_to != "":
                return SDFError(f"'relative_to' is not supported in SDF version {version} (added in 1.7)")
        _rotation_format = el.get("rotation_format", "euler_rpy")
        if isinstance(_rotation_format, SDFError):
            return _rotation_format.extend("@rotation_format")
        if _rotation_format is not None and cmp_version(version, "1.9") < 0:
            if _rotation_format != "euler_rpy":
                return SDFError(f"'rotation_format' is not supported in SDF version {version} (added in 1.9)")
        return cls(sdf_version=version, degrees=_degrees, frame=_frame, pose=_pose, relative_to=_relative_to, rotation_format=_rotation_format)


class Uri(BaseModel):
    def __init__(self, sdf_version: str, uri: str = "__default__"):
        self.__version__ = sdf_version
        self.uri = uri

    def to_version(self, target_version: str) -> "Uri":
        kwargs = {"sdf_version": target_version}
        kwargs["uri"] = self.uri
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("uri")
        if self.uri is not None:
            el.text = self.uri
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "__default__"
        _uri = _text
        if isinstance(_uri, SDFError):
            return _uri
        return cls(sdf_version=version, uri=_uri)


class Name(BaseModel):
    def __init__(self, sdf_version: str, name: str = "__default__"):
        self.__version__ = sdf_version
        self.name = name

    def to_version(self, target_version: str) -> "Name":
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("name")
        if self.name is not None:
            el.text = self.name
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "__default__"
        _name = _text
        if isinstance(_name, SDFError):
            return _name
        return cls(sdf_version=version, name=_name)


class Script(BaseModel):
    def __init__(self, sdf_version: str, name: "Name" = None, uri: List["Uri"] = None):
        self.__version__ = sdf_version
        self.name = name
        self.uri = uri or []

    def to_version(self, target_version: str) -> "Script":
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name.to_version(target_version) if self.name is not None else None
        kwargs["uri"] = [c.to_version(target_version) for c in (self.uri or [])]
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("script")
        if self.name is not None:
            el.append(self.name.to_sdf(version))
        for item in (self.uri or []):
            el.append(item.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_name = el.find("name")
        if _c_name is not None:
            _res = Name._from_sdf(_c_name, version)
            if isinstance(_res, SDFError):
                return _res.extend("name")
            _name = _res
        else:
            _name = None
        _uri = []
        for c in el.findall("uri"):
            _res = Uri._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("uri")
            _uri.append(_res)
        return cls(sdf_version=version, name=_name, uri=_uri)


class NormalMap(BaseModel):
    def __init__(self, sdf_version: str, normal_map: str = "__default__"):
        self.__version__ = sdf_version
        self.normal_map = normal_map

    def to_version(self, target_version: str) -> "NormalMap":
        kwargs = {"sdf_version": target_version}
        kwargs["normal_map"] = self.normal_map
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("normal_map")
        if self.normal_map is not None:
            el.text = self.normal_map
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "__default__"
        _normal_map = _text
        if isinstance(_normal_map, SDFError):
            return _normal_map
        return cls(sdf_version=version, normal_map=_normal_map)


class Shader(BaseModel):
    def __init__(self, sdf_version: str, normal_map: "NormalMap" = None, type: str = "pixel"):
        self.__version__ = sdf_version
        self.normal_map = normal_map
        self.type = type

    def to_version(self, target_version: str) -> "Shader":
        kwargs = {"sdf_version": target_version}
        kwargs["normal_map"] = self.normal_map.to_version(target_version) if self.normal_map is not None else None
        kwargs["type"] = self.type
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("shader")
        if self.normal_map is not None:
            el.append(self.normal_map.to_sdf(version))
        if self.type is not None:
            el.set("type", self.type)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_normal_map = el.find("normal_map")
        if _c_normal_map is not None:
            _res = NormalMap._from_sdf(_c_normal_map, version)
            if isinstance(_res, SDFError):
                return _res.extend("normal_map")
            _normal_map = _res
        else:
            _normal_map = None
        _type = el.get("type", "pixel")
        if isinstance(_type, SDFError):
            return _type.extend("@type")
        return cls(sdf_version=version, normal_map=_normal_map, type=_type)


class Lighting(BaseModel):
    def __init__(self, sdf_version: str, lighting: bool = True):
        self.__version__ = sdf_version
        self.lighting = lighting

    def to_version(self, target_version: str) -> "Lighting":
        kwargs = {"sdf_version": target_version}
        kwargs["lighting"] = self.lighting
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("lighting")
        if self.lighting is not None:
            el.text = str(self.lighting).lower()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or True
        _lighting = str(_text).strip().lower() == 'true'
        if isinstance(_lighting, SDFError):
            return _lighting
        return cls(sdf_version=version, lighting=_lighting)


class Ambient(BaseModel):
    def __init__(self, sdf_version: str, ambient: _SDFColor = None):
        self.__version__ = sdf_version
        if ambient is None:
            ambient = _SDFColor.from_sdf("0 0 0 1")
        self.ambient = ambient

    def to_version(self, target_version: str) -> "Ambient":
        kwargs = {"sdf_version": target_version}
        kwargs["ambient"] = self.ambient
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("ambient")
        if self.ambient is not None:
            el.text = self.ambient.to_sdf()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 0 1"
        _ambient = _SDFColor._from_sdf(_text, version)
        if isinstance(_ambient, SDFError):
            return _ambient
        return cls(sdf_version=version, ambient=_ambient)


class Diffuse(BaseModel):
    def __init__(self, sdf_version: str, diffuse: _SDFColor = None):
        self.__version__ = sdf_version
        if diffuse is None:
            diffuse = _SDFColor.from_sdf("0 0 0 1")
        self.diffuse = diffuse

    def to_version(self, target_version: str) -> "Diffuse":
        kwargs = {"sdf_version": target_version}
        kwargs["diffuse"] = self.diffuse
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("diffuse")
        if self.diffuse is not None:
            el.text = self.diffuse.to_sdf()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 0 1"
        _diffuse = _SDFColor._from_sdf(_text, version)
        if isinstance(_diffuse, SDFError):
            return _diffuse
        return cls(sdf_version=version, diffuse=_diffuse)


class Specular(BaseModel):
    def __init__(self, sdf_version: str, specular: _SDFColor = None):
        self.__version__ = sdf_version
        if specular is None:
            specular = _SDFColor.from_sdf("0 0 0 1")
        self.specular = specular

    def to_version(self, target_version: str) -> "Specular":
        kwargs = {"sdf_version": target_version}
        kwargs["specular"] = self.specular
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("specular")
        if self.specular is not None:
            el.text = self.specular.to_sdf()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 0 1"
        _specular = _SDFColor._from_sdf(_text, version)
        if isinstance(_specular, SDFError):
            return _specular
        return cls(sdf_version=version, specular=_specular)


class Emissive(BaseModel):
    def __init__(self, sdf_version: str, emissive: _SDFColor = None):
        self.__version__ = sdf_version
        if emissive is None:
            emissive = _SDFColor.from_sdf("0 0 0 1")
        self.emissive = emissive

    def to_version(self, target_version: str) -> "Emissive":
        kwargs = {"sdf_version": target_version}
        kwargs["emissive"] = self.emissive
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("emissive")
        if self.emissive is not None:
            el.text = self.emissive.to_sdf()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 0 1"
        _emissive = _SDFColor._from_sdf(_text, version)
        if isinstance(_emissive, SDFError):
            return _emissive
        return cls(sdf_version=version, emissive=_emissive)


class AlbedoMap(BaseModel):
    def __init__(self, sdf_version: str, albedo_map: str = ""):
        self.__version__ = sdf_version
        self.albedo_map = albedo_map

    def to_version(self, target_version: str) -> "AlbedoMap":
        kwargs = {"sdf_version": target_version}
        kwargs["albedo_map"] = self.albedo_map
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("albedo_map")
        if self.albedo_map is not None:
            el.text = self.albedo_map
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or ""
        _albedo_map = _text
        if isinstance(_albedo_map, SDFError):
            return _albedo_map
        return cls(sdf_version=version, albedo_map=_albedo_map)


class RoughnessMap(BaseModel):
    def __init__(self, sdf_version: str, roughness_map: str = ""):
        self.__version__ = sdf_version
        self.roughness_map = roughness_map

    def to_version(self, target_version: str) -> "RoughnessMap":
        kwargs = {"sdf_version": target_version}
        kwargs["roughness_map"] = self.roughness_map
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("roughness_map")
        if self.roughness_map is not None:
            el.text = self.roughness_map
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or ""
        _roughness_map = _text
        if isinstance(_roughness_map, SDFError):
            return _roughness_map
        return cls(sdf_version=version, roughness_map=_roughness_map)


class Roughness(BaseModel):
    def __init__(self, sdf_version: str, roughness: str = "0.5"):
        self.__version__ = sdf_version
        self.roughness = roughness

    def to_version(self, target_version: str) -> "Roughness":
        kwargs = {"sdf_version": target_version}
        kwargs["roughness"] = self.roughness
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("roughness")
        if self.roughness is not None:
            el.text = self.roughness
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0.5"
        _roughness = _text
        if isinstance(_roughness, SDFError):
            return _roughness
        return cls(sdf_version=version, roughness=_roughness)


class MetalnessMap(BaseModel):
    def __init__(self, sdf_version: str, metalness_map: str = ""):
        self.__version__ = sdf_version
        self.metalness_map = metalness_map

    def to_version(self, target_version: str) -> "MetalnessMap":
        kwargs = {"sdf_version": target_version}
        kwargs["metalness_map"] = self.metalness_map
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("metalness_map")
        if self.metalness_map is not None:
            el.text = self.metalness_map
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or ""
        _metalness_map = _text
        if isinstance(_metalness_map, SDFError):
            return _metalness_map
        return cls(sdf_version=version, metalness_map=_metalness_map)


class Metalness(BaseModel):
    def __init__(self, sdf_version: str, metalness: str = "0.5"):
        self.__version__ = sdf_version
        self.metalness = metalness

    def to_version(self, target_version: str) -> "Metalness":
        kwargs = {"sdf_version": target_version}
        kwargs["metalness"] = self.metalness
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("metalness")
        if self.metalness is not None:
            el.text = self.metalness
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0.5"
        _metalness = _text
        if isinstance(_metalness, SDFError):
            return _metalness
        return cls(sdf_version=version, metalness=_metalness)


class EnvironmentMap(BaseModel):
    def __init__(self, sdf_version: str, environment_map: str = ""):
        self.__version__ = sdf_version
        self.environment_map = environment_map

    def to_version(self, target_version: str) -> "EnvironmentMap":
        kwargs = {"sdf_version": target_version}
        kwargs["environment_map"] = self.environment_map
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("environment_map")
        if self.environment_map is not None:
            el.text = self.environment_map
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or ""
        _environment_map = _text
        if isinstance(_environment_map, SDFError):
            return _environment_map
        return cls(sdf_version=version, environment_map=_environment_map)


class AmbientOcclusionMap(BaseModel):
    def __init__(self, sdf_version: str, ambient_occlusion_map: str = ""):
        self.__version__ = sdf_version
        self.ambient_occlusion_map = ambient_occlusion_map

    def to_version(self, target_version: str) -> "AmbientOcclusionMap":
        kwargs = {"sdf_version": target_version}
        kwargs["ambient_occlusion_map"] = self.ambient_occlusion_map
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("ambient_occlusion_map")
        if self.ambient_occlusion_map is not None:
            el.text = self.ambient_occlusion_map
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or ""
        _ambient_occlusion_map = _text
        if isinstance(_ambient_occlusion_map, SDFError):
            return _ambient_occlusion_map
        return cls(sdf_version=version, ambient_occlusion_map=_ambient_occlusion_map)


class MetalNormalMap(BaseModel):
    def __init__(self, sdf_version: str, normal_map: str = "", type: str = "tangent"):
        self.__version__ = sdf_version
        self.normal_map = normal_map
        self.type = type

    def to_version(self, target_version: str) -> "MetalNormalMap":
        kwargs = {"sdf_version": target_version}
        kwargs["normal_map"] = self.normal_map
        kwargs["type"] = self.type
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("normal_map")
        if self.normal_map is not None:
            el.text = self.normal_map
        if self.type is not None:
            el.set("type", self.type)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or ""
        _normal_map = _text
        if isinstance(_normal_map, SDFError):
            return _normal_map
        _type = el.get("type", "tangent")
        if isinstance(_type, SDFError):
            return _type.extend("@type")
        return cls(sdf_version=version, normal_map=_normal_map, type=_type)


class EmissiveMap(BaseModel):
    def __init__(self, sdf_version: str, emissive_map: str = ""):
        self.__version__ = sdf_version
        self.emissive_map = emissive_map

    def to_version(self, target_version: str) -> "EmissiveMap":
        kwargs = {"sdf_version": target_version}
        kwargs["emissive_map"] = self.emissive_map
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("emissive_map")
        if self.emissive_map is not None:
            el.text = self.emissive_map
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or ""
        _emissive_map = _text
        if isinstance(_emissive_map, SDFError):
            return _emissive_map
        return cls(sdf_version=version, emissive_map=_emissive_map)


class LightMap(BaseModel):
    def __init__(self, sdf_version: str, light_map: str = "", uv_set: int = 0):
        self.__version__ = sdf_version
        self.light_map = light_map
        self.uv_set = uv_set

    def to_version(self, target_version: str) -> "LightMap":
        if self.light_map is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'light_map' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["light_map"] = self.light_map
        kwargs["uv_set"] = self.uv_set
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("light_map")
        if self.light_map is not None:
            el.text = self.light_map
        if self.uv_set is not None:
            el.set("uv_set", str(self.uv_set))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or ""
        _light_map = _text
        if isinstance(_light_map, SDFError):
            return _light_map
        if _light_map is not None and cmp_version(version, "1.7") < 0:
            if _light_map != "":
                return SDFError(f"'light_map' is not supported in SDF version {version} (added in 1.7)")
        _uv_set = _parse_uint32(el.get("uv_set", 0))
        if isinstance(_uv_set, SDFError):
            return _uv_set.extend("@uv_set")
        return cls(sdf_version=version, light_map=_light_map, uv_set=_uv_set)


class Metal(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        albedo_map: "AlbedoMap" = None,
        ambient_occlusion_map: "AmbientOcclusionMap" = None,
        emissive_map: "EmissiveMap" = None,
        environment_map: "EnvironmentMap" = None,
        light_map: "LightMap" = None,
        metalness: "Metalness" = None,
        metalness_map: "MetalnessMap" = None,
        normal_map: "MetalNormalMap" = None,
        roughness: "Roughness" = None,
        roughness_map: "RoughnessMap" = None
    ):
        self.__version__ = sdf_version
        self.albedo_map = albedo_map
        self.ambient_occlusion_map = ambient_occlusion_map
        self.emissive_map = emissive_map
        self.environment_map = environment_map
        self.light_map = light_map
        self.metalness = metalness
        self.metalness_map = metalness_map
        self.normal_map = normal_map
        self.roughness = roughness
        self.roughness_map = roughness_map

    def to_version(self, target_version: str) -> "Metal":
        if self.light_map is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'light_map' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["albedo_map"] = self.albedo_map.to_version(target_version) if self.albedo_map is not None else None
        kwargs["ambient_occlusion_map"] = self.ambient_occlusion_map.to_version(target_version) if self.ambient_occlusion_map is not None else None
        kwargs["emissive_map"] = self.emissive_map.to_version(target_version) if self.emissive_map is not None else None
        kwargs["environment_map"] = self.environment_map.to_version(target_version) if self.environment_map is not None else None
        kwargs["light_map"] = self.light_map.to_version(target_version) if self.light_map is not None else None
        kwargs["metalness"] = self.metalness.to_version(target_version) if self.metalness is not None else None
        kwargs["metalness_map"] = self.metalness_map.to_version(target_version) if self.metalness_map is not None else None
        kwargs["normal_map"] = self.normal_map.to_version(target_version) if self.normal_map is not None else None
        kwargs["roughness"] = self.roughness.to_version(target_version) if self.roughness is not None else None
        kwargs["roughness_map"] = self.roughness_map.to_version(target_version) if self.roughness_map is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("metal")
        if self.albedo_map is not None:
            el.append(self.albedo_map.to_sdf(version))
        if self.ambient_occlusion_map is not None:
            el.append(self.ambient_occlusion_map.to_sdf(version))
        if self.emissive_map is not None:
            el.append(self.emissive_map.to_sdf(version))
        if self.environment_map is not None:
            el.append(self.environment_map.to_sdf(version))
        if self.light_map is not None:
            el.append(self.light_map.to_sdf(version))
        if self.metalness is not None:
            el.append(self.metalness.to_sdf(version))
        if self.metalness_map is not None:
            el.append(self.metalness_map.to_sdf(version))
        if self.normal_map is not None:
            el.append(self.normal_map.to_sdf(version))
        if self.roughness is not None:
            el.append(self.roughness.to_sdf(version))
        if self.roughness_map is not None:
            el.append(self.roughness_map.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_albedo_map = el.find("albedo_map")
        if _c_albedo_map is not None:
            _res = AlbedoMap._from_sdf(_c_albedo_map, version)
            if isinstance(_res, SDFError):
                return _res.extend("albedo_map")
            _albedo_map = _res
        else:
            _albedo_map = None
        _c_ambient_occlusion_map = el.find("ambient_occlusion_map")
        if _c_ambient_occlusion_map is not None:
            _res = AmbientOcclusionMap._from_sdf(_c_ambient_occlusion_map, version)
            if isinstance(_res, SDFError):
                return _res.extend("ambient_occlusion_map")
            _ambient_occlusion_map = _res
        else:
            _ambient_occlusion_map = None
        _c_emissive_map = el.find("emissive_map")
        if _c_emissive_map is not None:
            _res = EmissiveMap._from_sdf(_c_emissive_map, version)
            if isinstance(_res, SDFError):
                return _res.extend("emissive_map")
            _emissive_map = _res
        else:
            _emissive_map = None
        _c_environment_map = el.find("environment_map")
        if _c_environment_map is not None:
            _res = EnvironmentMap._from_sdf(_c_environment_map, version)
            if isinstance(_res, SDFError):
                return _res.extend("environment_map")
            _environment_map = _res
        else:
            _environment_map = None
        _c_light_map = el.find("light_map")
        if _c_light_map is not None:
            _res = LightMap._from_sdf(_c_light_map, version)
            if isinstance(_res, SDFError):
                return _res.extend("light_map")
            _light_map = _res
        else:
            _light_map = None
        if _light_map is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'light_map' is not supported in SDF version {version} (added in 1.7)")
        _c_metalness = el.find("metalness")
        if _c_metalness is not None:
            _res = Metalness._from_sdf(_c_metalness, version)
            if isinstance(_res, SDFError):
                return _res.extend("metalness")
            _metalness = _res
        else:
            _metalness = None
        _c_metalness_map = el.find("metalness_map")
        if _c_metalness_map is not None:
            _res = MetalnessMap._from_sdf(_c_metalness_map, version)
            if isinstance(_res, SDFError):
                return _res.extend("metalness_map")
            _metalness_map = _res
        else:
            _metalness_map = None
        _c_normal_map = el.find("normal_map")
        if _c_normal_map is not None:
            _res = MetalNormalMap._from_sdf(_c_normal_map, version)
            if isinstance(_res, SDFError):
                return _res.extend("normal_map")
            _normal_map = _res
        else:
            _normal_map = None
        _c_roughness = el.find("roughness")
        if _c_roughness is not None:
            _res = Roughness._from_sdf(_c_roughness, version)
            if isinstance(_res, SDFError):
                return _res.extend("roughness")
            _roughness = _res
        else:
            _roughness = None
        _c_roughness_map = el.find("roughness_map")
        if _c_roughness_map is not None:
            _res = RoughnessMap._from_sdf(_c_roughness_map, version)
            if isinstance(_res, SDFError):
                return _res.extend("roughness_map")
            _roughness_map = _res
        else:
            _roughness_map = None
        return cls(sdf_version=version, albedo_map=_albedo_map, ambient_occlusion_map=_ambient_occlusion_map, emissive_map=_emissive_map, environment_map=_environment_map, light_map=_light_map, metalness=_metalness, metalness_map=_metalness_map, normal_map=_normal_map, roughness=_roughness, roughness_map=_roughness_map)


class SpecularMap(BaseModel):
    def __init__(self, sdf_version: str, specular_map: str = ""):
        self.__version__ = sdf_version
        self.specular_map = specular_map

    def to_version(self, target_version: str) -> "SpecularMap":
        kwargs = {"sdf_version": target_version}
        kwargs["specular_map"] = self.specular_map
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("specular_map")
        if self.specular_map is not None:
            el.text = self.specular_map
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or ""
        _specular_map = _text
        if isinstance(_specular_map, SDFError):
            return _specular_map
        return cls(sdf_version=version, specular_map=_specular_map)


class GlossinessMap(BaseModel):
    def __init__(self, sdf_version: str, glossiness_map: str = ""):
        self.__version__ = sdf_version
        self.glossiness_map = glossiness_map

    def to_version(self, target_version: str) -> "GlossinessMap":
        kwargs = {"sdf_version": target_version}
        kwargs["glossiness_map"] = self.glossiness_map
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("glossiness_map")
        if self.glossiness_map is not None:
            el.text = self.glossiness_map
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or ""
        _glossiness_map = _text
        if isinstance(_glossiness_map, SDFError):
            return _glossiness_map
        return cls(sdf_version=version, glossiness_map=_glossiness_map)


class Glossiness(BaseModel):
    def __init__(self, sdf_version: str, glossiness: str = "0"):
        self.__version__ = sdf_version
        self.glossiness = glossiness

    def to_version(self, target_version: str) -> "Glossiness":
        kwargs = {"sdf_version": target_version}
        kwargs["glossiness"] = self.glossiness
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("glossiness")
        if self.glossiness is not None:
            el.text = self.glossiness
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0"
        _glossiness = _text
        if isinstance(_glossiness, SDFError):
            return _glossiness
        return cls(sdf_version=version, glossiness=_glossiness)


class SpecularNormalMap(BaseModel):
    def __init__(self, sdf_version: str, normal_map: str = "", type: str = "tangent"):
        self.__version__ = sdf_version
        self.normal_map = normal_map
        self.type = type

    def to_version(self, target_version: str) -> "SpecularNormalMap":
        kwargs = {"sdf_version": target_version}
        kwargs["normal_map"] = self.normal_map
        kwargs["type"] = self.type
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("normal_map")
        if self.normal_map is not None:
            el.text = self.normal_map
        if self.type is not None:
            el.set("type", self.type)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or ""
        _normal_map = _text
        if isinstance(_normal_map, SDFError):
            return _normal_map
        _type = el.get("type", "tangent")
        if isinstance(_type, SDFError):
            return _type.extend("@type")
        return cls(sdf_version=version, normal_map=_normal_map, type=_type)


class PbrSpecular(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        albedo_map: "AlbedoMap" = None,
        ambient_occlusion_map: "AmbientOcclusionMap" = None,
        emissive_map: "EmissiveMap" = None,
        environment_map: "EnvironmentMap" = None,
        glossiness: "Glossiness" = None,
        glossiness_map: "GlossinessMap" = None,
        light_map: "LightMap" = None,
        normal_map: "SpecularNormalMap" = None,
        specular_map: "SpecularMap" = None
    ):
        self.__version__ = sdf_version
        self.albedo_map = albedo_map
        self.ambient_occlusion_map = ambient_occlusion_map
        self.emissive_map = emissive_map
        self.environment_map = environment_map
        self.glossiness = glossiness
        self.glossiness_map = glossiness_map
        self.light_map = light_map
        self.normal_map = normal_map
        self.specular_map = specular_map

    def to_version(self, target_version: str) -> "PbrSpecular":
        if self.light_map is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'light_map' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["albedo_map"] = self.albedo_map.to_version(target_version) if self.albedo_map is not None else None
        kwargs["ambient_occlusion_map"] = self.ambient_occlusion_map.to_version(target_version) if self.ambient_occlusion_map is not None else None
        kwargs["emissive_map"] = self.emissive_map.to_version(target_version) if self.emissive_map is not None else None
        kwargs["environment_map"] = self.environment_map.to_version(target_version) if self.environment_map is not None else None
        kwargs["glossiness"] = self.glossiness.to_version(target_version) if self.glossiness is not None else None
        kwargs["glossiness_map"] = self.glossiness_map.to_version(target_version) if self.glossiness_map is not None else None
        kwargs["light_map"] = self.light_map.to_version(target_version) if self.light_map is not None else None
        kwargs["normal_map"] = self.normal_map.to_version(target_version) if self.normal_map is not None else None
        kwargs["specular_map"] = self.specular_map.to_version(target_version) if self.specular_map is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("specular")
        if self.albedo_map is not None:
            el.append(self.albedo_map.to_sdf(version))
        if self.ambient_occlusion_map is not None:
            el.append(self.ambient_occlusion_map.to_sdf(version))
        if self.emissive_map is not None:
            el.append(self.emissive_map.to_sdf(version))
        if self.environment_map is not None:
            el.append(self.environment_map.to_sdf(version))
        if self.glossiness is not None:
            el.append(self.glossiness.to_sdf(version))
        if self.glossiness_map is not None:
            el.append(self.glossiness_map.to_sdf(version))
        if self.light_map is not None:
            el.append(self.light_map.to_sdf(version))
        if self.normal_map is not None:
            el.append(self.normal_map.to_sdf(version))
        if self.specular_map is not None:
            el.append(self.specular_map.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_albedo_map = el.find("albedo_map")
        if _c_albedo_map is not None:
            _res = AlbedoMap._from_sdf(_c_albedo_map, version)
            if isinstance(_res, SDFError):
                return _res.extend("albedo_map")
            _albedo_map = _res
        else:
            _albedo_map = None
        _c_ambient_occlusion_map = el.find("ambient_occlusion_map")
        if _c_ambient_occlusion_map is not None:
            _res = AmbientOcclusionMap._from_sdf(_c_ambient_occlusion_map, version)
            if isinstance(_res, SDFError):
                return _res.extend("ambient_occlusion_map")
            _ambient_occlusion_map = _res
        else:
            _ambient_occlusion_map = None
        _c_emissive_map = el.find("emissive_map")
        if _c_emissive_map is not None:
            _res = EmissiveMap._from_sdf(_c_emissive_map, version)
            if isinstance(_res, SDFError):
                return _res.extend("emissive_map")
            _emissive_map = _res
        else:
            _emissive_map = None
        _c_environment_map = el.find("environment_map")
        if _c_environment_map is not None:
            _res = EnvironmentMap._from_sdf(_c_environment_map, version)
            if isinstance(_res, SDFError):
                return _res.extend("environment_map")
            _environment_map = _res
        else:
            _environment_map = None
        _c_glossiness = el.find("glossiness")
        if _c_glossiness is not None:
            _res = Glossiness._from_sdf(_c_glossiness, version)
            if isinstance(_res, SDFError):
                return _res.extend("glossiness")
            _glossiness = _res
        else:
            _glossiness = None
        _c_glossiness_map = el.find("glossiness_map")
        if _c_glossiness_map is not None:
            _res = GlossinessMap._from_sdf(_c_glossiness_map, version)
            if isinstance(_res, SDFError):
                return _res.extend("glossiness_map")
            _glossiness_map = _res
        else:
            _glossiness_map = None
        _c_light_map = el.find("light_map")
        if _c_light_map is not None:
            _res = LightMap._from_sdf(_c_light_map, version)
            if isinstance(_res, SDFError):
                return _res.extend("light_map")
            _light_map = _res
        else:
            _light_map = None
        if _light_map is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'light_map' is not supported in SDF version {version} (added in 1.7)")
        _c_normal_map = el.find("normal_map")
        if _c_normal_map is not None:
            _res = SpecularNormalMap._from_sdf(_c_normal_map, version)
            if isinstance(_res, SDFError):
                return _res.extend("normal_map")
            _normal_map = _res
        else:
            _normal_map = None
        _c_specular_map = el.find("specular_map")
        if _c_specular_map is not None:
            _res = SpecularMap._from_sdf(_c_specular_map, version)
            if isinstance(_res, SDFError):
                return _res.extend("specular_map")
            _specular_map = _res
        else:
            _specular_map = None
        return cls(sdf_version=version, albedo_map=_albedo_map, ambient_occlusion_map=_ambient_occlusion_map, emissive_map=_emissive_map, environment_map=_environment_map, glossiness=_glossiness, glossiness_map=_glossiness_map, light_map=_light_map, normal_map=_normal_map, specular_map=_specular_map)


class Pbr(BaseModel):
    def __init__(self, sdf_version: str, metal: "Metal" = None, specular: "PbrSpecular" = None):
        self.__version__ = sdf_version
        self.metal = metal
        self.specular = specular

    def to_version(self, target_version: str) -> "Pbr":
        kwargs = {"sdf_version": target_version}
        kwargs["metal"] = self.metal.to_version(target_version) if self.metal is not None else None
        kwargs["specular"] = self.specular.to_version(target_version) if self.specular is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("pbr")
        if self.metal is not None:
            el.append(self.metal.to_sdf(version))
        if self.specular is not None:
            el.append(self.specular.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_metal = el.find("metal")
        if _c_metal is not None:
            _res = Metal._from_sdf(_c_metal, version)
            if isinstance(_res, SDFError):
                return _res.extend("metal")
            _metal = _res
        else:
            _metal = None
        _c_specular = el.find("specular")
        if _c_specular is not None:
            _res = PbrSpecular._from_sdf(_c_specular, version)
            if isinstance(_res, SDFError):
                return _res.extend("specular")
            _specular = _res
        else:
            _specular = None
        return cls(sdf_version=version, metal=_metal, specular=_specular)


class DoubleSided(BaseModel):
    def __init__(self, sdf_version: str, double_sided: bool = False):
        self.__version__ = sdf_version
        self.double_sided = double_sided

    def to_version(self, target_version: str) -> "DoubleSided":
        if self.double_sided is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'double_sided' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["double_sided"] = self.double_sided
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("double_sided")
        if self.double_sided is not None:
            el.text = str(self.double_sided).lower()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or False
        _double_sided = str(_text).strip().lower() == 'true'
        if isinstance(_double_sided, SDFError):
            return _double_sided
        if _double_sided is not None and cmp_version(version, "1.7") < 0:
            if _double_sided != False:
                return SDFError(f"'double_sided' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, double_sided=_double_sided)


class RenderOrder(BaseModel):
    def __init__(self, sdf_version: str, render_order: float = 0.0):
        self.__version__ = sdf_version
        self.render_order = render_order

    def to_version(self, target_version: str) -> "RenderOrder":
        if self.render_order is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'render_order' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["render_order"] = self.render_order
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("render_order")
        if self.render_order is not None:
            el.text = str(self.render_order)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _render_order = _parse_double(_text)
        if isinstance(_render_order, SDFError):
            return _render_order
        if _render_order is not None and cmp_version(version, "1.7") < 0:
            if _render_order != 0.0:
                return SDFError(f"'render_order' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, render_order=_render_order)


class Shininess(BaseModel):
    def __init__(self, sdf_version: str, shininess: float = 0):
        self.__version__ = sdf_version
        self.shininess = shininess

    def to_version(self, target_version: str) -> "Shininess":
        if self.shininess is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'shininess' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["shininess"] = self.shininess
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("shininess")
        if self.shininess is not None:
            el.text = str(self.shininess)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _shininess = _parse_double(_text)
        if isinstance(_shininess, SDFError):
            return _shininess
        if _shininess is not None and cmp_version(version, "1.7") < 0:
            if _shininess != 0:
                return SDFError(f"'shininess' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, shininess=_shininess)


class Material(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        ambient: "Ambient" = None,
        diffuse: "Diffuse" = None,
        double_sided: "DoubleSided" = None,
        emissive: "Emissive" = None,
        lighting: "Lighting" = None,
        pbr: "Pbr" = None,
        render_order: "RenderOrder" = None,
        script: "Script" = None,
        shader: "Shader" = None,
        shininess: "Shininess" = None,
        specular: "Specular" = None
    ):
        self.__version__ = sdf_version
        self.ambient = ambient
        self.diffuse = diffuse
        self.double_sided = double_sided
        self.emissive = emissive
        self.lighting = lighting
        self.pbr = pbr
        self.render_order = render_order
        self.script = script
        self.shader = shader
        self.shininess = shininess
        self.specular = specular

    def to_version(self, target_version: str) -> "Material":
        if self.double_sided is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'double_sided' is not supported in SDF version {target_version} (added in 1.7)")
        if self.render_order is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'render_order' is not supported in SDF version {target_version} (added in 1.7)")
        if self.shininess is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'shininess' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["ambient"] = self.ambient.to_version(target_version) if self.ambient is not None else None
        kwargs["diffuse"] = self.diffuse.to_version(target_version) if self.diffuse is not None else None
        kwargs["double_sided"] = self.double_sided.to_version(target_version) if self.double_sided is not None else None
        kwargs["emissive"] = self.emissive.to_version(target_version) if self.emissive is not None else None
        kwargs["lighting"] = self.lighting.to_version(target_version) if self.lighting is not None else None
        kwargs["pbr"] = self.pbr.to_version(target_version) if self.pbr is not None else None
        kwargs["render_order"] = self.render_order.to_version(target_version) if self.render_order is not None else None
        kwargs["script"] = self.script.to_version(target_version) if self.script is not None else None
        kwargs["shader"] = self.shader.to_version(target_version) if self.shader is not None else None
        kwargs["shininess"] = self.shininess.to_version(target_version) if self.shininess is not None else None
        kwargs["specular"] = self.specular.to_version(target_version) if self.specular is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("material")
        if self.ambient is not None:
            el.append(self.ambient.to_sdf(version))
        if self.diffuse is not None:
            el.append(self.diffuse.to_sdf(version))
        if self.double_sided is not None:
            el.append(self.double_sided.to_sdf(version))
        if self.emissive is not None:
            el.append(self.emissive.to_sdf(version))
        if self.lighting is not None:
            el.append(self.lighting.to_sdf(version))
        if self.pbr is not None:
            el.append(self.pbr.to_sdf(version))
        if self.render_order is not None:
            el.append(self.render_order.to_sdf(version))
        if self.script is not None:
            el.append(self.script.to_sdf(version))
        if self.shader is not None:
            el.append(self.shader.to_sdf(version))
        if self.shininess is not None:
            el.append(self.shininess.to_sdf(version))
        if self.specular is not None:
            el.append(self.specular.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_ambient = el.find("ambient")
        if _c_ambient is not None:
            _res = Ambient._from_sdf(_c_ambient, version)
            if isinstance(_res, SDFError):
                return _res.extend("ambient")
            _ambient = _res
        else:
            _ambient = None
        _c_diffuse = el.find("diffuse")
        if _c_diffuse is not None:
            _res = Diffuse._from_sdf(_c_diffuse, version)
            if isinstance(_res, SDFError):
                return _res.extend("diffuse")
            _diffuse = _res
        else:
            _diffuse = None
        _c_double_sided = el.find("double_sided")
        if _c_double_sided is not None:
            _res = DoubleSided._from_sdf(_c_double_sided, version)
            if isinstance(_res, SDFError):
                return _res.extend("double_sided")
            _double_sided = _res
        else:
            _double_sided = None
        if _double_sided is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'double_sided' is not supported in SDF version {version} (added in 1.7)")
        _c_emissive = el.find("emissive")
        if _c_emissive is not None:
            _res = Emissive._from_sdf(_c_emissive, version)
            if isinstance(_res, SDFError):
                return _res.extend("emissive")
            _emissive = _res
        else:
            _emissive = None
        _c_lighting = el.find("lighting")
        if _c_lighting is not None:
            _res = Lighting._from_sdf(_c_lighting, version)
            if isinstance(_res, SDFError):
                return _res.extend("lighting")
            _lighting = _res
        else:
            _lighting = None
        _c_pbr = el.find("pbr")
        if _c_pbr is not None:
            _res = Pbr._from_sdf(_c_pbr, version)
            if isinstance(_res, SDFError):
                return _res.extend("pbr")
            _pbr = _res
        else:
            _pbr = None
        _c_render_order = el.find("render_order")
        if _c_render_order is not None:
            _res = RenderOrder._from_sdf(_c_render_order, version)
            if isinstance(_res, SDFError):
                return _res.extend("render_order")
            _render_order = _res
        else:
            _render_order = None
        if _render_order is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'render_order' is not supported in SDF version {version} (added in 1.7)")
        _c_script = el.find("script")
        if _c_script is not None:
            _res = Script._from_sdf(_c_script, version)
            if isinstance(_res, SDFError):
                return _res.extend("script")
            _script = _res
        else:
            _script = None
        _c_shader = el.find("shader")
        if _c_shader is not None:
            _res = Shader._from_sdf(_c_shader, version)
            if isinstance(_res, SDFError):
                return _res.extend("shader")
            _shader = _res
        else:
            _shader = None
        _c_shininess = el.find("shininess")
        if _c_shininess is not None:
            _res = Shininess._from_sdf(_c_shininess, version)
            if isinstance(_res, SDFError):
                return _res.extend("shininess")
            _shininess = _res
        else:
            _shininess = None
        if _shininess is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'shininess' is not supported in SDF version {version} (added in 1.7)")
        _c_specular = el.find("specular")
        if _c_specular is not None:
            _res = Specular._from_sdf(_c_specular, version)
            if isinstance(_res, SDFError):
                return _res.extend("specular")
            _specular = _res
        else:
            _specular = None
        return cls(sdf_version=version, ambient=_ambient, diffuse=_diffuse, double_sided=_double_sided, emissive=_emissive, lighting=_lighting, pbr=_pbr, render_order=_render_order, script=_script, shader=_shader, shininess=_shininess, specular=_specular)


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
