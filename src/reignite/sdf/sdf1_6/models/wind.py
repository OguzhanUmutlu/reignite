from __future__ import annotations

from xml.etree import ElementTree as ET

from .linear_velocity import LinearVelocity
from ..model import Model


class Wind(Model):
    def __init__(self, linear_velocity: "LinearVelocity" = None):
        self.linear_velocity = linear_velocity

    def to_sdf(self) -> ET.Element:
        el = ET.Element("wind")
        if self.linear_velocity is not None:
            el.append(self.linear_velocity.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Wind":
        _c_linear_velocity = el.find("linear_velocity")
        _linear_velocity = LinearVelocity.from_sdf(_c_linear_velocity) if _c_linear_velocity is not None else None
        return cls(linear_velocity=_linear_velocity)
