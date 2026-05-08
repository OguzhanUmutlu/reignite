from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ....utils.pose import Pose


class Wrench(Model):
    def __init__(self, wrench: Pose = None):
        if wrench is None:
            wrench = Pose.from_sdf("0 0 0 0 0 0")
        self.wrench = wrench

    def to_sdf(self) -> ET.Element:
        el = ET.Element("wrench")
        if self.wrench is not None:
            el.text = self.wrench.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Wrench":
        _text = el.text or "0 0 0 0 0 0"
        _wrench = Pose.from_sdf(_text)
        return cls(wrench=_wrench)
