from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class Filename(Model):
    def __init__(self, filename: str = "__default__"):
        self.filename = filename

    def to_sdf(self) -> ET.Element:
        el = ET.Element("filename")
        if self.filename is not None:
            el.text = self.filename
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Filename":
        _text = el.text or "__default__"
        _filename = _text
        return cls(filename=_filename)
