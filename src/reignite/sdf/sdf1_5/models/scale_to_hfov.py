from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class ScaleToHfov(Model):
    def __init__(self, scale_to_hfov: bool = True):
        self.scale_to_hfov = scale_to_hfov

    def to_sdf(self) -> ET.Element:
        el = ET.Element("scale_to_hfov")
        if self.scale_to_hfov is not None:
            el.text = str(self.scale_to_hfov).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "ScaleToHfov":
        _text = el.text or True
        _scale_to_hfov = _text.strip().lower() == 'true'
        return cls(scale_to_hfov=_scale_to_hfov)
