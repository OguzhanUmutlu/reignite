from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class AutoInertiaParams(Model):
    def __init__(self):
        pass

    def to_sdf(self) -> ET.Element:
        el = ET.Element("auto_inertia_params")
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "AutoInertiaParams":
        return cls()
