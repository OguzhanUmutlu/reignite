from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class AllowAutoDisable(Model):
    def __init__(self, allow_auto_disable: bool = True):
        self.allow_auto_disable = allow_auto_disable

    def to_sdf(self) -> ET.Element:
        el = ET.Element("allow_auto_disable")
        if self.allow_auto_disable is not None:
            el.text = str(self.allow_auto_disable).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "AllowAutoDisable":
        _text = el.text or True
        _allow_auto_disable = _text.strip().lower() == 'true'
        return cls(allow_auto_disable=_allow_auto_disable)
