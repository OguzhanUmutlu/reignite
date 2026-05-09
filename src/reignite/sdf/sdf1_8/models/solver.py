from __future__ import annotations

from xml.etree import ElementTree as ET

from .solver_type import SolverType
from ...sdf1_7.models.solver import Solver as _PrevSolver


class Solver(_PrevSolver):
    def __init__(self, solver_type: "SolverType" = None):
        super().__init__()
        self.solver_type = solver_type

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.solver_type is not None:
            el.append(self.solver_type.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Solver":
        _c_solver_type = el.find("solver_type")
        _solver_type = SolverType.from_sdf(_c_solver_type) if _c_solver_type is not None else None
        return cls(solver_type=_solver_type)
