from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_6.models.ambient import Ambient as _PrevAmbient
from ....utils.color import Color


class Ambient(_PrevAmbient):
    def __init__(self, ambient: Color = None):
        if ambient is None:
            ambient = Color.from_sdf("0 0 0 1")
        super().__init__(ambient=ambient)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Ambient":
        _base = _PrevAmbient.from_sdf(el)
        return cls(ambient=_base.ambient)
