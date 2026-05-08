from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_9.models.horizontal import Horizontal as _PrevHorizontal
from .noise import Noise


class Horizontal(_PrevHorizontal):
    def __init__(self, noise: "Noise" = None):
        super().__init__(noise=noise)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Horizontal":
        _base = _PrevHorizontal.from_sdf(el)
        return cls(noise=_base.noise)
