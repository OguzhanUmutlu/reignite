from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_8.models.acceleration import Acceleration as _PrevAcceleration
from ....utils.pose import Pose


class Acceleration(_PrevAcceleration):
    def __init__(self, acceleration: Pose = None):
        if acceleration is None:
            acceleration = Pose.from_sdf("0 0 0 0 0 0")
        super().__init__(acceleration=acceleration)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Acceleration":
        _base = _PrevAcceleration.from_sdf(el)
        return cls(acceleration=_base.acceleration)
