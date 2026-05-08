from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_10.models.device import Device as _PrevDevice


class Device(_PrevDevice):
    def __init__(self, device: str = "default"):
        super().__init__(device=device)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Device":
        _base = _PrevDevice.from_sdf(el)
        return cls(device=_base.device)
