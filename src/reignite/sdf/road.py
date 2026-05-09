### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.color import Color
from ..utils.vector3 import Vector3
from ..utils.version import cmp_version


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



class Width(BaseModel):
    def __init__(self, sdf_version: str, width: float = 1.0):
        self.__version__ = sdf_version
        self.width = width

    def to_version(self, target_version: str) -> "Width":
        kwargs = {"sdf_version": target_version}
        kwargs["width"] = self.width
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("width")
        if self.width is None:
            raise ValueError(f"'width' is required in SDF version {version}")
        if self.width is not None:
            el.text = str(self.width)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        if el.text is None:
            return SDFError(f"'width' is required in SDF version {version}")
        _text = el.text or 1.0
        _width = _parse_double(_text)
        if isinstance(_width, SDFError):
            return _width
        return cls(sdf_version=version, width=_width)


class Point(BaseModel):
    def __init__(self, sdf_version: str, point: Vector3 = None):
        self.__version__ = sdf_version
        if point is None:
            point = Vector3.from_sdf("0 0 0")
        self.point = point

    def to_version(self, target_version: str) -> "Point":
        kwargs = {"sdf_version": target_version}
        kwargs["point"] = self.point
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("point")
        if self.point is None:
            raise ValueError(f"'point' is required in SDF version {version}")
        if self.point is not None:
            el.text = self.point.to_sdf()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        if el.text is None:
            return SDFError(f"'point' is required in SDF version {version}")
        _text = el.text or "0 0 0"
        _point = Vector3._from_sdf(_text, version)
        if isinstance(_point, SDFError):
            return _point
        return cls(sdf_version=version, point=_point)


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
        if self.uri is None:
            raise ValueError(f"'uri' is required in SDF version {version}")
        if self.uri is not None:
            el.text = self.uri
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        if el.text is None:
            return SDFError(f"'uri' is required in SDF version {version}")
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
        if self.name is None:
            raise ValueError(f"'name' is required in SDF version {version}")
        if self.name is not None:
            el.text = self.name
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        if el.text is None:
            return SDFError(f"'name' is required in SDF version {version}")
        _text = el.text or "__default__"
        _name = _text
        if isinstance(_name, SDFError):
            return _name
        return cls(sdf_version=version, name=_name)


