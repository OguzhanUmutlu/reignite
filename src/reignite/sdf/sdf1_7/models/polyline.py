from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..model import Model
from ...sdf1_6.models.polyline import Polyline as _PrevPolyline
from .point import Point
from .height import Height


class Polyline(_PrevPolyline):
    def __init__(self, point: List["Point"] = None, height: "Height" = None):
        super().__init__(point=point, height=height)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Polyline":
        _base = _PrevPolyline.from_sdf(el)
        return cls(point=_base.point, height=_base.height)
