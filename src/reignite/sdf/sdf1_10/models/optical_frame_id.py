from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_9.models.optical_frame_id import OpticalFrameId as _PrevOpticalFrameId


class OpticalFrameId(_PrevOpticalFrameId):
    def __init__(self, optical_frame_id: str = ""):
        super().__init__(optical_frame_id=optical_frame_id)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "OpticalFrameId":
        _base = _PrevOpticalFrameId.from_sdf(el)
        return cls(optical_frame_id=_base.optical_frame_id)
