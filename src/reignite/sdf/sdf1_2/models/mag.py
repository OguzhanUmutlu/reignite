from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_0.models.mag import Mag as _PrevMag
from ....utils.pose import Pose


class Mag(_PrevMag):
    def __init__(self, mag: Pose = None):
        if mag is None:
            mag = Pose.from_sdf("0 0 0 0 0 0")
        super().__init__(mag=mag)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Mag":
        _base = _PrevMag.from_sdf(el)
        return cls(mag=_base.mag)
