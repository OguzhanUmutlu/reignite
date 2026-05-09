from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_9.models.always_on import AlwaysOn as _PrevAlwaysOn


class AlwaysOn(_PrevAlwaysOn):
    def __init__(self, always_on: bool = False):
        super().__init__(always_on=always_on)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "AlwaysOn":
        _base = _PrevAlwaysOn.from_sdf(el)
        return cls(always_on=_base.always_on)
