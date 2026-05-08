from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..model import Model
from .width import Width
from .point import Point


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
