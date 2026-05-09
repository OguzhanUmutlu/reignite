from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_0.models.parent import Parent as _PrevParent


class Parent(_PrevParent):
    def __init__(self, parent: str = "__default__"):
        super().__init__()
        self.parent = parent

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.parent is not None:
            el.text = self.parent
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Parent":
        _text = el.text or "__default__"
        _parent = _text
        return cls(parent=_parent)
