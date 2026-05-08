from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_10.models.axis import Axis as _PrevAxis
from .mimic import Mimic
from .xyz import Xyz
from .dynamics import Dynamics
from .limit import Limit


class Axis(_PrevAxis):
    def __init__(
        self,
        mimic: "Mimic" = None,
        xyz: "Xyz" = None,
        dynamics: "Dynamics" = None,
        limit: "Limit" = None
    ):
        super().__init__(xyz=xyz, dynamics=dynamics, limit=limit)
        self.mimic = mimic

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.mimic is not None:
            el.append(self.mimic.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Axis":
        _base = _PrevAxis.from_sdf(el)
        _c_mimic = el.find("mimic")
        _mimic = Mimic.from_sdf(_c_mimic) if _c_mimic is not None else None
        return cls(mimic=_mimic, xyz=_base.xyz, dynamics=_base.dynamics, limit=_base.limit)