class Script(BaseModel):
    def __init__(self, sdf_version: str, uri: List["Uri"] = None, name: "Name" = None):
        self.__version__ = sdf_version
        self.uri = uri or []
        self.name = name

    def to_version(self, target_version: str) -> "Script":
        kwargs = {"sdf_version": target_version}
        kwargs["uri"] = [c.to_version(target_version) for c in (self.uri or [])]
        kwargs["name"] = self.name.to_version(target_version) if self.name is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("script")
        if not self.uri:
            raise ValueError(f"'uri' is required in SDF version {version}")
        for item in (self.uri or []):
            el.append(item.to_sdf(version))
        if self.name is None:
            raise ValueError(f"'name' is required in SDF version {version}")
        if self.name is not None:
            el.append(self.name.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _uri = []
        for c in el.findall("uri"):
            _res = Uri._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("uri")
            _uri.append(_res)
        if not _uri:
            return SDFError(f"'uri' is required in SDF version {version}")
        _c_name = el.find("name")
        if _c_name is not None:
            _res = Name._from_sdf(_c_name, version)
            if isinstance(_res, SDFError):
                return _res.extend("name")
            _name = _res
        else:
            _name = None
        if _name is None:
            return SDFError(f"'name' is required in SDF version {version}")
        return cls(sdf_version=version, uri=_uri, name=_name)


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
    def __init__(self, sdf_version: str, type: str = "pixel", normal_map: "NormalMap" = None):
        self.__version__ = sdf_version
        self.type = type
        self.normal_map = normal_map

    def to_version(self, target_version: str) -> "Shader":
        kwargs = {"sdf_version": target_version}
        kwargs["type"] = self.type
        kwargs["normal_map"] = self.normal_map.to_version(target_version) if self.normal_map is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("shader")
        if self.type is None:
            raise ValueError(f"'type' is required in SDF version {version}")
        if self.type is not None:
            el.set("type", self.type)
        if self.normal_map is not None:
            el.append(self.normal_map.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        if el.get("type") is None:
            return SDFError(f"'type' is required in SDF version {version}")
        _type = el.get("type", "pixel")
        if isinstance(_type, SDFError):
            return _type.extend("@type")
        _c_normal_map = el.find("normal_map")
        if _c_normal_map is not None:
            _res = NormalMap._from_sdf(_c_normal_map, version)
            if isinstance(_res, SDFError):
                return _res.extend("normal_map")
            _normal_map = _res
        else:
            _normal_map = None
        return cls(sdf_version=version, type=_type, normal_map=_normal_map)


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
    def __init__(self, sdf_version: str, ambient: Color = None):
        self.__version__ = sdf_version
        if ambient is None:
            ambient = Color.from_sdf("0 0 0 1")
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
        _ambient = Color._from_sdf(_text, version)
        if isinstance(_ambient, SDFError):
            return _ambient
        return cls(sdf_version=version, ambient=_ambient)


class Diffuse(BaseModel):
    def __init__(self, sdf_version: str, diffuse: Color = None):
        self.__version__ = sdf_version
        if diffuse is None:
            diffuse = Color.from_sdf("0 0 0 1")
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
        _diffuse = Color._from_sdf(_text, version)
        if isinstance(_diffuse, SDFError):
            return _diffuse
        return cls(sdf_version=version, diffuse=_diffuse)


class Specular(BaseModel):
    def __init__(self, sdf_version: str, specular: Color = None):
        self.__version__ = sdf_version
        if specular is None:
            specular = Color.from_sdf("0 0 0 1")
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
        _specular = Color._from_sdf(_text, version)
        if isinstance(_specular, SDFError):
            return _specular
        return cls(sdf_version=version, specular=_specular)


class Emissive(BaseModel):
    def __init__(self, sdf_version: str, emissive: Color = None):
        self.__version__ = sdf_version
        if emissive is None:
            emissive = Color.from_sdf("0 0 0 1")
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
        _emissive = Color._from_sdf(_text, version)
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
        roughness_map: "RoughnessMap" = None,
        roughness: "Roughness" = None,
        metalness_map: "MetalnessMap" = None,
        metalness: "Metalness" = None,
        environment_map: "EnvironmentMap" = None,
        ambient_occlusion_map: "AmbientOcclusionMap" = None,
        normal_map: "NormalMap" = None,
        emissive_map: "EmissiveMap" = None,
        light_map: "LightMap" = None
    ):
        self.__version__ = sdf_version
        self.albedo_map = albedo_map
        self.roughness_map = roughness_map
        self.roughness = roughness
        self.metalness_map = metalness_map
        self.metalness = metalness
        self.environment_map = environment_map
        self.ambient_occlusion_map = ambient_occlusion_map
        self.normal_map = normal_map
        self.emissive_map = emissive_map
        self.light_map = light_map

    def to_version(self, target_version: str) -> "Metal":
        if self.light_map is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'light_map' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["albedo_map"] = self.albedo_map.to_version(target_version) if self.albedo_map is not None else None
        kwargs["roughness_map"] = self.roughness_map.to_version(target_version) if self.roughness_map is not None else None
        kwargs["roughness"] = self.roughness.to_version(target_version) if self.roughness is not None else None
        kwargs["metalness_map"] = self.metalness_map.to_version(target_version) if self.metalness_map is not None else None
        kwargs["metalness"] = self.metalness.to_version(target_version) if self.metalness is not None else None
        kwargs["environment_map"] = self.environment_map.to_version(target_version) if self.environment_map is not None else None
        kwargs["ambient_occlusion_map"] = self.ambient_occlusion_map.to_version(target_version) if self.ambient_occlusion_map is not None else None
        kwargs["normal_map"] = self.normal_map.to_version(target_version) if self.normal_map is not None else None
        kwargs["emissive_map"] = self.emissive_map.to_version(target_version) if self.emissive_map is not None else None
        kwargs["light_map"] = self.light_map.to_version(target_version) if self.light_map is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("metal")
        if self.albedo_map is not None:
            el.append(self.albedo_map.to_sdf(version))
        if self.roughness_map is not None:
            el.append(self.roughness_map.to_sdf(version))
        if self.roughness is not None:
            el.append(self.roughness.to_sdf(version))
        if self.metalness_map is not None:
            el.append(self.metalness_map.to_sdf(version))
        if self.metalness is not None:
            el.append(self.metalness.to_sdf(version))
        if self.environment_map is not None:
            el.append(self.environment_map.to_sdf(version))
        if self.ambient_occlusion_map is not None:
            el.append(self.ambient_occlusion_map.to_sdf(version))
        if self.normal_map is not None:
            el.append(self.normal_map.to_sdf(version))
        if self.emissive_map is not None:
            el.append(self.emissive_map.to_sdf(version))
        if self.light_map is not None:
            el.append(self.light_map.to_sdf(version))
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
        _c_roughness_map = el.find("roughness_map")
        if _c_roughness_map is not None:
            _res = RoughnessMap._from_sdf(_c_roughness_map, version)
            if isinstance(_res, SDFError):
                return _res.extend("roughness_map")
            _roughness_map = _res
        else:
            _roughness_map = None
        _c_roughness = el.find("roughness")
        if _c_roughness is not None:
            _res = Roughness._from_sdf(_c_roughness, version)
            if isinstance(_res, SDFError):
                return _res.extend("roughness")
            _roughness = _res
        else:
            _roughness = None
        _c_metalness_map = el.find("metalness_map")
        if _c_metalness_map is not None:
            _res = MetalnessMap._from_sdf(_c_metalness_map, version)
            if isinstance(_res, SDFError):
                return _res.extend("metalness_map")
            _metalness_map = _res
        else:
            _metalness_map = None
        _c_metalness = el.find("metalness")
        if _c_metalness is not None:
            _res = Metalness._from_sdf(_c_metalness, version)
            if isinstance(_res, SDFError):
                return _res.extend("metalness")
            _metalness = _res
        else:
            _metalness = None
        _c_environment_map = el.find("environment_map")
        if _c_environment_map is not None:
            _res = EnvironmentMap._from_sdf(_c_environment_map, version)
            if isinstance(_res, SDFError):
                return _res.extend("environment_map")
            _environment_map = _res
        else:
            _environment_map = None
        _c_ambient_occlusion_map = el.find("ambient_occlusion_map")
        if _c_ambient_occlusion_map is not None:
            _res = AmbientOcclusionMap._from_sdf(_c_ambient_occlusion_map, version)
            if isinstance(_res, SDFError):
                return _res.extend("ambient_occlusion_map")
            _ambient_occlusion_map = _res
        else:
            _ambient_occlusion_map = None
        _c_normal_map = el.find("normal_map")
        if _c_normal_map is not None:
            _res = NormalMap._from_sdf(_c_normal_map, version)
            if isinstance(_res, SDFError):
                return _res.extend("normal_map")
            _normal_map = _res
        else:
            _normal_map = None
        _c_emissive_map = el.find("emissive_map")
        if _c_emissive_map is not None:
            _res = EmissiveMap._from_sdf(_c_emissive_map, version)
            if isinstance(_res, SDFError):
                return _res.extend("emissive_map")
            _emissive_map = _res
        else:
            _emissive_map = None
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
        return cls(sdf_version=version, albedo_map=_albedo_map, roughness_map=_roughness_map, roughness=_roughness, metalness_map=_metalness_map, metalness=_metalness, environment_map=_environment_map, ambient_occlusion_map=_ambient_occlusion_map, normal_map=_normal_map, emissive_map=_emissive_map, light_map=_light_map)


class Pbr(BaseModel):
    def __init__(self, sdf_version: str, metal: "Metal" = None, specular: "Specular" = None):
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
            _res = Specular._from_sdf(_c_specular, version)
            if isinstance(_res, SDFError):
                return _res.extend("specular")
            _specular = _res
        else:
            _specular = None
        return cls(sdf_version=version, metal=_metal, specular=_specular)


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


class Material(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        script: "Script" = None,
        shader: "Shader" = None,
        lighting: "Lighting" = None,
        ambient: "Ambient" = None,
        diffuse: "Diffuse" = None,
        specular: "Specular" = None,
        emissive: "Emissive" = None,
        pbr: "Pbr" = None,
        shininess: "Shininess" = None,
        render_order: "RenderOrder" = None,
        double_sided: "DoubleSided" = None
    ):
        self.__version__ = sdf_version
        self.script = script
        self.shader = shader
        self.lighting = lighting
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.emissive = emissive
        self.pbr = pbr
        self.shininess = shininess
        self.render_order = render_order
        self.double_sided = double_sided

    def to_version(self, target_version: str) -> "Material":
        if self.pbr is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'pbr' is not supported in SDF version {target_version} (added in 1.6)")
        if self.shininess is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'shininess' is not supported in SDF version {target_version} (added in 1.7)")
        if self.render_order is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'render_order' is not supported in SDF version {target_version} (added in 1.7)")
        if self.double_sided is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'double_sided' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["script"] = self.script.to_version(target_version) if self.script is not None else None
        kwargs["shader"] = self.shader.to_version(target_version) if self.shader is not None else None
        kwargs["lighting"] = self.lighting.to_version(target_version) if self.lighting is not None else None
        kwargs["ambient"] = self.ambient.to_version(target_version) if self.ambient is not None else None
        kwargs["diffuse"] = self.diffuse.to_version(target_version) if self.diffuse is not None else None
        kwargs["specular"] = self.specular.to_version(target_version) if self.specular is not None else None
        kwargs["emissive"] = self.emissive.to_version(target_version) if self.emissive is not None else None
        kwargs["pbr"] = self.pbr.to_version(target_version) if self.pbr is not None else None
        kwargs["shininess"] = self.shininess.to_version(target_version) if self.shininess is not None else None
        kwargs["render_order"] = self.render_order.to_version(target_version) if self.render_order is not None else None
        kwargs["double_sided"] = self.double_sided.to_version(target_version) if self.double_sided is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("material")
        if self.script is not None:
            el.append(self.script.to_sdf(version))
        if self.shader is not None:
            el.append(self.shader.to_sdf(version))
        if self.lighting is not None:
            el.append(self.lighting.to_sdf(version))
        if self.ambient is not None:
            el.append(self.ambient.to_sdf(version))
        if self.diffuse is not None:
            el.append(self.diffuse.to_sdf(version))
        if self.specular is not None:
            el.append(self.specular.to_sdf(version))
        if self.emissive is not None:
            el.append(self.emissive.to_sdf(version))
        if self.pbr is not None:
            el.append(self.pbr.to_sdf(version))
        if self.shininess is not None:
            el.append(self.shininess.to_sdf(version))
        if self.render_order is not None:
            el.append(self.render_order.to_sdf(version))
        if self.double_sided is not None:
            el.append(self.double_sided.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
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
        _c_lighting = el.find("lighting")
        if _c_lighting is not None:
            _res = Lighting._from_sdf(_c_lighting, version)
            if isinstance(_res, SDFError):
                return _res.extend("lighting")
            _lighting = _res
        else:
            _lighting = None
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
        _c_specular = el.find("specular")
        if _c_specular is not None:
            _res = Specular._from_sdf(_c_specular, version)
            if isinstance(_res, SDFError):
                return _res.extend("specular")
            _specular = _res
        else:
            _specular = None
        _c_emissive = el.find("emissive")
        if _c_emissive is not None:
            _res = Emissive._from_sdf(_c_emissive, version)
            if isinstance(_res, SDFError):
                return _res.extend("emissive")
            _emissive = _res
        else:
            _emissive = None
        _c_pbr = el.find("pbr")
        if _c_pbr is not None:
            _res = Pbr._from_sdf(_c_pbr, version)
            if isinstance(_res, SDFError):
                return _res.extend("pbr")
            _pbr = _res
        else:
            _pbr = None
        if _pbr is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'pbr' is not supported in SDF version {version} (added in 1.6)")
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
        return cls(sdf_version=version, script=_script, shader=_shader, lighting=_lighting, ambient=_ambient, diffuse=_diffuse, specular=_specular, emissive=_emissive, pbr=_pbr, shininess=_shininess, render_order=_render_order, double_sided=_double_sided)


class Road(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        name: str = "__default__",
        width: "Width" = None,
        point: List["Point"] = None,
        material: "Material" = None
    ):
        self.__version__ = sdf_version
        self.name = name
        self.width = width
        self.point = point or []
        self.material = material

    def to_version(self, target_version: str) -> "Road":
        if self.material is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'material' is not supported in SDF version {target_version} (added in 1.5)")
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["width"] = self.width.to_version(target_version) if self.width is not None else None
        kwargs["point"] = [c.to_version(target_version) for c in (self.point or [])]
        kwargs["material"] = self.material.to_version(target_version) if self.material is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("road")
        if self.name is None:
            raise ValueError(f"'name' is required in SDF version {version}")
        if self.name is not None:
            el.set("name", self.name)
        if self.width is None:
            raise ValueError(f"'width' is required in SDF version {version}")
        if self.width is not None:
            el.append(self.width.to_sdf(version))
        if not self.point:
            raise ValueError(f"'point' is required in SDF version {version}")
        for item in (self.point or []):
            el.append(item.to_sdf(version))
        if self.material is not None:
            el.append(self.material.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        if el.get("name") is None:
            return SDFError(f"'name' is required in SDF version {version}")
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        _c_width = el.find("width")
        if _c_width is not None:
            _res = Width._from_sdf(_c_width, version)
            if isinstance(_res, SDFError):
                return _res.extend("width")
            _width = _res
        else:
            _width = None
        if _width is None:
            return SDFError(f"'width' is required in SDF version {version}")
        _point = []
        for c in el.findall("point"):
            _res = Point._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("point")
            _point.append(_res)
        if not _point:
            return SDFError(f"'point' is required in SDF version {version}")
        _c_material = el.find("material")
        if _c_material is not None:
            _res = Material._from_sdf(_c_material, version)
            if isinstance(_res, SDFError):
                return _res.extend("material")
            _material = _res
        else:
            _material = None
        if _material is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'material' is not supported in SDF version {version} (added in 1.5)")
        return cls(sdf_version=version, name=_name, width=_width, point=_point, material=_material)
