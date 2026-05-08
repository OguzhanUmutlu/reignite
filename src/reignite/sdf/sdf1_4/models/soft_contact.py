from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from .dart import Dart


class SoftContact(Model):
    def __init__(self, dart: "Dart" = None):
        self.dart = dart

    def to_sdf(self) -> ET.Element:
        el = ET.Element("soft_contact")
        if self.dart is not None:
            el.append(self.dart.to_sdf())
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "SoftContact":
        _c_dart = el.find("dart")
        _dart = Dart.from_sdf(_c_dart) if _c_dart is not None else None
        return cls(dart=_dart)
