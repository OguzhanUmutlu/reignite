from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_0.models.grid import Grid as _PrevGrid


class Grid(_PrevGrid):
    def __init__(self, grid: bool = True):
        super().__init__()
        self.grid = grid

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        if self.grid is not None:
            el.text = str(self.grid).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Grid":
        _text = el.text or True
        _grid = _text.strip().lower() == 'true'
        return cls(grid=_grid)
