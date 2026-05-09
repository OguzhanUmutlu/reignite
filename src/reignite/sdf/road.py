### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.vector3 import Vector3 as _SDFVector3
from ..utils.version import cmp_version

from .material import Material


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



class Point(BaseModel):
    def __init__(self, sdf_version: str, point: _SDFVector3 = None):
        self.__version__ = sdf_version
        if point is None:
            point = _SDFVector3.from_sdf("0 0 0")
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
        if self.point is not None:
            el.text = self.point.to_sdf()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 0"
        _point = _SDFVector3._from_sdf(_text, version)
        if isinstance(_point, SDFError):
            return _point
        return cls(sdf_version=version, point=_point)


class Road(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        material: "Material" = None,
        name: str = "__default__",
        point: List["Point"] = None,
        width: "Width" = None
    ):
        self.__version__ = sdf_version
        self.material = material
        self.name = name
        self.point = point or []
        self.width = width

    def to_version(self, target_version: str) -> "Road":
        if self.material is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'material' is not supported in SDF version {target_version} (added in 1.5)")
        kwargs = {"sdf_version": target_version}
        kwargs["material"] = self.material.to_version(target_version) if self.material is not None else None
        kwargs["name"] = self.name
        kwargs["point"] = [c.to_version(target_version) for c in (self.point or [])]
        kwargs["width"] = self.width.to_version(target_version) if self.width is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("road")
        if self.material is not None:
            el.append(self.material.to_sdf(version))
        if self.name is not None:
            el.set("name", self.name)
        for item in (self.point or []):
            el.append(item.to_sdf(version))
        if self.width is not None:
            el.append(self.width.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
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
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        _point = []
        for c in el.findall("point"):
            _res = Point._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("point")
            _point.append(_res)
        _c_width = el.find("width")
        if _c_width is not None:
            _res = Width._from_sdf(_c_width, version)
            if isinstance(_res, SDFError):
                return _res.extend("width")
            _width = _res
        else:
            _width = None
        return cls(sdf_version=version, material=_material, name=_name, point=_point, width=_width)


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
        if self.width is not None:
            el.text = str(self.width)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1.0
        _width = _parse_double(_text)
        if isinstance(_width, SDFError):
            return _width
        return cls(sdf_version=version, width=_width)
