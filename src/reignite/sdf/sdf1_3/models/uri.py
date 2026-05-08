from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_2.models.uri import Uri as _PrevUri


class Uri(_PrevUri):
    def __init__(self, uri: str = "__default__"):
        super().__init__(uri=uri)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Uri":
        _base = _PrevUri.from_sdf(el)
        return cls(uri=_base.uri)
