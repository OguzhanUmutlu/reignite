from __future__ import annotations

from xml.etree import ElementTree as ET

from .filename import Filename
from .scale import Scale
from ...sdf1_6.models.skin import Skin as _PrevSkin


class Skin(_PrevSkin):
    def __init__(self, filename: "Filename" = None, scale: "Scale" = None):
        super().__init__(filename=filename, scale=scale)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Skin":
        _base = _PrevSkin.from_sdf(el)
        return cls(filename=_base.filename, scale=_base.scale)
