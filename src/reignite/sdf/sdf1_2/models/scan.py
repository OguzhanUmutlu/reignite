from __future__ import annotations

from xml.etree import ElementTree as ET

from .horizontal import Horizontal
from .vertical import Vertical
from ...sdf1_0.models.scan import Scan as _PrevScan


class Scan(_PrevScan):
    def __init__(self, horizontal: "Horizontal" = None, vertical: "Vertical" = None):
        super().__init__(horizontal=horizontal, vertical=vertical)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Scan":
        _base = _PrevScan.from_sdf(el)
        return cls(horizontal=_base.horizontal, vertical=_base.vertical)
