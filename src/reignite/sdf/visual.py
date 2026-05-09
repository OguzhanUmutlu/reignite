### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.color import Color as _SDFColor
from ..utils.pose import Pose as _SDFPose
from ..utils.vector2d import Vector2d as _SDFVector2d
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



class Size(BaseModel):
    def __init__(self, sdf_version: str, size: _SDFVector3 = None):
        self.__version__ = sdf_version
        if size is None:
            size = _SDFVector3.from_sdf("1 1 1")
        self.size = size

    def to_version(self, target_version: str) -> "Size":
        if self.size is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'size' is not supported in SDF version {target_version} (added in 1.2)")
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
        if _size is not None and cmp_version(version, "1.2") < 0:
            if _size != "1 1 1":
                return SDFError(f"'size' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, size=_size)


class Box(BaseModel):
    def __init__(self, sdf_version: str, size: _SDFVector3 = None):
        self.__version__ = sdf_version
        if size is None:
            size = _SDFVector3.from_sdf("1 1 1")
        self.size = size

    def to_version(self, target_version: str) -> "Box":
        if self.size is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'size' is not supported in SDF version {target_version} (removed in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["size"] = self.size
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("box")
        if self.size is not None:
            el.set("size", self.size.to_sdf())
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _size = _SDFVector3._from_sdf(el.get("size", "1 1 1"), version)
        if isinstance(_size, SDFError):
            return _size.extend("@size")
        return cls(sdf_version=version, size=_size)


class Radius(BaseModel):
    def __init__(self, sdf_version: str, radius: float = 1):
        self.__version__ = sdf_version
        self.radius = radius

    def to_version(self, target_version: str) -> "Radius":
        if self.radius is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'radius' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["radius"] = self.radius
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("radius")
        if self.radius is not None:
            el.text = str(self.radius)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _radius = _parse_double(_text)
        if isinstance(_radius, SDFError):
            return _radius
        if _radius is not None and cmp_version(version, "1.2") < 0:
            if _radius != 1:
                return SDFError(f"'radius' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, radius=_radius)


class Sphere(BaseModel):
    def __init__(self, sdf_version: str, radius: float = 1):
        self.__version__ = sdf_version
        self.radius = radius

    def to_version(self, target_version: str) -> "Sphere":
        if self.radius is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'radius' is not supported in SDF version {target_version} (removed in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["radius"] = self.radius
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("sphere")
        if self.radius is not None:
            el.set("radius", str(self.radius))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _radius = _parse_double(el.get("radius", 1))
        if isinstance(_radius, SDFError):
            return _radius.extend("@radius")
        return cls(sdf_version=version, radius=_radius)


class Length(BaseModel):
    def __init__(self, sdf_version: str, length: float = 1):
        self.__version__ = sdf_version
        self.length = length

    def to_version(self, target_version: str) -> "Length":
        if self.length is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'length' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["length"] = self.length
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("length")
        if self.length is not None:
            el.text = str(self.length)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _length = _parse_double(_text)
        if isinstance(_length, SDFError):
            return _length
        if _length is not None and cmp_version(version, "1.2") < 0:
            if _length != 1:
                return SDFError(f"'length' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, length=_length)


class Cylinder(BaseModel):
    def __init__(self, sdf_version: str, length: float = 1, radius: float = 1):
        self.__version__ = sdf_version
        self.length = length
        self.radius = radius

    def to_version(self, target_version: str) -> "Cylinder":
        if self.length is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'length' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.radius is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'radius' is not supported in SDF version {target_version} (removed in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["length"] = self.length
        kwargs["radius"] = self.radius
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("cylinder")
        if self.length is not None:
            el.set("length", str(self.length))
        if self.radius is not None:
            el.set("radius", str(self.radius))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _length = _parse_double(el.get("length", 1))
        if isinstance(_length, SDFError):
            return _length.extend("@length")
        _radius = _parse_double(el.get("radius", 1))
        if isinstance(_radius, SDFError):
            return _radius.extend("@radius")
        return cls(sdf_version=version, length=_length, radius=_radius)


class Uri(BaseModel):
    def __init__(self, sdf_version: str, uri: str = "__default__"):
        self.__version__ = sdf_version
        self.uri = uri

    def to_version(self, target_version: str) -> "Uri":
        if self.uri is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'uri' is not supported in SDF version {target_version} (added in 1.2)")
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
        if _uri is not None and cmp_version(version, "1.2") < 0:
            if _uri != "__default__":
                return SDFError(f"'uri' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, uri=_uri)


class Scale(BaseModel):
    def __init__(self, sdf_version: str, scale: _SDFVector3 = None):
        self.__version__ = sdf_version
        if scale is None:
            scale = _SDFVector3.from_sdf("1 1 1")
        self.scale = scale

    def to_version(self, target_version: str) -> "Scale":
        if self.scale is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'scale' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["scale"] = self.scale
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("scale")
        if self.scale is not None:
            el.text = self.scale.to_sdf()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "1 1 1"
        _scale = _SDFVector3._from_sdf(_text, version)
        if isinstance(_scale, SDFError):
            return _scale
        if _scale is not None and cmp_version(version, "1.2") < 0:
            if _scale != "1 1 1":
                return SDFError(f"'scale' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, scale=_scale)


class Filename(BaseModel):
    def __init__(self, sdf_version: str, filename: str = "__default__"):
        self.__version__ = sdf_version
        self.filename = filename

    def to_version(self, target_version: str) -> "Filename":
        if self.filename is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'filename' is not supported in SDF version {target_version} (added in 1.2)")
        if self.filename is not None and cmp_version(target_version, "1.3") >= 0:
            raise ValueError(f"'filename' is not supported in SDF version {target_version} (removed in 1.3)")
        kwargs = {"sdf_version": target_version}
        kwargs["filename"] = self.filename
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("filename")
        if self.filename is not None:
            el.text = self.filename
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "__default__"
        _filename = _text
        if isinstance(_filename, SDFError):
            return _filename
        if _filename is not None and cmp_version(version, "1.2") < 0:
            if _filename != "__default__":
                return SDFError(f"'filename' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, filename=_filename)


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


class Center(BaseModel):
    def __init__(self, sdf_version: str, center: bool = False):
        self.__version__ = sdf_version
        self.center = center

    def to_version(self, target_version: str) -> "Center":
        kwargs = {"sdf_version": target_version}
        kwargs["center"] = self.center
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("center")
        if self.center is not None:
            el.text = str(self.center).lower()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or False
        _center = str(_text).strip().lower() == 'true'
        if isinstance(_center, SDFError):
            return _center
        return cls(sdf_version=version, center=_center)


class Submesh(BaseModel):
    def __init__(self, sdf_version: str, center: "Center" = None, name: "Name" = None):
        self.__version__ = sdf_version
        self.center = center
        self.name = name

    def to_version(self, target_version: str) -> "Submesh":
        kwargs = {"sdf_version": target_version}
        kwargs["center"] = self.center.to_version(target_version) if self.center is not None else None
        kwargs["name"] = self.name.to_version(target_version) if self.name is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("submesh")
        if self.center is not None:
            el.append(self.center.to_sdf(version))
        if self.name is not None:
            el.append(self.name.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_center = el.find("center")
        if _c_center is not None:
            _res = Center._from_sdf(_c_center, version)
            if isinstance(_res, SDFError):
                return _res.extend("center")
            _center = _res
        else:
            _center = None
        _c_name = el.find("name")
        if _c_name is not None:
            _res = Name._from_sdf(_c_name, version)
            if isinstance(_res, SDFError):
                return _res.extend("name")
            _name = _res
        else:
            _name = None
        return cls(sdf_version=version, center=_center, name=_name)


class MaxConvexHulls(BaseModel):
    def __init__(self, sdf_version: str, max_convex_hulls: int = 16):
        self.__version__ = sdf_version
        self.max_convex_hulls = max_convex_hulls

    def to_version(self, target_version: str) -> "MaxConvexHulls":
        kwargs = {"sdf_version": target_version}
        kwargs["max_convex_hulls"] = self.max_convex_hulls
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("max_convex_hulls")
        if self.max_convex_hulls is not None:
            el.text = str(self.max_convex_hulls)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 16
        _max_convex_hulls = _parse_uint32(_text)
        if isinstance(_max_convex_hulls, SDFError):
            return _max_convex_hulls
        return cls(sdf_version=version, max_convex_hulls=_max_convex_hulls)


class VoxelResolution(BaseModel):
    def __init__(self, sdf_version: str, voxel_resolution: int = 200000):
        self.__version__ = sdf_version
        self.voxel_resolution = voxel_resolution

    def to_version(self, target_version: str) -> "VoxelResolution":
        kwargs = {"sdf_version": target_version}
        kwargs["voxel_resolution"] = self.voxel_resolution
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("voxel_resolution")
        if self.voxel_resolution is not None:
            el.text = str(self.voxel_resolution)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 200000
        _voxel_resolution = _parse_uint32(_text)
        if isinstance(_voxel_resolution, SDFError):
            return _voxel_resolution
        return cls(sdf_version=version, voxel_resolution=_voxel_resolution)


class ConvexDecomposition(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        max_convex_hulls: "MaxConvexHulls" = None,
        voxel_resolution: "VoxelResolution" = None
    ):
        self.__version__ = sdf_version
        self.max_convex_hulls = max_convex_hulls
        self.voxel_resolution = voxel_resolution

    def to_version(self, target_version: str) -> "ConvexDecomposition":
        kwargs = {"sdf_version": target_version}
        kwargs["max_convex_hulls"] = self.max_convex_hulls.to_version(target_version) if self.max_convex_hulls is not None else None
        kwargs["voxel_resolution"] = self.voxel_resolution.to_version(target_version) if self.voxel_resolution is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("convex_decomposition")
        if self.max_convex_hulls is not None:
            el.append(self.max_convex_hulls.to_sdf(version))
        if self.voxel_resolution is not None:
            el.append(self.voxel_resolution.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_max_convex_hulls = el.find("max_convex_hulls")
        if _c_max_convex_hulls is not None:
            _res = MaxConvexHulls._from_sdf(_c_max_convex_hulls, version)
            if isinstance(_res, SDFError):
                return _res.extend("max_convex_hulls")
            _max_convex_hulls = _res
        else:
            _max_convex_hulls = None
        _c_voxel_resolution = el.find("voxel_resolution")
        if _c_voxel_resolution is not None:
            _res = VoxelResolution._from_sdf(_c_voxel_resolution, version)
            if isinstance(_res, SDFError):
                return _res.extend("voxel_resolution")
            _voxel_resolution = _res
        else:
            _voxel_resolution = None
        return cls(sdf_version=version, max_convex_hulls=_max_convex_hulls, voxel_resolution=_voxel_resolution)


class Mesh(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        convex_decomposition: "ConvexDecomposition" = None,
        filename: str = "__default__",
        optimization: str = "",
        scale: _SDFVector3 = None,
        submesh: "Submesh" = None,
        uri: "Uri" = None
    ):
        self.__version__ = sdf_version
        if scale is None:
            scale = _SDFVector3.from_sdf("1 1 1")
        self.convex_decomposition = convex_decomposition
        self.filename = filename
        self.optimization = optimization
        self.scale = scale
        self.submesh = submesh
        self.uri = uri

    def to_version(self, target_version: str) -> "Mesh":
        if self.convex_decomposition is not None and cmp_version(target_version, "1.11") < 0:
            raise ValueError(f"'convex_decomposition' is not supported in SDF version {target_version} (added in 1.11)")
        if self.filename is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'filename' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.optimization is not None and cmp_version(target_version, "1.11") < 0:
            raise ValueError(f"'optimization' is not supported in SDF version {target_version} (added in 1.11)")
        if self.scale is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'scale' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.submesh is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'submesh' is not supported in SDF version {target_version} (added in 1.3)")
        if self.uri is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'uri' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["convex_decomposition"] = self.convex_decomposition.to_version(target_version) if self.convex_decomposition is not None else None
        kwargs["filename"] = self.filename
        kwargs["optimization"] = self.optimization
        kwargs["scale"] = self.scale
        kwargs["submesh"] = self.submesh.to_version(target_version) if self.submesh is not None else None
        kwargs["uri"] = self.uri.to_version(target_version) if self.uri is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("mesh")
        if self.convex_decomposition is not None:
            el.append(self.convex_decomposition.to_sdf(version))
        if self.filename is not None:
            el.set("filename", self.filename)
        if self.optimization is not None:
            el.set("optimization", self.optimization)
        if self.scale is not None:
            el.set("scale", self.scale.to_sdf())
        if self.submesh is not None:
            el.append(self.submesh.to_sdf(version))
        if self.uri is not None:
            el.append(self.uri.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_convex_decomposition = el.find("convex_decomposition")
        if _c_convex_decomposition is not None:
            _res = ConvexDecomposition._from_sdf(_c_convex_decomposition, version)
            if isinstance(_res, SDFError):
                return _res.extend("convex_decomposition")
            _convex_decomposition = _res
        else:
            _convex_decomposition = None
        if _convex_decomposition is not None and cmp_version(version, "1.11") < 0:
            return SDFError(f"'convex_decomposition' is not supported in SDF version {version} (added in 1.11)")
        _filename = el.get("filename", "__default__")
        if isinstance(_filename, SDFError):
            return _filename.extend("@filename")
        _optimization = el.get("optimization", "")
        if isinstance(_optimization, SDFError):
            return _optimization.extend("@optimization")
        if _optimization is not None and cmp_version(version, "1.11") < 0:
            if _optimization != "":
                return SDFError(f"'optimization' is not supported in SDF version {version} (added in 1.11)")
        _scale = _SDFVector3._from_sdf(el.get("scale", "1 1 1"), version)
        if isinstance(_scale, SDFError):
            return _scale.extend("@scale")
        _c_submesh = el.find("submesh")
        if _c_submesh is not None:
            _res = Submesh._from_sdf(_c_submesh, version)
            if isinstance(_res, SDFError):
                return _res.extend("submesh")
            _submesh = _res
        else:
            _submesh = None
        if _submesh is not None and cmp_version(version, "1.3") < 0:
            return SDFError(f"'submesh' is not supported in SDF version {version} (added in 1.3)")
        _c_uri = el.find("uri")
        if _c_uri is not None:
            _res = Uri._from_sdf(_c_uri, version)
            if isinstance(_res, SDFError):
                return _res.extend("uri")
            _uri = _res
        else:
            _uri = None
        if _uri is not None and cmp_version(version, "1.2") < 0:
            return SDFError(f"'uri' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, convex_decomposition=_convex_decomposition, filename=_filename, optimization=_optimization, scale=_scale, submesh=_submesh, uri=_uri)


class PlaneSize(BaseModel):
    def __init__(self, sdf_version: str, size: _SDFVector2d = None):
        self.__version__ = sdf_version
        if size is None:
            size = _SDFVector2d.from_sdf("1 1")
        self.size = size

    def to_version(self, target_version: str) -> "PlaneSize":
        if self.size is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'size' is not supported in SDF version {target_version} (added in 1.2)")
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
        _text = el.text or "1 1"
        _size = _SDFVector2d._from_sdf(_text, version)
        if isinstance(_size, SDFError):
            return _size
        if _size is not None and cmp_version(version, "1.2") < 0:
            if _size != "1 1":
                return SDFError(f"'size' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, size=_size)


class Normal(BaseModel):
    def __init__(self, sdf_version: str, normal: _SDFVector3 = None):
        self.__version__ = sdf_version
        if normal is None:
            normal = _SDFVector3.from_sdf("0 0 1")
        self.normal = normal

    def to_version(self, target_version: str) -> "Normal":
        if self.normal is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'normal' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["normal"] = self.normal
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("normal")
        if self.normal is not None:
            el.text = self.normal.to_sdf()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 1"
        _normal = _SDFVector3._from_sdf(_text, version)
        if isinstance(_normal, SDFError):
            return _normal
        if _normal is not None and cmp_version(version, "1.2") < 0:
            if _normal != "0 0 1":
                return SDFError(f"'normal' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, normal=_normal)


class Plane(BaseModel):
    def __init__(self, sdf_version: str, normal: _SDFVector3 = None, size: "PlaneSize" = None):
        self.__version__ = sdf_version
        if normal is None:
            normal = _SDFVector3.from_sdf("0 0 1")
        self.normal = normal
        self.size = size

    def to_version(self, target_version: str) -> "Plane":
        if self.normal is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'normal' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.size is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'size' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["normal"] = self.normal
        kwargs["size"] = self.size.to_version(target_version) if self.size is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("plane")
        if self.normal is not None:
            el.set("normal", self.normal.to_sdf())
        if self.size is not None:
            el.append(self.size.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _normal = _SDFVector3._from_sdf(el.get("normal", "0 0 1"), version)
        if isinstance(_normal, SDFError):
            return _normal.extend("@normal")
        _c_size = el.find("size")
        if _c_size is not None:
            _res = PlaneSize._from_sdf(_c_size, version)
            if isinstance(_res, SDFError):
                return _res.extend("size")
            _size = _res
        else:
            _size = None
        if _size is not None and cmp_version(version, "1.2") < 0:
            return SDFError(f"'size' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, normal=_normal, size=_size)


class Granularity(BaseModel):
    def __init__(self, sdf_version: str, granularity: int = 1):
        self.__version__ = sdf_version
        self.granularity = granularity

    def to_version(self, target_version: str) -> "Granularity":
        if self.granularity is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'granularity' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["granularity"] = self.granularity
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("granularity")
        if self.granularity is not None:
            el.text = str(self.granularity)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _granularity = _parse_int32(_text)
        if isinstance(_granularity, SDFError):
            return _granularity
        if _granularity is not None and cmp_version(version, "1.2") < 0:
            if _granularity != 1:
                return SDFError(f"'granularity' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, granularity=_granularity)


class ImageScale(BaseModel):
    def __init__(self, sdf_version: str, scale: float = 1):
        self.__version__ = sdf_version
        self.scale = scale

    def to_version(self, target_version: str) -> "ImageScale":
        if self.scale is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'scale' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["scale"] = self.scale
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("scale")
        if self.scale is not None:
            el.text = str(self.scale)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _scale = _parse_double(_text)
        if isinstance(_scale, SDFError):
            return _scale
        if _scale is not None and cmp_version(version, "1.2") < 0:
            if _scale != 1:
                return SDFError(f"'scale' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, scale=_scale)


class Height(BaseModel):
    def __init__(self, sdf_version: str, height: float = 1):
        self.__version__ = sdf_version
        self.height = height

    def to_version(self, target_version: str) -> "Height":
        if self.height is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'height' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["height"] = self.height
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("height")
        if self.height is not None:
            el.text = str(self.height)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _height = _parse_double(_text)
        if isinstance(_height, SDFError):
            return _height
        if _height is not None and cmp_version(version, "1.2") < 0:
            if _height != 1:
                return SDFError(f"'height' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, height=_height)


class Threshold(BaseModel):
    def __init__(self, sdf_version: str, threshold: int = 200):
        self.__version__ = sdf_version
        self.threshold = threshold

    def to_version(self, target_version: str) -> "Threshold":
        if self.threshold is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'threshold' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["threshold"] = self.threshold
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("threshold")
        if self.threshold is not None:
            el.text = str(self.threshold)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 200
        _threshold = _parse_int32(_text)
        if isinstance(_threshold, SDFError):
            return _threshold
        if _threshold is not None and cmp_version(version, "1.2") < 0:
            if _threshold != 200:
                return SDFError(f"'threshold' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, threshold=_threshold)


class Image(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        filename: str = "__default__",
        granularity: int = 1,
        height: float = 1,
        scale: float = 1,
        threshold: int = 200,
        uri: "Uri" = None
    ):
        self.__version__ = sdf_version
        self.filename = filename
        self.granularity = granularity
        self.height = height
        self.scale = scale
        self.threshold = threshold
        self.uri = uri

    def to_version(self, target_version: str) -> "Image":
        if self.filename is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'filename' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.granularity is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'granularity' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.height is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'height' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.scale is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'scale' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.threshold is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'threshold' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.uri is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'uri' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["filename"] = self.filename
        kwargs["granularity"] = self.granularity
        kwargs["height"] = self.height
        kwargs["scale"] = self.scale
        kwargs["threshold"] = self.threshold
        kwargs["uri"] = self.uri.to_version(target_version) if self.uri is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("image")
        if self.filename is not None:
            el.set("filename", self.filename)
        if self.granularity is not None:
            el.set("granularity", str(self.granularity))
        if self.height is not None:
            el.set("height", str(self.height))
        if self.scale is not None:
            el.set("scale", str(self.scale))
        if self.threshold is not None:
            el.set("threshold", str(self.threshold))
        if self.uri is not None:
            el.append(self.uri.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _filename = el.get("filename", "__default__")
        if isinstance(_filename, SDFError):
            return _filename.extend("@filename")
        _granularity = _parse_int32(el.get("granularity", 1))
        if isinstance(_granularity, SDFError):
            return _granularity.extend("@granularity")
        _height = _parse_double(el.get("height", 1))
        if isinstance(_height, SDFError):
            return _height.extend("@height")
        _scale = _parse_double(el.get("scale", 1))
        if isinstance(_scale, SDFError):
            return _scale.extend("@scale")
        _threshold = _parse_int32(el.get("threshold", 200))
        if isinstance(_threshold, SDFError):
            return _threshold.extend("@threshold")
        _c_uri = el.find("uri")
        if _c_uri is not None:
            _res = Uri._from_sdf(_c_uri, version)
            if isinstance(_res, SDFError):
                return _res.extend("uri")
            _uri = _res
        else:
            _uri = None
        if _uri is not None and cmp_version(version, "1.2") < 0:
            return SDFError(f"'uri' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, filename=_filename, granularity=_granularity, height=_height, scale=_scale, threshold=_threshold, uri=_uri)


class TextureSize(BaseModel):
    def __init__(self, sdf_version: str, size: float = 10):
        self.__version__ = sdf_version
        self.size = size

    def to_version(self, target_version: str) -> "TextureSize":
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
            el.text = str(self.size)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 10
        _size = _parse_double(_text)
        if isinstance(_size, SDFError):
            return _size
        return cls(sdf_version=version, size=_size)


class Diffuse(BaseModel):
    def __init__(self, sdf_version: str, diffuse: str = "__default__"):
        self.__version__ = sdf_version
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
            el.text = self.diffuse
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "__default__"
        _diffuse = _text
        if isinstance(_diffuse, SDFError):
            return _diffuse
        return cls(sdf_version=version, diffuse=_diffuse)


class TextureNormal(BaseModel):
    def __init__(self, sdf_version: str, normal: str = "__default__"):
        self.__version__ = sdf_version
        self.normal = normal

    def to_version(self, target_version: str) -> "TextureNormal":
        kwargs = {"sdf_version": target_version}
        kwargs["normal"] = self.normal
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("normal")
        if self.normal is not None:
            el.text = self.normal
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "__default__"
        _normal = _text
        if isinstance(_normal, SDFError):
            return _normal
        return cls(sdf_version=version, normal=_normal)


class Texture(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        diffuse: "Diffuse" = None,
        normal: "TextureNormal" = None,
        size: "TextureSize" = None
    ):
        self.__version__ = sdf_version
        self.diffuse = diffuse
        self.normal = normal
        self.size = size

    def to_version(self, target_version: str) -> "Texture":
        kwargs = {"sdf_version": target_version}
        kwargs["diffuse"] = self.diffuse.to_version(target_version) if self.diffuse is not None else None
        kwargs["normal"] = self.normal.to_version(target_version) if self.normal is not None else None
        kwargs["size"] = self.size.to_version(target_version) if self.size is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("texture")
        if self.diffuse is not None:
            el.append(self.diffuse.to_sdf(version))
        if self.normal is not None:
            el.append(self.normal.to_sdf(version))
        if self.size is not None:
            el.append(self.size.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_diffuse = el.find("diffuse")
        if _c_diffuse is not None:
            _res = Diffuse._from_sdf(_c_diffuse, version)
            if isinstance(_res, SDFError):
                return _res.extend("diffuse")
            _diffuse = _res
        else:
            _diffuse = None
        _c_normal = el.find("normal")
        if _c_normal is not None:
            _res = TextureNormal._from_sdf(_c_normal, version)
            if isinstance(_res, SDFError):
                return _res.extend("normal")
            _normal = _res
        else:
            _normal = None
        _c_size = el.find("size")
        if _c_size is not None:
            _res = TextureSize._from_sdf(_c_size, version)
            if isinstance(_res, SDFError):
                return _res.extend("size")
            _size = _res
        else:
            _size = None
        return cls(sdf_version=version, diffuse=_diffuse, normal=_normal, size=_size)


class MinHeight(BaseModel):
    def __init__(self, sdf_version: str, min_height: float = 0):
        self.__version__ = sdf_version
        self.min_height = min_height

    def to_version(self, target_version: str) -> "MinHeight":
        kwargs = {"sdf_version": target_version}
        kwargs["min_height"] = self.min_height
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("min_height")
        if self.min_height is not None:
            el.text = str(self.min_height)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _min_height = _parse_double(_text)
        if isinstance(_min_height, SDFError):
            return _min_height
        return cls(sdf_version=version, min_height=_min_height)


class FadeDist(BaseModel):
    def __init__(self, sdf_version: str, fade_dist: float = 0):
        self.__version__ = sdf_version
        self.fade_dist = fade_dist

    def to_version(self, target_version: str) -> "FadeDist":
        kwargs = {"sdf_version": target_version}
        kwargs["fade_dist"] = self.fade_dist
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("fade_dist")
        if self.fade_dist is not None:
            el.text = str(self.fade_dist)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _fade_dist = _parse_double(_text)
        if isinstance(_fade_dist, SDFError):
            return _fade_dist
        return cls(sdf_version=version, fade_dist=_fade_dist)


class Blend(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        fade_dist: "FadeDist" = None,
        min_height: "MinHeight" = None
    ):
        self.__version__ = sdf_version
        self.fade_dist = fade_dist
        self.min_height = min_height

    def to_version(self, target_version: str) -> "Blend":
        kwargs = {"sdf_version": target_version}
        kwargs["fade_dist"] = self.fade_dist.to_version(target_version) if self.fade_dist is not None else None
        kwargs["min_height"] = self.min_height.to_version(target_version) if self.min_height is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("blend")
        if self.fade_dist is not None:
            el.append(self.fade_dist.to_sdf(version))
        if self.min_height is not None:
            el.append(self.min_height.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_fade_dist = el.find("fade_dist")
        if _c_fade_dist is not None:
            _res = FadeDist._from_sdf(_c_fade_dist, version)
            if isinstance(_res, SDFError):
                return _res.extend("fade_dist")
            _fade_dist = _res
        else:
            _fade_dist = None
        _c_min_height = el.find("min_height")
        if _c_min_height is not None:
            _res = MinHeight._from_sdf(_c_min_height, version)
            if isinstance(_res, SDFError):
                return _res.extend("min_height")
            _min_height = _res
        else:
            _min_height = None
        return cls(sdf_version=version, fade_dist=_fade_dist, min_height=_min_height)


class Pos(BaseModel):
    def __init__(self, sdf_version: str, pos: _SDFVector3 = None):
        self.__version__ = sdf_version
        if pos is None:
            pos = _SDFVector3.from_sdf("0 0 0")
        self.pos = pos

    def to_version(self, target_version: str) -> "Pos":
        if self.pos is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pos' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["pos"] = self.pos
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("pos")
        if self.pos is not None:
            el.text = self.pos.to_sdf()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 0"
        _pos = _SDFVector3._from_sdf(_text, version)
        if isinstance(_pos, SDFError):
            return _pos
        if _pos is not None and cmp_version(version, "1.2") < 0:
            if _pos != "0 0 0":
                return SDFError(f"'pos' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, pos=_pos)


class UseTerrainPaging(BaseModel):
    def __init__(self, sdf_version: str, use_terrain_paging: bool = False):
        self.__version__ = sdf_version
        self.use_terrain_paging = use_terrain_paging

    def to_version(self, target_version: str) -> "UseTerrainPaging":
        if self.use_terrain_paging is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'use_terrain_paging' is not supported in SDF version {target_version} (added in 1.4)")
        kwargs = {"sdf_version": target_version}
        kwargs["use_terrain_paging"] = self.use_terrain_paging
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("use_terrain_paging")
        if self.use_terrain_paging is not None:
            el.text = str(self.use_terrain_paging).lower()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or False
        _use_terrain_paging = str(_text).strip().lower() == 'true'
        if isinstance(_use_terrain_paging, SDFError):
            return _use_terrain_paging
        if _use_terrain_paging is not None and cmp_version(version, "1.4") < 0:
            if _use_terrain_paging != False:
                return SDFError(f"'use_terrain_paging' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, use_terrain_paging=_use_terrain_paging)


class Sampling(BaseModel):
    def __init__(self, sdf_version: str, sampling: int = 2):
        self.__version__ = sdf_version
        self.sampling = sampling

    def to_version(self, target_version: str) -> "Sampling":
        if self.sampling is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'sampling' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["sampling"] = self.sampling
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("sampling")
        if self.sampling is not None:
            el.text = str(self.sampling)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 2
        _sampling = _parse_uint32(_text)
        if isinstance(_sampling, SDFError):
            return _sampling
        if _sampling is not None and cmp_version(version, "1.6") < 0:
            if _sampling != 2:
                return SDFError(f"'sampling' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, sampling=_sampling)


class Heightmap(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        blend: List["Blend"] = None,
        filename: str = "__default__",
        origin: _SDFVector3 = None,
        pos: "Pos" = None,
        sampling: "Sampling" = None,
        size: _SDFVector3 = None,
        texture: List["Texture"] = None,
        uri: "Uri" = None,
        use_terrain_paging: "UseTerrainPaging" = None
    ):
        self.__version__ = sdf_version
        if origin is None:
            origin = _SDFVector3.from_sdf("0 0 0")
        if size is None:
            size = _SDFVector3.from_sdf("1 1 1")
        self.blend = blend or []
        self.filename = filename
        self.origin = origin
        self.pos = pos
        self.sampling = sampling
        self.size = size
        self.texture = texture or []
        self.uri = uri
        self.use_terrain_paging = use_terrain_paging

    def to_version(self, target_version: str) -> "Heightmap":
        if self.filename is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'filename' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.origin is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'origin' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.pos is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pos' is not supported in SDF version {target_version} (added in 1.2)")
        if self.sampling is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'sampling' is not supported in SDF version {target_version} (added in 1.6)")
        if self.size is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'size' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.uri is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'uri' is not supported in SDF version {target_version} (added in 1.2)")
        if self.use_terrain_paging is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'use_terrain_paging' is not supported in SDF version {target_version} (added in 1.4)")
        kwargs = {"sdf_version": target_version}
        kwargs["blend"] = [c.to_version(target_version) for c in (self.blend or [])]
        kwargs["filename"] = self.filename
        kwargs["origin"] = self.origin
        kwargs["pos"] = self.pos.to_version(target_version) if self.pos is not None else None
        kwargs["sampling"] = self.sampling.to_version(target_version) if self.sampling is not None else None
        kwargs["size"] = self.size
        kwargs["texture"] = [c.to_version(target_version) for c in (self.texture or [])]
        kwargs["uri"] = self.uri.to_version(target_version) if self.uri is not None else None
        kwargs["use_terrain_paging"] = self.use_terrain_paging.to_version(target_version) if self.use_terrain_paging is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("heightmap")
        for item in (self.blend or []):
            el.append(item.to_sdf(version))
        if self.filename is not None:
            el.set("filename", self.filename)
        if self.origin is not None:
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = ET.Element("pos")
                _c_tmp.text = self.origin.to_sdf()
                el.append(_c_tmp)
            else:
                el.set("origin", self.origin.to_sdf())
        if self.pos is not None:
            el.append(self.pos.to_sdf(version))
        if self.sampling is not None:
            el.append(self.sampling.to_sdf(version))
        if self.size is not None:
            el.set("size", self.size.to_sdf())
        for item in (self.texture or []):
            el.append(item.to_sdf(version))
        if self.uri is not None:
            el.append(self.uri.to_sdf(version))
        if self.use_terrain_paging is not None:
            el.append(self.use_terrain_paging.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _blend = []
        for c in el.findall("blend"):
            _res = Blend._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("blend")
            _blend.append(_res)
        _filename = el.get("filename", "__default__")
        if isinstance(_filename, SDFError):
            return _filename.extend("@filename")
        _raw_origin = None
        if cmp_version(version, "1.2") >= 0:
            _c_tmp = el.find("pos")
            if _c_tmp is not None: _raw_origin = _c_tmp.text
        else:
            _raw_origin = el.get("origin")
        if _raw_origin is None: _raw_origin = "0 0 0"
        _origin = _SDFVector3._from_sdf(_raw_origin, version)
        if isinstance(_origin, SDFError):
            return _origin.extend("@origin")
        _c_pos = el.find("pos")
        if _c_pos is not None:
            _res = Pos._from_sdf(_c_pos, version)
            if isinstance(_res, SDFError):
                return _res.extend("pos")
            _pos = _res
        else:
            _pos = None
        if _pos is not None and cmp_version(version, "1.2") < 0:
            return SDFError(f"'pos' is not supported in SDF version {version} (added in 1.2)")
        _c_sampling = el.find("sampling")
        if _c_sampling is not None:
            _res = Sampling._from_sdf(_c_sampling, version)
            if isinstance(_res, SDFError):
                return _res.extend("sampling")
            _sampling = _res
        else:
            _sampling = None
        if _sampling is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'sampling' is not supported in SDF version {version} (added in 1.6)")
        _size = _SDFVector3._from_sdf(el.get("size", "1 1 1"), version)
        if isinstance(_size, SDFError):
            return _size.extend("@size")
        _texture = []
        for c in el.findall("texture"):
            _res = Texture._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("texture")
            _texture.append(_res)
        _c_uri = el.find("uri")
        if _c_uri is not None:
            _res = Uri._from_sdf(_c_uri, version)
            if isinstance(_res, SDFError):
                return _res.extend("uri")
            _uri = _res
        else:
            _uri = None
        if _uri is not None and cmp_version(version, "1.2") < 0:
            return SDFError(f"'uri' is not supported in SDF version {version} (added in 1.2)")
        _c_use_terrain_paging = el.find("use_terrain_paging")
        if _c_use_terrain_paging is not None:
            _res = UseTerrainPaging._from_sdf(_c_use_terrain_paging, version)
            if isinstance(_res, SDFError):
                return _res.extend("use_terrain_paging")
            _use_terrain_paging = _res
        else:
            _use_terrain_paging = None
        if _use_terrain_paging is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'use_terrain_paging' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, blend=_blend, filename=_filename, origin=_origin, pos=_pos, sampling=_sampling, size=_size, texture=_texture, uri=_uri, use_terrain_paging=_use_terrain_paging)


class Empty(BaseModel):
    def __init__(self, sdf_version: str):
        self.__version__ = sdf_version

    def to_version(self, target_version: str) -> "Empty":
        kwargs = {"sdf_version": target_version}
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("empty")
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        return cls(sdf_version=version)


class Point(BaseModel):
    def __init__(self, sdf_version: str, point: _SDFVector2d = None):
        self.__version__ = sdf_version
        if point is None:
            point = _SDFVector2d.from_sdf("0 0")
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
        _text = el.text or "0 0"
        _point = _SDFVector2d._from_sdf(_text, version)
        if isinstance(_point, SDFError):
            return _point
        return cls(sdf_version=version, point=_point)


class PolylineHeight(BaseModel):
    def __init__(self, sdf_version: str, height: float = 1.0):
        self.__version__ = sdf_version
        self.height = height

    def to_version(self, target_version: str) -> "PolylineHeight":
        kwargs = {"sdf_version": target_version}
        kwargs["height"] = self.height
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("height")
        if self.height is not None:
            el.text = str(self.height)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1.0
        _height = _parse_double(_text)
        if isinstance(_height, SDFError):
            return _height
        return cls(sdf_version=version, height=_height)


class Polyline(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        height: "PolylineHeight" = None,
        point: List["Point"] = None
    ):
        self.__version__ = sdf_version
        self.height = height
        self.point = point or []

    def to_version(self, target_version: str) -> "Polyline":
        kwargs = {"sdf_version": target_version}
        kwargs["height"] = self.height.to_version(target_version) if self.height is not None else None
        kwargs["point"] = [c.to_version(target_version) for c in (self.point or [])]
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("polyline")
        if self.height is not None:
            el.append(self.height.to_sdf(version))
        for item in (self.point or []):
            el.append(item.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_height = el.find("height")
        if _c_height is not None:
            _res = PolylineHeight._from_sdf(_c_height, version)
            if isinstance(_res, SDFError):
                return _res.extend("height")
            _height = _res
        else:
            _height = None
        _point = []
        for c in el.findall("point"):
            _res = Point._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("point")
            _point.append(_res)
        return cls(sdf_version=version, height=_height, point=_point)


class CapsuleRadius(BaseModel):
    def __init__(self, sdf_version: str, radius: float = 0.5):
        self.__version__ = sdf_version
        self.radius = radius

    def to_version(self, target_version: str) -> "CapsuleRadius":
        kwargs = {"sdf_version": target_version}
        kwargs["radius"] = self.radius
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("radius")
        if self.radius is not None:
            el.text = str(self.radius)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.5
        _radius = _parse_double(_text)
        if isinstance(_radius, SDFError):
            return _radius
        return cls(sdf_version=version, radius=_radius)


class Capsule(BaseModel):
    def __init__(self, sdf_version: str, length: "Length" = None, radius: "CapsuleRadius" = None):
        self.__version__ = sdf_version
        self.length = length
        self.radius = radius

    def to_version(self, target_version: str) -> "Capsule":
        kwargs = {"sdf_version": target_version}
        kwargs["length"] = self.length.to_version(target_version) if self.length is not None else None
        kwargs["radius"] = self.radius.to_version(target_version) if self.radius is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("capsule")
        if self.length is not None:
            el.append(self.length.to_sdf(version))
        if self.radius is not None:
            el.append(self.radius.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_length = el.find("length")
        if _c_length is not None:
            _res = Length._from_sdf(_c_length, version)
            if isinstance(_res, SDFError):
                return _res.extend("length")
            _length = _res
        else:
            _length = None
        _c_radius = el.find("radius")
        if _c_radius is not None:
            _res = CapsuleRadius._from_sdf(_c_radius, version)
            if isinstance(_res, SDFError):
                return _res.extend("radius")
            _radius = _res
        else:
            _radius = None
        return cls(sdf_version=version, length=_length, radius=_radius)


class Radii(BaseModel):
    def __init__(self, sdf_version: str, radii: _SDFVector3 = None):
        self.__version__ = sdf_version
        if radii is None:
            radii = _SDFVector3.from_sdf("1 1 1")
        self.radii = radii

    def to_version(self, target_version: str) -> "Radii":
        kwargs = {"sdf_version": target_version}
        kwargs["radii"] = self.radii
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("radii")
        if self.radii is not None:
            el.text = self.radii.to_sdf()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "1 1 1"
        _radii = _SDFVector3._from_sdf(_text, version)
        if isinstance(_radii, SDFError):
            return _radii
        return cls(sdf_version=version, radii=_radii)


class Ellipsoid(BaseModel):
    def __init__(self, sdf_version: str, radii: "Radii" = None):
        self.__version__ = sdf_version
        self.radii = radii

    def to_version(self, target_version: str) -> "Ellipsoid":
        kwargs = {"sdf_version": target_version}
        kwargs["radii"] = self.radii.to_version(target_version) if self.radii is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("ellipsoid")
        if self.radii is not None:
            el.append(self.radii.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_radii = el.find("radii")
        if _c_radii is not None:
            _res = Radii._from_sdf(_c_radii, version)
            if isinstance(_res, SDFError):
                return _res.extend("radii")
            _radii = _res
        else:
            _radii = None
        return cls(sdf_version=version, radii=_radii)


class Cone(BaseModel):
    def __init__(self, sdf_version: str, length: "Length" = None, radius: "Radius" = None):
        self.__version__ = sdf_version
        self.length = length
        self.radius = radius

    def to_version(self, target_version: str) -> "Cone":
        kwargs = {"sdf_version": target_version}
        kwargs["length"] = self.length.to_version(target_version) if self.length is not None else None
        kwargs["radius"] = self.radius.to_version(target_version) if self.radius is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("cone")
        if self.length is not None:
            el.append(self.length.to_sdf(version))
        if self.radius is not None:
            el.append(self.radius.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_length = el.find("length")
        if _c_length is not None:
            _res = Length._from_sdf(_c_length, version)
            if isinstance(_res, SDFError):
                return _res.extend("length")
            _length = _res
        else:
            _length = None
        _c_radius = el.find("radius")
        if _c_radius is not None:
            _res = Radius._from_sdf(_c_radius, version)
            if isinstance(_res, SDFError):
                return _res.extend("radius")
            _radius = _res
        else:
            _radius = None
        return cls(sdf_version=version, length=_length, radius=_radius)


class Geometry(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        box: "Box" = None,
        capsule: "Capsule" = None,
        cone: "Cone" = None,
        cylinder: "Cylinder" = None,
        ellipsoid: "Ellipsoid" = None,
        empty: "Empty" = None,
        heightmap: "Heightmap" = None,
        image: "Image" = None,
        mesh: "Mesh" = None,
        plane: "Plane" = None,
        polyline: "Polyline" = None,
        sphere: "Sphere" = None
    ):
        self.__version__ = sdf_version
        self.box = box
        self.capsule = capsule
        self.cone = cone
        self.cylinder = cylinder
        self.ellipsoid = ellipsoid
        self.empty = empty
        self.heightmap = heightmap
        self.image = image
        self.mesh = mesh
        self.plane = plane
        self.polyline = polyline
        self.sphere = sphere

    def to_version(self, target_version: str) -> "Geometry":
        if self.capsule is not None and cmp_version(target_version, "1.8") < 0:
            raise ValueError(f"'capsule' is not supported in SDF version {target_version} (added in 1.8)")
        if self.cone is not None and cmp_version(target_version, "1.11") < 0:
            raise ValueError(f"'cone' is not supported in SDF version {target_version} (added in 1.11)")
        if self.ellipsoid is not None and cmp_version(target_version, "1.8") < 0:
            raise ValueError(f"'ellipsoid' is not supported in SDF version {target_version} (added in 1.8)")
        if self.empty is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'empty' is not supported in SDF version {target_version} (added in 1.3)")
        if self.polyline is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'polyline' is not supported in SDF version {target_version} (added in 1.5)")
        kwargs = {"sdf_version": target_version}
        kwargs["box"] = self.box.to_version(target_version) if self.box is not None else None
        kwargs["capsule"] = self.capsule.to_version(target_version) if self.capsule is not None else None
        kwargs["cone"] = self.cone.to_version(target_version) if self.cone is not None else None
        kwargs["cylinder"] = self.cylinder.to_version(target_version) if self.cylinder is not None else None
        kwargs["ellipsoid"] = self.ellipsoid.to_version(target_version) if self.ellipsoid is not None else None
        kwargs["empty"] = self.empty.to_version(target_version) if self.empty is not None else None
        kwargs["heightmap"] = self.heightmap.to_version(target_version) if self.heightmap is not None else None
        kwargs["image"] = self.image.to_version(target_version) if self.image is not None else None
        kwargs["mesh"] = self.mesh.to_version(target_version) if self.mesh is not None else None
        kwargs["plane"] = self.plane.to_version(target_version) if self.plane is not None else None
        kwargs["polyline"] = self.polyline.to_version(target_version) if self.polyline is not None else None
        kwargs["sphere"] = self.sphere.to_version(target_version) if self.sphere is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("geometry")
        if self.box is not None:
            el.append(self.box.to_sdf(version))
        if self.capsule is not None:
            el.append(self.capsule.to_sdf(version))
        if self.cone is not None:
            el.append(self.cone.to_sdf(version))
        if self.cylinder is not None:
            el.append(self.cylinder.to_sdf(version))
        if self.ellipsoid is not None:
            el.append(self.ellipsoid.to_sdf(version))
        if self.empty is not None:
            el.append(self.empty.to_sdf(version))
        if self.heightmap is not None:
            el.append(self.heightmap.to_sdf(version))
        if self.image is not None:
            el.append(self.image.to_sdf(version))
        if self.mesh is not None:
            el.append(self.mesh.to_sdf(version))
        if self.plane is not None:
            el.append(self.plane.to_sdf(version))
        if self.polyline is not None:
            el.append(self.polyline.to_sdf(version))
        if self.sphere is not None:
            el.append(self.sphere.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_box = el.find("box")
        if _c_box is not None:
            _res = Box._from_sdf(_c_box, version)
            if isinstance(_res, SDFError):
                return _res.extend("box")
            _box = _res
        else:
            _box = None
        _c_capsule = el.find("capsule")
        if _c_capsule is not None:
            _res = Capsule._from_sdf(_c_capsule, version)
            if isinstance(_res, SDFError):
                return _res.extend("capsule")
            _capsule = _res
        else:
            _capsule = None
        if _capsule is not None and cmp_version(version, "1.8") < 0:
            return SDFError(f"'capsule' is not supported in SDF version {version} (added in 1.8)")
        _c_cone = el.find("cone")
        if _c_cone is not None:
            _res = Cone._from_sdf(_c_cone, version)
            if isinstance(_res, SDFError):
                return _res.extend("cone")
            _cone = _res
        else:
            _cone = None
        if _cone is not None and cmp_version(version, "1.11") < 0:
            return SDFError(f"'cone' is not supported in SDF version {version} (added in 1.11)")
        _c_cylinder = el.find("cylinder")
        if _c_cylinder is not None:
            _res = Cylinder._from_sdf(_c_cylinder, version)
            if isinstance(_res, SDFError):
                return _res.extend("cylinder")
            _cylinder = _res
        else:
            _cylinder = None
        _c_ellipsoid = el.find("ellipsoid")
        if _c_ellipsoid is not None:
            _res = Ellipsoid._from_sdf(_c_ellipsoid, version)
            if isinstance(_res, SDFError):
                return _res.extend("ellipsoid")
            _ellipsoid = _res
        else:
            _ellipsoid = None
        if _ellipsoid is not None and cmp_version(version, "1.8") < 0:
            return SDFError(f"'ellipsoid' is not supported in SDF version {version} (added in 1.8)")
        _c_empty = el.find("empty")
        if _c_empty is not None:
            _res = Empty._from_sdf(_c_empty, version)
            if isinstance(_res, SDFError):
                return _res.extend("empty")
            _empty = _res
        else:
            _empty = None
        if _empty is not None and cmp_version(version, "1.3") < 0:
            return SDFError(f"'empty' is not supported in SDF version {version} (added in 1.3)")
        _c_heightmap = el.find("heightmap")
        if _c_heightmap is not None:
            _res = Heightmap._from_sdf(_c_heightmap, version)
            if isinstance(_res, SDFError):
                return _res.extend("heightmap")
            _heightmap = _res
        else:
            _heightmap = None
        _c_image = el.find("image")
        if _c_image is not None:
            _res = Image._from_sdf(_c_image, version)
            if isinstance(_res, SDFError):
                return _res.extend("image")
            _image = _res
        else:
            _image = None
        _c_mesh = el.find("mesh")
        if _c_mesh is not None:
            _res = Mesh._from_sdf(_c_mesh, version)
            if isinstance(_res, SDFError):
                return _res.extend("mesh")
            _mesh = _res
        else:
            _mesh = None
        _c_plane = el.find("plane")
        if _c_plane is not None:
            _res = Plane._from_sdf(_c_plane, version)
            if isinstance(_res, SDFError):
                return _res.extend("plane")
            _plane = _res
        else:
            _plane = None
        _c_polyline = el.find("polyline")
        if _c_polyline is not None:
            _res = Polyline._from_sdf(_c_polyline, version)
            if isinstance(_res, SDFError):
                return _res.extend("polyline")
            _polyline = _res
        else:
            _polyline = None
        if _polyline is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'polyline' is not supported in SDF version {version} (added in 1.5)")
        _c_sphere = el.find("sphere")
        if _c_sphere is not None:
            _res = Sphere._from_sdf(_c_sphere, version)
            if isinstance(_res, SDFError):
                return _res.extend("sphere")
            _sphere = _res
        else:
            _sphere = None
        return cls(sdf_version=version, box=_box, capsule=_capsule, cone=_cone, cylinder=_cylinder, ellipsoid=_ellipsoid, empty=_empty, heightmap=_heightmap, image=_image, mesh=_mesh, plane=_plane, polyline=_polyline, sphere=_sphere)


class Origin(BaseModel):
    def __init__(self, sdf_version: str, pose: _SDFPose = None):
        self.__version__ = sdf_version
        if pose is None:
            pose = _SDFPose.from_sdf("0 0 0 0 0 0")
        self.pose = pose

    def to_version(self, target_version: str) -> "Origin":
        kwargs = {"sdf_version": target_version}
        kwargs["pose"] = self.pose
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("origin")
        if self.pose is not None:
            el.set("pose", self.pose.to_sdf())
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _pose = _SDFPose._from_sdf(el.get("pose", "0 0 0 0 0 0"), version)
        if isinstance(_pose, SDFError):
            return _pose.extend("@pose")
        return cls(sdf_version=version, pose=_pose)


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


class Ambient(BaseModel):
    def __init__(self, sdf_version: str, ambient: _SDFColor = None, rgba: _SDFColor = None):
        self.__version__ = sdf_version
        if ambient is None:
            ambient = _SDFColor.from_sdf("0 0 0 1")
        if rgba is None:
            rgba = _SDFColor.from_sdf("0 0 0 1")
        self.ambient = ambient
        self.rgba = rgba

    def to_version(self, target_version: str) -> "Ambient":
        if self.rgba is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'rgba' is not supported in SDF version {target_version} (removed in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["ambient"] = self.ambient
        kwargs["rgba"] = self.rgba
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("ambient")
        if self.ambient is not None:
            el.text = self.ambient.to_sdf()
        if self.rgba is not None:
            el.set("rgba", self.rgba.to_sdf())
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 0 1"
        _ambient = _SDFColor._from_sdf(_text, version)
        if isinstance(_ambient, SDFError):
            return _ambient
        _rgba = _SDFColor._from_sdf(el.get("rgba", "0 0 0 1"), version)
        if isinstance(_rgba, SDFError):
            return _rgba.extend("@rgba")
        return cls(sdf_version=version, ambient=_ambient, rgba=_rgba)


class MaterialDiffuse(BaseModel):
    def __init__(self, sdf_version: str, diffuse: _SDFColor = None, rgba: _SDFColor = None):
        self.__version__ = sdf_version
        if diffuse is None:
            diffuse = _SDFColor.from_sdf("0 0 0 1")
        if rgba is None:
            rgba = _SDFColor.from_sdf("0 0 0 1")
        self.diffuse = diffuse
        self.rgba = rgba

    def to_version(self, target_version: str) -> "MaterialDiffuse":
        if self.rgba is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'rgba' is not supported in SDF version {target_version} (removed in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["diffuse"] = self.diffuse
        kwargs["rgba"] = self.rgba
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("diffuse")
        if self.diffuse is not None:
            el.text = self.diffuse.to_sdf()
        if self.rgba is not None:
            el.set("rgba", self.rgba.to_sdf())
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 0 1"
        _diffuse = _SDFColor._from_sdf(_text, version)
        if isinstance(_diffuse, SDFError):
            return _diffuse
        _rgba = _SDFColor._from_sdf(el.get("rgba", "0 0 0 1"), version)
        if isinstance(_rgba, SDFError):
            return _rgba.extend("@rgba")
        return cls(sdf_version=version, diffuse=_diffuse, rgba=_rgba)


class Specular(BaseModel):
    def __init__(self, sdf_version: str, rgba: _SDFColor = None, specular: _SDFColor = None):
        self.__version__ = sdf_version
        if rgba is None:
            rgba = _SDFColor.from_sdf("0 0 0 1")
        if specular is None:
            specular = _SDFColor.from_sdf("0 0 0 1")
        self.rgba = rgba
        self.specular = specular

    def to_version(self, target_version: str) -> "Specular":
        if self.rgba is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'rgba' is not supported in SDF version {target_version} (removed in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["rgba"] = self.rgba
        kwargs["specular"] = self.specular
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("specular")
        if self.rgba is not None:
            el.set("rgba", self.rgba.to_sdf())
        if self.specular is not None:
            el.text = self.specular.to_sdf()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _rgba = _SDFColor._from_sdf(el.get("rgba", "0 0 0 1"), version)
        if isinstance(_rgba, SDFError):
            return _rgba.extend("@rgba")
        _text = el.text or "0 0 0 1"
        _specular = _SDFColor._from_sdf(_text, version)
        if isinstance(_specular, SDFError):
            return _specular
        return cls(sdf_version=version, rgba=_rgba, specular=_specular)


class Emissive(BaseModel):
    def __init__(self, sdf_version: str, emissive: _SDFColor = None, rgba: _SDFColor = None):
        self.__version__ = sdf_version
        if emissive is None:
            emissive = _SDFColor.from_sdf("0 0 0 1")
        if rgba is None:
            rgba = _SDFColor.from_sdf("0 0 0 1")
        self.emissive = emissive
        self.rgba = rgba

    def to_version(self, target_version: str) -> "Emissive":
        if self.rgba is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'rgba' is not supported in SDF version {target_version} (removed in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["emissive"] = self.emissive
        kwargs["rgba"] = self.rgba
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("emissive")
        if self.emissive is not None:
            el.text = self.emissive.to_sdf()
        if self.rgba is not None:
            el.set("rgba", self.rgba.to_sdf())
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 0 1"
        _emissive = _SDFColor._from_sdf(_text, version)
        if isinstance(_emissive, SDFError):
            return _emissive
        _rgba = _SDFColor._from_sdf(el.get("rgba", "0 0 0 1"), version)
        if isinstance(_rgba, SDFError):
            return _rgba.extend("@rgba")
        return cls(sdf_version=version, emissive=_emissive, rgba=_rgba)


class Script(BaseModel):
    def __init__(self, sdf_version: str, name: "Name" = None, uri: "Uri" = None):
        self.__version__ = sdf_version
        self.name = name
        self.uri = uri

    def to_version(self, target_version: str) -> "Script":
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name.to_version(target_version) if self.name is not None else None
        kwargs["uri"] = self.uri.to_version(target_version) if self.uri is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("script")
        if self.name is not None:
            el.append(self.name.to_sdf(version))
        if self.uri is not None:
            el.append(self.uri.to_sdf(version))
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
        _c_uri = el.find("uri")
        if _c_uri is not None:
            _res = Uri._from_sdf(_c_uri, version)
            if isinstance(_res, SDFError):
                return _res.extend("uri")
            _uri = _res
        else:
            _uri = None
        return cls(sdf_version=version, name=_name, uri=_uri)


class Lighting(BaseModel):
    def __init__(self, sdf_version: str, lighting: bool = True):
        self.__version__ = sdf_version
        self.lighting = lighting

    def to_version(self, target_version: str) -> "Lighting":
        if self.lighting is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'lighting' is not supported in SDF version {target_version} (added in 1.4)")
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
        if _lighting is not None and cmp_version(version, "1.4") < 0:
            if _lighting != True:
                return SDFError(f"'lighting' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, lighting=_lighting)


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
        diffuse: "MaterialDiffuse" = None,
        double_sided: "DoubleSided" = None,
        emissive: "Emissive" = None,
        lighting: "Lighting" = None,
        pbr: "Pbr" = None,
        render_order: "RenderOrder" = None,
        script: str = "__default__",
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
        if self.lighting is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'lighting' is not supported in SDF version {target_version} (added in 1.4)")
        if self.pbr is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'pbr' is not supported in SDF version {target_version} (added in 1.6)")
        if self.render_order is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'render_order' is not supported in SDF version {target_version} (added in 1.7)")
        if self.script is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'script' is not supported in SDF version {target_version} (removed in 1.2)")
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
        kwargs["script"] = self.script
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
            el.set("script", self.script)
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
            _res = MaterialDiffuse._from_sdf(_c_diffuse, version)
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
        if _lighting is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'lighting' is not supported in SDF version {version} (added in 1.4)")
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
        _script = el.get("script", "__default__")
        if isinstance(_script, SDFError):
            return _script.extend("@script")
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


class CastShadows(BaseModel):
    def __init__(self, sdf_version: str, cast_shadows: bool = True):
        self.__version__ = sdf_version
        self.cast_shadows = cast_shadows

    def to_version(self, target_version: str) -> "CastShadows":
        if self.cast_shadows is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'cast_shadows' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["cast_shadows"] = self.cast_shadows
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("cast_shadows")
        if self.cast_shadows is not None:
            el.text = str(self.cast_shadows).lower()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or True
        _cast_shadows = str(_text).strip().lower() == 'true'
        if isinstance(_cast_shadows, SDFError):
            return _cast_shadows
        if _cast_shadows is not None and cmp_version(version, "1.2") < 0:
            if _cast_shadows != True:
                return SDFError(f"'cast_shadows' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, cast_shadows=_cast_shadows)


class LaserRetro(BaseModel):
    def __init__(self, sdf_version: str, laser_retro: float = 0.0):
        self.__version__ = sdf_version
        self.laser_retro = laser_retro

    def to_version(self, target_version: str) -> "LaserRetro":
        if self.laser_retro is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'laser_retro' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["laser_retro"] = self.laser_retro
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("laser_retro")
        if self.laser_retro is not None:
            el.text = str(self.laser_retro)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _laser_retro = _parse_double(_text)
        if isinstance(_laser_retro, SDFError):
            return _laser_retro
        if _laser_retro is not None and cmp_version(version, "1.2") < 0:
            if _laser_retro != 0.0:
                return SDFError(f"'laser_retro' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, laser_retro=_laser_retro)


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
        if self.frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.pose is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.2)")
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
        if _frame is not None and cmp_version(version, "1.5") < 0:
            if _frame != "":
                return SDFError(f"'frame' is not supported in SDF version {version} (added in 1.5)")
        _text = el.text or "0 0 0 0 0 0"
        _pose = _SDFPose._from_sdf(_text, version)
        if isinstance(_pose, SDFError):
            return _pose
        if _pose is not None and cmp_version(version, "1.2") < 0:
            if _pose != "0 0 0 0 0 0":
                return SDFError(f"'pose' is not supported in SDF version {version} (added in 1.2)")
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


class Transparency(BaseModel):
    def __init__(self, sdf_version: str, transparency: float = 0.0):
        self.__version__ = sdf_version
        self.transparency = transparency

    def to_version(self, target_version: str) -> "Transparency":
        if self.transparency is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'transparency' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["transparency"] = self.transparency
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("transparency")
        if self.transparency is not None:
            el.text = str(self.transparency)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _transparency = _parse_double(_text)
        if isinstance(_transparency, SDFError):
            return _transparency
        if _transparency is not None and cmp_version(version, "1.2") < 0:
            if _transparency != 0.0:
                return SDFError(f"'transparency' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, transparency=_transparency)


class Plugin(BaseModel):
    def __init__(self, sdf_version: str, filename: str = "__default__", name: str = "__default__"):
        self.__version__ = sdf_version
        self.filename = filename
        self.name = name

    def to_version(self, target_version: str) -> "Plugin":
        kwargs = {"sdf_version": target_version}
        kwargs["filename"] = self.filename
        kwargs["name"] = self.name
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("plugin")
        if self.filename is not None:
            el.set("filename", self.filename)
        if self.name is not None:
            el.set("name", self.name)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _filename = el.get("filename", "__default__")
        if isinstance(_filename, SDFError):
            return _filename.extend("@filename")
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        return cls(sdf_version=version, filename=_filename, name=_name)


class Layer(BaseModel):
    def __init__(self, sdf_version: str, layer: int = 0):
        self.__version__ = sdf_version
        self.layer = layer

    def to_version(self, target_version: str) -> "Layer":
        kwargs = {"sdf_version": target_version}
        kwargs["layer"] = self.layer
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("layer")
        if self.layer is not None:
            el.text = str(self.layer)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _layer = _parse_int32(_text)
        if isinstance(_layer, SDFError):
            return _layer
        return cls(sdf_version=version, layer=_layer)


class Meta(BaseModel):
    def __init__(self, sdf_version: str, layer: "Layer" = None):
        self.__version__ = sdf_version
        self.layer = layer

    def to_version(self, target_version: str) -> "Meta":
        kwargs = {"sdf_version": target_version}
        kwargs["layer"] = self.layer.to_version(target_version) if self.layer is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("meta")
        if self.layer is not None:
            el.append(self.layer.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_layer = el.find("layer")
        if _c_layer is not None:
            _res = Layer._from_sdf(_c_layer, version)
            if isinstance(_res, SDFError):
                return _res.extend("layer")
            _layer = _res
        else:
            _layer = None
        return cls(sdf_version=version, layer=_layer)


class FramePose(BaseModel):
    _MIGRATIONS = [{"version": "1.7", "ops": [{"type": "move", "from": "frame", "to": "relative_to"}]}]

    def __init__(self, sdf_version: str, frame: str = "", pose: _SDFPose = None):
        self.__version__ = sdf_version
        if pose is None:
            pose = _SDFPose.from_sdf("0 0 0 0 0 0")
        self.frame = frame
        self.pose = pose

    def to_version(self, target_version: str) -> "FramePose":
        kwargs = {"sdf_version": target_version}
        kwargs["frame"] = self.frame
        kwargs["pose"] = self.pose
        new_obj = self.__class__(**kwargs)
        apply_migrations(new_obj, target_version)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("pose")
        if self.frame is not None:
            el.set("frame", self.frame)
        if self.pose is not None:
            el.text = self.pose.to_sdf()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _frame = el.get("frame", "")
        if isinstance(_frame, SDFError):
            return _frame.extend("@frame")
        _text = el.text or "0 0 0 0 0 0"
        _pose = _SDFPose._from_sdf(_text, version)
        if isinstance(_pose, SDFError):
            return _pose
        return cls(sdf_version=version, frame=_frame, pose=_pose)


class Frame(BaseModel):
    def __init__(self, sdf_version: str, name: str = "", pose: "FramePose" = None):
        self.__version__ = sdf_version
        self.name = name
        self.pose = pose

    def to_version(self, target_version: str) -> "Frame":
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("frame")
        if self.name is None:
            raise ValueError(f"'name' is required in SDF version {version}")
        if self.name is not None:
            el.set("name", self.name)
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        if el.get("name") is None:
            return SDFError(f"'name' is required in SDF version {version}")
        _name = el.get("name", "")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        _c_pose = el.find("pose")
        if _c_pose is not None:
            _res = FramePose._from_sdf(_c_pose, version)
            if isinstance(_res, SDFError):
                return _res.extend("pose")
            _pose = _res
        else:
            _pose = None
        return cls(sdf_version=version, name=_name, pose=_pose)


class VisibilityFlags(BaseModel):
    def __init__(self, sdf_version: str, visibility_flags: int = 4294967295):
        self.__version__ = sdf_version
        self.visibility_flags = visibility_flags

    def to_version(self, target_version: str) -> "VisibilityFlags":
        if self.visibility_flags is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'visibility_flags' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["visibility_flags"] = self.visibility_flags
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("visibility_flags")
        if self.visibility_flags is not None:
            el.text = str(self.visibility_flags)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 4294967295
        _visibility_flags = _parse_uint32(_text)
        if isinstance(_visibility_flags, SDFError):
            return _visibility_flags
        if _visibility_flags is not None and cmp_version(version, "1.7") < 0:
            if _visibility_flags != 4294967295:
                return SDFError(f"'visibility_flags' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, visibility_flags=_visibility_flags)


class Visual(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        cast_shadows: bool = True,
        frame: List["Frame"] = None,
        geometry: "Geometry" = None,
        laser_retro: float = 0.0,
        material: "Material" = None,
        meta: "Meta" = None,
        name: str = "__default__",
        origin: "Origin" = None,
        plugin: List["Plugin"] = None,
        pose: "Pose" = None,
        transparency: float = 0.0,
        visibility_flags: "VisibilityFlags" = None
    ):
        self.__version__ = sdf_version
        self.cast_shadows = cast_shadows
        self.frame = frame or []
        self.geometry = geometry
        self.laser_retro = laser_retro
        self.material = material
        self.meta = meta
        self.name = name
        self.origin = origin
        self.plugin = plugin or []
        self.pose = pose
        self.transparency = transparency
        self.visibility_flags = visibility_flags

    def to_version(self, target_version: str) -> "Visual":
        if self.cast_shadows is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'cast_shadows' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.laser_retro is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'laser_retro' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.meta is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'meta' is not supported in SDF version {target_version} (added in 1.5)")
        if self.origin is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'origin' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.plugin is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'plugin' is not supported in SDF version {target_version} (added in 1.3)")
        if self.pose is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.2)")
        if self.transparency is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'transparency' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.visibility_flags is not None and cmp_version(target_version, "1.7") < 0:
            raise ValueError(f"'visibility_flags' is not supported in SDF version {target_version} (added in 1.7)")
        kwargs = {"sdf_version": target_version}
        kwargs["cast_shadows"] = self.cast_shadows
        kwargs["frame"] = [c.to_version(target_version) for c in (self.frame or [])]
        kwargs["geometry"] = self.geometry.to_version(target_version) if self.geometry is not None else None
        kwargs["laser_retro"] = self.laser_retro
        kwargs["material"] = self.material.to_version(target_version) if self.material is not None else None
        kwargs["meta"] = self.meta.to_version(target_version) if self.meta is not None else None
        kwargs["name"] = self.name
        kwargs["origin"] = self.origin.to_version(target_version) if self.origin is not None else None
        kwargs["plugin"] = [c.to_version(target_version) for c in (self.plugin or [])]
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["transparency"] = self.transparency
        kwargs["visibility_flags"] = self.visibility_flags.to_version(target_version) if self.visibility_flags is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("visual")
        if self.cast_shadows is not None:
            el.set("cast_shadows", str(self.cast_shadows).lower())
        for item in (self.frame or []):
            el.append(item.to_sdf(version))
        if self.geometry is None:
            self.geometry = Geometry(sdf_version=version)
        if self.geometry is not None:
            el.append(self.geometry.to_sdf(version))
        if self.laser_retro is not None:
            el.set("laser_retro", str(self.laser_retro))
        if self.material is not None:
            el.append(self.material.to_sdf(version))
        if self.meta is not None:
            el.append(self.meta.to_sdf(version))
        if self.name is not None:
            el.set("name", self.name)
        if self.origin is not None:
            el.append(self.origin.to_sdf(version))
        for item in (self.plugin or []):
            el.append(item.to_sdf(version))
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        if self.transparency is not None:
            el.set("transparency", str(self.transparency))
        if self.visibility_flags is not None:
            el.append(self.visibility_flags.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _cast_shadows = str(el.get("cast_shadows", True)).strip().lower() == 'true'
        if isinstance(_cast_shadows, SDFError):
            return _cast_shadows.extend("@cast_shadows")
        _frame = []
        for c in el.findall("frame"):
            _res = Frame._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("frame")
            _frame.append(_res)
        if _frame and cmp_version(version, "1.5") < 0:
            return SDFError(f"'frame' is not supported in SDF version {version} (added in 1.5)")
        _c_geometry = el.find("geometry")
        if _c_geometry is not None:
            _res = Geometry._from_sdf(_c_geometry, version)
            if isinstance(_res, SDFError):
                return _res.extend("geometry")
            _geometry = _res
        else:
            _res = Geometry._from_sdf(ET.Element("geometry"), version)
            if isinstance(_res, SDFError):
                return _res.extend("geometry")
            _geometry = _res
        _laser_retro = _parse_double(el.get("laser_retro", 0.0))
        if isinstance(_laser_retro, SDFError):
            return _laser_retro.extend("@laser_retro")
        _c_material = el.find("material")
        if _c_material is not None:
            _res = Material._from_sdf(_c_material, version)
            if isinstance(_res, SDFError):
                return _res.extend("material")
            _material = _res
        else:
            _material = None
        _c_meta = el.find("meta")
        if _c_meta is not None:
            _res = Meta._from_sdf(_c_meta, version)
            if isinstance(_res, SDFError):
                return _res.extend("meta")
            _meta = _res
        else:
            _meta = None
        if _meta is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'meta' is not supported in SDF version {version} (added in 1.5)")
        _name = el.get("name", "__default__")
        if isinstance(_name, SDFError):
            return _name.extend("@name")
        _c_origin = el.find("origin")
        if _c_origin is not None:
            _res = Origin._from_sdf(_c_origin, version)
            if isinstance(_res, SDFError):
                return _res.extend("origin")
            _origin = _res
        else:
            _origin = None
        _plugin = []
        for c in el.findall("plugin"):
            _res = Plugin._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("plugin")
            _plugin.append(_res)
        if _plugin and cmp_version(version, "1.3") < 0:
            return SDFError(f"'plugin' is not supported in SDF version {version} (added in 1.3)")
        _c_pose = el.find("pose")
        if _c_pose is not None:
            _res = Pose._from_sdf(_c_pose, version)
            if isinstance(_res, SDFError):
                return _res.extend("pose")
            _pose = _res
        else:
            _pose = None
        if _pose is not None and cmp_version(version, "1.2") < 0:
            return SDFError(f"'pose' is not supported in SDF version {version} (added in 1.2)")
        _transparency = _parse_double(el.get("transparency", 0.0))
        if isinstance(_transparency, SDFError):
            return _transparency.extend("@transparency")
        _c_visibility_flags = el.find("visibility_flags")
        if _c_visibility_flags is not None:
            _res = VisibilityFlags._from_sdf(_c_visibility_flags, version)
            if isinstance(_res, SDFError):
                return _res.extend("visibility_flags")
            _visibility_flags = _res
        else:
            _visibility_flags = None
        if _visibility_flags is not None and cmp_version(version, "1.7") < 0:
            return SDFError(f"'visibility_flags' is not supported in SDF version {version} (added in 1.7)")
        return cls(sdf_version=version, cast_shadows=_cast_shadows, frame=_frame, geometry=_geometry, laser_retro=_laser_retro, material=_material, meta=_meta, name=_name, origin=_origin, plugin=_plugin, pose=_pose, transparency=_transparency, visibility_flags=_visibility_flags)
