from __future__ import annotations

from xml.etree import ElementTree as ET

from .max_angle import MaxAngle
from .min_angle import MinAngle
from .resolution import Resolution
from .samples import Samples
from ...sdf1_2.models.vertical import Vertical as _PrevVertical


class Vertical(_PrevVertical):
    def __init__(
            self,
            samples: "Samples" = None,
            resolution: "Resolution" = None,
            min_angle: "MinAngle" = None,
            max_angle: "MaxAngle" = None
    ):
        super().__init__(samples=samples, resolution=resolution, min_angle=min_angle, max_angle=max_angle)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Vertical":
        _base = _PrevVertical.from_sdf(el)
        return cls(samples=_base.samples, resolution=_base.resolution, min_angle=_base.min_angle,
                   max_angle=_base.max_angle)
