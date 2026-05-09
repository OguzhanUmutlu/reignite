from __future__ import annotations

from xml.etree import ElementTree as ET

from .geometry import Geometry
from .max import Max
from .min import Min
from .radius import Radius
from ...sdf1_5.models.sonar import Sonar as _PrevSonar


class Sonar(_PrevSonar):
    def __init__(
            self,
            geometry: "Geometry" = None,
            min: "Min" = None,
            max: "Max" = None,
            radius: "Radius" = None
    ):
        super().__init__(min=min, max=max, radius=radius)
        self.geometry = geometry

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.geometry is not None:
            el.append(self.geometry.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Sonar":
        _base = _PrevSonar.from_sdf(el)
        _c_geometry = el.find("geometry")
        _geometry = Geometry.from_sdf(_c_geometry) if _c_geometry is not None else None
        return cls(geometry=_geometry, min=_base.min, max=_base.max, radius=_base.radius)
