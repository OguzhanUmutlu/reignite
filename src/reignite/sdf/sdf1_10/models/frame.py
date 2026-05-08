from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_9.models.frame import Frame as _PrevFrame


class Frame(_PrevFrame):
    def __init__(self, frame: str = "child"):
        super().__init__(frame=frame)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Frame":
        _base = _PrevFrame.from_sdf(el)
        return cls(frame=_base.frame)
