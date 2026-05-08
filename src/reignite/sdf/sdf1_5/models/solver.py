from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_4.models.solver import Solver as _PrevSolver
from .type import Type
from .min_step_size import MinStepSize
from .iters import Iters
from .sor import Sor


class Solver(_PrevSolver):
    def __init__(
        self,
        type: "Type" = None,
        min_step_size: "MinStepSize" = None,
        iters: "Iters" = None,
        sor: "Sor" = None
    ):
        super().__init__(type=type, min_step_size=min_step_size, iters=iters, sor=sor)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Solver":
        _base = _PrevSolver.from_sdf(el)
        return cls(type=_base.type, min_step_size=_base.min_step_size, iters=_base.iters, sor=_base.sor)
