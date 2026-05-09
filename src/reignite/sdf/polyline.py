from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ._base import Model
from ..utils.vector2d import Vector2d


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


class Height(Model):
    def __init__(self, sdf_version: str, height: float = 1.0):
        self.__version__ = sdf_version
        self.height = height

    def to_version(self, target_version: str) -> "Height":
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
        _text = el.text or 1.0
        _height = _parse_double(_text)
        return cls(sdf_version=version, height=_height)


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
