from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_6.models.step import Step as _PrevStep
from ....utils.vector3 import Vector3


class Step(_PrevStep):
    def __init__(self, step: Vector3 = None):
        if step is None:
            step = Vector3.from_sdf("0.5 0.5 0")
        super().__init__(step=step)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Step":
        _base = _PrevStep.from_sdf(el)
        return cls(step=_base.step)
