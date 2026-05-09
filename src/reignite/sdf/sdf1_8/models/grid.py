from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_7.models.grid import Grid as _PrevGrid


class Grid(_PrevGrid):
    def __init__(self, grid: bool = True):
        super().__init__(grid=grid)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Grid":
        _base = _PrevGrid.from_sdf(el)
        return cls(grid=_base.grid)
