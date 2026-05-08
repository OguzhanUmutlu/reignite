from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class CubemapUri(Model):
    def __init__(self, cubemap_uri: str = ""):
        self.cubemap_uri = cubemap_uri

    def to_sdf(self) -> ET.Element:
        el = ET.Element("cubemap_uri")
        if self.cubemap_uri is not None:
            el.text = self.cubemap_uri
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "CubemapUri":
        _text = el.text or ""
        _cubemap_uri = _text
        return cls(cubemap_uri=_cubemap_uri)
