from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_0.models.background import Background as _PrevBackground
from ....utils.color import Color


class Background(_PrevBackground):
    def __init__(self, background: Color = None):
        if background is None:
            background = Color.from_sdf(".7 .7 .7 1")
        super().__init__()
        self.background = background

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.background is not None:
            el.text = self.background.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Background":
        _text = el.text or ".7 .7 .7 1"
        _background = Color.from_sdf(_text)
        return cls(background=_background)
