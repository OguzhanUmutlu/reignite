from __future__ import annotations

from xml.etree import ElementTree as ET

from .constant import Constant
from .linear import Linear
from .quadratic import Quadratic
from .range import Range
from ...sdf1_10.models.attenuation import Attenuation as _PrevAttenuation


class Attenuation(_PrevAttenuation):
    def __init__(
            self,
            range: "Range" = None,
            linear: "Linear" = None,
            constant: "Constant" = None,
            quadratic: "Quadratic" = None
    ):
        super().__init__(range=range, linear=linear, constant=constant, quadratic=quadratic)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Attenuation":
        _base = _PrevAttenuation.from_sdf(el)
        return cls(range=_base.range, linear=_base.linear, constant=_base.constant, quadratic=_base.quadratic)
