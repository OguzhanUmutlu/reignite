from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_6.models.child import Child as _PrevChild


class Child(_PrevChild):
    def __init__(self, child: str = "__default__"):
        super().__init__(child=child)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Child":
        _base = _PrevChild.from_sdf(el)
        return cls(child=_base.child)
