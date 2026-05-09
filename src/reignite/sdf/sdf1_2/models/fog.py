from __future__ import annotations

from xml.etree import ElementTree as ET

from .color import Color
from .density import Density
from .end import End
from .start import Start
from .type import Type
from ...sdf1_0.models.fog import Fog as _PrevFog


class Fog(_PrevFog):
    def __init__(
            self,
            color: "Color" = None,
            type: "Type" = None,
            start: "Start" = None,
            end: "End" = None,
            density: "Density" = None
    ):
        super().__init__(type=type, start=start, end=end, density=density)
        self.color = color

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.color is not None:
            el.append(self.color.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Fog":
        _base = _PrevFog.from_sdf(el)
        _c_color = el.find("color")
        _color = Color.from_sdf(_c_color) if _c_color is not None else None
        return cls(color=_color, type=_base.type, start=_base.start, end=_base.end, density=_base.density)
