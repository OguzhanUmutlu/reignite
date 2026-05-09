from __future__ import annotations

from xml.etree import ElementTree as ET

from .collision_detector import CollisionDetector
from .solver import Solver
from ..model import Model


class Dart(Model):
    def __init__(self, solver: "Solver" = None, collision_detector: "CollisionDetector" = None):
        self.solver = solver
        self.collision_detector = collision_detector

    def to_sdf(self) -> ET.Element:
        el = ET.Element("dart")
        if self.solver is not None:
            el.append(self.solver.to_sdf())
        if self.collision_detector is not None:
            el.append(self.collision_detector.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Dart":
        _c_solver = el.find("solver")
        _solver = Solver.from_sdf(_c_solver) if _c_solver is not None else None
        _c_collision_detector = el.find("collision_detector")
        _collision_detector = CollisionDetector.from_sdf(
            _c_collision_detector) if _c_collision_detector is not None else None
        return cls(solver=_solver, collision_detector=_collision_detector)
