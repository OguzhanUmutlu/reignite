from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_7.models.output import Output as _PrevOutput


class Output(_PrevOutput):
    def __init__(self, output: str = "depths"):
        super().__init__(output=output)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Output":
        _base = _PrevOutput.from_sdf(el)
        return cls(output=_base.output)
