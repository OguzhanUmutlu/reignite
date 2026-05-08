from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_11.models.loop import Loop as _PrevLoop


class Loop(_PrevLoop):
    def __init__(self, loop: bool = False):
        super().__init__(loop=loop)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Loop":
        _base = _PrevLoop.from_sdf(el)
        return cls(loop=_base.loop)
