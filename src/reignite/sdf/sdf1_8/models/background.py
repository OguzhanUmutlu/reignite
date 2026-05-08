from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_7.models.background import Background as _PrevBackground
from ....utils.color import Color


class Background(_PrevBackground):
    def __init__(self, background: Color = None):
        if background is None:
            background = Color.from_sdf(".7 .7 .7 1")
        super().__init__(background=background)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Background":
        _base = _PrevBackground.from_sdf(el)
        return cls(background=_base.background)
