from __future__ import annotations

from xml.etree import ElementTree as ET

from .noise import Noise
from ..model import Model


class Horizontal(Model):
    def __init__(self, noise: "Noise" = None):
        self.noise = noise

    def to_sdf(self) -> ET.Element:
        el = ET.Element("horizontal")
        if self.noise is not None:
            el.append(self.noise.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Horizontal":
        _c_noise = el.find("noise")
        _noise = Noise.from_sdf(_c_noise) if _c_noise is not None else None
        return cls(noise=_noise)
