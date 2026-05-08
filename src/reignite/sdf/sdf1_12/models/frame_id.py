from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class FrameId(Model):
    def __init__(self, frame_id: str = ""):
        self.frame_id = frame_id

    def to_sdf(self) -> ET.Element:
        el = ET.Element("frame_id")
        if self.frame_id is not None:
            el.text = self.frame_id
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "FrameId":
        _text = el.text or ""
        _frame_id = _text
        return cls(frame_id=_frame_id)
