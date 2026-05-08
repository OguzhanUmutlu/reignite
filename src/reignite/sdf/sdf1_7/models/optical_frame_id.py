from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class OpticalFrameId(Model):
    def __init__(self, optical_frame_id: str = ""):
        self.optical_frame_id = optical_frame_id

    def to_sdf(self) -> ET.Element:
        el = ET.Element("optical_frame_id")
        if self.optical_frame_id is not None:
            el.text = self.optical_frame_id
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "OpticalFrameId":
        _text = el.text or ""
        _optical_frame_id = _text
        return cls(optical_frame_id=_optical_frame_id)
