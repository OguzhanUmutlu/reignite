from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..model import Model
from .point import Point
from .height import Height


class Polyline(Model):
    def __init__(self, point: List["Point"] = None, height: "Height" = None):
        self.point = point or []
        self.height = height

    def to_sdf(self) -> ET.Element:
        el = ET.Element("polyline")
        for item in (self.point or []):
            el.append(item.to_sdf())
        if self.height is not None:
            el.append(self.height.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Polyline":
        _point = [Point.from_sdf(c) for c in el.findall("point")]
        _c_height = el.find("height")
        _height = Height.from_sdf(_c_height) if _c_height is not None else None
        return cls(point=_point, height=_height)
