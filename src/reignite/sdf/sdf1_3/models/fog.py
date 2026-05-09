from __future__ import annotations

from xml.etree import ElementTree as ET

from .color import Color
from .density import Density
from .end import End
from .start import Start
from ..model import Model


class Type(Model):
    def __init__(self, type: str = "quick"):
        self.type = type

    def to_sdf(self) -> ET.Element:
        el = ET.Element("type")
        if self.type is not None:
            el.text = self.type
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Type":
        _text = el.text or "quick"
        _type = _text
        return cls(type=_type)


class Fog(Model):
    def __init__(
            self,
            color: "Color" = None,
            type: "Type" = None,
            start: "Start" = None,
            end: "End" = None,
            density: "Density" = None
    ):
        self.color = color
        self.type = type
        self.start = start
        self.end = end
        self.density = density

    def to_sdf(self) -> ET.Element:
        el = ET.Element("fog")
        if self.color is not None:
            el.append(self.color.to_sdf())
        if self.type is not None:
            el.append(self.type.to_sdf())
        if self.start is not None:
            el.append(self.start.to_sdf())
        if self.end is not None:
            el.append(self.end.to_sdf())
        if self.density is not None:
            el.append(self.density.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Fog":
        _c_color = el.find("color")
        _color = Color.from_sdf(_c_color) if _c_color is not None else None
        _c_type = el.find("type")
        _type = Type.from_sdf(_c_type) if _c_type is not None else None
        _c_start = el.find("start")
        _start = Start.from_sdf(_c_start) if _c_start is not None else None
        _c_end = el.find("end")
        _end = End.from_sdf(_c_end) if _c_end is not None else None
        _c_density = el.find("density")
        _density = Density.from_sdf(_c_density) if _c_density is not None else None
        return cls(color=_color, type=_type, start=_start, end=_end, density=_density)
