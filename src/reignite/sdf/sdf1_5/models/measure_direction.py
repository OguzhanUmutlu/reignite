from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class MeasureDirection(Model):
    def __init__(self, measure_direction: str = "child_to_parent"):
        self.measure_direction = measure_direction

    def to_sdf(self) -> ET.Element:
        el = ET.Element("measure_direction")
        if self.measure_direction is not None:
            el.text = self.measure_direction
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "MeasureDirection":
        _text = el.text or "child_to_parent"
        _measure_direction = _text
        return cls(measure_direction=_measure_direction)
