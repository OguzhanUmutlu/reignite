from __future__ import annotations

from xml.etree import ElementTree as ET

from .angular import Angular
from .linear import Linear
from ..model import Model


class VelocityDecay(Model):
    def __init__(self, linear: "Linear" = None, angular: "Angular" = None):
        self.linear = linear
        self.angular = angular

    def to_sdf(self) -> ET.Element:
        el = ET.Element("velocity_decay")
        if self.linear is not None:
            el.append(self.linear.to_sdf())
        if self.angular is not None:
            el.append(self.angular.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "VelocityDecay":
        _c_linear = el.find("linear")
        _linear = Linear.from_sdf(_c_linear) if _c_linear is not None else None
        _c_angular = el.find("angular")
        _angular = Angular.from_sdf(_c_angular) if _c_angular is not None else None
        return cls(linear=_linear, angular=_angular)
