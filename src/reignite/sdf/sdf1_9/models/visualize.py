from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_8.models.visualize import Visualize as _PrevVisualize


class Visualize(_PrevVisualize):
    def __init__(self, visualize: bool = False):
        super().__init__(visualize=visualize)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Visualize":
        _base = _PrevVisualize.from_sdf(el)
        return cls(visualize=_base.visualize)
