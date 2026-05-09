from __future__ import annotations

from xml.etree import ElementTree as ET

from .max import Max
from .min import Min
from .resolution import Resolution
from ...sdf1_6.models.range import Range as _PrevRange


class Range(_PrevRange):
    def __init__(self, min: "Min" = None, max: "Max" = None, resolution: "Resolution" = None):
        super().__init__(min=min, max=max, resolution=resolution)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Range":
        _base = _PrevRange.from_sdf(el)
        return cls(min=_base.min, max=_base.max, resolution=_base.resolution)
