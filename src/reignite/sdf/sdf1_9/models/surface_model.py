from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_8.models.surface_model import SurfaceModel as _PrevSurfaceModel


class SurfaceModel(_PrevSurfaceModel):
    def __init__(self, surface_model: str = "EARTH_WGS84"):
        super().__init__(surface_model=surface_model)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "SurfaceModel":
        _base = _PrevSurfaceModel.from_sdf(el)
        return cls(surface_model=_base.surface_model)
