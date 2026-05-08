from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from .layer import Layer


class Meta(Model):
    def __init__(self, layer: "Layer" = None):
        self.layer = layer

    def to_sdf(self) -> ET.Element:
        el = ET.Element("meta")
        if self.layer is not None:
            el.append(self.layer.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Meta":
        _c_layer = el.find("layer")
        _layer = Layer.from_sdf(_c_layer) if _c_layer is not None else None
        return cls(layer=_layer)
