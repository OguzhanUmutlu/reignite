from __future__ import annotations

from xml.etree import ElementTree as ET

from .device import Device
from ..model import Model


class Audio(Model):
    def __init__(self, device: "Device" = None):
        self.device = device

    def to_sdf(self) -> ET.Element:
        el = ET.Element("audio")
        if self.device is not None:
            el.append(self.device.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Audio":
        _c_device = el.find("device")
        _device = Device.from_sdf(_c_device) if _c_device is not None else None
        return cls(device=_device)
