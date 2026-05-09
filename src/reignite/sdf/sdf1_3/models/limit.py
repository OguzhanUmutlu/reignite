from __future__ import annotations

from xml.etree import ElementTree as ET

from .effort import Effort
from .lower import Lower
from .upper import Upper
from .velocity import Velocity
from ...sdf1_2.models.limit import Limit as _PrevLimit


class Limit(_PrevLimit):
    def __init__(
            self,
            lower: "Lower" = None,
            upper: "Upper" = None,
            effort: "Effort" = None,
            velocity: "Velocity" = None
    ):
        super().__init__()
        self.lower = lower
        self.upper = upper
        self.effort = effort
        self.velocity = velocity

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.lower is not None:
            el.append(self.lower.to_sdf())
        if self.upper is not None:
            el.append(self.upper.to_sdf())
        if self.effort is not None:
            el.append(self.effort.to_sdf())
        if self.velocity is not None:
            el.append(self.velocity.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Limit":
        _c_lower = el.find("lower")
        _lower = Lower.from_sdf(_c_lower) if _c_lower is not None else None
        _c_upper = el.find("upper")
        _upper = Upper.from_sdf(_c_upper) if _c_upper is not None else None
        _c_effort = el.find("effort")
        _effort = Effort.from_sdf(_c_effort) if _c_effort is not None else None
        _c_velocity = el.find("velocity")
        _velocity = Velocity.from_sdf(_c_velocity) if _c_velocity is not None else None
        return cls(lower=_lower, upper=_upper, effort=_effort, velocity=_velocity)
