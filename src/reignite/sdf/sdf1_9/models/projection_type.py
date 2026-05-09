from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_8.models.projection_type import ProjectionType as _PrevProjectionType


class ProjectionType(_PrevProjectionType):
    def __init__(self, projection_type: str = "perspective"):
        super().__init__(projection_type=projection_type)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "ProjectionType":
        _base = _PrevProjectionType.from_sdf(el)
        return cls(projection_type=_base.projection_type)
