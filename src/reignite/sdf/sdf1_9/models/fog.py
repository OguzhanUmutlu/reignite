from __future__ import annotations

from xml.etree import ElementTree as ET

from .color import Color
from .density import Density
from .end import End
from .start import Start
from ...sdf1_8.models.fog import Fog as _PrevFog
from ...sdf1_8.models.type import Type as _PrevType


class Type(_PrevType):
    def __init__(self, type: str = "none"):
        super().__init__(type=type)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Type":
        _base = _PrevType.from_sdf(el)
        return cls(type=_base.type)


class Fog(_PrevFog):
    def __init__(
            self,
            color: "Color" = None,
            type: "Type" = None,
            start: "Start" = None,
            end: "End" = None,
            density: "Density" = None
    ):
        super().__init__(color=color, type=type, start=start, end=end, density=density)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Fog":
        _base = _PrevFog.from_sdf(el)
        return cls(color=_base.color, type=_base.type, start=_base.start, end=_base.end, density=_base.density)
