from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_5.models.wrench import Wrench as _PrevWrench
from ....utils.pose import Pose


class Wrench(_PrevWrench):
    def __init__(self, wrench: Pose = None):
        if wrench is None:
            wrench = Pose.from_sdf("0 0 0 0 0 0")
        super().__init__(wrench=wrench)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Wrench":
        _base = _PrevWrench.from_sdf(el)
        return cls(wrench=_base.wrench)
