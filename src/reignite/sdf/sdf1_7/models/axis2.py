from __future__ import annotations

from xml.etree import ElementTree as ET

from .dynamics import Dynamics
from .initial_position import InitialPosition
from .limit import Limit
from .xyz import Xyz
from ...sdf1_6.models.axis2 import Axis2 as _PrevAxis2


class Axis2(_PrevAxis2):
    def __init__(
            self,
            initial_position: "InitialPosition" = None,
            xyz: "Xyz" = None,
            dynamics: "Dynamics" = None,
            limit: "Limit" = None
    ):
        super().__init__(initial_position=initial_position, xyz=xyz, dynamics=dynamics, limit=limit)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Axis2":
        _base = _PrevAxis2.from_sdf(el)
        return cls(initial_position=_base.initial_position, xyz=_base.xyz, dynamics=_base.dynamics, limit=_base.limit)
