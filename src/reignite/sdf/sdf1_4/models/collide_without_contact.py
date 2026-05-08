from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model


class CollideWithoutContact(Model):
    def __init__(self, collide_without_contact: bool = False):
        self.collide_without_contact = collide_without_contact

    def to_sdf(self) -> ET.Element:
        el = ET.Element("collide_without_contact")
        if self.collide_without_contact is not None:
            el.text = str(self.collide_without_contact).lower()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "CollideWithoutContact":
        _text = el.text or False
        _collide_without_contact = _text.strip().lower() == 'true'
        return cls(collide_without_contact=_collide_without_contact)
