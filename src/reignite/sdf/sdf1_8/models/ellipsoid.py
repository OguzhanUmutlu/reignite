from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from .radii import Radii


class Ellipsoid(Model):
    def __init__(self, radii: "Radii" = None):
        self.radii = radii

    def to_sdf(self) -> ET.Element:
        el = ET.Element("ellipsoid")
        if self.radii is not None:
            el.append(self.radii.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Ellipsoid":
        _c_radii = el.find("radii")
        _radii = Radii.from_sdf(_c_radii) if _c_radii is not None else None
        return cls(radii=_radii)
