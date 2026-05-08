from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_11.models.attenuation import Attenuation as _PrevAttenuation
from .range import Range
from .linear import Linear
from .constant import Constant
from .quadratic import Quadratic


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
