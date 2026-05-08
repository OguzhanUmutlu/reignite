from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class MustBeBaseLink(Model):
    def __init__(self, must_be_base_link: bool = False):
        self.must_be_base_link = must_be_base_link

    def to_sdf(self) -> ET.Element:
        el = ET.Element("must_be_base_link")
        if self.must_be_base_link is not None:
            el.text = str(self.must_be_base_link).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "MustBeBaseLink":
        _text = el.text or False
        _must_be_base_link = _text.strip().lower() == 'true'
        return cls(must_be_base_link=_must_be_base_link)
