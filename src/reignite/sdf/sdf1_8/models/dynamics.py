from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_7.models.dynamics import Dynamics as _PrevDynamics
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
        super().__init__(damping=damping, friction=friction, spring_reference=spring_reference, spring_stiffness=spring_stiffness)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Dynamics":
        _base = _PrevDynamics.from_sdf(el)
        return cls(damping=_base.damping, friction=_base.friction, spring_reference=_base.spring_reference, spring_stiffness=_base.spring_stiffness)
