from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_6.models.stiffness import Stiffness as _PrevStiffness
from ...sdf1_6.models.dissipation import Dissipation as _PrevDissipation
from ...sdf1_6.models.limit import Limit as _PrevLimit
from .lower import Lower
from .upper import Upper
from .effort import Effort
from .velocity import Velocity


import math
import sys

def _parse_int32(raw: str) -> int:
    v = int(raw)
    if not (-2147483648 <= v <= 2147483647):
        raise ValueError(f"int32 out of range: {v}")
    return v


def _parse_uint32(raw: str) -> int:
    v = int(raw)
    if not (0 <= v <= 4294967295):
        raise ValueError(f"uint32 out of range: {v}")
    return v


def _parse_double(raw: str) -> float:
    v = float(raw)
    if not math.isfinite(v) or abs(v) > 1.7976931348623157e+308:
        raise ValueError(f"double out of range: {raw}")
    return v



class Stiffness(_PrevStiffness):
    def __init__(self, stiffness: float = 100.0):
        super().__init__(stiffness=stiffness)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Stiffness":
        _base = _PrevStiffness.from_sdf(el)
        return cls(stiffness=_base.stiffness)


class Dissipation(_PrevDissipation):
    def __init__(self, dissipation: float = 1.0):
        super().__init__(dissipation=dissipation)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Dissipation":
        _base = _PrevDissipation.from_sdf(el)
        return cls(dissipation=_base.dissipation)


class Limit(_PrevLimit):
    def __init__(
        self,
        lower: "Lower" = None,
        upper: "Upper" = None,
        effort: "Effort" = None,
        velocity: "Velocity" = None,
        stiffness: "Stiffness" = None,
        dissipation: "Dissipation" = None
    ):
        super().__init__()
        self.lower = lower
        self.upper = upper
        self.effort = effort
        self.velocity = velocity
        self.stiffness = stiffness
        self.dissipation = dissipation

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
        if self.stiffness is not None:
            el.append(self.stiffness.to_sdf())
        if self.dissipation is not None:
            el.append(self.dissipation.to_sdf())
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
        _c_stiffness = el.find("stiffness")
        _stiffness = Stiffness.from_sdf(_c_stiffness) if _c_stiffness is not None else None
        _c_dissipation = el.find("dissipation")
        _dissipation = Dissipation.from_sdf(_c_dissipation) if _c_dissipation is not None else None
        return cls(lower=_lower, upper=_upper, effort=_effort, velocity=_velocity, stiffness=_stiffness, dissipation=_dissipation)
