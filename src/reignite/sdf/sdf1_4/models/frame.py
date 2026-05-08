from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class Frame(Model):
    def __init__(self, frame: str = "parent"):
        self.frame = frame

    def to_sdf(self) -> ET.Element:
        el = ET.Element("frame")
        if self.frame is not None:
            el.text = self.frame
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Frame":
        _text = el.text or "parent"
        _frame = _text
        return cls(frame=_frame)
