from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_10.models.vertical import Vertical as _PrevVertical
from .noise import Noise


class Vertical(_PrevVertical):
    def __init__(self, noise: "Noise" = None):
        super().__init__(noise=noise)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Vertical":
        _base = _PrevVertical.from_sdf(el)
        return cls(noise=_base.noise)
