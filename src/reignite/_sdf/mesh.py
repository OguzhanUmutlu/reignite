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
        def __init__(
            self,
            sdf_version: str | None = None,
            max_convex_hulls: int = 16,
            voxel_resolution: int = 200000
        ):
            super().__init__(sdf_version)
            self.max_convex_hulls = max_convex_hulls
            self.voxel_resolution = voxel_resolution

        def to_version(self, target_version: str) -> "Mesh.ConvexDecomposition":
            kwargs = {"sdf_version": target_version}
            kwargs["max_convex_hulls"] = self.max_convex_hulls
            kwargs["voxel_resolution"] = self.voxel_resolution
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
                _c_tmp = ET.Element("max_convex_hulls")
                _c_tmp.text = str(self.max_convex_hulls)
                el.append(_c_tmp)
            if self.voxel_resolution is not None:
                _c_tmp = ET.Element("voxel_resolution")
                _c_tmp.text = str(self.voxel_resolution)
                el.append(_c_tmp)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Mesh.ConvexDecomposition | SDFError":
            _c_tmp = el.find("max_convex_hulls")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 16
                _val = _parse_uint32(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("max_convex_hulls")
                _max_convex_hulls = _val
            else:
                _max_convex_hulls = None
            _c_tmp = el.find("voxel_resolution")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else 200000
                _val = _parse_uint32(_text)
                if isinstance(_val, SDFError):
                    return _val.extend("voxel_resolution")
                _voxel_resolution = _val
            else:
                _voxel_resolution = None
            return cls(sdf_version=version, max_convex_hulls=_max_convex_hulls, voxel_resolution=_voxel_resolution)

    class Submesh(BaseModel):
        def __init__(
            self,
            sdf_version: str | None = None,
            center: bool = False,
            name: str = "__default__"
        ):
            super().__init__(sdf_version)
            self.center = center
            self.name = name

        def to_version(self, target_version: str) -> "Mesh.Submesh":
            kwargs = {"sdf_version": target_version}
            kwargs["center"] = self.center
            kwargs["name"] = self.name
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
                _c_tmp = ET.Element("center")
                _c_tmp.text = str(self.center).lower()
                el.append(_c_tmp)
            if self.name is not None:
                _c_tmp = ET.Element("name")
                _c_tmp.text = self.name
                el.append(_c_tmp)
            return el

        @classmethod
        def _from_sdf(cls, el: ET.Element, version: str) -> "Mesh.Submesh | SDFError":
            _c_tmp = el.find("center")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else False
                _val = str(_text).strip().lower() == 'true'
                if isinstance(_val, SDFError):
                    return _val.extend("center")
                _center = _val
            else:
                _center = None
            _c_tmp = el.find("name")
            if _c_tmp is not None:
                _text = _c_tmp.text if _c_tmp.text is not None else "__default__"
                _val = _text
                if isinstance(_val, SDFError):
                    return _val.extend("name")
                _name = _val
            else:
                _name = None
            return cls(sdf_version=version, center=_center, name=_name)

    def __init__(
        self,
        sdf_version: str | None = None,
        convex_decomposition: "Mesh.ConvexDecomposition" = None,
        optimization: str = "",
        scale: _SDFVector3 = None,
        submesh: "Mesh.Submesh" = None,
        uri: str = "__default__"
    ):
        super().__init__(sdf_version)
        if scale is None:
            scale = _SDFVector3.from_sdf("1 1 1", version=sdf_version)
        self.convex_decomposition = convex_decomposition
        self.optimization = optimization
        self.scale = scale
        self.submesh = submesh
        self.uri = uri
        if self.convex_decomposition is not None and hasattr(self.convex_decomposition, 'to_version'):
            if getattr(self.convex_decomposition, '__version__', None) is None:
                self.convex_decomposition.__version__ = self.__version__
            elif getattr(self.convex_decomposition, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.convex_decomposition = self.convex_decomposition.to_version(self.__version__)
        if self.submesh is not None and hasattr(self.submesh, 'to_version'):
            if getattr(self.submesh, '__version__', None) is None:
                self.submesh.__version__ = self.__version__
            elif getattr(self.submesh, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.submesh = self.submesh.to_version(self.__version__)

    def to_version(self, target_version: str) -> "Mesh":
        if self.convex_decomposition is not None and cmp_version(target_version, "1.11") < 0:
            raise ValueError(f"'convex_decomposition' is not supported in SDF version {target_version} (added in 1.11)")
        if self.optimization is not None and cmp_version(target_version, "1.11") < 0:
            raise ValueError(f"'optimization' is not supported in SDF version {target_version} (added in 1.11)")
        kwargs = {"sdf_version": target_version}
        kwargs["convex_decomposition"] = self.convex_decomposition.to_version(target_version) if hasattr(self.convex_decomposition, "to_version") else self.convex_decomposition
        kwargs["optimization"] = self.optimization
        kwargs["scale"] = self.scale
        kwargs["submesh"] = self.submesh.to_version(target_version) if hasattr(self.submesh, "to_version") else self.submesh
        kwargs["uri"] = self.uri
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
            if hasattr(self.convex_decomposition, 'to_sdf'):
                _child_res = self.convex_decomposition.to_sdf(version)
            else:
                _child_res = str(self.convex_decomposition)
            if isinstance(_child_res, str):
                _item_el = ET.Element('convex_decomposition')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.optimization is not None:
            el.set("optimization", self.optimization)
        if self.scale is not None:
            _c_tmp = ET.Element("scale")
            _c_tmp.text = self.scale.to_sdf(version)
            el.append(_c_tmp)
        if self.submesh is not None:
            if hasattr(self.submesh, 'to_sdf'):
                _child_res = self.submesh.to_sdf(version)
            else:
                _child_res = str(self.submesh)
            if isinstance(_child_res, str):
                _item_el = ET.Element('submesh')
                _item_el.text = _child_res
            else:
                _item_el = _child_res
            el.append(_item_el)
        if self.uri is not None:
            _c_tmp = ET.Element("uri")
            _c_tmp.text = self.uri
            el.append(_c_tmp)
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
        _c_tmp = el.find("scale")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "1 1 1"
            _val = _SDFVector3._from_sdf(_text, version)
            if isinstance(_val, SDFError):
                return _val.extend("scale")
            _scale = _val
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
        _c_tmp = el.find("uri")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "__default__"
            _val = _text
            if isinstance(_val, SDFError):
                return _val.extend("uri")
            _uri = _val
        else:
            _uri = None
        return cls(sdf_version=version, convex_decomposition=_convex_decomposition, optimization=_optimization, scale=_scale, submesh=_submesh, uri=_uri)
