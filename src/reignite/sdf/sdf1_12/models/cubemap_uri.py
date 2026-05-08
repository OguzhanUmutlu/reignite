from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_11.models.cubemap_uri import CubemapUri as _PrevCubemapUri


class CubemapUri(_PrevCubemapUri):
    def __init__(self, cubemap_uri: str = ""):
        super().__init__(cubemap_uri=cubemap_uri)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "CubemapUri":
        _base = _PrevCubemapUri.from_sdf(el)
        return cls(cubemap_uri=_base.cubemap_uri)
