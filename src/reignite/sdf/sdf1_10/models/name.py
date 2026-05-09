from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_9.models.name import Name as _PrevName


class Name(_PrevName):
    def __init__(self, name: str = "__default__"):
        super().__init__(name=name)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Name":
        _base = _PrevName.from_sdf(el)
        return cls(name=_base.name)
