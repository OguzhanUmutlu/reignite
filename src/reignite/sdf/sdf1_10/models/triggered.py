from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_9.models.triggered import Triggered as _PrevTriggered


class Triggered(_PrevTriggered):
    def __init__(self, triggered: bool = False):
        super().__init__(triggered=triggered)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Triggered":
        _base = _PrevTriggered.from_sdf(el)
        return cls(triggered=_base.triggered)
