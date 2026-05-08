from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class WorldFrameOrientation(Model):
    def __init__(self, world_frame_orientation: str = "ENU"):
        self.world_frame_orientation = world_frame_orientation

    def to_sdf(self) -> ET.Element:
        el = ET.Element("world_frame_orientation")
        if self.world_frame_orientation is not None:
            el.text = self.world_frame_orientation
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "WorldFrameOrientation":
        _text = el.text or "ENU"
        _world_frame_orientation = _text
        return cls(world_frame_orientation=_world_frame_orientation)
