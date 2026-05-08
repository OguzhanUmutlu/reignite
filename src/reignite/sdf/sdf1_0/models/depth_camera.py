from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class DepthCamera(Model):
    def __init__(self, output: str = "depths"):
        self.output = output

    def to_sdf(self) -> ET.Element:
        el = ET.Element("depth_camera")
        if self.output is not None:
            el.set("output", self.output)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "DepthCamera":
        _output = el.get("output", "depths")
        return cls(output=_output)
