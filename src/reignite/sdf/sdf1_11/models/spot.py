from __future__ import annotations

from xml.etree import ElementTree as ET

from .falloff import Falloff
from .inner_angle import InnerAngle
from .outer_angle import OuterAngle
from ...sdf1_10.models.spot import Spot as _PrevSpot


class Spot(_PrevSpot):
    def __init__(
            self,
            inner_angle: "InnerAngle" = None,
            outer_angle: "OuterAngle" = None,
            falloff: "Falloff" = None
    ):
        super().__init__(inner_angle=inner_angle, outer_angle=outer_angle, falloff=falloff)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Spot":
        _base = _PrevSpot.from_sdf(el)
        return cls(inner_angle=_base.inner_angle, outer_angle=_base.outer_angle, falloff=_base.falloff)
