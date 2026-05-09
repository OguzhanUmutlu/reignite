from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_10.models.use_patch_radius import UsePatchRadius as _PrevUsePatchRadius


class UsePatchRadius(_PrevUsePatchRadius):
    def __init__(self, use_patch_radius: bool = True):
        super().__init__(use_patch_radius=use_patch_radius)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "UsePatchRadius":
        _base = _PrevUsePatchRadius.from_sdf(el)
        return cls(use_patch_radius=_base.use_patch_radius)
