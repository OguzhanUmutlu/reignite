from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_9.models.cfm_damping import CfmDamping as _PrevCfmDamping


class CfmDamping(_PrevCfmDamping):
    def __init__(self, cfm_damping: bool = False):
        super().__init__(cfm_damping=cfm_damping)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "CfmDamping":
        _base = _PrevCfmDamping.from_sdf(el)
        return cls(cfm_damping=_base.cfm_damping)
