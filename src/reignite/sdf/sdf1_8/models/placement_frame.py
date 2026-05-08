from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class PlacementFrame(Model):
    def __init__(self, placement_frame: str = ""):
        self.placement_frame = placement_frame

    def to_sdf(self) -> ET.Element:
        el = ET.Element("placement_frame")
        if self.placement_frame is not None:
            el.text = self.placement_frame
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "PlacementFrame":
        _text = el.text or ""
        _placement_frame = _text
        return cls(placement_frame=_placement_frame)
