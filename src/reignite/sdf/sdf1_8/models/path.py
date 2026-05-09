from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_7.models.path import Path as _PrevPath


class Path(_PrevPath):
    def __init__(self, path: str = "__default__"):
        super().__init__(path=path)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Path":
        _base = _PrevPath.from_sdf(el)
        return cls(path=_base.path)
