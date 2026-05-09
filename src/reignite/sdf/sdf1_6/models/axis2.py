from __future__ import annotations

from xml.etree import ElementTree as ET

from .dynamics import Dynamics
from .initial_position import InitialPosition
from .limit import Limit
from .use_parent_model_frame import UseParentModelFrame
from .xyz import Xyz
from ...sdf1_5.models.axis2 import Axis2 as _PrevAxis2


class Axis2(_PrevAxis2):
    def __init__(
            self,
            initial_position: "InitialPosition" = None,
            xyz: "Xyz" = None,
            use_parent_model_frame: "UseParentModelFrame" = None,
            dynamics: "Dynamics" = None,
            limit: "Limit" = None
    ):
        super().__init__(xyz=xyz, use_parent_model_frame=use_parent_model_frame, dynamics=dynamics, limit=limit)
        self.initial_position = initial_position

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.initial_position is not None:
            el.append(self.initial_position.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Axis2":
        _base = _PrevAxis2.from_sdf(el)
        _c_initial_position = el.find("initial_position")
        _initial_position = InitialPosition.from_sdf(_c_initial_position) if _c_initial_position is not None else None
        return cls(initial_position=_initial_position, xyz=_base.xyz,
                   use_parent_model_frame=_base.use_parent_model_frame, dynamics=_base.dynamics, limit=_base.limit)
