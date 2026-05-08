from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_4.models.dynamics import Dynamics as _PrevDynamics
from .damping import Damping
from .friction import Friction
from .spring_reference import SpringReference
from .spring_stiffness import SpringStiffness


class Dynamics(_PrevDynamics):
    def __init__(
        self,
        damping: "Damping" = None,
        friction: "Friction" = None,
        spring_reference: "SpringReference" = None,
        spring_stiffness: "SpringStiffness" = None
    ):
        super().__init__(damping=damping, friction=friction)
        self.spring_reference = spring_reference
        self.spring_stiffness = spring_stiffness

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.spring_reference is not None:
            el.append(self.spring_reference.to_sdf())
        if self.spring_stiffness is not None:
            el.append(self.spring_stiffness.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Dynamics":
        _base = _PrevDynamics.from_sdf(el)
        _c_spring_reference = el.find("spring_reference")
        _spring_reference = SpringReference.from_sdf(_c_spring_reference) if _c_spring_reference is not None else None
        _c_spring_stiffness = el.find("spring_stiffness")
        _spring_stiffness = SpringStiffness.from_sdf(_c_spring_stiffness) if _c_spring_stiffness is not None else None
        return cls(damping=_base.damping, friction=_base.friction, spring_reference=_spring_reference, spring_stiffness=_spring_stiffness)
