from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_6.models.sphere import Sphere as _PrevSphere
from .radius import Radius


class Sphere(_PrevSphere):
    def __init__(self, radius: "Radius" = None):
        super().__init__(radius=radius)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Sphere":
        _base = _PrevSphere.from_sdf(el)
        return cls(radius=_base.radius)
