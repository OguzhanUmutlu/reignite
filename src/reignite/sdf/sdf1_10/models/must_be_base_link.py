from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_9.models.must_be_base_link import MustBeBaseLink as _PrevMustBeBaseLink


class MustBeBaseLink(_PrevMustBeBaseLink):
    def __init__(self, must_be_base_link: bool = False):
        super().__init__(must_be_base_link=must_be_base_link)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "MustBeBaseLink":
        _base = _PrevMustBeBaseLink.from_sdf(el)
        return cls(must_be_base_link=_base.must_be_base_link)
