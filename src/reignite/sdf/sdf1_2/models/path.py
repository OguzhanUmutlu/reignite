from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class Path(Model):
    def __init__(self, path: str = "__default__"):
        self.path = path

    def to_sdf(self) -> ET.Element:
        el = ET.Element("path")
        if self.path is not None:
            el.text = self.path
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Path":
        _text = el.text or "__default__"
        _path = _text
        return cls(path=_path)
