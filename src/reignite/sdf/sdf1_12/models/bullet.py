from __future__ import annotations

from xml.etree import ElementTree as ET

from .constraints import Constraints
from .solver import Solver
from ...sdf1_11.models.bullet import Bullet as _PrevBullet


class Bullet(_PrevBullet):
    def __init__(self, solver: "Solver" = None, constraints: "Constraints" = None):
        super().__init__(solver=solver, constraints=constraints)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Bullet":
        _base = _PrevBullet.from_sdf(el)
        return cls(solver=_base.solver, constraints=_base.constraints)
