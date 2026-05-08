from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class Grid(Model):
    def __init__(self, enabled: bool = True):
        self.enabled = enabled

    def to_sdf(self) -> ET.Element:
        el = ET.Element("grid")
        if self.enabled is not None:
            el.set("enabled", str(self.enabled).lower())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Grid":
        _enabled = el.get("enabled", True).strip().lower() == 'true'
        return cls(enabled=_enabled)
