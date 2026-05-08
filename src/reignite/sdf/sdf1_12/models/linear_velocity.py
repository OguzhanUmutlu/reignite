from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ....utils.vector3 import Vector3


class LinearVelocity(Model):
    def __init__(self, linear_velocity: Vector3 = None):
        if linear_velocity is None:
            linear_velocity = Vector3.from_sdf("0 0 0")
        self.linear_velocity = linear_velocity

    def to_sdf(self) -> ET.Element:
        el = ET.Element("linear_velocity")
        if self.linear_velocity is not None:
            el.text = self.linear_velocity.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "LinearVelocity":
        _text = el.text or "0 0 0"
        _linear_velocity = Vector3.from_sdf(_text)
        return cls(linear_velocity=_linear_velocity)
