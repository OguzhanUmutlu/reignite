from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_9.models.measure_direction import MeasureDirection as _PrevMeasureDirection


class MeasureDirection(_PrevMeasureDirection):
    def __init__(self, measure_direction: str = "child_to_parent"):
        super().__init__(measure_direction=measure_direction)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "MeasureDirection":
        _base = _PrevMeasureDirection.from_sdf(el)
        return cls(measure_direction=_base.measure_direction)
