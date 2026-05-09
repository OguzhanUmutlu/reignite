from __future__ import annotations

from xml.etree import ElementTree as ET

from .dynamics import Dynamics
from .limit import Limit
from .use_parent_model_frame import UseParentModelFrame
from .xyz import Xyz
from ...sdf1_4.models.axis import Axis as _PrevAxis


class Axis(_PrevAxis):
    def __init__(
            self,
            xyz: "Xyz" = None,
            use_parent_model_frame: "UseParentModelFrame" = None,
            dynamics: "Dynamics" = None,
            limit: "Limit" = None
    ):
        super().__init__(xyz=xyz, dynamics=dynamics, limit=limit)
        self.use_parent_model_frame = use_parent_model_frame

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.use_parent_model_frame is not None:
            el.append(self.use_parent_model_frame.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Axis":
        _base = _PrevAxis.from_sdf(el)
        _c_use_parent_model_frame = el.find("use_parent_model_frame")
        _use_parent_model_frame = UseParentModelFrame.from_sdf(
            _c_use_parent_model_frame) if _c_use_parent_model_frame is not None else None
        return cls(xyz=_base.xyz, use_parent_model_frame=_use_parent_model_frame, dynamics=_base.dynamics,
                   limit=_base.limit)
