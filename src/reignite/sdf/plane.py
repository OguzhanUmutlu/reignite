### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.vector2d import Vector2d as _SDFVector2d
from ..utils.vector3 import Vector3 as _SDFVector3


class Plane(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        normal: _SDFVector3 = None,
        size: _SDFVector2d = None
    ):
        super().__init__(sdf_version)
        if normal is None:
            normal = _SDFVector3.from_sdf("0 0 1", version=sdf_version)
        if size is None:
            size = _SDFVector2d.from_sdf("1 1", version=sdf_version)
        self.normal = normal
        self.size = size

    def to_version(self, target_version: str) -> "Plane":
        kwargs = {"sdf_version": target_version}
        kwargs["normal"] = self.normal
        kwargs["size"] = self.size
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("plane")
        if self.normal is not None:
            _c_tmp = ET.Element("normal")
            _c_tmp.text = self.normal.to_sdf(version)
            el.append(_c_tmp)
        if self.size is not None:
            _c_tmp = ET.Element("size")
            _c_tmp.text = self.size.to_sdf(version)
            el.append(_c_tmp)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Plane | SDFError":
        _c_tmp = el.find("normal")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "0 0 1"
            _val = _SDFVector3._from_sdf(_text, version)
            if isinstance(_val, SDFError):
                return _val.extend("normal")
            _normal = _val
        else:
            _normal = None
        _c_tmp = el.find("size")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "1 1"
            _val = _SDFVector2d._from_sdf(_text, version)
            if isinstance(_val, SDFError):
                return _val.extend("size")
            _size = _val
        else:
            _size = None
        return cls(sdf_version=version, normal=_normal, size=_size)
