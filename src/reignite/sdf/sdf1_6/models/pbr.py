from __future__ import annotations

from xml.etree import ElementTree as ET

from .metal import Metal
from .specular import Specular
from ..model import Model


class Pbr(Model):
    def __init__(self, metal: "Metal" = None, specular: "Specular" = None):
        self.metal = metal
        self.specular = specular

    def to_sdf(self) -> ET.Element:
        el = ET.Element("pbr")
        if self.metal is not None:
            el.append(self.metal.to_sdf())
        if self.specular is not None:
            el.append(self.specular.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Pbr":
        _c_metal = el.find("metal")
        _metal = Metal.from_sdf(_c_metal) if _c_metal is not None else None
        _c_specular = el.find("specular")
        _specular = Specular.from_sdf(_c_specular) if _c_specular is not None else None
        return cls(metal=_metal, specular=_specular)
