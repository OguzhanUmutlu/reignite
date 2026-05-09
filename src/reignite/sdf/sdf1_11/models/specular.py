from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_10.models.specular import Specular as _PrevSpecular
from ....utils.color import Color


class Specular(_PrevSpecular):
    def __init__(self, specular: Color = None):
        if specular is None:
            specular = Color.from_sdf("0 0 0 1")
        super().__init__()
        self.specular = specular

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.specular is not None:
            el.text = self.specular.to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Specular":
        _text = el.text or "0 0 0 1"
        _specular = Color.from_sdf(_text)
        return cls(specular=_specular)
