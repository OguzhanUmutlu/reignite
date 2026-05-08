from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class Device(Model):
    def __init__(self, device: str = "default"):
        self.device = device

    def to_sdf(self) -> ET.Element:
        el = ET.Element("device")
        if self.device is not None:
            el.text = self.device
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Device":
        _text = el.text or "default"
        _device = _text
        return cls(device=_device)
