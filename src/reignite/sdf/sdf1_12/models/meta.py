from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_11.models.meta import Meta as _PrevMeta
from .layer import Layer


class Meta(_PrevMeta):
    def __init__(self, layer: "Layer" = None):
        super().__init__(layer=layer)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Meta":
        _base = _PrevMeta.from_sdf(el)
        return cls(layer=_base.layer)
