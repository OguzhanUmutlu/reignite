from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_10.models.parent import Parent as _PrevParent


class Parent(_PrevParent):
    def __init__(self, parent: str = "__default__"):
        super().__init__(parent=parent)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Parent":
        _base = _PrevParent.from_sdf(el)
        return cls(parent=_base.parent)
