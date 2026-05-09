from __future__ import annotations

from xml.etree import ElementTree as ET

from .cols import Cols
from .rows import Rows
from .step import Step
from .type import Type
from ...sdf1_7.models.distribution import Distribution as _PrevDistribution


class Distribution(_PrevDistribution):
    def __init__(
            self,
            type: "Type" = None,
            rows: "Rows" = None,
            cols: "Cols" = None,
            step: "Step" = None
    ):
        super().__init__(type=type, rows=rows, cols=cols, step=step)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Distribution":
        _base = _PrevDistribution.from_sdf(el)
        return cls(type=_base.type, rows=_base.rows, cols=_base.cols, step=_base.step)
