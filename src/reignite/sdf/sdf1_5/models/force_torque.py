from __future__ import annotations

from xml.etree import ElementTree as ET

from .frame import Frame
from .measure_direction import MeasureDirection
from ...sdf1_4.models.force_torque import ForceTorque as _PrevForceTorque


class ForceTorque(_PrevForceTorque):
    def __init__(self, frame: "Frame" = None, measure_direction: "MeasureDirection" = None):
        super().__init__(frame=frame)
        self.measure_direction = measure_direction

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.measure_direction is not None:
            el.append(self.measure_direction.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "ForceTorque":
        _base = _PrevForceTorque.from_sdf(el)
        _c_measure_direction = el.find("measure_direction")
        _measure_direction = MeasureDirection.from_sdf(
            _c_measure_direction) if _c_measure_direction is not None else None
        return cls(frame=_base.frame, measure_direction=_measure_direction)
