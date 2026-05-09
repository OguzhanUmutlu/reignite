from __future__ import annotations

from xml.etree import ElementTree as ET

from .dynamics import Dynamics
from .limit import Limit
from .xyz import Xyz
from ...sdf1_0.models.axis import Axis as _PrevAxis


class Axis(_PrevAxis):
    def __init__(self, xyz: "Xyz" = None, dynamics: "Dynamics" = None, limit: "Limit" = None):
        super().__init__(xyz=xyz, dynamics=dynamics, limit=limit)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Axis":
        _base = _PrevAxis.from_sdf(el)
        return cls(xyz=_base.xyz, dynamics=_base.dynamics, limit=_base.limit)
