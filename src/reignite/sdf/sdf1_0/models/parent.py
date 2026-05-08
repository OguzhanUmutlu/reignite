from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class Parent(Model):
    def __init__(self, link: str = "__default__"):
        self.link = link

    def to_sdf(self) -> ET.Element:
        el = ET.Element("parent")
        if self.link is not None:
            el.set("link", self.link)
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Parent":
        _link = el.get("link", "__default__")
        return cls(link=_link)
