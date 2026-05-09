from __future__ import annotations

from xml.etree import ElementTree as ET

from .restitution_coefficient import RestitutionCoefficient
from .threshold import Threshold
from ...sdf1_11.models.bounce import Bounce as _PrevBounce


class Bounce(_PrevBounce):
    def __init__(
            self,
            restitution_coefficient: "RestitutionCoefficient" = None,
            threshold: "Threshold" = None
    ):
        super().__init__()
        self.restitution_coefficient = restitution_coefficient
        self.threshold = threshold

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.restitution_coefficient is not None:
            el.append(self.restitution_coefficient.to_sdf())
        if self.threshold is not None:
            el.append(self.threshold.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Bounce":
        _c_restitution_coefficient = el.find("restitution_coefficient")
        _restitution_coefficient = RestitutionCoefficient.from_sdf(
            _c_restitution_coefficient) if _c_restitution_coefficient is not None else None
        _c_threshold = el.find("threshold")
        _threshold = Threshold.from_sdf(_c_threshold) if _c_threshold is not None else None
        return cls(restitution_coefficient=_restitution_coefficient, threshold=_threshold)
