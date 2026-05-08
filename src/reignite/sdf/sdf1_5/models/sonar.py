from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_4.models.sonar import Sonar as _PrevSonar
from .min import Min
from .max import Max
from .radius import Radius


class Sonar(_PrevSonar):
    def __init__(self, min: "Min" = None, max: "Max" = None, radius: "Radius" = None):
        super().__init__(min=min, max=max, radius=radius)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Sonar":
        _base = _PrevSonar.from_sdf(el)
        return cls(min=_base.min, max=_base.max, radius=_base.radius)
