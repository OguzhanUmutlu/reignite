from __future__ import annotations

from xml.etree import ElementTree as ET

from .bounce import Bounce
from .contact import Contact
from .friction import Friction
from ..model import Model


class Surface(Model):
    def __init__(
            self,
            bounce: "Bounce" = None,
            friction: "Friction" = None,
            contact: "Contact" = None
    ):
        self.bounce = bounce
        self.friction = friction
        self.contact = contact

    def to_sdf(self) -> ET.Element:
        el = ET.Element("surface")
        if self.bounce is not None:
            el.append(self.bounce.to_sdf())
        if self.friction is not None:
            el.append(self.friction.to_sdf())
        if self.contact is not None:
            el.append(self.contact.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Surface":
        _c_bounce = el.find("bounce")
        _bounce = Bounce.from_sdf(_c_bounce) if _c_bounce is not None else None
        _c_friction = el.find("friction")
        _friction = Friction.from_sdf(_c_friction) if _c_friction is not None else None
        _c_contact = el.find("contact")
        _contact = Contact.from_sdf(_c_contact) if _c_contact is not None else None
        return cls(bounce=_bounce, friction=_friction, contact=_contact)
