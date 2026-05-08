from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from .inner_angle import InnerAngle
from .outer_angle import OuterAngle
from .falloff import Falloff


class Spot(Model):
    def __init__(
        self,
        inner_angle: "InnerAngle" = None,
        outer_angle: "OuterAngle" = None,
        falloff: "Falloff" = None
    ):
        self.inner_angle = inner_angle
        self.outer_angle = outer_angle
        self.falloff = falloff

    def to_sdf(self) -> ET.Element:
        el = ET.Element("spot")
        if self.inner_angle is not None:
            el.append(self.inner_angle.to_sdf())
        if self.outer_angle is not None:
            el.append(self.outer_angle.to_sdf())
        if self.falloff is not None:
            el.append(self.falloff.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Spot":
        _c_inner_angle = el.find("inner_angle")
        _inner_angle = InnerAngle.from_sdf(_c_inner_angle) if _c_inner_angle is not None else None
        _c_outer_angle = el.find("outer_angle")
        _outer_angle = OuterAngle.from_sdf(_c_outer_angle) if _c_outer_angle is not None else None
        _c_falloff = el.find("falloff")
        _falloff = Falloff.from_sdf(_c_falloff) if _c_falloff is not None else None
        return cls(inner_angle=_inner_angle, outer_angle=_outer_angle, falloff=_falloff)
