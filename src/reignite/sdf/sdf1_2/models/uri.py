from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class Uri(Model):
    def __init__(self, uri: str = "__default__"):
        self.uri = uri

    def to_sdf(self) -> ET.Element:
        el = ET.Element("uri")
        if self.uri is not None:
            el.text = self.uri
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Uri":
        _text = el.text or "__default__"
        _uri = _text
        return cls(uri=_uri)
