from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class SegmentationType(Model):
    def __init__(self, segmentation_type: str = "semantic"):
        self.segmentation_type = segmentation_type

    def to_sdf(self) -> ET.Element:
        el = ET.Element("segmentation_type")
        if self.segmentation_type is not None:
            el.text = self.segmentation_type
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "SegmentationType":
        _text = el.text or "semantic"
        _segmentation_type = _text
        return cls(segmentation_type=_segmentation_type)
