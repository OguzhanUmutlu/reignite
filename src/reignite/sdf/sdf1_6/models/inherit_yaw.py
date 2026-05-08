from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class InheritYaw(Model):
    def __init__(self, inherit_yaw: bool = False):
        self.inherit_yaw = inherit_yaw

    def to_sdf(self) -> ET.Element:
        el = ET.Element("inherit_yaw")
        if self.inherit_yaw is not None:
            el.text = str(self.inherit_yaw).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "InheritYaw":
        _text = el.text or False
        _inherit_yaw = _text.strip().lower() == 'true'
        return cls(inherit_yaw=_inherit_yaw)
