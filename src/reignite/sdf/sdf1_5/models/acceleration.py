from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ....utils.pose import Pose


class Acceleration(Model):
    def __init__(self, acceleration: Pose = None):
        if acceleration is None:
            acceleration = Pose.from_sdf("0 0 0 0 0 0")
        self.acceleration = acceleration

    def to_sdf(self) -> ET.Element:
        el = ET.Element("acceleration")
        if self.acceleration is not None:
            el.text = self.acceleration.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Acceleration":
        _text = el.text or "0 0 0 0 0 0"
        _acceleration = Pose.from_sdf(_text)
        return cls(acceleration=_acceleration)
