from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class UseTerrainPaging(Model):
    def __init__(self, use_terrain_paging: bool = False):
        self.use_terrain_paging = use_terrain_paging

    def to_sdf(self) -> ET.Element:
        el = ET.Element("use_terrain_paging")
        if self.use_terrain_paging is not None:
            el.text = str(self.use_terrain_paging).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "UseTerrainPaging":
        _text = el.text or False
        _use_terrain_paging = _text.strip().lower() == 'true'
        return cls(use_terrain_paging=_use_terrain_paging)
