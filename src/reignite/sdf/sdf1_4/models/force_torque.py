from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from .frame import Frame


class ForceTorque(Model):
    def __init__(self, frame: "Frame" = None):
        self.frame = frame

    def to_sdf(self) -> ET.Element:
        el = ET.Element("force_torque")
        if self.frame is not None:
            el.append(self.frame.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "ForceTorque":
        _c_frame = el.find("frame")
        _frame = Frame.from_sdf(_c_frame) if _c_frame is not None else None
        return cls(frame=_frame)
