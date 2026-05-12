### THIS FILE WAS AUTO-GENERATED ###
from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

from typing import List

from ..utils.model import BaseModel
from ..utils.errors import SDFError
from ..utils.vector2d import Vector2d as _SDFVector2d


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



class Height(BaseModel):
    def __init__(self, sdf_version: str | None = None, height: float = 1.0):
        self.__version__ = sdf_version
        self.height = height

    def to_version(self, target_version: str) -> "Height":
        kwargs = {"sdf_version": target_version}
        kwargs["height"] = self.height
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
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


class Point(BaseModel):
    def __init__(self, sdf_version: str | None = None, point: _SDFVector2d = None):
        self.__version__ = sdf_version
        if point is None:
            point = _SDFVector2d.from_sdf("0 0", version=sdf_version)
        self.point = point

    def to_version(self, target_version: str) -> "Point":
        kwargs = {"sdf_version": target_version}
        kwargs["point"] = self.point
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("point")
        if self.point is not None:
            el.text = self.point.to_sdf(version)
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _text = el.text or "0 0"
        _point = _SDFVector2d._from_sdf(_text, version)
        if isinstance(_point, SDFError):
            return _point
        return cls(sdf_version=version, point=_point)


class Polyline(BaseModel):
    def __init__(
        self,
        sdf_version: str | None = None,
        height: "Height" = None,
        points: List["Point"] = None
    ):
        self.__version__ = sdf_version
        self.height = height
        self.points = points or []
        if self.height is not None:
            if getattr(self.height, '__version__', None) is None:
                self.height.__version__ = self.__version__
            elif getattr(self.height, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.height = self.height.to_version(self.__version__)
        for _i, _c in enumerate(self.points):
            if getattr(_c, '__version__', None) is None:
                _c.__version__ = self.__version__
            elif getattr(_c, '__version__', None) != self.__version__ and self.__version__ is not None:
                self.points[_i] = _c.to_version(self.__version__)

    def to_version(self, target_version: str) -> "Polyline":
        kwargs = {"sdf_version": target_version}
        kwargs["height"] = self.height.to_version(target_version) if self.height is not None else None
        kwargs["points"] = [c.to_version(target_version) for c in (self.points or [])]
        new_obj = self.__class__(**kwargs)
        return new_obj

    def to_sdf(self, version: str | None = None) -> ET.Element:
        if self.__version__ is None and version is not None:
            self.__version__ = version
        elif version is not None and version != self.__version__:
            return self.to_version(version).to_sdf()
        version = self.__version__ or version
        el = ET.Element("polyline")
        if self.height is not None:
            el.append(self.height.to_sdf(version))
        for item in (self.points or []):
            el.append(item.to_sdf(version))
        return el

    @classmethod
    def _from_sdf(cls, el: ET.Element, version: str):
        _c_height = el.find("height")
        if _c_height is not None:
            _res = Height._from_sdf(_c_height, version)
            if isinstance(_res, SDFError):
                return _res.extend("height")
            _height = _res
        else:
            _height = None
        _points = []
        for c in el.findall("point"):
            _res = Point._from_sdf(c, version)
            if isinstance(_res, SDFError):
                return _res.extend("point")
            _points.append(_res)
        return cls(sdf_version=version, height=_height, points=_points)
