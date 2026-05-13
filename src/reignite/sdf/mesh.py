### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.vector3 import Vector3 as _SDFVector3
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



class Mesh(BaseModel):
    class ConvexDecomposition(BaseModel):
        class MaxConvexHulls(BaseModel):
            def __init__(self, sdf_version: str | None = None, max_convex_hulls: int = 16):
                super().__init__(sdf_version)
                self.max_convex_hulls = max_convex_hulls

            def to_version(self, target_version: str) -> "Mesh.ConvexDecomposition.MaxConvexHulls":
                kwargs = {"sdf_version": target_version}
                kwargs["max_convex_hulls"] = self.max_convex_hulls
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("max_convex_hulls")
                if self.max_convex_hulls is not None:
                    el.text = str(self.max_convex_hulls)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Mesh.ConvexDecomposition.MaxConvexHulls | SDFError":
                _text = el.text or 16
                _max_convex_hulls = _parse_uint32(_text)
                if isinstance(_max_convex_hulls, SDFError):
                    return _max_convex_hulls
                return cls(sdf_version=version, max_convex_hulls=_max_convex_hulls)

        class VoxelResolution(BaseModel):
            def __init__(self, sdf_version: str | None = None, voxel_resolution: int = 200000):
                super().__init__(sdf_version)
                self.voxel_resolution = voxel_resolution

            def to_version(self, target_version: str) -> "Mesh.ConvexDecomposition.VoxelResolution":
                kwargs = {"sdf_version": target_version}
                kwargs["voxel_resolution"] = self.voxel_resolution
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("voxel_resolution")
                if self.voxel_resolution is not None:
                    el.text = str(self.voxel_resolution)
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Mesh.ConvexDecomposition.VoxelResolution | SDFError":
                _text = el.text or 200000
                _voxel_resolution = _parse_uint32(_text)
                if isinstance(_voxel_resolution, SDFError):
                    return _voxel_resolution
                return cls(sdf_version=version, voxel_resolution=_voxel_resolution)

        def __init__(
            self,
            sdf_version: str | None = None,
            max_convex_hulls: "Mesh.ConvexDecomposition.MaxConvexHulls" = None,
            voxel_resolution: "Mesh.ConvexDecomposition.VoxelResolution" = None
        ):
            super().__init__(sdf_version)
            self.max_convex_hulls = max_convex_hulls
            self.voxel_resolution = voxel_resolution
            if self.max_convex_hulls is not None:
                if getattr(self.max_convex_hulls, '__version__', None) is None:
                    self.max_convex_hulls.__version__ = self.__version__
                elif getattr(self.max_convex_hulls, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.max_convex_hulls = self.max_convex_hulls.to_version(self.__version__)
            if self.voxel_resolution is not None:
                if getattr(self.voxel_resolution, '__version__', None) is None:
                    self.voxel_resolution.__version__ = self.__version__
                elif getattr(self.voxel_resolution, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.voxel_resolution = self.voxel_resolution.to_version(self.__version__)

        def to_version(self, target_version: str) -> "Mesh.ConvexDecomposition":
            kwargs = {"sdf_version": target_version}
            kwargs["max_convex_hulls"] = self.max_convex_hulls.to_version(target_version) if self.max_convex_hulls is not None else None
            kwargs["voxel_resolution"] = self.voxel_resolution.to_version(target_version) if self.voxel_resolution is not None else None
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("convex_decomposition")
            if self.max_convex_hulls is not None:
                el.append(self.max_convex_hulls.to_sdf(version))
            if self.voxel_resolution is not None:
                el.append(self.voxel_resolution.to_sdf(version))
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Mesh.ConvexDecomposition | SDFError":
            _c_max_convex_hulls = el.find("max_convex_hulls")
            if _c_max_convex_hulls is not None:
                _res = cls.MaxConvexHulls._from_sdf(_c_max_convex_hulls, version)
                if isinstance(_res, SDFError):
                    return _res.extend("max_convex_hulls")
                _max_convex_hulls = _res
            else:
                _max_convex_hulls = None
            _c_voxel_resolution = el.find("voxel_resolution")
            if _c_voxel_resolution is not None:
                _res = cls.VoxelResolution._from_sdf(_c_voxel_resolution, version)
                if isinstance(_res, SDFError):
                    return _res.extend("voxel_resolution")
                _voxel_resolution = _res
            else:
                _voxel_resolution = None
            return cls(sdf_version=version, max_convex_hulls=_max_convex_hulls, voxel_resolution=_voxel_resolution)

    class Scale(BaseModel):
        def __init__(self, sdf_version: str | None = None, scale: _SDFVector3 = None):
            super().__init__(sdf_version)
            if scale is None:
                scale = _SDFVector3.from_sdf("1 1 1", version=sdf_version)
            self.scale = scale

        def to_version(self, target_version: str) -> "Mesh.Scale":
            kwargs = {"sdf_version": target_version}
            kwargs["scale"] = self.scale
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("scale")
            if self.scale is not None:
                el.text = self.scale.to_sdf(version)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Mesh.Scale | SDFError":
            _text = el.text or "1 1 1"
            _scale = _SDFVector3._from_sdf(_text, version)
            if isinstance(_scale, SDFError):
                return _scale
            return cls(sdf_version=version, scale=_scale)

    class Submesh(BaseModel):
        class Center(BaseModel):
            def __init__(self, sdf_version: str | None = None, center: bool = False):
                super().__init__(sdf_version)
                self.center = center

            def to_version(self, target_version: str) -> "Mesh.Submesh.Center":
                kwargs = {"sdf_version": target_version}
                kwargs["center"] = self.center
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("center")
                if self.center is not None:
                    el.text = str(self.center).lower()
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Mesh.Submesh.Center | SDFError":
                _text = el.text or False
                _center = str(_text).strip().lower() == 'true'
                if isinstance(_center, SDFError):
                    return _center
                return cls(sdf_version=version, center=_center)

        class Name(BaseModel):
            def __init__(self, sdf_version: str | None = None, name: str = "__default__"):
                super().__init__(sdf_version)
                self.name = name

            def to_version(self, target_version: str) -> "Mesh.Submesh.Name":
                kwargs = {"sdf_version": target_version}
                kwargs["name"] = self.name
                new_obj = self.__class__(**kwargs)
                return new_obj

            def to_sdf(self, version: str | None = None) -> ET.Element:
                if self.__version__ is None and version is not None:
                    self.__version__ = version
                elif version is not None and version != self.__version__:
                    return self.to_version(version).to_sdf()
                version = self.__version__ or version
                el = ET.Element("name")
                if self.name is not None:
                    el.text = self.name
                return el

            @classmethod
            def _from_sdf(cls, el: ET.Element, version: str) -> "Mesh.Submesh.Name | SDFError":
                _text = el.text or "__default__"
                _name = _text
                if isinstance(_name, SDFError):
                    return _name
                return cls(sdf_version=version, name=_name)

        def __init__(
            self,
            sdf_version: str | None = None,
            center: "Mesh.Submesh.Center" = None,
            name: "Mesh.Submesh.Name" = None
        ):
            super().__init__(sdf_version)
            self.center = center
            self.name = name
            if self.center is not None:
                if getattr(self.center, '__version__', None) is None:
                    self.center.__version__ = self.__version__
                elif getattr(self.center, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.center = self.center.to_version(self.__version__)
            if self.name is not None:
                if getattr(self.name, '__version__', None) is None:
                    self.name.__version__ = self.__version__
                elif getattr(self.name, '__version__', None) != self.__version__ and self.__version__ is not None:
                    self.name = self.name.to_version(self.__version__)

        def to_version(self, target_version: str) -> "Mesh.Submesh":
            kwargs = {"sdf_version": target_version}
            kwargs["center"] = self.center.to_version(target_version) if self.center is not None else None
            kwargs["name"] = self.name.to_version(target_version) if self.name is not None else None
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("submesh")
            if self.center is not None:
                el.append(self.center.to_sdf(version))
            if self.name is not None:
                el.append(self.name.to_sdf(version))
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Mesh.Submesh | SDFError":
            _c_center = el.find("center")
            if _c_center is not None:
                _res = cls.Center._from_sdf(_c_center, version)
                if isinstance(_res, SDFError):
                    return _res.extend("center")
                _center = _res
            else:
                _center = None
            _c_name = el.find("name")
            if _c_name is not None:
                _res = cls.Name._from_sdf(_c_name, version)
                if isinstance(_res, SDFError):
                    return _res.extend("name")
                _name = _res
            else:
                _name = None
            return cls(sdf_version=version, center=_center, name=_name)

    class Uri(BaseModel):
        def __init__(self, sdf_version: str | None = None, uri: str = "__default__"):
            super().__init__(sdf_version)
            self.uri = uri

        def to_version(self, target_version: str) -> "Mesh.Uri":
            kwargs = {"sdf_version": target_version}
            kwargs["uri"] = self.uri
            new_obj = self.__class__(**kwargs)
            return new_obj

        def to_sdf(self, version: str | None = None) -> ET.Element:
            if self.__version__ is None and version is not None:
                self.__version__ = version
            elif version is not None and version != self.__version__:
                return self.to_version(version).to_sdf()
            version = self.__version__ or version
            el = ET.Element("uri")
            if self.uri is not None:
                el.text = self.uri
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Mesh.Uri | SDFError":
            _text = el.text or "__default__"
            _uri = _text
            if isinstance(_uri, SDFError):
                return _uri
            return cls(sdf_version=version, uri=_uri)

    def __init__(
        self,
        sdf_version: str | None = None,
        convex_decomposition: "Mesh.ConvexDecomposition" = None,
        optimization: str = "",
        scale: "Mesh.Scale" = None,
        submesh: "Mesh.Submesh" = None,
        uri: "Mesh.Uri" = None
    ):
        super().__init__(sdf_version)
        self.convex_decomposition = convex_decomposition
        self.optimization = optimization
        self.scale = scale
        self.submesh = submesh
        self.uri = uri
        if self.convex_decomposition is not None:
            if getattr(self.convex_decomposition, '__version__', None) is None:
                self.convex_decomposition.__version__ = self.__version__
            elif getattr(self.convex_decomposition, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.convex_decomposition = self.convex_decomposition.to_version(self.__version__)
        if self.scale is not None:
            if getattr(self.scale, '__version__', None) is None:
                self.scale.__version__ = self.__version__
            elif getattr(self.scale, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.scale = self.scale.to_version(self.__version__)
        if self.submesh is not None:
            if getattr(self.submesh, '__version__', None) is None:
                self.submesh.__version__ = self.__version__
            elif getattr(self.submesh, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.submesh = self.submesh.to_version(self.__version__)
        if self.uri is not None:
            if getattr(self.uri, '__version__', None) is None:
                self.uri.__version__ = self.__version__
            elif getattr(self.uri, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.uri = self.uri.to_version(self.__version__)

    def to_version(self, target_version: str) -> "Mesh":
        if self.convex_decomposition is not None and cmp_version(target_version, "1.11") < 0:
            raise ValueError(f"'convex_decomposition' is not supported in SDF version {target_version} (added in 1.11)")
        if self.optimization is not None and cmp_version(target_version, "1.11") < 0:
            raise ValueError(f"'optimization' is not supported in SDF version {target_version} (added in 1.11)")
        kwargs = {"sdf_version": target_version}
        kwargs["convex_decomposition"] = self.convex_decomposition.to_version(target_version) if self.convex_decomposition is not None else None
        kwargs["optimization"] = self.optimization
        kwargs["scale"] = self.scale.to_version(target_version) if self.scale is not None else None
        kwargs["submesh"] = self.submesh.to_version(target_version) if self.submesh is not None else None
        kwargs["uri"] = self.uri.to_version(target_version) if self.uri is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("mesh")
        if self.convex_decomposition is not None:
            el.append(self.convex_decomposition.to_sdf(version))
        if self.optimization is not None:
            el.set("optimization", self.optimization)
        if self.scale is not None:
            el.append(self.scale.to_sdf(version))
        if self.submesh is not None:
            el.append(self.submesh.to_sdf(version))
        if self.uri is not None:
            el.append(self.uri.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Mesh | SDFError":
        _c_convex_decomposition = el.find("convex_decomposition")
        if _c_convex_decomposition is not None:
            _res = cls.ConvexDecomposition._from_sdf(_c_convex_decomposition, version)
            if isinstance(_res, SDFError):
                return _res.extend("convex_decomposition")
            _convex_decomposition = _res
        else:
            _convex_decomposition = None
        if _convex_decomposition is not None and cmp_version(version, "1.11") < 0:
            return SDFError(f"'convex_decomposition' is not supported in SDF version {version} (added in 1.11)")
        _optimization = el.get("optimization", "")
        if isinstance(_optimization, SDFError):
            return _optimization.extend("@optimization")
        if _optimization is not None and cmp_version(version, "1.11") < 0:
            if _optimization != "":
                return SDFError(f"'optimization' is not supported in SDF version {version} (added in 1.11)")
        _c_scale = el.find("scale")
        if _c_scale is not None:
            _res = cls.Scale._from_sdf(_c_scale, version)
            if isinstance(_res, SDFError):
                return _res.extend("scale")
            _scale = _res
        else:
            _scale = None
        _c_submesh = el.find("submesh")
        if _c_submesh is not None:
            _res = cls.Submesh._from_sdf(_c_submesh, version)
            if isinstance(_res, SDFError):
                return _res.extend("submesh")
            _submesh = _res
        else:
            _submesh = None
        _c_uri = el.find("uri")
        if _c_uri is not None:
            _res = cls.Uri._from_sdf(_c_uri, version)
            if isinstance(_res, SDFError):
                return _res.extend("uri")
            _uri = _res
        else:
            _uri = None
        return cls(sdf_version=version, convex_decomposition=_convex_decomposition, optimization=_optimization, scale=_scale, submesh=_submesh, uri=_uri)
