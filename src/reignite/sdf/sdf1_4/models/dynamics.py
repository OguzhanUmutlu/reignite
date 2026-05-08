from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_3.models.dynamics import Dynamics as _PrevDynamics
from .damping import Damping
from .friction import Friction


class Dynamics(_PrevDynamics):
    def __init__(self, damping: "Damping" = None, friction: "Friction" = None):
        super().__init__(damping=damping, friction=friction)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Dynamics":
        _base = _PrevDynamics.from_sdf(el)
        return cls(damping=_base.damping, friction=_base.friction)
