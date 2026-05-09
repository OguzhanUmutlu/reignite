from __future__ import annotations

from xml.etree import ElementTree as ET

from ...sdf1_7.models.rfidtag import Rfidtag as _PrevRfidtag


class Rfidtag(_PrevRfidtag):
    def __init__(self):
        super().__init__()

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Rfidtag":
        return cls()
