from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_11.models.ellipsoid import Ellipsoid as _PrevEllipsoid
from .radii import Radii


class Ellipsoid(_PrevEllipsoid):
    def __init__(self, radii: "Radii" = None):
        super().__init__(radii=radii)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Ellipsoid":
        _base = _PrevEllipsoid.from_sdf(el)
        return cls(radii=_base.radii)
