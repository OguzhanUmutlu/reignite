from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_9.models.solver_type import SolverType as _PrevSolverType


class SolverType(_PrevSolverType):
    def __init__(self, solver_type: str = "dantzig"):
        super().__init__(solver_type=solver_type)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "SolverType":
        _base = _PrevSolverType.from_sdf(el)
        return cls(solver_type=_base.solver_type)
