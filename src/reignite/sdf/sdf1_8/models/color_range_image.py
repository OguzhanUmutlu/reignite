from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_7.models.color_range_image import ColorRangeImage as _PrevColorRangeImage


class ColorRangeImage(_PrevColorRangeImage):
    def __init__(self, color_range_image: str = ""):
        super().__init__(color_range_image=color_range_image)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "ColorRangeImage":
        _base = _PrevColorRangeImage.from_sdf(el)
        return cls(color_range_image=_base.color_range_image)
