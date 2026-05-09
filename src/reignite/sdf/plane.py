### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.vector2d import Vector2d as _SDFVector2d
from ..utils.vector3 import Vector3 as _SDFVector3


class Normal(BaseModel):
    def __init__(self, sdf_version: str, normal: _SDFVector3 = None):
        self.__version__ = sdf_version
        if normal is None:
            normal = _SDFVector3.from_sdf("0 0 1")
        self.normal = normal

    def to_version(self, target_version: str) -> "Normal":
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
        return cls(sdf_version=version, normal=_normal)


class Plane(BaseModel):
    def __init__(self, sdf_version: str, normal: "Normal" = None, size: "Size" = None):
        self.__version__ = sdf_version
        self.normal = normal
        self.size = size

    def to_version(self, target_version: str) -> "Plane":
        kwargs = {"sdf_version": target_version}
        kwargs["normal"] = self.normal.to_version(target_version) if self.normal is not None else None
        kwargs["size"] = self.size.to_version(target_version) if self.size is not None else None
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str = None) -> ET.Element:
        if version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = version or self.__version__
        el = ET.Element("plane")
        if self.normal is not None:
            el.append(self.normal.to_sdf(version))
        if self.size is not None:
            el.append(self.size.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_normal = el.find("normal")
        if _c_normal is not None:
            _res = Normal._from_sdf(_c_normal, version)
            if isinstance(_res, SDFError):
                return _res.extend("normal")
            _normal = _res
        else:
            _normal = None
        _c_size = el.find("size")
        if _c_size is not None:
            _res = Size._from_sdf(_c_size, version)
            if isinstance(_res, SDFError):
                return _res.extend("size")
            _size = _res
        else:
            _size = None
        return cls(sdf_version=version, normal=_normal, size=_size)


class Size(BaseModel):
    def __init__(self, sdf_version: str, size: _SDFVector2d = None):
        self.__version__ = sdf_version
        if size is None:
            size = _SDFVector2d.from_sdf("1 1")
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
        _text = el.text or "1 1"
        _size = _SDFVector2d._from_sdf(_text, version)
        if isinstance(_size, SDFError):
            return _size
        return cls(sdf_version=version, size=_size)
