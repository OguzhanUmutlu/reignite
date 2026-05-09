from __future__ import annotations

from xml.etree import ElementTree as ET

from .collision_detector import CollisionDetector
from .solver import Solver
from ...sdf1_9.models.dart import Dart as _PrevDart


class Dart(_PrevDart):
    def __init__(self, solver: "Solver" = None, collision_detector: "CollisionDetector" = None):
        super().__init__(solver=solver, collision_detector=collision_detector)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Dart":
        _base = _PrevDart.from_sdf(el)
        return cls(solver=_base.solver, collision_detector=_base.collision_detector)
