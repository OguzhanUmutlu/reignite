from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_10.models.scale_to_hfov import ScaleToHfov as _PrevScaleToHfov


class ScaleToHfov(_PrevScaleToHfov):
    def __init__(self, scale_to_hfov: bool = True):
        super().__init__(scale_to_hfov=scale_to_hfov)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "ScaleToHfov":
        _base = _PrevScaleToHfov.from_sdf(el)
        return cls(scale_to_hfov=_base.scale_to_hfov)
