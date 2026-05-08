from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ....utils.vector3 import Vector3


class AngularAcceleration(Model):
    def __init__(self, angular_acceleration: Vector3 = None, degrees: bool = False):
        if angular_acceleration is None:
            angular_acceleration = Vector3.from_sdf("0 0 0")
        self.angular_acceleration = angular_acceleration
        self.degrees = degrees

    def to_sdf(self) -> ET.Element:
        el = ET.Element("angular_acceleration")
        if self.angular_acceleration is not None:
            el.text = self.angular_acceleration.to_sdf()
        if self.degrees is not None:
            el.set("degrees", str(self.degrees).lower())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "AngularAcceleration":
        _text = el.text or "0 0 0"
        _angular_acceleration = Vector3.from_sdf(_text)
        _degrees = el.get("degrees", False).strip().lower() == 'true'
        return cls(angular_acceleration=_angular_acceleration, degrees=_degrees)
