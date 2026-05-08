from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_6.models.color_start import ColorStart as _PrevColorStart
from ....utils.color import Color


class ColorStart(_PrevColorStart):
    def __init__(self, color_start: Color = None):
        if color_start is None:
            color_start = Color.from_sdf("1 1 1 1")
        super().__init__(color_start=color_start)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "ColorStart":
        _base = _PrevColorStart.from_sdf(el)
        return cls(color_start=_base.color_start)
