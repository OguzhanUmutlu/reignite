from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class Grid(Model):
    def __init__(self, grid: bool = True):
        self.grid = grid

    def to_sdf(self) -> ET.Element:
        el = ET.Element("grid")
        if self.grid is not None:
            el.text = str(self.grid).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Grid":
        _text = el.text or True
        _grid = _text.strip().lower() == 'true'
        return cls(grid=_grid)
