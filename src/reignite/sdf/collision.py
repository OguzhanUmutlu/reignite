### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
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


class BounceThreshold(BaseModel):
    def __init__(self, sdf_version: str, threshold: float = 100000):
        self.__version__ = sdf_version
        self.threshold = threshold

    def to_version(self, target_version: str) -> "BounceThreshold":
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
        _text = el.text or 100000
        _threshold = _parse_double(_text)
        if isinstance(_threshold, SDFError):
            return _threshold
        if _threshold is not None and cmp_version(version, "1.2") < 0:
            if _threshold != 100000:
                return SDFError(f"'threshold' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, threshold=_threshold)


class RestitutionCoefficient(BaseModel):
    def __init__(self, sdf_version: str, restitution_coefficient: float = 0):
        self.__version__ = sdf_version
        self.restitution_coefficient = restitution_coefficient

    def to_version(self, target_version: str) -> "RestitutionCoefficient":
        if self.restitution_coefficient is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'restitution_coefficient' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["restitution_coefficient"] = self.restitution_coefficient
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("restitution_coefficient")
        if self.restitution_coefficient is not None:
            el.text = str(self.restitution_coefficient)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _restitution_coefficient = _parse_double(_text)
        if isinstance(_restitution_coefficient, SDFError):
            return _restitution_coefficient
        if _restitution_coefficient is not None and cmp_version(version, "1.2") < 0:
            if _restitution_coefficient != 0:
                return SDFError(f"'restitution_coefficient' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, restitution_coefficient=_restitution_coefficient)


class Bounce(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        restitution_coefficient: float = 0,
        threshold: float = 100000
    ):
        self.__version__ = sdf_version
        self.restitution_coefficient = restitution_coefficient
        self.threshold = threshold

    def to_version(self, target_version: str) -> "Bounce":
        if self.restitution_coefficient is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'restitution_coefficient' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.threshold is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'threshold' is not supported in SDF version {target_version} (removed in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["restitution_coefficient"] = self.restitution_coefficient
        kwargs["threshold"] = self.threshold
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("bounce")
        if self.restitution_coefficient is not None:
            el.set("restitution_coefficient", str(self.restitution_coefficient))
        if self.threshold is not None:
            el.set("threshold", str(self.threshold))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _restitution_coefficient = _parse_double(el.get("restitution_coefficient", 0))
        if isinstance(_restitution_coefficient, SDFError):
            return _restitution_coefficient.extend("@restitution_coefficient")
        _threshold = _parse_double(el.get("threshold", 100000))
        if isinstance(_threshold, SDFError):
            return _threshold.extend("@threshold")
        return cls(sdf_version=version, restitution_coefficient=_restitution_coefficient, threshold=_threshold)


class Fdir1(BaseModel):
    def __init__(self, sdf_version: str, fdir1: _SDFVector3 = None):
        self.__version__ = sdf_version
        if fdir1 is None:
            fdir1 = _SDFVector3.from_sdf("0 0 0")
        self.fdir1 = fdir1

    def to_version(self, target_version: str) -> "Fdir1":
        if self.fdir1 is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'fdir1' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["fdir1"] = self.fdir1
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("fdir1")
        if self.fdir1 is not None:
            el.text = self.fdir1.to_sdf()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0 0"
        _fdir1 = _SDFVector3._from_sdf(_text, version)
        if isinstance(_fdir1, SDFError):
            return _fdir1
        if _fdir1 is not None and cmp_version(version, "1.2") < 0:
            if _fdir1 != "0 0 0":
                return SDFError(f"'fdir1' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, fdir1=_fdir1)


class Mu(BaseModel):
    def __init__(self, sdf_version: str, mu: float = -1):
        self.__version__ = sdf_version
        self.mu = mu

    def to_version(self, target_version: str) -> "Mu":
        if self.mu is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'mu' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["mu"] = self.mu
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("mu")
        if self.mu is not None:
            el.text = str(self.mu)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or -1
        _mu = _parse_double(_text)
        if isinstance(_mu, SDFError):
            return _mu
        if _mu is not None and cmp_version(version, "1.2") < 0:
            if _mu != -1:
                return SDFError(f"'mu' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, mu=_mu)


class Slip1(BaseModel):
    def __init__(self, sdf_version: str, slip1: float = 0.0):
        self.__version__ = sdf_version
        self.slip1 = slip1

    def to_version(self, target_version: str) -> "Slip1":
        if self.slip1 is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'slip1' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["slip1"] = self.slip1
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("slip1")
        if self.slip1 is not None:
            el.text = str(self.slip1)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _slip1 = _parse_double(_text)
        if isinstance(_slip1, SDFError):
            return _slip1
        if _slip1 is not None and cmp_version(version, "1.2") < 0:
            if _slip1 != 0.0:
                return SDFError(f"'slip1' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, slip1=_slip1)


class Slip2(BaseModel):
    def __init__(self, sdf_version: str, slip2: float = 0.0):
        self.__version__ = sdf_version
        self.slip2 = slip2

    def to_version(self, target_version: str) -> "Slip2":
        if self.slip2 is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'slip2' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["slip2"] = self.slip2
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("slip2")
        if self.slip2 is not None:
            el.text = str(self.slip2)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _slip2 = _parse_double(_text)
        if isinstance(_slip2, SDFError):
            return _slip2
        if _slip2 is not None and cmp_version(version, "1.2") < 0:
            if _slip2 != 0.0:
                return SDFError(f"'slip2' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, slip2=_slip2)


class Mu2(BaseModel):
    def __init__(self, sdf_version: str, mu2: float = -1):
        self.__version__ = sdf_version
        self.mu2 = mu2

    def to_version(self, target_version: str) -> "Mu2":
        if self.mu2 is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'mu2' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["mu2"] = self.mu2
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("mu2")
        if self.mu2 is not None:
            el.text = str(self.mu2)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or -1
        _mu2 = _parse_double(_text)
        if isinstance(_mu2, SDFError):
            return _mu2
        if _mu2 is not None and cmp_version(version, "1.2") < 0:
            if _mu2 != -1:
                return SDFError(f"'mu2' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, mu2=_mu2)


class Ode(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        fdir1: _SDFVector3 = None,
        mu: float = -1,
        mu2: float = -1,
        slip1: float = 0.0,
        slip2: float = 0.0
    ):
        self.__version__ = sdf_version
        if fdir1 is None:
            fdir1 = _SDFVector3.from_sdf("0 0 0")
        self.fdir1 = fdir1
        self.mu = mu
        self.mu2 = mu2
        self.slip1 = slip1
        self.slip2 = slip2

    def to_version(self, target_version: str) -> "Ode":
        if self.fdir1 is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'fdir1' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.mu is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'mu' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.mu2 is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'mu2' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.slip1 is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'slip1' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.slip2 is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'slip2' is not supported in SDF version {target_version} (removed in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["fdir1"] = self.fdir1
        kwargs["mu"] = self.mu
        kwargs["mu2"] = self.mu2
        kwargs["slip1"] = self.slip1
        kwargs["slip2"] = self.slip2
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("ode")
        if self.fdir1 is not None:
            el.set("fdir1", self.fdir1.to_sdf())
        if self.mu is not None:
            el.set("mu", str(self.mu))
        if self.mu2 is not None:
            el.set("mu2", str(self.mu2))
        if self.slip1 is not None:
            el.set("slip1", str(self.slip1))
        if self.slip2 is not None:
            el.set("slip2", str(self.slip2))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _fdir1 = _SDFVector3._from_sdf(el.get("fdir1", "0 0 0"), version)
        if isinstance(_fdir1, SDFError):
            return _fdir1.extend("@fdir1")
        _mu = _parse_double(el.get("mu", -1))
        if isinstance(_mu, SDFError):
            return _mu.extend("@mu")
        _mu2 = _parse_double(el.get("mu2", -1))
        if isinstance(_mu2, SDFError):
            return _mu2.extend("@mu2")
        _slip1 = _parse_double(el.get("slip1", 0.0))
        if isinstance(_slip1, SDFError):
            return _slip1.extend("@slip1")
        _slip2 = _parse_double(el.get("slip2", 0.0))
        if isinstance(_slip2, SDFError):
            return _slip2.extend("@slip2")
        return cls(sdf_version=version, fdir1=_fdir1, mu=_mu, mu2=_mu2, slip1=_slip1, slip2=_slip2)


class BulletFriction(BaseModel):
    def __init__(self, sdf_version: str, friction: float = 1):
        self.__version__ = sdf_version
        self.friction = friction

    def to_version(self, target_version: str) -> "BulletFriction":
        kwargs = {"sdf_version": target_version}
        kwargs["friction"] = self.friction
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("friction")
        if self.friction is not None:
            el.text = str(self.friction)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _friction = _parse_double(_text)
        if isinstance(_friction, SDFError):
            return _friction
        return cls(sdf_version=version, friction=_friction)


class Friction2(BaseModel):
    def __init__(self, sdf_version: str, friction2: float = 1):
        self.__version__ = sdf_version
        self.friction2 = friction2

    def to_version(self, target_version: str) -> "Friction2":
        kwargs = {"sdf_version": target_version}
        kwargs["friction2"] = self.friction2
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("friction2")
        if self.friction2 is not None:
            el.text = str(self.friction2)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _friction2 = _parse_double(_text)
        if isinstance(_friction2, SDFError):
            return _friction2
        return cls(sdf_version=version, friction2=_friction2)


class RollingFriction(BaseModel):
    def __init__(self, sdf_version: str, rolling_friction: float = 1):
        self.__version__ = sdf_version
        self.rolling_friction = rolling_friction

    def to_version(self, target_version: str) -> "RollingFriction":
        kwargs = {"sdf_version": target_version}
        kwargs["rolling_friction"] = self.rolling_friction
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("rolling_friction")
        if self.rolling_friction is not None:
            el.text = str(self.rolling_friction)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _rolling_friction = _parse_double(_text)
        if isinstance(_rolling_friction, SDFError):
            return _rolling_friction
        return cls(sdf_version=version, rolling_friction=_rolling_friction)


class Bullet(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        fdir1: "Fdir1" = None,
        friction: "BulletFriction" = None,
        friction2: "Friction2" = None,
        rolling_friction: "RollingFriction" = None
    ):
        self.__version__ = sdf_version
        self.fdir1 = fdir1
        self.friction = friction
        self.friction2 = friction2
        self.rolling_friction = rolling_friction

    def to_version(self, target_version: str) -> "Bullet":
        kwargs = {"sdf_version": target_version}
        kwargs["fdir1"] = self.fdir1.to_version(target_version) if self.fdir1 is not None else None
        kwargs["friction"] = self.friction.to_version(target_version) if self.friction is not None else None
        kwargs["friction2"] = self.friction2.to_version(target_version) if self.friction2 is not None else None
        kwargs["rolling_friction"] = self.rolling_friction.to_version(target_version) if self.rolling_friction is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("bullet")
        if self.fdir1 is not None:
            el.append(self.fdir1.to_sdf(version))
        if self.friction is not None:
            el.append(self.friction.to_sdf(version))
        if self.friction2 is not None:
            el.append(self.friction2.to_sdf(version))
        if self.rolling_friction is not None:
            el.append(self.rolling_friction.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_fdir1 = el.find("fdir1")
        if _c_fdir1 is not None:
            _res = Fdir1._from_sdf(_c_fdir1, version)
            if isinstance(_res, SDFError):
                return _res.extend("fdir1")
            _fdir1 = _res
        else:
            _fdir1 = None
        _c_friction = el.find("friction")
        if _c_friction is not None:
            _res = BulletFriction._from_sdf(_c_friction, version)
            if isinstance(_res, SDFError):
                return _res.extend("friction")
            _friction = _res
        else:
            _friction = None
        _c_friction2 = el.find("friction2")
        if _c_friction2 is not None:
            _res = Friction2._from_sdf(_c_friction2, version)
            if isinstance(_res, SDFError):
                return _res.extend("friction2")
            _friction2 = _res
        else:
            _friction2 = None
        _c_rolling_friction = el.find("rolling_friction")
        if _c_rolling_friction is not None:
            _res = RollingFriction._from_sdf(_c_rolling_friction, version)
            if isinstance(_res, SDFError):
                return _res.extend("rolling_friction")
            _rolling_friction = _res
        else:
            _rolling_friction = None
        return cls(sdf_version=version, fdir1=_fdir1, friction=_friction, friction2=_friction2, rolling_friction=_rolling_friction)


class Coefficient(BaseModel):
    def __init__(self, sdf_version: str, coefficient: float = 1.0):
        self.__version__ = sdf_version
        self.coefficient = coefficient

    def to_version(self, target_version: str) -> "Coefficient":
        kwargs = {"sdf_version": target_version}
        kwargs["coefficient"] = self.coefficient
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("coefficient")
        if self.coefficient is not None:
            el.text = str(self.coefficient)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1.0
        _coefficient = _parse_double(_text)
        if isinstance(_coefficient, SDFError):
            return _coefficient
        return cls(sdf_version=version, coefficient=_coefficient)


class UsePatchRadius(BaseModel):
    def __init__(self, sdf_version: str, use_patch_radius: bool = True):
        self.__version__ = sdf_version
        self.use_patch_radius = use_patch_radius

    def to_version(self, target_version: str) -> "UsePatchRadius":
        kwargs = {"sdf_version": target_version}
        kwargs["use_patch_radius"] = self.use_patch_radius
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("use_patch_radius")
        if self.use_patch_radius is not None:
            el.text = str(self.use_patch_radius).lower()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or True
        _use_patch_radius = str(_text).strip().lower() == 'true'
        if isinstance(_use_patch_radius, SDFError):
            return _use_patch_radius
        return cls(sdf_version=version, use_patch_radius=_use_patch_radius)


class PatchRadius(BaseModel):
    def __init__(self, sdf_version: str, patch_radius: float = 0):
        self.__version__ = sdf_version
        self.patch_radius = patch_radius

    def to_version(self, target_version: str) -> "PatchRadius":
        kwargs = {"sdf_version": target_version}
        kwargs["patch_radius"] = self.patch_radius
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("patch_radius")
        if self.patch_radius is not None:
            el.text = str(self.patch_radius)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _patch_radius = _parse_double(_text)
        if isinstance(_patch_radius, SDFError):
            return _patch_radius
        return cls(sdf_version=version, patch_radius=_patch_radius)


class SurfaceRadius(BaseModel):
    def __init__(self, sdf_version: str, surface_radius: float = 0.0):
        self.__version__ = sdf_version
        self.surface_radius = surface_radius

    def to_version(self, target_version: str) -> "SurfaceRadius":
        kwargs = {"sdf_version": target_version}
        kwargs["surface_radius"] = self.surface_radius
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("surface_radius")
        if self.surface_radius is not None:
            el.text = str(self.surface_radius)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _surface_radius = _parse_double(_text)
        if isinstance(_surface_radius, SDFError):
            return _surface_radius
        return cls(sdf_version=version, surface_radius=_surface_radius)


class Slip(BaseModel):
    def __init__(self, sdf_version: str, slip: float = 0.0):
        self.__version__ = sdf_version
        self.slip = slip

    def to_version(self, target_version: str) -> "Slip":
        kwargs = {"sdf_version": target_version}
        kwargs["slip"] = self.slip
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("slip")
        if self.slip is not None:
            el.text = str(self.slip)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.0
        _slip = _parse_double(_text)
        if isinstance(_slip, SDFError):
            return _slip
        return cls(sdf_version=version, slip=_slip)


class TorsionalOde(BaseModel):
    def __init__(self, sdf_version: str, slip: "Slip" = None):
        self.__version__ = sdf_version
        self.slip = slip

    def to_version(self, target_version: str) -> "TorsionalOde":
        kwargs = {"sdf_version": target_version}
        kwargs["slip"] = self.slip.to_version(target_version) if self.slip is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("ode")
        if self.slip is not None:
            el.append(self.slip.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_slip = el.find("slip")
        if _c_slip is not None:
            _res = Slip._from_sdf(_c_slip, version)
            if isinstance(_res, SDFError):
                return _res.extend("slip")
            _slip = _res
        else:
            _slip = None
        return cls(sdf_version=version, slip=_slip)


class Torsional(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        coefficient: "Coefficient" = None,
        ode: "TorsionalOde" = None,
        patch_radius: "PatchRadius" = None,
        surface_radius: "SurfaceRadius" = None,
        use_patch_radius: "UsePatchRadius" = None
    ):
        self.__version__ = sdf_version
        self.coefficient = coefficient
        self.ode = ode
        self.patch_radius = patch_radius
        self.surface_radius = surface_radius
        self.use_patch_radius = use_patch_radius

    def to_version(self, target_version: str) -> "Torsional":
        kwargs = {"sdf_version": target_version}
        kwargs["coefficient"] = self.coefficient.to_version(target_version) if self.coefficient is not None else None
        kwargs["ode"] = self.ode.to_version(target_version) if self.ode is not None else None
        kwargs["patch_radius"] = self.patch_radius.to_version(target_version) if self.patch_radius is not None else None
        kwargs["surface_radius"] = self.surface_radius.to_version(target_version) if self.surface_radius is not None else None
        kwargs["use_patch_radius"] = self.use_patch_radius.to_version(target_version) if self.use_patch_radius is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("torsional")
        if self.coefficient is not None:
            el.append(self.coefficient.to_sdf(version))
        if self.ode is not None:
            el.append(self.ode.to_sdf(version))
        if self.patch_radius is not None:
            el.append(self.patch_radius.to_sdf(version))
        if self.surface_radius is not None:
            el.append(self.surface_radius.to_sdf(version))
        if self.use_patch_radius is not None:
            el.append(self.use_patch_radius.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_coefficient = el.find("coefficient")
        if _c_coefficient is not None:
            _res = Coefficient._from_sdf(_c_coefficient, version)
            if isinstance(_res, SDFError):
                return _res.extend("coefficient")
            _coefficient = _res
        else:
            _coefficient = None
        _c_ode = el.find("ode")
        if _c_ode is not None:
            _res = TorsionalOde._from_sdf(_c_ode, version)
            if isinstance(_res, SDFError):
                return _res.extend("ode")
            _ode = _res
        else:
            _ode = None
        _c_patch_radius = el.find("patch_radius")
        if _c_patch_radius is not None:
            _res = PatchRadius._from_sdf(_c_patch_radius, version)
            if isinstance(_res, SDFError):
                return _res.extend("patch_radius")
            _patch_radius = _res
        else:
            _patch_radius = None
        _c_surface_radius = el.find("surface_radius")
        if _c_surface_radius is not None:
            _res = SurfaceRadius._from_sdf(_c_surface_radius, version)
            if isinstance(_res, SDFError):
                return _res.extend("surface_radius")
            _surface_radius = _res
        else:
            _surface_radius = None
        _c_use_patch_radius = el.find("use_patch_radius")
        if _c_use_patch_radius is not None:
            _res = UsePatchRadius._from_sdf(_c_use_patch_radius, version)
            if isinstance(_res, SDFError):
                return _res.extend("use_patch_radius")
            _use_patch_radius = _res
        else:
            _use_patch_radius = None
        return cls(sdf_version=version, coefficient=_coefficient, ode=_ode, patch_radius=_patch_radius, surface_radius=_surface_radius, use_patch_radius=_use_patch_radius)


class Friction(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        bullet: "Bullet" = None,
        ode: "Ode" = None,
        torsional: "Torsional" = None
    ):
        self.__version__ = sdf_version
        self.bullet = bullet
        self.ode = ode
        self.torsional = torsional

    def to_version(self, target_version: str) -> "Friction":
        if self.bullet is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'bullet' is not supported in SDF version {target_version} (added in 1.4)")
        if self.torsional is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'torsional' is not supported in SDF version {target_version} (added in 1.5)")
        kwargs = {"sdf_version": target_version}
        kwargs["bullet"] = self.bullet.to_version(target_version) if self.bullet is not None else None
        kwargs["ode"] = self.ode.to_version(target_version) if self.ode is not None else None
        kwargs["torsional"] = self.torsional.to_version(target_version) if self.torsional is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("friction")
        if self.bullet is not None:
            el.append(self.bullet.to_sdf(version))
        if self.ode is not None:
            el.append(self.ode.to_sdf(version))
        if self.torsional is not None:
            el.append(self.torsional.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_bullet = el.find("bullet")
        if _c_bullet is not None:
            _res = Bullet._from_sdf(_c_bullet, version)
            if isinstance(_res, SDFError):
                return _res.extend("bullet")
            _bullet = _res
        else:
            _bullet = None
        if _bullet is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'bullet' is not supported in SDF version {version} (added in 1.4)")
        _c_ode = el.find("ode")
        if _c_ode is not None:
            _res = Ode._from_sdf(_c_ode, version)
            if isinstance(_res, SDFError):
                return _res.extend("ode")
            _ode = _res
        else:
            _ode = None
        _c_torsional = el.find("torsional")
        if _c_torsional is not None:
            _res = Torsional._from_sdf(_c_torsional, version)
            if isinstance(_res, SDFError):
                return _res.extend("torsional")
            _torsional = _res
        else:
            _torsional = None
        if _torsional is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'torsional' is not supported in SDF version {version} (added in 1.5)")
        return cls(sdf_version=version, bullet=_bullet, ode=_ode, torsional=_torsional)


class SoftCfm(BaseModel):
    def __init__(self, sdf_version: str, soft_cfm: float = 0):
        self.__version__ = sdf_version
        self.soft_cfm = soft_cfm

    def to_version(self, target_version: str) -> "SoftCfm":
        if self.soft_cfm is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'soft_cfm' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["soft_cfm"] = self.soft_cfm
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("soft_cfm")
        if self.soft_cfm is not None:
            el.text = str(self.soft_cfm)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _soft_cfm = _parse_double(_text)
        if isinstance(_soft_cfm, SDFError):
            return _soft_cfm
        if _soft_cfm is not None and cmp_version(version, "1.2") < 0:
            if _soft_cfm != 0:
                return SDFError(f"'soft_cfm' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, soft_cfm=_soft_cfm)


class MaxVel(BaseModel):
    def __init__(self, sdf_version: str, max_vel: float = 0.01):
        self.__version__ = sdf_version
        self.max_vel = max_vel

    def to_version(self, target_version: str) -> "MaxVel":
        if self.max_vel is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'max_vel' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["max_vel"] = self.max_vel
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("max_vel")
        if self.max_vel is not None:
            el.text = str(self.max_vel)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.01
        _max_vel = _parse_double(_text)
        if isinstance(_max_vel, SDFError):
            return _max_vel
        if _max_vel is not None and cmp_version(version, "1.2") < 0:
            if _max_vel != 0.01:
                return SDFError(f"'max_vel' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, max_vel=_max_vel)


class MinDepth(BaseModel):
    def __init__(self, sdf_version: str, min_depth: float = 0):
        self.__version__ = sdf_version
        self.min_depth = min_depth

    def to_version(self, target_version: str) -> "MinDepth":
        if self.min_depth is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'min_depth' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["min_depth"] = self.min_depth
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("min_depth")
        if self.min_depth is not None:
            el.text = str(self.min_depth)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _min_depth = _parse_double(_text)
        if isinstance(_min_depth, SDFError):
            return _min_depth
        if _min_depth is not None and cmp_version(version, "1.2") < 0:
            if _min_depth != 0:
                return SDFError(f"'min_depth' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, min_depth=_min_depth)


class Kd(BaseModel):
    def __init__(self, sdf_version: str, kd: float = 1.0):
        self.__version__ = sdf_version
        self.kd = kd

    def to_version(self, target_version: str) -> "Kd":
        if self.kd is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'kd' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["kd"] = self.kd
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("kd")
        if self.kd is not None:
            el.text = str(self.kd)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1.0
        _kd = _parse_double(_text)
        if isinstance(_kd, SDFError):
            return _kd
        if _kd is not None and cmp_version(version, "1.2") < 0:
            if _kd != 1.0:
                return SDFError(f"'kd' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, kd=_kd)


class SoftErp(BaseModel):
    def __init__(self, sdf_version: str, soft_erp: float = 0.2):
        self.__version__ = sdf_version
        self.soft_erp = soft_erp

    def to_version(self, target_version: str) -> "SoftErp":
        if self.soft_erp is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'soft_erp' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["soft_erp"] = self.soft_erp
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("soft_erp")
        if self.soft_erp is not None:
            el.text = str(self.soft_erp)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.2
        _soft_erp = _parse_double(_text)
        if isinstance(_soft_erp, SDFError):
            return _soft_erp
        if _soft_erp is not None and cmp_version(version, "1.2") < 0:
            if _soft_erp != 0.2:
                return SDFError(f"'soft_erp' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, soft_erp=_soft_erp)


class Kp(BaseModel):
    def __init__(self, sdf_version: str, kp: float = 1000000000000.0):
        self.__version__ = sdf_version
        self.kp = kp

    def to_version(self, target_version: str) -> "Kp":
        if self.kp is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'kp' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["kp"] = self.kp
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("kp")
        if self.kp is not None:
            el.text = str(self.kp)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1000000000000.0
        _kp = _parse_double(_text)
        if isinstance(_kp, SDFError):
            return _kp
        if _kp is not None and cmp_version(version, "1.2") < 0:
            if _kp != 1000000000000.0:
                return SDFError(f"'kp' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, kp=_kp)


class ContactOde(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        kd: float = 1.0,
        kp: float = 1000000000000.0,
        max_vel: float = 0.01,
        min_depth: float = 0,
        soft_cfm: float = 0,
        soft_erp: float = 0.2
    ):
        self.__version__ = sdf_version
        self.kd = kd
        self.kp = kp
        self.max_vel = max_vel
        self.min_depth = min_depth
        self.soft_cfm = soft_cfm
        self.soft_erp = soft_erp

    def to_version(self, target_version: str) -> "ContactOde":
        if self.kd is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'kd' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.kp is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'kp' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.max_vel is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'max_vel' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.min_depth is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'min_depth' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.soft_cfm is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'soft_cfm' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.soft_erp is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'soft_erp' is not supported in SDF version {target_version} (removed in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["kd"] = self.kd
        kwargs["kp"] = self.kp
        kwargs["max_vel"] = self.max_vel
        kwargs["min_depth"] = self.min_depth
        kwargs["soft_cfm"] = self.soft_cfm
        kwargs["soft_erp"] = self.soft_erp
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("ode")
        if self.kd is not None:
            el.set("kd", str(self.kd))
        if self.kp is not None:
            el.set("kp", str(self.kp))
        if self.max_vel is not None:
            el.set("max_vel", str(self.max_vel))
        if self.min_depth is not None:
            el.set("min_depth", str(self.min_depth))
        if self.soft_cfm is not None:
            el.set("soft_cfm", str(self.soft_cfm))
        if self.soft_erp is not None:
            el.set("soft_erp", str(self.soft_erp))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _kd = _parse_double(el.get("kd", 1.0))
        if isinstance(_kd, SDFError):
            return _kd.extend("@kd")
        _kp = _parse_double(el.get("kp", 1000000000000.0))
        if isinstance(_kp, SDFError):
            return _kp.extend("@kp")
        _max_vel = _parse_double(el.get("max_vel", 0.01))
        if isinstance(_max_vel, SDFError):
            return _max_vel.extend("@max_vel")
        _min_depth = _parse_double(el.get("min_depth", 0))
        if isinstance(_min_depth, SDFError):
            return _min_depth.extend("@min_depth")
        _soft_cfm = _parse_double(el.get("soft_cfm", 0))
        if isinstance(_soft_cfm, SDFError):
            return _soft_cfm.extend("@soft_cfm")
        _soft_erp = _parse_double(el.get("soft_erp", 0.2))
        if isinstance(_soft_erp, SDFError):
            return _soft_erp.extend("@soft_erp")
        return cls(sdf_version=version, kd=_kd, kp=_kp, max_vel=_max_vel, min_depth=_min_depth, soft_cfm=_soft_cfm, soft_erp=_soft_erp)


class CollideBitmask(BaseModel):
    def __init__(self, sdf_version: str, collide_bitmask: int = 1):
        self.__version__ = sdf_version
        self.collide_bitmask = collide_bitmask

    def to_version(self, target_version: str) -> "CollideBitmask":
        if self.collide_bitmask is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'collide_bitmask' is not supported in SDF version {target_version} (added in 1.4)")
        kwargs = {"sdf_version": target_version}
        kwargs["collide_bitmask"] = self.collide_bitmask
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("collide_bitmask")
        if self.collide_bitmask is not None:
            el.text = str(self.collide_bitmask)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _collide_bitmask = _parse_uint32(_text)
        if isinstance(_collide_bitmask, SDFError):
            return _collide_bitmask
        if _collide_bitmask is not None and cmp_version(version, "1.4") < 0:
            if _collide_bitmask != 1:
                return SDFError(f"'collide_bitmask' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, collide_bitmask=_collide_bitmask)


class SplitImpulse(BaseModel):
    def __init__(self, sdf_version: str, split_impulse: bool = True):
        self.__version__ = sdf_version
        self.split_impulse = split_impulse

    def to_version(self, target_version: str) -> "SplitImpulse":
        kwargs = {"sdf_version": target_version}
        kwargs["split_impulse"] = self.split_impulse
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("split_impulse")
        if self.split_impulse is not None:
            el.text = str(self.split_impulse).lower()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or True
        _split_impulse = str(_text).strip().lower() == 'true'
        if isinstance(_split_impulse, SDFError):
            return _split_impulse
        return cls(sdf_version=version, split_impulse=_split_impulse)


class SplitImpulsePenetrationThreshold(BaseModel):
    def __init__(self, sdf_version: str, split_impulse_penetration_threshold: float = -0.01):
        self.__version__ = sdf_version
        self.split_impulse_penetration_threshold = split_impulse_penetration_threshold

    def to_version(self, target_version: str) -> "SplitImpulsePenetrationThreshold":
        kwargs = {"sdf_version": target_version}
        kwargs["split_impulse_penetration_threshold"] = self.split_impulse_penetration_threshold
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("split_impulse_penetration_threshold")
        if self.split_impulse_penetration_threshold is not None:
            el.text = str(self.split_impulse_penetration_threshold)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or -0.01
        _split_impulse_penetration_threshold = _parse_double(_text)
        if isinstance(_split_impulse_penetration_threshold, SDFError):
            return _split_impulse_penetration_threshold
        return cls(sdf_version=version, split_impulse_penetration_threshold=_split_impulse_penetration_threshold)


class ContactBullet(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        kd: "Kd" = None,
        kp: "Kp" = None,
        soft_cfm: "SoftCfm" = None,
        soft_erp: "SoftErp" = None,
        split_impulse: "SplitImpulse" = None,
        split_impulse_penetration_threshold: "SplitImpulsePenetrationThreshold" = None
    ):
        self.__version__ = sdf_version
        self.kd = kd
        self.kp = kp
        self.soft_cfm = soft_cfm
        self.soft_erp = soft_erp
        self.split_impulse = split_impulse
        self.split_impulse_penetration_threshold = split_impulse_penetration_threshold

    def to_version(self, target_version: str) -> "ContactBullet":
        kwargs = {"sdf_version": target_version}
        kwargs["kd"] = self.kd.to_version(target_version) if self.kd is not None else None
        kwargs["kp"] = self.kp.to_version(target_version) if self.kp is not None else None
        kwargs["soft_cfm"] = self.soft_cfm.to_version(target_version) if self.soft_cfm is not None else None
        kwargs["soft_erp"] = self.soft_erp.to_version(target_version) if self.soft_erp is not None else None
        kwargs["split_impulse"] = self.split_impulse.to_version(target_version) if self.split_impulse is not None else None
        kwargs["split_impulse_penetration_threshold"] = self.split_impulse_penetration_threshold.to_version(target_version) if self.split_impulse_penetration_threshold is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("bullet")
        if self.kd is not None:
            el.append(self.kd.to_sdf(version))
        if self.kp is not None:
            el.append(self.kp.to_sdf(version))
        if self.soft_cfm is not None:
            el.append(self.soft_cfm.to_sdf(version))
        if self.soft_erp is not None:
            el.append(self.soft_erp.to_sdf(version))
        if self.split_impulse is not None:
            el.append(self.split_impulse.to_sdf(version))
        if self.split_impulse_penetration_threshold is not None:
            el.append(self.split_impulse_penetration_threshold.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_kd = el.find("kd")
        if _c_kd is not None:
            _res = Kd._from_sdf(_c_kd, version)
            if isinstance(_res, SDFError):
                return _res.extend("kd")
            _kd = _res
        else:
            _kd = None
        _c_kp = el.find("kp")
        if _c_kp is not None:
            _res = Kp._from_sdf(_c_kp, version)
            if isinstance(_res, SDFError):
                return _res.extend("kp")
            _kp = _res
        else:
            _kp = None
        _c_soft_cfm = el.find("soft_cfm")
        if _c_soft_cfm is not None:
            _res = SoftCfm._from_sdf(_c_soft_cfm, version)
            if isinstance(_res, SDFError):
                return _res.extend("soft_cfm")
            _soft_cfm = _res
        else:
            _soft_cfm = None
        _c_soft_erp = el.find("soft_erp")
        if _c_soft_erp is not None:
            _res = SoftErp._from_sdf(_c_soft_erp, version)
            if isinstance(_res, SDFError):
                return _res.extend("soft_erp")
            _soft_erp = _res
        else:
            _soft_erp = None
        _c_split_impulse = el.find("split_impulse")
        if _c_split_impulse is not None:
            _res = SplitImpulse._from_sdf(_c_split_impulse, version)
            if isinstance(_res, SDFError):
                return _res.extend("split_impulse")
            _split_impulse = _res
        else:
            _split_impulse = None
        _c_split_impulse_penetration_threshold = el.find("split_impulse_penetration_threshold")
        if _c_split_impulse_penetration_threshold is not None:
            _res = SplitImpulsePenetrationThreshold._from_sdf(_c_split_impulse_penetration_threshold, version)
            if isinstance(_res, SDFError):
                return _res.extend("split_impulse_penetration_threshold")
            _split_impulse_penetration_threshold = _res
        else:
            _split_impulse_penetration_threshold = None
        return cls(sdf_version=version, kd=_kd, kp=_kp, soft_cfm=_soft_cfm, soft_erp=_soft_erp, split_impulse=_split_impulse, split_impulse_penetration_threshold=_split_impulse_penetration_threshold)


class CollideWithoutContactBitmask(BaseModel):
    def __init__(self, sdf_version: str, collide_without_contact_bitmask: int = 1):
        self.__version__ = sdf_version
        self.collide_without_contact_bitmask = collide_without_contact_bitmask

    def to_version(self, target_version: str) -> "CollideWithoutContactBitmask":
        if self.collide_without_contact_bitmask is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'collide_without_contact_bitmask' is not supported in SDF version {target_version} (added in 1.4)")
        kwargs = {"sdf_version": target_version}
        kwargs["collide_without_contact_bitmask"] = self.collide_without_contact_bitmask
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("collide_without_contact_bitmask")
        if self.collide_without_contact_bitmask is not None:
            el.text = str(self.collide_without_contact_bitmask)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1
        _collide_without_contact_bitmask = _parse_uint32(_text)
        if isinstance(_collide_without_contact_bitmask, SDFError):
            return _collide_without_contact_bitmask
        if _collide_without_contact_bitmask is not None and cmp_version(version, "1.4") < 0:
            if _collide_without_contact_bitmask != 1:
                return SDFError(f"'collide_without_contact_bitmask' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, collide_without_contact_bitmask=_collide_without_contact_bitmask)


class CollideWithoutContact(BaseModel):
    def __init__(self, sdf_version: str, collide_without_contact: bool = False):
        self.__version__ = sdf_version
        self.collide_without_contact = collide_without_contact

    def to_version(self, target_version: str) -> "CollideWithoutContact":
        if self.collide_without_contact is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'collide_without_contact' is not supported in SDF version {target_version} (added in 1.4)")
        kwargs = {"sdf_version": target_version}
        kwargs["collide_without_contact"] = self.collide_without_contact
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("collide_without_contact")
        if self.collide_without_contact is not None:
            el.text = str(self.collide_without_contact).lower()
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or False
        _collide_without_contact = str(_text).strip().lower() == 'true'
        if isinstance(_collide_without_contact, SDFError):
            return _collide_without_contact
        if _collide_without_contact is not None and cmp_version(version, "1.4") < 0:
            if _collide_without_contact != False:
                return SDFError(f"'collide_without_contact' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, collide_without_contact=_collide_without_contact)


class PoissonsRatio(BaseModel):
    def __init__(self, sdf_version: str, poissons_ratio: float = 0.3):
        self.__version__ = sdf_version
        self.poissons_ratio = poissons_ratio

    def to_version(self, target_version: str) -> "PoissonsRatio":
        if self.poissons_ratio is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'poissons_ratio' is not supported in SDF version {target_version} (added in 1.5)")
        kwargs = {"sdf_version": target_version}
        kwargs["poissons_ratio"] = self.poissons_ratio
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("poissons_ratio")
        if self.poissons_ratio is not None:
            el.text = str(self.poissons_ratio)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.3
        _poissons_ratio = _parse_double(_text)
        if isinstance(_poissons_ratio, SDFError):
            return _poissons_ratio
        if _poissons_ratio is not None and cmp_version(version, "1.5") < 0:
            if _poissons_ratio != 0.3:
                return SDFError(f"'poissons_ratio' is not supported in SDF version {version} (added in 1.5)")
        return cls(sdf_version=version, poissons_ratio=_poissons_ratio)


class ElasticModulus(BaseModel):
    def __init__(self, sdf_version: str, elastic_modulus: float = -1):
        self.__version__ = sdf_version
        self.elastic_modulus = elastic_modulus

    def to_version(self, target_version: str) -> "ElasticModulus":
        if self.elastic_modulus is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'elastic_modulus' is not supported in SDF version {target_version} (added in 1.5)")
        kwargs = {"sdf_version": target_version}
        kwargs["elastic_modulus"] = self.elastic_modulus
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("elastic_modulus")
        if self.elastic_modulus is not None:
            el.text = str(self.elastic_modulus)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or -1
        _elastic_modulus = _parse_double(_text)
        if isinstance(_elastic_modulus, SDFError):
            return _elastic_modulus
        if _elastic_modulus is not None and cmp_version(version, "1.5") < 0:
            if _elastic_modulus != -1:
                return SDFError(f"'elastic_modulus' is not supported in SDF version {version} (added in 1.5)")
        return cls(sdf_version=version, elastic_modulus=_elastic_modulus)


class CategoryBitmask(BaseModel):
    def __init__(self, sdf_version: str, category_bitmask: int = 65535):
        self.__version__ = sdf_version
        self.category_bitmask = category_bitmask

    def to_version(self, target_version: str) -> "CategoryBitmask":
        if self.category_bitmask is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'category_bitmask' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["category_bitmask"] = self.category_bitmask
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("category_bitmask")
        if self.category_bitmask is not None:
            el.text = str(self.category_bitmask)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 65535
        _category_bitmask = _parse_uint32(_text)
        if isinstance(_category_bitmask, SDFError):
            return _category_bitmask
        if _category_bitmask is not None and cmp_version(version, "1.6") < 0:
            if _category_bitmask != 65535:
                return SDFError(f"'category_bitmask' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, category_bitmask=_category_bitmask)


class Contact(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        bullet: "ContactBullet" = None,
        category_bitmask: "CategoryBitmask" = None,
        collide_bitmask: "CollideBitmask" = None,
        collide_without_contact: "CollideWithoutContact" = None,
        collide_without_contact_bitmask: "CollideWithoutContactBitmask" = None,
        elastic_modulus: "ElasticModulus" = None,
        ode: "ContactOde" = None,
        poissons_ratio: "PoissonsRatio" = None
    ):
        self.__version__ = sdf_version
        self.bullet = bullet
        self.category_bitmask = category_bitmask
        self.collide_bitmask = collide_bitmask
        self.collide_without_contact = collide_without_contact
        self.collide_without_contact_bitmask = collide_without_contact_bitmask
        self.elastic_modulus = elastic_modulus
        self.ode = ode
        self.poissons_ratio = poissons_ratio

    def to_version(self, target_version: str) -> "Contact":
        if self.bullet is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'bullet' is not supported in SDF version {target_version} (added in 1.4)")
        if self.category_bitmask is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'category_bitmask' is not supported in SDF version {target_version} (added in 1.6)")
        if self.collide_bitmask is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'collide_bitmask' is not supported in SDF version {target_version} (added in 1.4)")
        if self.collide_without_contact is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'collide_without_contact' is not supported in SDF version {target_version} (added in 1.4)")
        if self.collide_without_contact_bitmask is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'collide_without_contact_bitmask' is not supported in SDF version {target_version} (added in 1.4)")
        if self.elastic_modulus is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'elastic_modulus' is not supported in SDF version {target_version} (added in 1.5)")
        if self.poissons_ratio is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'poissons_ratio' is not supported in SDF version {target_version} (added in 1.5)")
        kwargs = {"sdf_version": target_version}
        kwargs["bullet"] = self.bullet.to_version(target_version) if self.bullet is not None else None
        kwargs["category_bitmask"] = self.category_bitmask.to_version(target_version) if self.category_bitmask is not None else None
        kwargs["collide_bitmask"] = self.collide_bitmask.to_version(target_version) if self.collide_bitmask is not None else None
        kwargs["collide_without_contact"] = self.collide_without_contact.to_version(target_version) if self.collide_without_contact is not None else None
        kwargs["collide_without_contact_bitmask"] = self.collide_without_contact_bitmask.to_version(target_version) if self.collide_without_contact_bitmask is not None else None
        kwargs["elastic_modulus"] = self.elastic_modulus.to_version(target_version) if self.elastic_modulus is not None else None
        kwargs["ode"] = self.ode.to_version(target_version) if self.ode is not None else None
        kwargs["poissons_ratio"] = self.poissons_ratio.to_version(target_version) if self.poissons_ratio is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("contact")
        if self.bullet is not None:
            el.append(self.bullet.to_sdf(version))
        if self.category_bitmask is not None:
            el.append(self.category_bitmask.to_sdf(version))
        if self.collide_bitmask is not None:
            el.append(self.collide_bitmask.to_sdf(version))
        if self.collide_without_contact is not None:
            el.append(self.collide_without_contact.to_sdf(version))
        if self.collide_without_contact_bitmask is not None:
            el.append(self.collide_without_contact_bitmask.to_sdf(version))
        if self.elastic_modulus is not None:
            el.append(self.elastic_modulus.to_sdf(version))
        if self.ode is not None:
            el.append(self.ode.to_sdf(version))
        if self.poissons_ratio is not None:
            el.append(self.poissons_ratio.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_bullet = el.find("bullet")
        if _c_bullet is not None:
            _res = ContactBullet._from_sdf(_c_bullet, version)
            if isinstance(_res, SDFError):
                return _res.extend("bullet")
            _bullet = _res
        else:
            _bullet = None
        if _bullet is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'bullet' is not supported in SDF version {version} (added in 1.4)")
        _c_category_bitmask = el.find("category_bitmask")
        if _c_category_bitmask is not None:
            _res = CategoryBitmask._from_sdf(_c_category_bitmask, version)
            if isinstance(_res, SDFError):
                return _res.extend("category_bitmask")
            _category_bitmask = _res
        else:
            _category_bitmask = None
        if _category_bitmask is not None and cmp_version(version, "1.6") < 0:
            return SDFError(f"'category_bitmask' is not supported in SDF version {version} (added in 1.6)")
        _c_collide_bitmask = el.find("collide_bitmask")
        if _c_collide_bitmask is not None:
            _res = CollideBitmask._from_sdf(_c_collide_bitmask, version)
            if isinstance(_res, SDFError):
                return _res.extend("collide_bitmask")
            _collide_bitmask = _res
        else:
            _collide_bitmask = None
        if _collide_bitmask is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'collide_bitmask' is not supported in SDF version {version} (added in 1.4)")
        _c_collide_without_contact = el.find("collide_without_contact")
        if _c_collide_without_contact is not None:
            _res = CollideWithoutContact._from_sdf(_c_collide_without_contact, version)
            if isinstance(_res, SDFError):
                return _res.extend("collide_without_contact")
            _collide_without_contact = _res
        else:
            _collide_without_contact = None
        if _collide_without_contact is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'collide_without_contact' is not supported in SDF version {version} (added in 1.4)")
        _c_collide_without_contact_bitmask = el.find("collide_without_contact_bitmask")
        if _c_collide_without_contact_bitmask is not None:
            _res = CollideWithoutContactBitmask._from_sdf(_c_collide_without_contact_bitmask, version)
            if isinstance(_res, SDFError):
                return _res.extend("collide_without_contact_bitmask")
            _collide_without_contact_bitmask = _res
        else:
            _collide_without_contact_bitmask = None
        if _collide_without_contact_bitmask is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'collide_without_contact_bitmask' is not supported in SDF version {version} (added in 1.4)")
        _c_elastic_modulus = el.find("elastic_modulus")
        if _c_elastic_modulus is not None:
            _res = ElasticModulus._from_sdf(_c_elastic_modulus, version)
            if isinstance(_res, SDFError):
                return _res.extend("elastic_modulus")
            _elastic_modulus = _res
        else:
            _elastic_modulus = None
        if _elastic_modulus is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'elastic_modulus' is not supported in SDF version {version} (added in 1.5)")
        _c_ode = el.find("ode")
        if _c_ode is not None:
            _res = ContactOde._from_sdf(_c_ode, version)
            if isinstance(_res, SDFError):
                return _res.extend("ode")
            _ode = _res
        else:
            _ode = None
        _c_poissons_ratio = el.find("poissons_ratio")
        if _c_poissons_ratio is not None:
            _res = PoissonsRatio._from_sdf(_c_poissons_ratio, version)
            if isinstance(_res, SDFError):
                return _res.extend("poissons_ratio")
            _poissons_ratio = _res
        else:
            _poissons_ratio = None
        if _poissons_ratio is not None and cmp_version(version, "1.5") < 0:
            return SDFError(f"'poissons_ratio' is not supported in SDF version {version} (added in 1.5)")
        return cls(sdf_version=version, bullet=_bullet, category_bitmask=_category_bitmask, collide_bitmask=_collide_bitmask, collide_without_contact=_collide_without_contact, collide_without_contact_bitmask=_collide_without_contact_bitmask, elastic_modulus=_elastic_modulus, ode=_ode, poissons_ratio=_poissons_ratio)


class BoneAttachment(BaseModel):
    def __init__(self, sdf_version: str, bone_attachment: float = 100.0):
        self.__version__ = sdf_version
        self.bone_attachment = bone_attachment

    def to_version(self, target_version: str) -> "BoneAttachment":
        kwargs = {"sdf_version": target_version}
        kwargs["bone_attachment"] = self.bone_attachment
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("bone_attachment")
        if self.bone_attachment is not None:
            el.text = str(self.bone_attachment)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 100.0
        _bone_attachment = _parse_double(_text)
        if isinstance(_bone_attachment, SDFError):
            return _bone_attachment
        return cls(sdf_version=version, bone_attachment=_bone_attachment)


class Stiffness(BaseModel):
    def __init__(self, sdf_version: str, stiffness: float = 100.0):
        self.__version__ = sdf_version
        self.stiffness = stiffness

    def to_version(self, target_version: str) -> "Stiffness":
        kwargs = {"sdf_version": target_version}
        kwargs["stiffness"] = self.stiffness
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("stiffness")
        if self.stiffness is not None:
            el.text = str(self.stiffness)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 100.0
        _stiffness = _parse_double(_text)
        if isinstance(_stiffness, SDFError):
            return _stiffness
        return cls(sdf_version=version, stiffness=_stiffness)


class Damping(BaseModel):
    def __init__(self, sdf_version: str, damping: float = 10.0):
        self.__version__ = sdf_version
        self.damping = damping

    def to_version(self, target_version: str) -> "Damping":
        kwargs = {"sdf_version": target_version}
        kwargs["damping"] = self.damping
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("damping")
        if self.damping is not None:
            el.text = str(self.damping)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 10.0
        _damping = _parse_double(_text)
        if isinstance(_damping, SDFError):
            return _damping
        return cls(sdf_version=version, damping=_damping)


class FleshMassFraction(BaseModel):
    def __init__(self, sdf_version: str, flesh_mass_fraction: float = 0.05):
        self.__version__ = sdf_version
        self.flesh_mass_fraction = flesh_mass_fraction

    def to_version(self, target_version: str) -> "FleshMassFraction":
        kwargs = {"sdf_version": target_version}
        kwargs["flesh_mass_fraction"] = self.flesh_mass_fraction
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("flesh_mass_fraction")
        if self.flesh_mass_fraction is not None:
            el.text = str(self.flesh_mass_fraction)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0.05
        _flesh_mass_fraction = _parse_double(_text)
        if isinstance(_flesh_mass_fraction, SDFError):
            return _flesh_mass_fraction
        return cls(sdf_version=version, flesh_mass_fraction=_flesh_mass_fraction)


class Dart(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        bone_attachment: "BoneAttachment" = None,
        damping: "Damping" = None,
        flesh_mass_fraction: "FleshMassFraction" = None,
        stiffness: "Stiffness" = None
    ):
        self.__version__ = sdf_version
        self.bone_attachment = bone_attachment
        self.damping = damping
        self.flesh_mass_fraction = flesh_mass_fraction
        self.stiffness = stiffness

    def to_version(self, target_version: str) -> "Dart":
        kwargs = {"sdf_version": target_version}
        kwargs["bone_attachment"] = self.bone_attachment.to_version(target_version) if self.bone_attachment is not None else None
        kwargs["damping"] = self.damping.to_version(target_version) if self.damping is not None else None
        kwargs["flesh_mass_fraction"] = self.flesh_mass_fraction.to_version(target_version) if self.flesh_mass_fraction is not None else None
        kwargs["stiffness"] = self.stiffness.to_version(target_version) if self.stiffness is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("dart")
        if self.bone_attachment is not None:
            el.append(self.bone_attachment.to_sdf(version))
        if self.damping is not None:
            el.append(self.damping.to_sdf(version))
        if self.flesh_mass_fraction is not None:
            el.append(self.flesh_mass_fraction.to_sdf(version))
        if self.stiffness is not None:
            el.append(self.stiffness.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_bone_attachment = el.find("bone_attachment")
        if _c_bone_attachment is not None:
            _res = BoneAttachment._from_sdf(_c_bone_attachment, version)
            if isinstance(_res, SDFError):
                return _res.extend("bone_attachment")
            _bone_attachment = _res
        else:
            _bone_attachment = None
        _c_damping = el.find("damping")
        if _c_damping is not None:
            _res = Damping._from_sdf(_c_damping, version)
            if isinstance(_res, SDFError):
                return _res.extend("damping")
            _damping = _res
        else:
            _damping = None
        _c_flesh_mass_fraction = el.find("flesh_mass_fraction")
        if _c_flesh_mass_fraction is not None:
            _res = FleshMassFraction._from_sdf(_c_flesh_mass_fraction, version)
            if isinstance(_res, SDFError):
                return _res.extend("flesh_mass_fraction")
            _flesh_mass_fraction = _res
        else:
            _flesh_mass_fraction = None
        _c_stiffness = el.find("stiffness")
        if _c_stiffness is not None:
            _res = Stiffness._from_sdf(_c_stiffness, version)
            if isinstance(_res, SDFError):
                return _res.extend("stiffness")
            _stiffness = _res
        else:
            _stiffness = None
        return cls(sdf_version=version, bone_attachment=_bone_attachment, damping=_damping, flesh_mass_fraction=_flesh_mass_fraction, stiffness=_stiffness)


class SoftContact(BaseModel):
    def __init__(self, sdf_version: str, dart: "Dart" = None):
        self.__version__ = sdf_version
        self.dart = dart

    def to_version(self, target_version: str) -> "SoftContact":
        kwargs = {"sdf_version": target_version}
        kwargs["dart"] = self.dart.to_version(target_version) if self.dart is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("soft_contact")
        if self.dart is not None:
            el.append(self.dart.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_dart = el.find("dart")
        if _c_dart is not None:
            _res = Dart._from_sdf(_c_dart, version)
            if isinstance(_res, SDFError):
                return _res.extend("dart")
            _dart = _res
        else:
            _dart = None
        return cls(sdf_version=version, dart=_dart)


class Surface(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        bounce: "Bounce" = None,
        contact: "Contact" = None,
        friction: "Friction" = None,
        soft_contact: "SoftContact" = None
    ):
        self.__version__ = sdf_version
        self.bounce = bounce
        self.contact = contact
        self.friction = friction
        self.soft_contact = soft_contact

    def to_version(self, target_version: str) -> "Surface":
        if self.soft_contact is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'soft_contact' is not supported in SDF version {target_version} (added in 1.4)")
        kwargs = {"sdf_version": target_version}
        kwargs["bounce"] = self.bounce.to_version(target_version) if self.bounce is not None else None
        kwargs["contact"] = self.contact.to_version(target_version) if self.contact is not None else None
        kwargs["friction"] = self.friction.to_version(target_version) if self.friction is not None else None
        kwargs["soft_contact"] = self.soft_contact.to_version(target_version) if self.soft_contact is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("surface")
        if self.bounce is not None:
            el.append(self.bounce.to_sdf(version))
        if self.contact is not None:
            el.append(self.contact.to_sdf(version))
        if self.friction is not None:
            el.append(self.friction.to_sdf(version))
        if self.soft_contact is not None:
            el.append(self.soft_contact.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_bounce = el.find("bounce")
        if _c_bounce is not None:
            _res = Bounce._from_sdf(_c_bounce, version)
            if isinstance(_res, SDFError):
                return _res.extend("bounce")
            _bounce = _res
        else:
            _bounce = None
        _c_contact = el.find("contact")
        if _c_contact is not None:
            _res = Contact._from_sdf(_c_contact, version)
            if isinstance(_res, SDFError):
                return _res.extend("contact")
            _contact = _res
        else:
            _contact = None
        _c_friction = el.find("friction")
        if _c_friction is not None:
            _res = Friction._from_sdf(_c_friction, version)
            if isinstance(_res, SDFError):
                return _res.extend("friction")
            _friction = _res
        else:
            _friction = None
        _c_soft_contact = el.find("soft_contact")
        if _c_soft_contact is not None:
            _res = SoftContact._from_sdf(_c_soft_contact, version)
            if isinstance(_res, SDFError):
                return _res.extend("soft_contact")
            _soft_contact = _res
        else:
            _soft_contact = None
        if _soft_contact is not None and cmp_version(version, "1.4") < 0:
            return SDFError(f"'soft_contact' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, bounce=_bounce, contact=_contact, friction=_friction, soft_contact=_soft_contact)


class MaxContacts(BaseModel):
    def __init__(self, sdf_version: str, max_contacts: int = 10):
        self.__version__ = sdf_version
        self.max_contacts = max_contacts

    def to_version(self, target_version: str) -> "MaxContacts":
        kwargs = {"sdf_version": target_version}
        kwargs["max_contacts"] = self.max_contacts
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("max_contacts")
        if self.max_contacts is not None:
            el.text = str(self.max_contacts)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 10
        _max_contacts = _parse_int32(_text)
        if isinstance(_max_contacts, SDFError):
            return _max_contacts
        return cls(sdf_version=version, max_contacts=_max_contacts)


class Mass(BaseModel):
    def __init__(self, sdf_version: str, mass: float = 0):
        self.__version__ = sdf_version
        self.mass = mass

    def to_version(self, target_version: str) -> "Mass":
        if self.mass is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'mass' is not supported in SDF version {target_version} (removed in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["mass"] = self.mass
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("mass")
        if self.mass is not None:
            el.text = str(self.mass)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 0
        _mass = _parse_double(_text)
        if isinstance(_mass, SDFError):
            return _mass
        return cls(sdf_version=version, mass=_mass)


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


class LaserRetro(BaseModel):
    def __init__(self, sdf_version: str, laser_retro: float = 0):
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
        _text = el.text or 0
        _laser_retro = _parse_double(_text)
        if isinstance(_laser_retro, SDFError):
            return _laser_retro
        if _laser_retro is not None and cmp_version(version, "1.2") < 0:
            if _laser_retro != 0:
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


class AutoInertiaParams(BaseModel):
    def __init__(self, sdf_version: str):
        self.__version__ = sdf_version

    def to_version(self, target_version: str) -> "AutoInertiaParams":
        kwargs = {"sdf_version": target_version}
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("auto_inertia_params")
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        return cls(sdf_version=version)


class Density(BaseModel):
    def __init__(self, sdf_version: str, density: float = 1000.0):
        self.__version__ = sdf_version
        self.density = density

    def to_version(self, target_version: str) -> "Density":
        if self.density is not None and cmp_version(target_version, "1.11") < 0:
            raise ValueError(f"'density' is not supported in SDF version {target_version} (added in 1.11)")
        kwargs = {"sdf_version": target_version}
        kwargs["density"] = self.density
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("density")
        if self.density is not None:
            el.text = str(self.density)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or 1000.0
        _density = _parse_double(_text)
        if isinstance(_density, SDFError):
            return _density
        if _density is not None and cmp_version(version, "1.11") < 0:
            if _density != 1000.0:
                return SDFError(f"'density' is not supported in SDF version {version} (added in 1.11)")
        return cls(sdf_version=version, density=_density)


class Collision(BaseModel):
    def __init__(
        self,
        sdf_version: str,
        auto_inertia_params: "AutoInertiaParams" = None,
        density: "Density" = None,
        frame: List["Frame"] = None,
        geometry: "Geometry" = None,
        laser_retro: float = 0,
        mass: "Mass" = None,
        max_contacts: "MaxContacts" = None,
        name: str = "__default__",
        origin: "Origin" = None,
        pose: "Pose" = None,
        surface: "Surface" = None
    ):
        self.__version__ = sdf_version
        self.auto_inertia_params = auto_inertia_params
        self.density = density
        self.frame = frame or []
        self.geometry = geometry
        self.laser_retro = laser_retro
        self.mass = mass
        self.max_contacts = max_contacts
        self.name = name
        self.origin = origin
        self.pose = pose
        self.surface = surface

    def to_version(self, target_version: str) -> "Collision":
        if self.auto_inertia_params is not None and cmp_version(target_version, "1.11") < 0:
            raise ValueError(f"'auto_inertia_params' is not supported in SDF version {target_version} (added in 1.11)")
        if self.density is not None and cmp_version(target_version, "1.11") < 0:
            raise ValueError(f"'density' is not supported in SDF version {target_version} (added in 1.11)")
        if self.frame is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (added in 1.5)")
        if self.frame is not None and cmp_version(target_version, "1.7") >= 0:
            raise ValueError(f"'frame' is not supported in SDF version {target_version} (removed in 1.7)")
        if self.laser_retro is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'laser_retro' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.mass is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'mass' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.origin is not None and cmp_version(target_version, "1.2") >= 0:
            raise ValueError(f"'origin' is not supported in SDF version {target_version} (removed in 1.2)")
        if self.pose is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pose' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["auto_inertia_params"] = self.auto_inertia_params.to_version(target_version) if self.auto_inertia_params is not None else None
        kwargs["density"] = self.density.to_version(target_version) if self.density is not None else None
        kwargs["frame"] = [c.to_version(target_version) for c in (self.frame or [])]
        kwargs["geometry"] = self.geometry.to_version(target_version) if self.geometry is not None else None
        kwargs["laser_retro"] = self.laser_retro
        kwargs["mass"] = self.mass.to_version(target_version) if self.mass is not None else None
        kwargs["max_contacts"] = self.max_contacts.to_version(target_version) if self.max_contacts is not None else None
        kwargs["name"] = self.name
        kwargs["origin"] = self.origin.to_version(target_version) if self.origin is not None else None
        kwargs["pose"] = self.pose.to_version(target_version) if self.pose is not None else None
        kwargs["surface"] = self.surface.to_version(target_version) if self.surface is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("collision")
        if self.auto_inertia_params is not None:
            el.append(self.auto_inertia_params.to_sdf(version))
        if self.density is not None:
            el.append(self.density.to_sdf(version))
        for item in (self.frame or []):
            el.append(item.to_sdf(version))
        if self.geometry is None:
            self.geometry = Geometry(sdf_version=version)
        if self.geometry is not None:
            el.append(self.geometry.to_sdf(version))
        if self.laser_retro is not None:
            el.set("laser_retro", str(self.laser_retro))
        if self.mass is not None:
            el.append(self.mass.to_sdf(version))
        if self.max_contacts is not None:
            el.append(self.max_contacts.to_sdf(version))
        if self.name is not None:
            el.set("name", self.name)
        if self.origin is not None:
            el.append(self.origin.to_sdf(version))
        if self.pose is not None:
            el.append(self.pose.to_sdf(version))
        if self.surface is not None:
            el.append(self.surface.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_auto_inertia_params = el.find("auto_inertia_params")
        if _c_auto_inertia_params is not None:
            _res = AutoInertiaParams._from_sdf(_c_auto_inertia_params, version)
            if isinstance(_res, SDFError):
                return _res.extend("auto_inertia_params")
            _auto_inertia_params = _res
        else:
            _auto_inertia_params = None
        if _auto_inertia_params is not None and cmp_version(version, "1.11") < 0:
            return SDFError(f"'auto_inertia_params' is not supported in SDF version {version} (added in 1.11)")
        _c_density = el.find("density")
        if _c_density is not None:
            _res = Density._from_sdf(_c_density, version)
            if isinstance(_res, SDFError):
                return _res.extend("density")
            _density = _res
        else:
            _density = None
        if _density is not None and cmp_version(version, "1.11") < 0:
            return SDFError(f"'density' is not supported in SDF version {version} (added in 1.11)")
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
        _laser_retro = _parse_double(el.get("laser_retro", 0))
        if isinstance(_laser_retro, SDFError):
            return _laser_retro.extend("@laser_retro")
        _c_mass = el.find("mass")
        if _c_mass is not None:
            _res = Mass._from_sdf(_c_mass, version)
            if isinstance(_res, SDFError):
                return _res.extend("mass")
            _mass = _res
        else:
            _mass = None
        _c_max_contacts = el.find("max_contacts")
        if _c_max_contacts is not None:
            _res = MaxContacts._from_sdf(_c_max_contacts, version)
            if isinstance(_res, SDFError):
                return _res.extend("max_contacts")
            _max_contacts = _res
        else:
            _max_contacts = None
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
        _c_surface = el.find("surface")
        if _c_surface is not None:
            _res = Surface._from_sdf(_c_surface, version)
            if isinstance(_res, SDFError):
                return _res.extend("surface")
            _surface = _res
        else:
            _surface = None
        return cls(sdf_version=version, auto_inertia_params=_auto_inertia_params, density=_density, frame=_frame, geometry=_geometry, laser_retro=_laser_retro, mass=_mass, max_contacts=_max_contacts, name=_name, origin=_origin, pose=_pose, surface=_surface)
