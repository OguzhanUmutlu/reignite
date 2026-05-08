from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_0.models.box import Box as _PrevBox
from .size import Size


class Box(_PrevBox):
    def __init__(self, size: "Size" = None):
        super().__init__(size=size)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Box":
        _base = _PrevBox.from_sdf(el)
        return cls(size=_base.size)
