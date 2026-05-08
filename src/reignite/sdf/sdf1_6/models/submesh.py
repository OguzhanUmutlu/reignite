from __future__ import annotations

from xml.etree import ElementTree as ET

from ..model import Model
from ...sdf1_5.models.submesh import Submesh as _PrevSubmesh
from .name import Name
from .center import Center


class Submesh(_PrevSubmesh):
    def __init__(self, name: "Name" = None, center: "Center" = None):
        super().__init__(name=name, center=center)

    def to_sdf(self) -> ET.Element:
        el = super().to_sdf()
        return el

    @classmethod
    def from_sdf(cls, el: ET.Element) -> "Submesh":
        _base = _PrevSubmesh.from_sdf(el)
        return cls(name=_base.name, center=_base.center)
