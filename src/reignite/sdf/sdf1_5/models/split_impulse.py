from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_4.models.split_impulse import SplitImpulse as _PrevSplitImpulse


class SplitImpulse(_PrevSplitImpulse):
    def __init__(self, split_impulse: bool = True):
        super().__init__(split_impulse=split_impulse)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "SplitImpulse":
        _base = _PrevSplitImpulse.from_sdf(el)
        return cls(split_impulse=_base.split_impulse)
