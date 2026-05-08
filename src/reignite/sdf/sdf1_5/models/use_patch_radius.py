from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class UsePatchRadius(Model):
    def __init__(self, use_patch_radius: bool = True):
        self.use_patch_radius = use_patch_radius

    def to_sdf(self) -> ET.Element:
        el = ET.Element("use_patch_radius")
        if self.use_patch_radius is not None:
            el.text = str(self.use_patch_radius).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "UsePatchRadius":
        _text = el.text or True
        _use_patch_radius = _text.strip().lower() == 'true'
        return cls(use_patch_radius=_use_patch_radius)
