from __future__ import annotations

from xml.etree import ElementTree as ET

from .mag import Mag
from .pos import Pos
from ..model import Model


class Wrench(Model):
    def __init__(self, pos: "Pos" = None, mag: "Mag" = None):
        self.pos = pos
        self.mag = mag

    def to_sdf(self) -> ET.Element:
        el = ET.Element("wrench")
        if self.pos is not None:
            el.append(self.pos.to_sdf())
        if self.mag is not None:
            el.append(self.mag.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Wrench":
        _c_pos = el.find("pos")
        _pos = Pos.from_sdf(_c_pos) if _c_pos is not None else None
        _c_mag = el.find("mag")
        _mag = Mag.from_sdf(_c_mag) if _c_mag is not None else None
        return cls(pos=_pos, mag=_mag)
