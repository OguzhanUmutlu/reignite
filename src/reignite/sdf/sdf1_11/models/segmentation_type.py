from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_10.models.segmentation_type import SegmentationType as _PrevSegmentationType


class SegmentationType(_PrevSegmentationType):
    def __init__(self, segmentation_type: str = "semantic"):
        super().__init__(segmentation_type=segmentation_type)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "SegmentationType":
        _base = _PrevSegmentationType.from_sdf(el)
        return cls(segmentation_type=_base.segmentation_type)
