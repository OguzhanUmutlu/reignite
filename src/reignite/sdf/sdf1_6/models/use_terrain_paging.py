from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_5.models.use_terrain_paging import UseTerrainPaging as _PrevUseTerrainPaging


class UseTerrainPaging(_PrevUseTerrainPaging):
    def __init__(self, use_terrain_paging: bool = False):
        super().__init__(use_terrain_paging=use_terrain_paging)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "UseTerrainPaging":
        _base = _PrevUseTerrainPaging.from_sdf(el)
        return cls(use_terrain_paging=_base.use_terrain_paging)
