from __future__ import annotations

from xml.etree import ElementTree as ET

from .far import Far
from .near import Near
from ...sdf1_9.models.clip import Clip as _PrevClip


class Clip(_PrevClip):
    def __init__(self, near: "Near" = None, far: "Far" = None):
        super().__init__(near=near, far=far)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Clip":
        _base = _PrevClip.from_sdf(el)
        return cls(near=_base.near, far=_base.far)
