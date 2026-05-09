from __future__ import annotations

from xml.etree import ElementTree as ET

from .constant import Constant
from .linear import Linear
from .quadratic import Quadratic
from .range import Range
from ..model import Model


class Attenuation(Model):
    def __init__(
            self,
            range: "Range" = None,
            linear: "Linear" = None,
            constant: "Constant" = None,
            quadratic: "Quadratic" = None
    ):
        self.range = range
        self.linear = linear
        self.constant = constant
        self.quadratic = quadratic

    def to_sdf(self) -> ET.Element:
        el = ET.Element("attenuation")
        if self.range is not None:
            el.append(self.range.to_sdf())
        if self.linear is not None:
            el.append(self.linear.to_sdf())
        if self.constant is not None:
            el.append(self.constant.to_sdf())
        if self.quadratic is not None:
            el.append(self.quadratic.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Attenuation":
        _c_range = el.find("range")
        _range = Range.from_sdf(_c_range) if _c_range is not None else None
        _c_linear = el.find("linear")
        _linear = Linear.from_sdf(_c_linear) if _c_linear is not None else None
        _c_constant = el.find("constant")
        _constant = Constant.from_sdf(_c_constant) if _c_constant is not None else None
        _c_quadratic = el.find("quadratic")
        _quadratic = Quadratic.from_sdf(_c_quadratic) if _c_quadratic is not None else None
        return cls(range=_range, linear=_linear, constant=_constant, quadratic=_quadratic)
