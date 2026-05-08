from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ....utils.vector3 import Vector3


class Step(Model):
    def __init__(self, step: Vector3 = None):
        if step is None:
            step = Vector3.from_sdf("0.5 0.5 0")
        self.step = step

    def to_sdf(self) -> ET.Element:
        el = ET.Element("step")
        if self.step is not None:
            el.text = self.step.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Step":
        _text = el.text or "0.5 0.5 0"
        _step = Vector3.from_sdf(_text)
        return cls(step=_step)
