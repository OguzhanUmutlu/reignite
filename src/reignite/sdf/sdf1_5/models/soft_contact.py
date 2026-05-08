from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_4.models.soft_contact import SoftContact as _PrevSoftContact
from .dart import Dart


class SoftContact(_PrevSoftContact):
    def __init__(self, dart: "Dart" = None):
        super().__init__(dart=dart)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "SoftContact":
        _base = _PrevSoftContact.from_sdf(el)
        return cls(dart=_base.dart)
