from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class Save(Model):
    def __init__(self, enabled: bool = False, path: str = "__default__"):
        self.enabled = enabled
        self.path = path

    def to_sdf(self) -> ET.Element:
        el = ET.Element("save")
        if self.enabled is not None:
            el.set("enabled", str(self.enabled).lower())
        if self.path is not None:
            el.set("path", self.path)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Save":
        _enabled = el.get("enabled", False).strip().lower() == 'true'
        _path = el.get("path", "__default__")
        return cls(enabled=_enabled, path=_path)
