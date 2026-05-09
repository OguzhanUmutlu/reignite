from __future__ import annotations

import math
from typing import List
from xml.etree import ElementTree as ET

from ..model import Model
from ....utils.vector3 import Vector3


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
    if not math.isfinite(v) or abs(v) > 1.7976931348623157e+308:
        raise ValueError(f"double out of range: {raw}")
    return v


class Width(Model):
    def __init__(self, width: float = 1.0):
        self.width = width

    def to_sdf(self) -> ET.Element:
        el = ET.Element("width")
        if self.width is not None:
            el.text = str(self.width)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Width":
        _text = el.text or 1.0
        _width = _parse_double(_text)
        return cls(width=_width)


class Point(Model):
    def __init__(self, point: Vector3 = None):
        if point is None:
            point = Vector3.from_sdf("0 0 0")
        self.point = point

    def to_sdf(self) -> ET.Element:
        el = ET.Element("point")
        if self.point is not None:
            el.text = self.point.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Point":
        _text = el.text or "0 0 0"
        _point = Vector3.from_sdf(_text)
        return cls(point=_point)


class Road(Model):
    def __init__(
            self,
            name: str = "__default__",
            width: "Width" = None,
            point: List["Point"] = None
    ):
        self.name = name
        self.width = width
        self.point = point or []

    def to_sdf(self) -> ET.Element:
        el = ET.Element("road")
        if self.name is not None:
            el.set("name", self.name)
        if self.width is not None:
            el.append(self.width.to_sdf())
        for item in (self.point or []):
            el.append(item.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Road":
        _name = el.get("name", "__default__")
        _c_width = el.find("width")
        _width = Width.from_sdf(_c_width) if _c_width is not None else None
        _point = [Point.from_sdf(c) for c in el.findall("point")]
        return cls(name=_name, width=_width, point=_point)
