from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class SolverType(Model):
    def __init__(self, solver_type: str = "dantzig"):
        self.solver_type = solver_type

    def to_sdf(self) -> ET.Element:
        el = ET.Element("solver_type")
        if self.solver_type is not None:
            el.text = self.solver_type
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "SolverType":
        _text = el.text or "dantzig"
        _solver_type = _text
        return cls(solver_type=_solver_type)
