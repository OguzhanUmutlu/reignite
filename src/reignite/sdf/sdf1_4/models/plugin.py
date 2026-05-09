from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_3.models.plugin import Plugin as _PrevPlugin


class Plugin(_PrevPlugin):
    def __init__(self, name: str = "__default__", filename: str = "__default__"):
        super().__init__(name=name, filename=filename)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Plugin":
        _base = _PrevPlugin.from_sdf(el)
        return cls(name=_base.name, filename=_base.filename)
