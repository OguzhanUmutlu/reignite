from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ....utils.pose import Pose


class Velocity(Model):
    def __init__(self, velocity: Pose = None):
        if velocity is None:
            velocity = Pose.from_sdf("0 0 0 0 0 0")
        self.velocity = velocity

    def to_sdf(self) -> ET.Element:
        el = ET.Element("velocity")
        if self.velocity is not None:
            el.text = self.velocity.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Velocity":
        _text = el.text or "0 0 0 0 0 0"
        _velocity = Pose.from_sdf(_text)
        return cls(velocity=_velocity)
