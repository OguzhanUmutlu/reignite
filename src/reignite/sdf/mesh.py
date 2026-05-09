from __future__ import annotations

from xml.etree import ElementTree as ET

from ._base import Model
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



class Uri(Model):
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
    def from_sdf(cls, el: ET.Element, version: str) -> "Uri":
        _text = el.text or "__default__"
        _uri = _text
        return cls(sdf_version=version, uri=_uri)


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


class Scale(Model):
    def __init__(self, sdf_version: str, scale: Vector3 = None):
        self.__version__ = sdf_version
        if scale is None:
            scale = Vector3.from_sdf("1 1 1")
        self.scale = scale

    def to_version(self, target_version: str) -> "Scale":
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
        return cls(sdf_version=version, scale=_scale)


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
        optimization: str = "",
        uri: "Uri" = None,
        submesh: "Submesh" = None,
        scale: "Scale" = None,
        convex_decomposition: "ConvexDecomposition" = None
    ):
        self.__version__ = sdf_version
        self.optimization = optimization
        self.uri = uri
        self.submesh = submesh
        self.scale = scale
        self.convex_decomposition = convex_decomposition

    def to_version(self, target_version: str) -> "Mesh":
        if self.optimization is not None and cmp_version(target_version, "1.11") < 0:
            raise ValueError(f"'optimization' is not supported in SDF version {target_version} (added in 1.11)")
        if self.convex_decomposition is not None and cmp_version(target_version, "1.11") < 0:
            raise ValueError(f"'convex_decomposition' is not supported in SDF version {target_version} (added in 1.11)")
        kwargs = {"sdf_version": target_version}
        kwargs["optimization"] = self.optimization
        kwargs["uri"] = self.uri.to_version(target_version) if self.uri is not None else None
        kwargs["submesh"] = self.submesh.to_version(target_version) if self.submesh is not None else None
        kwargs["scale"] = self.scale.to_version(target_version) if self.scale is not None else None
        kwargs["convex_decomposition"] = self.convex_decomposition.to_version(target_version) if self.convex_decomposition is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("mesh")
        if self.optimization is not None:
            el.set("optimization", self.optimization)
        if self.uri is not None:
            el.append(self.uri.to_sdf(version))
        if self.submesh is not None:
            el.append(self.submesh.to_sdf(version))
        if self.scale is not None:
            el.append(self.scale.to_sdf(version))
        if self.convex_decomposition is not None:
            el.append(self.convex_decomposition.to_sdf(version))
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element, version: str) -> "Mesh":
        _optimization = el.get("optimization", "")
        if _optimization is not None and cmp_version(version, "1.11") < 0:
            if _optimization != "":
                raise ValueError(f"'optimization' is not supported in SDF version {version} (added in 1.11)")
        _c_uri = el.find("uri")
        _uri = Uri.from_sdf(_c_uri, version) if _c_uri is not None else None
        _c_submesh = el.find("submesh")
        _submesh = Submesh.from_sdf(_c_submesh, version) if _c_submesh is not None else None
        _c_scale = el.find("scale")
        _scale = Scale.from_sdf(_c_scale, version) if _c_scale is not None else None
        _c_convex_decomposition = el.find("convex_decomposition")
        _convex_decomposition = ConvexDecomposition.from_sdf(_c_convex_decomposition, version) if _c_convex_decomposition is not None else None
        if _convex_decomposition is not None and cmp_version(version, "1.11") < 0:
            raise ValueError(f"'convex_decomposition' is not supported in SDF version {version} (added in 1.11)")
        return cls(sdf_version=version, optimization=_optimization, uri=_uri, submesh=_submesh, scale=_scale, convex_decomposition=_convex_decomposition)
