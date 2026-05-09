from __future__ import annotations

from xml.etree import ElementTree as ET

from .noise import Noise
from ...sdf1_9.models.horizontal import Horizontal as _PrevHorizontal


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
