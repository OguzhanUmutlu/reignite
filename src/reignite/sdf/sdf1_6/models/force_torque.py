from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_5.models.force_torque import ForceTorque as _PrevForceTorque
from .frame import Frame
from .measure_direction import MeasureDirection


class ForceTorque(_PrevForceTorque):
    def __init__(self, frame: "Frame" = None, measure_direction: "MeasureDirection" = None):
        super().__init__(frame=frame, measure_direction=measure_direction)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "ForceTorque":
        _base = _PrevForceTorque.from_sdf(el)
        return cls(frame=_base.frame, measure_direction=_base.measure_direction)
