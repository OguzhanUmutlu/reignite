from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_8.models.placement_frame import PlacementFrame as _PrevPlacementFrame


class PlacementFrame(_PrevPlacementFrame):
    def __init__(self, placement_frame: str = ""):
        super().__init__(placement_frame=placement_frame)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "PlacementFrame":
        _base = _PrevPlacementFrame.from_sdf(el)
        return cls(placement_frame=_base.placement_frame)
