from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ....utils.pose import Pose


class Mag(Model):
    def __init__(self, mag: Pose = None):
        if mag is None:
            mag = Pose.from_sdf("0 0 0 0 0 0")
        self.mag = mag

    def to_sdf(self) -> ET.Element:
        el = ET.Element("mag")
        if self.mag is not None:
            el.text = self.mag.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Mag":
        _text = el.text or "0 0 0 0 0 0"
        _mag = Pose.from_sdf(_text)
        return cls(mag=_mag)
