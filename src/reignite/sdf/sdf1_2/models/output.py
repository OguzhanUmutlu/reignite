from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class Output(Model):
    def __init__(self, output: str = "depths"):
        self.output = output

    def to_sdf(self) -> ET.Element:
        el = ET.Element("output")
        if self.output is not None:
            el.text = self.output
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Output":
        _text = el.text or "depths"
        _output = _text
        return cls(output=_output)
