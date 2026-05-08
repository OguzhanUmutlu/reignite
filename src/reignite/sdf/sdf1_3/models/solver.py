from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_2.models.solver import Solver as _PrevSolver
from .type import Type
from .dt import Dt
from .iters import Iters
from .precon_iters import PreconIters
from .sor import Sor


class Solver(_PrevSolver):
    def __init__(
        self,
        type: "Type" = None,
        dt: "Dt" = None,
        iters: "Iters" = None,
        precon_iters: "PreconIters" = None,
        sor: "Sor" = None
    ):
        super().__init__(type=type, dt=dt, iters=iters, precon_iters=precon_iters, sor=sor)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Solver":
        _base = _PrevSolver.from_sdf(el)
        return cls(type=_base.type, dt=_base.dt, iters=_base.iters, precon_iters=_base.precon_iters, sor=_base.sor)
