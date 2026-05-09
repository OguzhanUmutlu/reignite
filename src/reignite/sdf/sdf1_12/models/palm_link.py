from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_11.models.palm_link import PalmLink as _PrevPalmLink


class PalmLink(_PrevPalmLink):
    def __init__(self, palm_link: str = "__default__"):
        super().__init__(palm_link=palm_link)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "PalmLink":
        _base = _PrevPalmLink.from_sdf(el)
        return cls(palm_link=_base.palm_link)
