from __future__ import annotations

from xml.etree import ElementTree as ET

from .device import Device
from ...sdf1_9.models.audio import Audio as _PrevAudio


class Audio(_PrevAudio):
    def __init__(self, device: "Device" = None):
        super().__init__(device=device)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Audio":
        _base = _PrevAudio.from_sdf(el)
        return cls(device=_base.device)
