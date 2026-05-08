from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..model import Model
from ...sdf1_0.models.road import Road as _PrevRoad
from .width import Width
from .point import Point


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
