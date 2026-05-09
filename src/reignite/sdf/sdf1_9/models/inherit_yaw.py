from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_8.models.inherit_yaw import InheritYaw as _PrevInheritYaw


class InheritYaw(_PrevInheritYaw):
    def __init__(self, inherit_yaw: bool = False):
        super().__init__(inherit_yaw=inherit_yaw)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "InheritYaw":
        _base = _PrevInheritYaw.from_sdf(el)
        return cls(inherit_yaw=_base.inherit_yaw)
