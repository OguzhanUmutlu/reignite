from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class EnvironmentMap(Model):
    def __init__(self, environment_map: str = ""):
        self.environment_map = environment_map

    def to_sdf(self) -> ET.Element:
        el = ET.Element("environment_map")
        if self.environment_map is not None:
            el.text = self.environment_map
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "EnvironmentMap":
        _text = el.text or ""
        _environment_map = _text
        return cls(environment_map=_environment_map)
