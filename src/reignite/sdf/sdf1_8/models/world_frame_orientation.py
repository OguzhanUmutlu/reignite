from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_7.models.world_frame_orientation import WorldFrameOrientation as _PrevWorldFrameOrientation


class WorldFrameOrientation(_PrevWorldFrameOrientation):
    def __init__(self, world_frame_orientation: str = "ENU"):
        super().__init__(world_frame_orientation=world_frame_orientation)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "WorldFrameOrientation":
        _base = _PrevWorldFrameOrientation.from_sdf(el)
        return cls(world_frame_orientation=_base.world_frame_orientation)
