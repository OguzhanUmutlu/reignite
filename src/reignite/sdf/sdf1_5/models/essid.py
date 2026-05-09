from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_4.models.essid import Essid as _PrevEssid


class Essid(_PrevEssid):
    def __init__(self, essid: str = "wireless"):
        super().__init__(essid=essid)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Essid":
        _base = _PrevEssid.from_sdf(el)
        return cls(essid=_base.essid)
