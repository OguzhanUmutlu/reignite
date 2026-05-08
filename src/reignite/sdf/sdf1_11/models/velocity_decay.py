from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_10.models.velocity_decay import VelocityDecay as _PrevVelocityDecay
from .linear import Linear
from .angular import Angular


class VelocityDecay(_PrevVelocityDecay):
    def __init__(self, linear: "Linear" = None, angular: "Angular" = None):
        super().__init__(linear=linear, angular=angular)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "VelocityDecay":
        _base = _PrevVelocityDecay.from_sdf(el)
        return cls(linear=_base.linear, angular=_base.angular)
