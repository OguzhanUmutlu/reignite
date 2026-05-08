from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_4.models.fog import Fog as _PrevFog
from .color import Color
from .type import Type
from .start import Start
from .end import End
from .density import Density


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
