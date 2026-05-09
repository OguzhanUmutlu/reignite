from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_9.models.localization import Localization as _PrevLocalization


class Localization(_PrevLocalization):
    def __init__(self, localization: str = "CUSTOM"):
        super().__init__(localization=localization)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Localization":
        _base = _PrevLocalization.from_sdf(el)
        return cls(localization=_base.localization)
