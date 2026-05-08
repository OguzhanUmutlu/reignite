from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class SurfaceModel(Model):
    def __init__(self, surface_model: str = "EARTH_WGS84"):
        self.surface_model = surface_model

    def to_sdf(self) -> ET.Element:
        el = ET.Element("surface_model")
        if self.surface_model is not None:
            el.text = self.surface_model
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "SurfaceModel":
        _text = el.text or "EARTH_WGS84"
        _surface_model = _text
        return cls(surface_model=_surface_model)
