from __future__ import annotations

from xml.etree import ElementTree as ET

from typing import List

from ..model import Model


class Name(Model):
    def __init__(self, name: str = "__default__"):
        self.name = name

    def to_sdf(self) -> ET.Element:
        el = ET.Element("name")
        if self.name is not None:
            el.text = self.name
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Name":
        _text = el.text or "__default__"
        _name = _text
        return cls(name=_name)


class Deletions(Model):
    def __init__(self, name: List["Name"] = None):
        self.name = name or []

    def to_sdf(self) -> ET.Element:
        el = ET.Element("deletions")
        for item in (self.name or []):
            el.append(item.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Deletions":
        _name = [Name.from_sdf(c) for c in el.findall("name")]
        return cls(name=_name)
