from __future__ import annotations

from typing import List
from xml.etree import ElementTree as ET

from .material import Material
from .width import Width
from ...sdf1_4.models.point import Point as _PrevPoint
from ...sdf1_4.models.road import Road as _PrevRoad
from ....utils.vector2d import Vector2d


class Point(_PrevPoint):
    def __init__(self, point: Vector2d = None):
        if point is None:
            point = Vector2d.from_sdf("0 0")
        super().__init__(point=point)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Point":
        _base = _PrevPoint.from_sdf(el)
        return cls(point=_base.point)


class Road(_PrevRoad):
    def __init__(
            self,
            name: str = "__default__",
            material: "Material" = None,
            width: "Width" = None,
            point: List["Point"] = None
    ):
        super().__init__(name=name, width=width, point=point)
        self.material = material

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.material is not None:
            el.append(self.material.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Road":
        _base = _PrevRoad.from_sdf(el)
        _c_material = el.find("material")
        _material = Material.from_sdf(_c_material) if _c_material is not None else None
        return cls(name=_base.name, material=_material, width=_base.width, point=_base.point)
