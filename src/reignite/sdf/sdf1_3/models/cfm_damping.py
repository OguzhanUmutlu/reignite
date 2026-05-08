from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class CfmDamping(Model):
    def __init__(self, cfm_damping: bool = False):
        self.cfm_damping = cfm_damping

    def to_sdf(self) -> ET.Element:
        el = ET.Element("cfm_damping")
        if self.cfm_damping is not None:
            el.text = str(self.cfm_damping).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "CfmDamping":
        _text = el.text or False
        _cfm_damping = _text.strip().lower() == 'true'
        return cls(cfm_damping=_cfm_damping)
