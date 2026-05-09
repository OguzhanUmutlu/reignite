from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_2.models.filename import Filename as _PrevFilename


class Filename(_PrevFilename):
    def __init__(self, filename: str = "__default__"):
        super().__init__(filename=filename)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Filename":
        _base = _PrevFilename.from_sdf(el)
        return cls(filename=_base.filename)
