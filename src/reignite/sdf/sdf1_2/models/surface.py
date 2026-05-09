from __future__ import annotations

from xml.etree import ElementTree as ET

from .bounce import Bounce
from .contact import Contact
from .friction import Friction
from ...sdf1_0.models.surface import Surface as _PrevSurface


class Surface(_PrevSurface):
    def __init__(
            self,
            bounce: "Bounce" = None,
            friction: "Friction" = None,
            contact: "Contact" = None
    ):
        super().__init__(bounce=bounce, friction=friction, contact=contact)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Surface":
        _base = _PrevSurface.from_sdf(el)
        return cls(bounce=_base.bounce, friction=_base.friction, contact=_base.contact)
