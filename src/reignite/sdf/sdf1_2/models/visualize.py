from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class Visualize(Model):
    def __init__(self, visualize: bool = False):
        self.visualize = visualize

    def to_sdf(self) -> ET.Element:
        el = ET.Element("visualize")
        if self.visualize is not None:
            el.text = str(self.visualize).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Visualize":
        _text = el.text or False
        _visualize = _text.strip().lower() == 'true'
        return cls(visualize=_visualize)
