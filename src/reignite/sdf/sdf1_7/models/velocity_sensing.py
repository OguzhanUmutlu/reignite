from __future__ import annotations

from xml.etree import ElementTree as ET

from .horizontal import Horizontal
from .vertical import Vertical
from ..model import Model


class VelocitySensing(Model):
    def __init__(self, horizontal: "Horizontal" = None, vertical: "Vertical" = None):
        self.horizontal = horizontal
        self.vertical = vertical

    def to_sdf(self) -> ET.Element:
        el = ET.Element("velocity_sensing")
        if self.horizontal is not None:
            el.append(self.horizontal.to_sdf())
        if self.vertical is not None:
            el.append(self.vertical.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "VelocitySensing":
        _c_horizontal = el.find("horizontal")
        _horizontal = Horizontal.from_sdf(_c_horizontal) if _c_horizontal is not None else None
        _c_vertical = el.find("vertical")
        _vertical = Vertical.from_sdf(_c_vertical) if _c_vertical is not None else None
        return cls(horizontal=_horizontal, vertical=_vertical)
