from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class ProjectionType(Model):
    def __init__(self, projection_type: str = "perspective"):
        self.projection_type = projection_type

    def to_sdf(self) -> ET.Element:
        el = ET.Element("projection_type")
        if self.projection_type is not None:
            el.text = self.projection_type
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "ProjectionType":
        _text = el.text or "perspective"
        _projection_type = _text
        return cls(projection_type=_projection_type)
