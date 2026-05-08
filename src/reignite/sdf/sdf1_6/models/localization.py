from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class Localization(Model):
    def __init__(self, localization: str = "CUSTOM"):
        self.localization = localization

    def to_sdf(self) -> ET.Element:
        el = ET.Element("localization")
        if self.localization is not None:
            el.text = self.localization
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Localization":
        _text = el.text or "CUSTOM"
        _localization = _text
        return cls(localization=_localization)
