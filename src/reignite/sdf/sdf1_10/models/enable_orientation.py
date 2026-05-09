from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_9.models.enable_orientation import EnableOrientation as _PrevEnableOrientation


class EnableOrientation(_PrevEnableOrientation):
    def __init__(self, enable_orientation: bool = True):
        super().__init__(enable_orientation=enable_orientation)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "EnableOrientation":
        _base = _PrevEnableOrientation.from_sdf(el)
        return cls(enable_orientation=_base.enable_orientation)
