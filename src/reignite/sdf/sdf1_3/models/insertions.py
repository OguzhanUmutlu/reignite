from __future__ import annotations

from typing import List
from xml.etree import ElementTree as ET

from .model import Model


class Insertions(Model):
    def __init__(self, model: List["Model"] = None):
        self.model = model or []

    def to_sdf(self) -> ET.Element:
        el = ET.Element("insertions")
        for item in (self.model or []):
            el.append(item.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Insertions":
        _model = [Model.from_sdf(c) for c in el.findall("model")]
        return cls(model=_model)
