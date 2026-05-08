from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_4.models.velocity_sensing import VelocitySensing as _PrevVelocitySensing
from .horizontal import Horizontal
from .vertical import Vertical


class VelocitySensing(_PrevVelocitySensing):
    def __init__(self, horizontal: "Horizontal" = None, vertical: "Vertical" = None):
        super().__init__(horizontal=horizontal, vertical=vertical)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "VelocitySensing":
        _base = _PrevVelocitySensing.from_sdf(el)
        return cls(horizontal=_base.horizontal, vertical=_base.vertical)
