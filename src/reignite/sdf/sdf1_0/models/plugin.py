from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class Plugin(Model):
    def __init__(self, name: str = "__default__", filename: str = "__default__"):
        self.name = name
        self.filename = filename

    def to_sdf(self) -> ET.Element:
        el = ET.Element("plugin")
        if self.name is not None:
            el.set("name", self.name)
        if self.filename is not None:
            el.set("filename", self.filename)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Plugin":
        _name = el.get("name", "__default__")
        _filename = el.get("filename", "__default__")
        return cls(name=_name, filename=_filename)
