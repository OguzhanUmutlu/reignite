from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from .solver import Solver
from .constraints import Constraints


class Ode(Model):
    def __init__(self, solver: "Solver" = None, constraints: "Constraints" = None):
        self.solver = solver
        self.constraints = constraints

    def to_sdf(self) -> ET.Element:
        el = ET.Element("ode")
        if self.solver is not None:
            el.append(self.solver.to_sdf())
        if self.constraints is not None:
            el.append(self.constraints.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Ode":
        _c_solver = el.find("solver")
        _solver = Solver.from_sdf(_c_solver) if _c_solver is not None else None
        _c_constraints = el.find("constraints")
        _constraints = Constraints.from_sdf(_c_constraints) if _c_constraints is not None else None
        return cls(solver=_solver, constraints=_constraints)
