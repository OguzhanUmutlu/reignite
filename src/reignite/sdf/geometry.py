from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ._base import Model
from ..utils.vector2d import Vector2d
from ..utils.vector3 import Vector3
from ..utils.version import cmp_version


import math

def _parse_int32(raw: str) -> int:
    v = int(raw)
    if not (-2147483648 <= v <= 2147483647):
        raise ValueError(f"int32 out of range: {v}")
    return v


def _parse_uint32(raw: str) -> int:
    v = int(raw)
    if not (0 <= v <= 4294967295):
        raise ValueError(f"uint32 out of range: {v}")
    return v


def _parse_double(raw: str) -> float:
    v = float(raw)
    if not math.isfinite(v) or abs(v) > math.inf:
        raise ValueError(f"double out of range: {raw}")
    return v



class Size(Model):
    def __init__(self, sdf_version: str, size: Vector3 = None):
        self.__version__ = sdf_version
        if size is None:
            size = Vector3.from_sdf("1 1 1")
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Size":
        _text = el.text or "1 1 1"
        _size = Vector3.from_sdf(_text)
        if _size is not None and cmp_version(version, "1.2") < 0:
            if _size != "1 1 1":
                raise ValueError(f"'size' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, size=_size)


class Box(Model):
    def __init__(self, sdf_version: str, size: Vector3 = None):
        self.__version__ = sdf_version
        if size is None:
            size = Vector3.from_sdf("1 1 1")
        self.size = size

    def to_version(self, target_version: str) -> "Box":
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Box":
        _size = Vector3.from_sdf(el.get("size", "1 1 1"))
        return cls(sdf_version=version, size=_size)


class Radius(Model):
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Radius":
        _text = el.text or 1
        _radius = _parse_double(_text)
        if _radius is not None and cmp_version(version, "1.2") < 0:
            if _radius != 1:
                raise ValueError(f"'radius' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, radius=_radius)


class Sphere(Model):
    def __init__(self, sdf_version: str, radius: float = 1):
        self.__version__ = sdf_version
        self.radius = radius

    def to_version(self, target_version: str) -> "Sphere":
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Sphere":
        _radius = _parse_double(el.get("radius", 1))
        return cls(sdf_version=version, radius=_radius)


class Length(Model):
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Length":
        _text = el.text or 1
        _length = _parse_double(_text)
        if _length is not None and cmp_version(version, "1.2") < 0:
            if _length != 1:
                raise ValueError(f"'length' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, length=_length)


class Cylinder(Model):
    def __init__(self, sdf_version: str, radius: float = 1, length: float = 1):
        self.__version__ = sdf_version
        self.radius = radius
        self.length = length

    def to_version(self, target_version: str) -> "Cylinder":
        kwargs = {"sdf_version": target_version}
        kwargs["radius"] = self.radius
        kwargs["length"] = self.length
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("cylinder")
        if self.radius is not None:
            el.set("radius", str(self.radius))
        if self.length is not None:
            el.set("length", str(self.length))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Cylinder":
        _radius = _parse_double(el.get("radius", 1))
        _length = _parse_double(el.get("length", 1))
        return cls(sdf_version=version, radius=_radius, length=_length)


class Filename(Model):
    def __init__(self, sdf_version: str, filename: str = "__default__"):
        self.__version__ = sdf_version
        self.filename = filename

    def to_version(self, target_version: str) -> "Filename":
        if self.filename is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'filename' is not supported in SDF version {target_version} (added in 1.2)")
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Filename":
        _text = el.text or "__default__"
        _filename = _text
        if _filename is not None and cmp_version(version, "1.2") < 0:
            if _filename != "__default__":
                raise ValueError(f"'filename' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, filename=_filename)


class Uri(Model):
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Uri":
        _text = el.text or "__default__"
        _uri = _text
        if _uri is not None and cmp_version(version, "1.2") < 0:
            if _uri != "__default__":
                raise ValueError(f"'uri' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, uri=_uri)


class Scale(Model):
    def __init__(self, sdf_version: str, scale: Vector3 = None):
        self.__version__ = sdf_version
        if scale is None:
            scale = Vector3.from_sdf("1 1 1")
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Scale":
        _text = el.text or "1 1 1"
        _scale = Vector3.from_sdf(_text)
        if _scale is not None and cmp_version(version, "1.2") < 0:
            if _scale != "1 1 1":
                raise ValueError(f"'scale' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, scale=_scale)


class Name(Model):
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Name":
        _text = el.text or "__default__"
        _name = _text
        return cls(sdf_version=version, name=_name)


class Center(Model):
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Center":
        _text = el.text or False
        _center = _text.strip().lower() == 'true'
        return cls(sdf_version=version, center=_center)


class Submesh(Model):
    def __init__(self, sdf_version: str, name: "Name" = None, center: "Center" = None):
        self.__version__ = sdf_version
        self.name = name
        self.center = center

    def to_version(self, target_version: str) -> "Submesh":
        kwargs = {"sdf_version": target_version}
        kwargs["name"] = self.name.to_version(target_version) if self.name is not None else None
        kwargs["center"] = self.center.to_version(target_version) if self.center is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("submesh")
        if self.name is not None:
            el.append(self.name.to_sdf(version))
        if self.center is not None:
            el.append(self.center.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Submesh":
        _c_name = el.find("name")
        _name = Name.from_sdf(_c_name, version) if _c_name is not None else None
        _c_center = el.find("center")
        _center = Center.from_sdf(_c_center, version) if _c_center is not None else None
        return cls(sdf_version=version, name=_name, center=_center)


class MaxConvexHulls(Model):
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
    def from_sdf(cls, el: ET.Element, version: str) -> "MaxConvexHulls":
        _text = el.text or 16
        _max_convex_hulls = _parse_uint32(_text)
        return cls(sdf_version=version, max_convex_hulls=_max_convex_hulls)


class VoxelResolution(Model):
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
    def from_sdf(cls, el: ET.Element, version: str) -> "VoxelResolution":
        _text = el.text or 200000
        _voxel_resolution = _parse_uint32(_text)
        return cls(sdf_version=version, voxel_resolution=_voxel_resolution)


class ConvexDecomposition(Model):
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
    def from_sdf(cls, el: ET.Element, version: str) -> "ConvexDecomposition":
        _c_max_convex_hulls = el.find("max_convex_hulls")
        _max_convex_hulls = MaxConvexHulls.from_sdf(_c_max_convex_hulls, version) if _c_max_convex_hulls is not None else None
        _c_voxel_resolution = el.find("voxel_resolution")
        _voxel_resolution = VoxelResolution.from_sdf(_c_voxel_resolution, version) if _c_voxel_resolution is not None else None
        return cls(sdf_version=version, max_convex_hulls=_max_convex_hulls, voxel_resolution=_voxel_resolution)


class Mesh(Model):
    def __init__(
        self,
        sdf_version: str,
        filename: str = "__default__",
        scale: Vector3 = None,
        optimization: str = "",
        uri: "Uri" = None,
        submesh: "Submesh" = None,
        convex_decomposition: "ConvexDecomposition" = None
    ):
        self.__version__ = sdf_version
        if scale is None:
            scale = Vector3.from_sdf("1 1 1")
        self.filename = filename
        self.scale = scale
        self.optimization = optimization
        self.uri = uri
        self.submesh = submesh
        self.convex_decomposition = convex_decomposition

    def to_version(self, target_version: str) -> "Mesh":
        if self.optimization is not None and cmp_version(target_version, "1.11") < 0:
            raise ValueError(f"'optimization' is not supported in SDF version {target_version} (added in 1.11)")
        if self.uri is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'uri' is not supported in SDF version {target_version} (added in 1.2)")
        if self.submesh is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'submesh' is not supported in SDF version {target_version} (added in 1.3)")
        if self.convex_decomposition is not None and cmp_version(target_version, "1.11") < 0:
            raise ValueError(f"'convex_decomposition' is not supported in SDF version {target_version} (added in 1.11)")
        kwargs = {"sdf_version": target_version}
        kwargs["filename"] = self.filename
        kwargs["scale"] = self.scale
        kwargs["optimization"] = self.optimization
        kwargs["uri"] = self.uri.to_version(target_version) if self.uri is not None else None
        kwargs["submesh"] = self.submesh.to_version(target_version) if self.submesh is not None else None
        kwargs["convex_decomposition"] = self.convex_decomposition.to_version(target_version) if self.convex_decomposition is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("mesh")
        if self.filename is not None:
            el.set("filename", self.filename)
        if self.scale is not None:
            el.set("scale", self.scale.to_sdf())
        if self.optimization is not None:
            el.set("optimization", self.optimization)
        if self.uri is not None:
            el.append(self.uri.to_sdf(version))
        if self.submesh is not None:
            el.append(self.submesh.to_sdf(version))
        if self.convex_decomposition is not None:
            el.append(self.convex_decomposition.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Mesh":
        _filename = el.get("filename", "__default__")
        _scale = Vector3.from_sdf(el.get("scale", "1 1 1"))
        _optimization = el.get("optimization", "")
        if _optimization is not None and cmp_version(version, "1.11") < 0:
            if _optimization != "":
                raise ValueError(f"'optimization' is not supported in SDF version {version} (added in 1.11)")
        _c_uri = el.find("uri")
        _uri = Uri.from_sdf(_c_uri, version) if _c_uri is not None else None
        if _uri is not None and cmp_version(version, "1.2") < 0:
            raise ValueError(f"'uri' is not supported in SDF version {version} (added in 1.2)")
        _c_submesh = el.find("submesh")
        _submesh = Submesh.from_sdf(_c_submesh, version) if _c_submesh is not None else None
        if _submesh is not None and cmp_version(version, "1.3") < 0:
            raise ValueError(f"'submesh' is not supported in SDF version {version} (added in 1.3)")
        _c_convex_decomposition = el.find("convex_decomposition")
        _convex_decomposition = ConvexDecomposition.from_sdf(_c_convex_decomposition, version) if _c_convex_decomposition is not None else None
        if _convex_decomposition is not None and cmp_version(version, "1.11") < 0:
            raise ValueError(f"'convex_decomposition' is not supported in SDF version {version} (added in 1.11)")
        return cls(sdf_version=version, filename=_filename, scale=_scale, optimization=_optimization, uri=_uri, submesh=_submesh, convex_decomposition=_convex_decomposition)


class Normal(Model):
    def __init__(self, sdf_version: str, normal: Vector3 = None):
        self.__version__ = sdf_version
        if normal is None:
            normal = Vector3.from_sdf("0 0 1")
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Normal":
        _text = el.text or "0 0 1"
        _normal = Vector3.from_sdf(_text)
        if _normal is not None and cmp_version(version, "1.2") < 0:
            if _normal != "0 0 1":
                raise ValueError(f"'normal' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, normal=_normal)


class Plane(Model):
    def __init__(self, sdf_version: str, normal: Vector3 = None, size: "Size" = None):
        self.__version__ = sdf_version
        if normal is None:
            normal = Vector3.from_sdf("0 0 1")
        self.normal = normal
        self.size = size

    def to_version(self, target_version: str) -> "Plane":
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Plane":
        _normal = Vector3.from_sdf(el.get("normal", "0 0 1"))
        _c_size = el.find("size")
        _size = Size.from_sdf(_c_size, version) if _c_size is not None else None
        if _size is not None and cmp_version(version, "1.2") < 0:
            raise ValueError(f"'size' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, normal=_normal, size=_size)


class Threshold(Model):
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Threshold":
        _text = el.text or 200
        _threshold = _parse_int32(_text)
        if _threshold is not None and cmp_version(version, "1.2") < 0:
            if _threshold != 200:
                raise ValueError(f"'threshold' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, threshold=_threshold)


class Height(Model):
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Height":
        _text = el.text or 1
        _height = _parse_double(_text)
        if _height is not None and cmp_version(version, "1.2") < 0:
            if _height != 1:
                raise ValueError(f"'height' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, height=_height)


class Granularity(Model):
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Granularity":
        _text = el.text or 1
        _granularity = _parse_int32(_text)
        if _granularity is not None and cmp_version(version, "1.2") < 0:
            if _granularity != 1:
                raise ValueError(f"'granularity' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, granularity=_granularity)


class Image(Model):
    def __init__(
        self,
        sdf_version: str,
        filename: str = "__default__",
        scale: float = 1,
        threshold: int = 200,
        height: float = 1,
        granularity: int = 1,
        uri: "Uri" = None
    ):
        self.__version__ = sdf_version
        self.filename = filename
        self.scale = scale
        self.threshold = threshold
        self.height = height
        self.granularity = granularity
        self.uri = uri

    def to_version(self, target_version: str) -> "Image":
        if self.uri is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'uri' is not supported in SDF version {target_version} (added in 1.2)")
        kwargs = {"sdf_version": target_version}
        kwargs["filename"] = self.filename
        kwargs["scale"] = self.scale
        kwargs["threshold"] = self.threshold
        kwargs["height"] = self.height
        kwargs["granularity"] = self.granularity
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
        if self.scale is not None:
            el.set("scale", str(self.scale))
        if self.threshold is not None:
            el.set("threshold", str(self.threshold))
        if self.height is not None:
            el.set("height", str(self.height))
        if self.granularity is not None:
            el.set("granularity", str(self.granularity))
        if self.uri is not None:
            el.append(self.uri.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Image":
        _filename = el.get("filename", "__default__")
        _scale = _parse_double(el.get("scale", 1))
        _threshold = _parse_int32(el.get("threshold", 200))
        _height = _parse_double(el.get("height", 1))
        _granularity = _parse_int32(el.get("granularity", 1))
        _c_uri = el.find("uri")
        _uri = Uri.from_sdf(_c_uri, version) if _c_uri is not None else None
        if _uri is not None and cmp_version(version, "1.2") < 0:
            raise ValueError(f"'uri' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, filename=_filename, scale=_scale, threshold=_threshold, height=_height, granularity=_granularity, uri=_uri)


class Diffuse(Model):
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Diffuse":
        _text = el.text or "__default__"
        _diffuse = _text
        return cls(sdf_version=version, diffuse=_diffuse)


class Texture(Model):
    def __init__(
        self,
        sdf_version: str,
        size: "Size" = None,
        diffuse: "Diffuse" = None,
        normal: "Normal" = None
    ):
        self.__version__ = sdf_version
        self.size = size
        self.diffuse = diffuse
        self.normal = normal

    def to_version(self, target_version: str) -> "Texture":
        kwargs = {"sdf_version": target_version}
        kwargs["size"] = self.size.to_version(target_version) if self.size is not None else None
        kwargs["diffuse"] = self.diffuse.to_version(target_version) if self.diffuse is not None else None
        kwargs["normal"] = self.normal.to_version(target_version) if self.normal is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("texture")
        if self.size is not None:
            el.append(self.size.to_sdf(version))
        if self.diffuse is not None:
            el.append(self.diffuse.to_sdf(version))
        if self.normal is not None:
            el.append(self.normal.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Texture":
        _c_size = el.find("size")
        _size = Size.from_sdf(_c_size, version) if _c_size is not None else None
        _c_diffuse = el.find("diffuse")
        _diffuse = Diffuse.from_sdf(_c_diffuse, version) if _c_diffuse is not None else None
        _c_normal = el.find("normal")
        _normal = Normal.from_sdf(_c_normal, version) if _c_normal is not None else None
        return cls(sdf_version=version, size=_size, diffuse=_diffuse, normal=_normal)


class MinHeight(Model):
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
    def from_sdf(cls, el: ET.Element, version: str) -> "MinHeight":
        _text = el.text or 0
        _min_height = _parse_double(_text)
        return cls(sdf_version=version, min_height=_min_height)


class FadeDist(Model):
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
    def from_sdf(cls, el: ET.Element, version: str) -> "FadeDist":
        _text = el.text or 0
        _fade_dist = _parse_double(_text)
        return cls(sdf_version=version, fade_dist=_fade_dist)


class Blend(Model):
    def __init__(
        self,
        sdf_version: str,
        min_height: "MinHeight" = None,
        fade_dist: "FadeDist" = None
    ):
        self.__version__ = sdf_version
        self.min_height = min_height
        self.fade_dist = fade_dist

    def to_version(self, target_version: str) -> "Blend":
        kwargs = {"sdf_version": target_version}
        kwargs["min_height"] = self.min_height.to_version(target_version) if self.min_height is not None else None
        kwargs["fade_dist"] = self.fade_dist.to_version(target_version) if self.fade_dist is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("blend")
        if self.min_height is not None:
            el.append(self.min_height.to_sdf(version))
        if self.fade_dist is not None:
            el.append(self.fade_dist.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Blend":
        _c_min_height = el.find("min_height")
        _min_height = MinHeight.from_sdf(_c_min_height, version) if _c_min_height is not None else None
        _c_fade_dist = el.find("fade_dist")
        _fade_dist = FadeDist.from_sdf(_c_fade_dist, version) if _c_fade_dist is not None else None
        return cls(sdf_version=version, min_height=_min_height, fade_dist=_fade_dist)


class Pos(Model):
    def __init__(self, sdf_version: str, pos: Vector3 = None):
        self.__version__ = sdf_version
        if pos is None:
            pos = Vector3.from_sdf("0 0 0")
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Pos":
        _text = el.text or "0 0 0"
        _pos = Vector3.from_sdf(_text)
        if _pos is not None and cmp_version(version, "1.2") < 0:
            if _pos != "0 0 0":
                raise ValueError(f"'pos' is not supported in SDF version {version} (added in 1.2)")
        return cls(sdf_version=version, pos=_pos)


class UseTerrainPaging(Model):
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
    def from_sdf(cls, el: ET.Element, version: str) -> "UseTerrainPaging":
        _text = el.text or False
        _use_terrain_paging = _text.strip().lower() == 'true'
        if _use_terrain_paging is not None and cmp_version(version, "1.4") < 0:
            if _use_terrain_paging != False:
                raise ValueError(f"'use_terrain_paging' is not supported in SDF version {version} (added in 1.4)")
        return cls(sdf_version=version, use_terrain_paging=_use_terrain_paging)


class Sampling(Model):
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Sampling":
        _text = el.text or 2
        _sampling = _parse_uint32(_text)
        if _sampling is not None and cmp_version(version, "1.6") < 0:
            if _sampling != 2:
                raise ValueError(f"'sampling' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, sampling=_sampling)


class Heightmap(Model):
    def __init__(
        self,
        sdf_version: str,
        filename: str = "__default__",
        size: Vector3 = None,
        origin: Vector3 = None,
        texture: List["Texture"] = None,
        blend: List["Blend"] = None,
        uri: "Uri" = None,
        pos: "Pos" = None,
        use_terrain_paging: "UseTerrainPaging" = None,
        sampling: "Sampling" = None
    ):
        self.__version__ = sdf_version
        if size is None:
            size = Vector3.from_sdf("1 1 1")
        if origin is None:
            origin = Vector3.from_sdf("0 0 0")
        self.filename = filename
        self.size = size
        self.origin = origin
        self.texture = texture or []
        self.blend = blend or []
        self.uri = uri
        self.pos = pos
        self.use_terrain_paging = use_terrain_paging
        self.sampling = sampling

    def to_version(self, target_version: str) -> "Heightmap":
        if self.uri is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'uri' is not supported in SDF version {target_version} (added in 1.2)")
        if self.pos is not None and cmp_version(target_version, "1.2") < 0:
            raise ValueError(f"'pos' is not supported in SDF version {target_version} (added in 1.2)")
        if self.use_terrain_paging is not None and cmp_version(target_version, "1.4") < 0:
            raise ValueError(f"'use_terrain_paging' is not supported in SDF version {target_version} (added in 1.4)")
        if self.sampling is not None and cmp_version(target_version, "1.6") < 0:
            raise ValueError(f"'sampling' is not supported in SDF version {target_version} (added in 1.6)")
        kwargs = {"sdf_version": target_version}
        kwargs["filename"] = self.filename
        kwargs["size"] = self.size
        kwargs["origin"] = self.origin
        kwargs["texture"] = [c.to_version(target_version) for c in (self.texture or [])]
        kwargs["blend"] = [c.to_version(target_version) for c in (self.blend or [])]
        kwargs["uri"] = self.uri.to_version(target_version) if self.uri is not None else None
        kwargs["pos"] = self.pos.to_version(target_version) if self.pos is not None else None
        kwargs["use_terrain_paging"] = self.use_terrain_paging.to_version(target_version) if self.use_terrain_paging is not None else None
        kwargs["sampling"] = self.sampling.to_version(target_version) if self.sampling is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("heightmap")
        if self.filename is not None:
            el.set("filename", self.filename)
        if self.size is not None:
            el.set("size", self.size.to_sdf())
        if self.origin is not None:
            if cmp_version(version, "1.2") >= 0:
                _c_tmp = ET.Element("pos")
                _c_tmp.text = self.origin.to_sdf()
                el.append(_c_tmp)
            else:
                el.set("origin", self.origin.to_sdf())
        for item in (self.texture or []):
            el.append(item.to_sdf(version))
        for item in (self.blend or []):
            el.append(item.to_sdf(version))
        if self.uri is not None:
            el.append(self.uri.to_sdf(version))
        if self.pos is not None:
            el.append(self.pos.to_sdf(version))
        if self.use_terrain_paging is not None:
            el.append(self.use_terrain_paging.to_sdf(version))
        if self.sampling is not None:
            el.append(self.sampling.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Heightmap":
        _filename = el.get("filename", "__default__")
        _size = Vector3.from_sdf(el.get("size", "1 1 1"))
        _raw_origin = None
        if cmp_version(version, "1.2") >= 0:
            _c_tmp = el.find("pos")
            if _c_tmp is not None: _raw_origin = _c_tmp.text
        else:
            _raw_origin = el.get("origin")
        if _raw_origin is None: _raw_origin = "0 0 0"
        _origin = Vector3.from_sdf(_raw_origin)
        _texture = [Texture.from_sdf(c, version) for c in el.findall("texture")]
        _blend = [Blend.from_sdf(c, version) for c in el.findall("blend")]
        _c_uri = el.find("uri")
        _uri = Uri.from_sdf(_c_uri, version) if _c_uri is not None else None
        if _uri is not None and cmp_version(version, "1.2") < 0:
            raise ValueError(f"'uri' is not supported in SDF version {version} (added in 1.2)")
        _c_pos = el.find("pos")
        _pos = Pos.from_sdf(_c_pos, version) if _c_pos is not None else None
        if _pos is not None and cmp_version(version, "1.2") < 0:
            raise ValueError(f"'pos' is not supported in SDF version {version} (added in 1.2)")
        _c_use_terrain_paging = el.find("use_terrain_paging")
        _use_terrain_paging = UseTerrainPaging.from_sdf(_c_use_terrain_paging, version) if _c_use_terrain_paging is not None else None
        if _use_terrain_paging is not None and cmp_version(version, "1.4") < 0:
            raise ValueError(f"'use_terrain_paging' is not supported in SDF version {version} (added in 1.4)")
        _c_sampling = el.find("sampling")
        _sampling = Sampling.from_sdf(_c_sampling, version) if _c_sampling is not None else None
        if _sampling is not None and cmp_version(version, "1.6") < 0:
            raise ValueError(f"'sampling' is not supported in SDF version {version} (added in 1.6)")
        return cls(sdf_version=version, filename=_filename, size=_size, origin=_origin, texture=_texture, blend=_blend, uri=_uri, pos=_pos, use_terrain_paging=_use_terrain_paging, sampling=_sampling)


class Empty(Model):
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Empty":
        return cls(sdf_version=version)


class Point(Model):
    def __init__(self, sdf_version: str, point: Vector2d = None):
        self.__version__ = sdf_version
        if point is None:
            point = Vector2d.from_sdf("0 0")
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Point":
        _text = el.text or "0 0"
        _point = Vector2d.from_sdf(_text)
        return cls(sdf_version=version, point=_point)


class Polyline(Model):
    def __init__(self, sdf_version: str, point: List["Point"] = None, height: "Height" = None):
        self.__version__ = sdf_version
        self.point = point or []
        self.height = height

    def to_version(self, target_version: str) -> "Polyline":
        kwargs = {"sdf_version": target_version}
        kwargs["point"] = [c.to_version(target_version) for c in (self.point or [])]
        kwargs["height"] = self.height.to_version(target_version) if self.height is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("polyline")
        for item in (self.point or []):
            el.append(item.to_sdf(version))
        if self.height is not None:
            el.append(self.height.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Polyline":
        _point = [Point.from_sdf(c, version) for c in el.findall("point")]
        _c_height = el.find("height")
        _height = Height.from_sdf(_c_height, version) if _c_height is not None else None
        return cls(sdf_version=version, point=_point, height=_height)


class Capsule(Model):
    def __init__(self, sdf_version: str, radius: "Radius" = None, length: "Length" = None):
        self.__version__ = sdf_version
        self.radius = radius
        self.length = length

    def to_version(self, target_version: str) -> "Capsule":
        kwargs = {"sdf_version": target_version}
        kwargs["radius"] = self.radius.to_version(target_version) if self.radius is not None else None
        kwargs["length"] = self.length.to_version(target_version) if self.length is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("capsule")
        if self.radius is not None:
            el.append(self.radius.to_sdf(version))
        if self.length is not None:
            el.append(self.length.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Capsule":
        _c_radius = el.find("radius")
        _radius = Radius.from_sdf(_c_radius, version) if _c_radius is not None else None
        _c_length = el.find("length")
        _length = Length.from_sdf(_c_length, version) if _c_length is not None else None
        return cls(sdf_version=version, radius=_radius, length=_length)


class Radii(Model):
    def __init__(self, sdf_version: str, radii: Vector3 = None):
        self.__version__ = sdf_version
        if radii is None:
            radii = Vector3.from_sdf("1 1 1")
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Radii":
        _text = el.text or "1 1 1"
        _radii = Vector3.from_sdf(_text)
        return cls(sdf_version=version, radii=_radii)


class Ellipsoid(Model):
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Ellipsoid":
        _c_radii = el.find("radii")
        _radii = Radii.from_sdf(_c_radii, version) if _c_radii is not None else None
        return cls(sdf_version=version, radii=_radii)


class Cone(Model):
    def __init__(self, sdf_version: str, radius: "Radius" = None, length: "Length" = None):
        self.__version__ = sdf_version
        self.radius = radius
        self.length = length

    def to_version(self, target_version: str) -> "Cone":
        kwargs = {"sdf_version": target_version}
        kwargs["radius"] = self.radius.to_version(target_version) if self.radius is not None else None
        kwargs["length"] = self.length.to_version(target_version) if self.length is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("cone")
        if self.radius is not None:
            el.append(self.radius.to_sdf(version))
        if self.length is not None:
            el.append(self.length.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Cone":
        _c_radius = el.find("radius")
        _radius = Radius.from_sdf(_c_radius, version) if _c_radius is not None else None
        _c_length = el.find("length")
        _length = Length.from_sdf(_c_length, version) if _c_length is not None else None
        return cls(sdf_version=version, radius=_radius, length=_length)


class Geometry(Model):
    def __init__(
        self,
        sdf_version: str,
        box: "Box" = None,
        sphere: "Sphere" = None,
        cylinder: "Cylinder" = None,
        mesh: "Mesh" = None,
        plane: "Plane" = None,
        image: "Image" = None,
        heightmap: "Heightmap" = None,
        empty: "Empty" = None,
        polyline: "Polyline" = None,
        capsule: "Capsule" = None,
        ellipsoid: "Ellipsoid" = None,
        cone: "Cone" = None
    ):
        self.__version__ = sdf_version
        self.box = box
        self.sphere = sphere
        self.cylinder = cylinder
        self.mesh = mesh
        self.plane = plane
        self.image = image
        self.heightmap = heightmap
        self.empty = empty
        self.polyline = polyline
        self.capsule = capsule
        self.ellipsoid = ellipsoid
        self.cone = cone

    def to_version(self, target_version: str) -> "Geometry":
        if self.empty is not None and cmp_version(target_version, "1.3") < 0:
            raise ValueError(f"'empty' is not supported in SDF version {target_version} (added in 1.3)")
        if self.polyline is not None and cmp_version(target_version, "1.5") < 0:
            raise ValueError(f"'polyline' is not supported in SDF version {target_version} (added in 1.5)")
        if self.capsule is not None and cmp_version(target_version, "1.8") < 0:
            raise ValueError(f"'capsule' is not supported in SDF version {target_version} (added in 1.8)")
        if self.ellipsoid is not None and cmp_version(target_version, "1.8") < 0:
            raise ValueError(f"'ellipsoid' is not supported in SDF version {target_version} (added in 1.8)")
        if self.cone is not None and cmp_version(target_version, "1.11") < 0:
            raise ValueError(f"'cone' is not supported in SDF version {target_version} (added in 1.11)")
        kwargs = {"sdf_version": target_version}
        kwargs["box"] = self.box.to_version(target_version) if self.box is not None else None
        kwargs["sphere"] = self.sphere.to_version(target_version) if self.sphere is not None else None
        kwargs["cylinder"] = self.cylinder.to_version(target_version) if self.cylinder is not None else None
        kwargs["mesh"] = self.mesh.to_version(target_version) if self.mesh is not None else None
        kwargs["plane"] = self.plane.to_version(target_version) if self.plane is not None else None
        kwargs["image"] = self.image.to_version(target_version) if self.image is not None else None
        kwargs["heightmap"] = self.heightmap.to_version(target_version) if self.heightmap is not None else None
        kwargs["empty"] = self.empty.to_version(target_version) if self.empty is not None else None
        kwargs["polyline"] = self.polyline.to_version(target_version) if self.polyline is not None else None
        kwargs["capsule"] = self.capsule.to_version(target_version) if self.capsule is not None else None
        kwargs["ellipsoid"] = self.ellipsoid.to_version(target_version) if self.ellipsoid is not None else None
        kwargs["cone"] = self.cone.to_version(target_version) if self.cone is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("geometry")
        if self.box is not None:
            el.append(self.box.to_sdf(version))
        if self.sphere is not None:
            el.append(self.sphere.to_sdf(version))
        if self.cylinder is not None:
            el.append(self.cylinder.to_sdf(version))
        if self.mesh is not None:
            el.append(self.mesh.to_sdf(version))
        if self.plane is not None:
            el.append(self.plane.to_sdf(version))
        if self.image is not None:
            el.append(self.image.to_sdf(version))
        if self.heightmap is not None:
            el.append(self.heightmap.to_sdf(version))
        if self.empty is not None:
            el.append(self.empty.to_sdf(version))
        if self.polyline is not None:
            el.append(self.polyline.to_sdf(version))
        if self.capsule is not None:
            el.append(self.capsule.to_sdf(version))
        if self.ellipsoid is not None:
            el.append(self.ellipsoid.to_sdf(version))
        if self.cone is not None:
            el.append(self.cone.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Geometry":
        _c_box = el.find("box")
        _box = Box.from_sdf(_c_box, version) if _c_box is not None else None
        _c_sphere = el.find("sphere")
        _sphere = Sphere.from_sdf(_c_sphere, version) if _c_sphere is not None else None
        _c_cylinder = el.find("cylinder")
        _cylinder = Cylinder.from_sdf(_c_cylinder, version) if _c_cylinder is not None else None
        _c_mesh = el.find("mesh")
        _mesh = Mesh.from_sdf(_c_mesh, version) if _c_mesh is not None else None
        _c_plane = el.find("plane")
        _plane = Plane.from_sdf(_c_plane, version) if _c_plane is not None else None
        _c_image = el.find("image")
        _image = Image.from_sdf(_c_image, version) if _c_image is not None else None
        _c_heightmap = el.find("heightmap")
        _heightmap = Heightmap.from_sdf(_c_heightmap, version) if _c_heightmap is not None else None
        _c_empty = el.find("empty")
        _empty = Empty.from_sdf(_c_empty, version) if _c_empty is not None else None
        if _empty is not None and cmp_version(version, "1.3") < 0:
            raise ValueError(f"'empty' is not supported in SDF version {version} (added in 1.3)")
        _c_polyline = el.find("polyline")
        _polyline = Polyline.from_sdf(_c_polyline, version) if _c_polyline is not None else None
        if _polyline is not None and cmp_version(version, "1.5") < 0:
            raise ValueError(f"'polyline' is not supported in SDF version {version} (added in 1.5)")
        _c_capsule = el.find("capsule")
        _capsule = Capsule.from_sdf(_c_capsule, version) if _c_capsule is not None else None
        if _capsule is not None and cmp_version(version, "1.8") < 0:
            raise ValueError(f"'capsule' is not supported in SDF version {version} (added in 1.8)")
        _c_ellipsoid = el.find("ellipsoid")
        _ellipsoid = Ellipsoid.from_sdf(_c_ellipsoid, version) if _c_ellipsoid is not None else None
        if _ellipsoid is not None and cmp_version(version, "1.8") < 0:
            raise ValueError(f"'ellipsoid' is not supported in SDF version {version} (added in 1.8)")
        _c_cone = el.find("cone")
        _cone = Cone.from_sdf(_c_cone, version) if _c_cone is not None else None
        if _cone is not None and cmp_version(version, "1.11") < 0:
            raise ValueError(f"'cone' is not supported in SDF version {version} (added in 1.11)")
        return cls(sdf_version=version, box=_box, sphere=_sphere, cylinder=_cylinder, mesh=_mesh, plane=_plane, image=_image, heightmap=_heightmap, empty=_empty, polyline=_polyline, capsule=_capsule, ellipsoid=_ellipsoid, cone=_cone)
