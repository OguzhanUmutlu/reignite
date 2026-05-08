from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_5.models.specular import Specular as _PrevSpecular
from ....utils.color import Color


class Specular(_PrevSpecular):
    def __init__(self, specular: Color = None):
        if specular is None:
            specular = Color.from_sdf("0 0 0 1")
        super().__init__(specular=specular)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Specular":
        _base = _PrevSpecular.from_sdf(el)
        return cls(specular=_base.specular)
