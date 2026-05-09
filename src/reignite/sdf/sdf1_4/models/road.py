from __future__ import annotations

from typing import List
from xml.etree import ElementTree as ET

from .point import Point
from .width import Width
from ...sdf1_3.models.road import Road as _PrevRoad


class Road(_PrevRoad):
    def __init__(
            self,
            name: str = "__default__",
            width: "Width" = None,
            point: List["Point"] = None
    ):
        super().__init__(name=name, width=width, point=point)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Road":
        _base = _PrevRoad.from_sdf(el)
        return cls(name=_base.name, width=_base.width, point=_base.point)
