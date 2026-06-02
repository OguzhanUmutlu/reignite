### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

from xml.etree import ElementTree as ET

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.vector2d import Vector2d as _Vector2dT, _vector2d
from ..utils.vector3 import Vector3 as _Vector3T, _vector3

def _parse_vector2d(raw: str) -> _Vector2dT | SDFError:
    try:
        return _vector2d(raw)
    except ValueError as e:
        return SDFError(str(e))

def _parse_vector3(raw: str) -> _Vector3T | SDFError:
    try:
        return _vector3(raw)
    except ValueError as e:
        return SDFError(str(e))


# noinspection PyUnusedImports
class Plane(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        normal: _Vector3T | None = None,
        size: _Vector2dT | None = None
    ):
        super().__init__(sdf_version)
        self.normal = _vector3("0 0 1") if normal is None else _vector3(normal)
        self.size = _vector2d("1 1") if size is None else _vector2d(size)

    def to_version(self, target_version: str) -> "Plane":
        kwargs: dict = {"sdf_version": target_version, "normal": self.normal, "size": self.size}
        return self.__class__(**kwargs)

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.sdfversion is None and version is not None:
            self.sdfversion = version
        elif version is not None and version != self.sdfversion:
            return self.to_version(str(version)).to_sdf()
        el = ET.Element("plane")
        if self.normal is not None:
            _c_tmp = ET.Element("normal")
            _c_tmp.text = str(self.normal)
            el.append(_c_tmp)
        if self.size is not None:
            _c_tmp = ET.Element("size")
            _c_tmp.text = str(self.size)
            el.append(_c_tmp)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str) -> "Plane | SDFError":
        _c_tmp = el.find("normal")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "0 0 1"
            _val = _parse_vector3(_text)
            if isinstance(_val, SDFError):
                return _val.extend("normal")
            _normal = _val
        else:
            _normal = None
        _c_tmp = el.find("size")
        if _c_tmp is not None:
            _text = _c_tmp.text if _c_tmp.text is not None else "1 1"
            _val = _parse_vector2d(_text)
            if isinstance(_val, SDFError):
                return _val.extend("size")
            _size = _val
        else:
            _size = None
        return cls(sdf_version=version, normal=_normal, size=_size)
