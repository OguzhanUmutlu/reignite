from __future__ import annotations

from xml.etree import ElementTree as ET

from .horizontal import Horizontal
from .vertical import Vertical
from ...sdf1_11.models.position_sensing import PositionSensing as _PrevPositionSensing


class PositionSensing(_PrevPositionSensing):
    def __init__(self, horizontal: "Horizontal" = None, vertical: "Vertical" = None):
        super().__init__(horizontal=horizontal, vertical=vertical)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "PositionSensing":
        _base = _PrevPositionSensing.from_sdf(el)
        return cls(horizontal=_base.horizontal, vertical=_base.vertical)
