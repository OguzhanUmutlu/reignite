from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_6.models.wind import Wind as _PrevWind
from .linear_velocity import LinearVelocity


class Wind(_PrevWind):
    def __init__(self, linear_velocity: "LinearVelocity" = None):
        super().__init__(linear_velocity=linear_velocity)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Wind":
        _base = _PrevWind.from_sdf(el)
        return cls(linear_velocity=_base.linear_velocity)
